/**
 * @file   gpio_test.c
 * @author Derek Molloy
 * Modified by: Sam Hedrick
 * @date   19 April 2015
 * @brief  A kernel module for controlling a GPIO LED/button pair. The device mounts devices via
 * sysfs /sys/class/gpio/gpio115 and gpio49. Therefore, this test LKM circuit assumes that an LED
 * is attached to GPIO 49 which is on P9_23 and the button is attached to GPIO 115 on P9_27. There
 * is no requirement for a custom overlay, as the pins are in their default mux mode states.
 * @see http://www.derekmolloy.ie/
*/

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/gpio.h>                 // Required for the GPIO functions
#include <linux/interrupt.h>            // Required for the IRQ code

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Derek Molloy");
MODULE_DESCRIPTION("A Button/LED test driver for the BBB");
MODULE_VERSION("0.1");

static unsigned int gpioLED = 47;       ///< hard coding the LED gpio for this example to P9_23 (GPIO49)
static unsigned int gpioButton = 68;   ///< hard coding the button gpio for this example to P9_27 (GPIO115)
static unsigned int gpioLED2 = 50;
static unsigned int gpioButton2 = 67; 
static unsigned int irqNumber, irqNumber2;          ///< Used to share the IRQ number within this file
static unsigned int numberPresses = 0;  ///< For information, store the number of button presses
static bool	    ledOn = 0;          ///< Is the LED on or off? Used to invert its state (off by default)
static bool     ledOn2 = 0;

/// Function prototype for the custom IRQ handler function -- see below for the implementation
static irq_handler_t  ebbgpio_irq_handler(unsigned int irq, void *dev_id, struct pt_regs *regs);
// static irq_handler_t  ebbgpio_irq2_handler(unsigned int irq, void *dev_id, struct pt_regs *regs);

/** @brief The LKM initialization function
 *  The static keyword restricts the visibility of the function to within this C file. The __init
 *  macro means that for a built-in driver (not a LKM) the function is only used at initialization
 *  time and that it can be discarded and its memory freed up after that point. In this example this
 *  function sets up the GPIOs and the IRQ
 *  @return returns 0 if successful
 */
static int __init ebbgpio_init(void){
   int result = 0;
   int result2 = 0;
   printk(KERN_INFO "GPIO_TEST: Initializing the GPIO_TEST LKM\n");
   // Is the GPIO a valid GPIO number (e.g., the BBB has 4x32 but not all available)
   if (!gpio_is_valid(gpioLED)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO\n");
      return -ENODEV;
   }
   // Going to set up the LED. It is a GPIO in output mode and will be on by default
   // ledOn = true;
   gpio_request(gpioLED, "sysfs");          // gpioLED is hardcoded to 49, request it
   gpio_direction_output(gpioLED, ledOn);   // Set the gpio to be in output mode and on
   gpio_set_value(gpioLED, 0);          // Not required as set by line above (here for reference)
   gpio_export(gpioLED, false);             // Causes gpio49 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   gpio_request(gpioButton, "sysfs");       // Set up the gpioButton
   gpio_direction_input(gpioButton);        // Set the button GPIO to be an input
   gpio_set_debounce(gpioButton, 200);      // Debounce the button with a delay of 200ms
   gpio_export(gpioButton, false);          // Causes gpio115 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
			                    
// 	ledOn2 = true;
   gpio_request(gpioLED2, "sysfs");          // gpioLED is hardcoded to 49, request it
   gpio_direction_output(gpioLED2, ledOn2);   // Set the gpio to be in output mode and on
   gpio_set_value(gpioLED2, 0);          // Not required as set by line above (here for reference)
   gpio_export(gpioLED2, false);             // Causes gpio49 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   gpio_request(gpioButton2, "sysfs");       // Set up the gpioButton
   gpio_direction_input(gpioButton2);        // Set the button GPIO to be an input
   gpio_set_debounce(gpioButton2, 200);      // Debounce the button with a delay of 200ms
   gpio_export(gpioButton2, false);          // Causes gpio115 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   // Perform a quick test to see that the button is working as expected on LKM load
   printk(KERN_INFO "GPIO_TEST: The button states are currently: %d %d\n", gpio_get_value(gpioButton), gpio_get_value(gpioButton2));

   // GPIO numbers and IRQ numbers are not the same! This function performs the mapping for us
   irqNumber = gpio_to_irq(gpioButton);
   irqNumber2 = gpio_to_irq(gpioButton2);
   printk(KERN_INFO "GPIO_TEST: The button is mapped to IRQ: %d %d\n", irqNumber, irqNumber2);

   // This next call requests an interrupt line
   result = request_irq(irqNumber,             // The interrupt number requested
                        (irq_handler_t) ebbgpio_irq_handler, // The pointer to the handler function below
                        IRQF_TRIGGER_RISING,   // Interrupt on rising edge (button press, not release)
                        "ebb_gpio_handler",    // Used in /proc/interrupts to identify the owner
                        NULL);                 // The *dev_id for shared interrupt lines, NULL is okay

   result2 = request_irq(irqNumber2,             // The interrupt number requested
                        (irq_handler_t) ebbgpio_irq_handler, // The pointer to the handler function below
                        IRQF_TRIGGER_RISING,   // Interrupt on rising edge (button press, not release)
                        "ebb_gpio_handler",    // Used in /proc/interrupts to identify the owner
                        NULL);                 // The *dev_id for shared interrupt lines, NULL is okay

   printk(KERN_INFO "GPIO_TEST: The interrupt request result are: %d %d\n", result, result2);
   return result;
}

/** @brief The LKM cleanup function
 *  Similar to the initialization function, it is static. The __exit macro notifies that if this
 *  code is used for a built-in driver (not a LKM) that this function is not required. Used to release the
 *  GPIOs and display cleanup messages.
 */
static void __exit ebbgpio_exit(void){
   printk(KERN_INFO "GPIO_TEST: The button states are currently: %d %d\n", gpio_get_value(gpioButton), gpio_get_value(gpioButton2));
   printk(KERN_INFO "GPIO_TEST: The button was pressed %d times\n", numberPresses);
   gpio_set_value(gpioLED, 0);              // Turn the LED off, makes it clear the device was unloaded
   gpio_unexport(gpioLED);                  // Unexport the LED GPIO
   free_irq(irqNumber, NULL);               // Free the IRQ number, no *dev_id required in this case
   gpio_unexport(gpioButton);               // Unexport the Button GPIO
   gpio_free(gpioLED);                      // Free the LED GPIO
   gpio_free(gpioButton);                   // Free the Button GPIO
   
   gpio_set_value(gpioLED2, 0);              // Turn the LED off, makes it clear the device was unloaded
   gpio_unexport(gpioLED2);                  // Unexport the LED GPIO
   free_irq(irqNumber2, NULL);               // Free the IRQ number, no *dev_id required in this case
   gpio_unexport(gpioButton2);               // Unexport the Button GPIO
   gpio_free(gpioLED2);                      // Free the LED GPIO
   gpio_free(gpioButton2);                   // Free the Button GPIO
   printk(KERN_INFO "GPIO_TEST: Goodbye from the LKM!\n");
}

/** @brief The GPIO IRQ Handler function
 *  This function is a custom interrupt handler that is attached to the GPIO above. The same interrupt
 *  handler cannot be invoked concurrently as the interrupt line is masked out until the function is complete.
 *  This function is static as it should not be invoked directly from outside of this file.
 *  @param irq    the IRQ number that is associated with the GPIO -- useful for logging.
 *  @param dev_id the *dev_id that is provided -- can be used to identify which device caused the interrupt
 *  Not used in this example as NULL is passed.
 *  @param regs   h/w specific register values -- only really ever used for debugging.
 *  return returns IRQ_HANDLED if successful -- should return IRQ_NONE otherwise.
 */
// static irq_handler_t ebbgpio_irq_handler(unsigned int irq, void *dev_id, struct pt_regs *regs){
//    ledOn = !ledOn;                          // Invert the LED state on each button press
//    // ledOn2 = !ledOn2;
//    gpio_set_value(gpioLED, ledOn);          // Set the physical LED accordingly
//    // gpio_set_value(gpioLED2, gpio_get_value(gpioButton2));
//    printk(KERN_INFO "GPIO_TEST: Interrupt! (button 1 state is %d) (button 2 state is %d)\n", gpio_get_value(gpioButton), gpio_get_value(gpioButton2));
//    numberPresses++;                         // Global coumakenter, will be outputted when the module is unloaded
//    return (irq_handler_t) IRQ_HANDLED;      // Announce that the IRQ has been handled correctly
// }

static irq_handler_t ebbgpio_irq_handler(unsigned int irq, void *dev_id, struct pt_regs *regs){
   if(irq == irqNumber){
      ledOn = !ledOn;
      gpio_set_value(gpioLED, ledOn);          // Set the physical LED accordingly   
   } else {
      ledOn2 = !ledOn2;
      gpio_set_value(gpioLED2, ledOn2);
   }
   printk(KERN_INFO "GPIO_TEST: Interrupt! (button 1 state is %d) (button 2 state is %d)\n", gpio_get_value(gpioButton), gpio_get_value(gpioButton2));
   numberPresses++;                         // Global coumakenter, will be outputted when the module is unloaded
   return (irq_handler_t) IRQ_HANDLED;      // Announce that the IRQ has been handled correctly
}

/// This next calls are  mandatory -- they identify the initialization function
/// and the cleanup function (as above).
module_init(ebbgpio_init);
module_exit(ebbgpio_exit);
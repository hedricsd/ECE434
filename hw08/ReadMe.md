# hw08
- Blinking an LED
- PWM Generator
- Controlling the PWM Frequency (Optional)
- Reading an Input at Regular Intervals (optional)
- Analog Wave Generator (Optional)

## Blinking an LED
![image](https://user-images.githubusercontent.com/45342964/141369383-fca28f96-b618-476d-97d4-ad27af8d4480.png)

To start this code, the input is make TARGET=hello.pru0.
To stop this code, the input in make TARGET=hello.pru0 stop.
When I set the delay cycles to zero, I got the highest frequency to be around 12.6 MHz. It was slightly jittery and unstable as the higher the frequency went.

## PWM Generator
![image](https://user-images.githubusercontent.com/45342964/141369464-a14a6dcf-ee82-4053-8b5d-8f4dd4683048.png)

The waveform is much more stable and symmetric for the PWM generator. The Std Dev in the frequency was read as 0 Mhz as you can see from the picture. There is almost no jitter as well.


## Controlling the PWM Frequency
![image](https://user-images.githubusercontent.com/45342964/141369358-5298292a-8e05-45e6-81b4-85519d49d257.png)

The oscilliscope I used only had two channels so I was not able to get a reading on all the channels at once. The output pins that are being driven are P9_28, P9_29, P9_30, and P9_31. The bits of __R30 that are being used are 0(P9_31), 1(P9_30), 2(P9_29), 3(P9_28). The highest frequency I got was 327 KHz, with a slight bit of jitter. The pwm-test.c program changed the on off times as well.


## Reading an Input at Regular Intervals
![image](https://user-images.githubusercontent.com/45342964/141369327-6ad9029b-0768-416e-adeb-101c78b06b61.png)

For this section, I read the button (Lower Waveform) and use that to turn on the LED (Upper Waveform). It is hard to tell the exact speed that the code transfers the input to the output, but it seems to be quicker than if it was using the GPIO ports.

## Analog Wave Generator
I did not get to this part of this hw.


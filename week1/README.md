
# LED Blink Project

## Project Title

Week 1 – LED Blink using Arduino Uno

## Project Overview

This project demonstrates the basics of controlling an LED using an Arduino Uno. The LED is programmed to turn ON and OFF repeatedly, creating a blinking effect. The project helps beginners understand digital output, delays, and the structure of an Arduino program (`setup()` and `loop()` functions).

## Hardware Required

- Arduino Uno
- USB Cable (Type-A to Type-B)
- 1 × LED
- 1 × 220 Ω Resistor
- Breadboard
- Male-to-Male Jumper Wires
- Computer with Arduino IDE installed

## Circuit Diagram Description:

- Connect the long leg (anode) of the LED to **Digital Pin 13** through a **220 Ω resistor**.
- Connect the short leg (cathode) of the LED to the **GND** pin of the Arduino.
- Connect the Arduino Uno to the computer using the USB cable.


## How to Upload Code

1. Connect the Arduino Uno to your computer using the USB cable.
2. Open the Arduino IDE.
3. Open the `led_blink.ino` sketch.
4. Select Tools → Board → Arduino Uno.
5. Select the correct COM Port from Tools → Port.
6. Click the Verify button to compile the code.
7. Click the Upload button.
8. Wait until the message "Done uploading" appears.
9. Observe the LED connected to Pin 13 blinking.

## Expected Output

- The LED connected to Digital Pin 13 turns **ON** for one second.
- The LED turns **OFF** for one second.
- This process repeats continuously.
- If Serial Monitor messages are included, they can be viewed by opening **Tools → Serial Monitor** at the correct baud rate.


## Troubleshooting Tips

1. Ensure the correct Board (Arduino Uno) and COM Port are selected in the Arduino IDE.
2. Verify that the LED is connected with the correct polarity (long leg to Pin 13 through the resistor, short leg to GND).
3. Check that all jumper wires and the resistor are securely connected.
4. Make sure the USB cable supports data transfer and is properly connected.


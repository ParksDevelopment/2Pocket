# 2Pocket

[Introduction](#Introduction)

[Info and Production](#Production)

[PCB](#PCB)

[Firmware](#Firmware)

[Case](#Case)

[Overview](#Overview)

## Introduciton

The 2Pocket is a pocket keyboard originally created for the [Pocket Keyboard Design Contest](https://chrischrislolo.github.io/orthoLabLogs/pocket-keyboard-design-contest-00.html). As such it was designed to meet the criteria of the contest as closely as possible while still being a practical keyboard for daily use. The feature list of the 2Pocket is pretty fleshed out including:

- 36 Kailh Choc V1 Low Profile Hot swap sockets (Using [Sunset](https://lowprokb.ca/collections/switches/products/sunset-tactile-choc-switches) switches for all pictures)
- Bluetooth support between halves and computer
- On board ADXL345 for step counting
- 2 additional 6 mm Push button switches used for bluetooth and additional controls controls
- Full open source customizeable keymap in KMK. ZMK to be included soon
- 2 3.7V 1100 mAh batteries
- Magnetic casing to make the board unibody for preference, saving space, or travel
- Small enough to fit in your pocket! (according to the contest which gives a 190mm x 76mm x 22mm bounding box with the 2Pocket coming in comfortably at 190mm x 74.8mm x 22mm)

The idea behind the board was to create something that you can put in your pocket, ie fitting the bounding box, but does not force you to make any compromises to your work flow. I work a full time job as an software engineer and use a 36 key layout called [Miryoku](https://github.com/manna-harbour/miryoku_kmk) so it was important to me above all else to fit that standard so 36 keys was a must for me. Another key requirement for me was bluetooth. If this would be a pocket board then I would need it to be easier to bring places than my normal keyboard. The size helps but keeping it wireless allows me to pick it up on the way out the door or throw it in my bag without any fear of not having the necessary parts to make it run. Finally I wanted to play into the pocket part of the challenge which lead to the on board ADXL345. If I plan on keeping the board in my pocket It is already in the prime position to track my steps, and by mapping a button press to output my number of steps on the screen I am able to quickly see where I am at on the given day or trip. It gives me a great reason to still carry the board around even if I am not sure it will come in handy. Its not as accurate as a smart watch or even a smartphone but it gets pretty close and I am continuing to improve the step counting algorithem and features.

## Production

I will briefly explain below how to reproduce the board as well as discuss improvements I would like to make in the future on the project in each area. The production of the board is reletively simple, but will require either a 3D printer or ordering the case parts through a provider. I also chose to solder some parts and order the board with other parts soldered on. If you have a soldering station I would recommend you do the same but you can choose whatever works best for you. Below is the parts list which does not inclued the pcb or the case which will be discussed later:

| Part Name  | Quantity   | Solder by hand   |
|------------|------------|------------|
| Multilayer Ceramic Capacitors MLCC - SMD/SMT 1uF| 4| NO|
| Tantalum Capacitors - Solid SMD 16V 10uF| 2| Row 2 Col 3|


## PCB

## Firmware

## Case

## Overview

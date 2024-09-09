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

I will briefly explain below how to reproduce the board as well as discuss improvements that could be made in the future on the project in each area so. The production of the board is reletively simple, but will require either a 3D printer or ordering the case parts through a provider. I also chose to solder some parts and order the board with other parts soldered on. If you have a soldering station I would recommend you do the same but you can choose whatever works best for you. Below is the parts list which does not inclued the pcb or the case which will be discussed later:

| Part Name  | Quantity   | Solder by hand   |
|------------|------------|------------|
| Ceramic Capacitors 1uF| 4| NO|
| Tantalum Capacitors 10uF| 2| NO|
| ADXL345 | 2| NO|
| 1N4148 Diode | 38| NO|
| 4.7 k oHm Resistor | 4| NO|
| 2 pin Jst socket | 2| YES|
| 6 mm push button switches | 2| YES|
| Choc hotswap sockets | 36| YES|
| Xiao NRF52840 | 2| YES|
| EEMB Lithium Polymer Battery 3.7V 1100mAh | 2| DNA|

most of these the brand doesn't matter but the case is modeled to fit this specific battery so if you would like to use a different battery you need to make some modifications.

## PCB

The PCB has a footprint of 185mm x 71mm x 1.6mm which does not give a ton of room for the case but it is hard to scale it down much without giving up keys or making the wiring much more complicated. To order the case go to the PCB folder in this repo and then go to the production folder in there. that includes the gerber files as well as the BOM and POS files needed to order from jlcpbc. The original kicad project is there as well so if you need to regenerate the files that should be possible. the BOM will only inclued the parts I list as not soldered by hand. in addition double check the position of the ADXL345s. they should always be oriented so pin one is on the side closer to the Xiao board. Once the board is ordered just snap it in the middle and trim off any parts left over on the side. Then solder the remaining part on. 

I am pretty happy with the pcb but there are 2 bi changes I would make:

1. I would wire the ncf pins on the xiao to the interupt pins on the adxl345. The ncf pins can act as extra gpio pins with some software changes and connecting them to the adxl345 would let me do things like shake to undo or stop any keystrokes if it detects the board has been knocked off. this stuff could still be done as is but I would need to check often and it would hurt the battery.
2. I could include a coulple mounting holes. I got by ok without them but some holes that are purely for helping connect it to the case would open up how you can design the case quite a bit.

## Firmware

The firmware is written in KMK. To install it just follow the [getting started](https://kmkfw.io/Getting_Started/) guide on the KMK site. After getting circuit python and kmk installed you should then follow the [bluetooth guide](https://kmkfw.io/ble_hid/) just up to adding the adafruit bluetooth folder into your project. Once that is done you can go to this repo, go to firmware, go to kmk and replace your code.py with the one there then take the adxl345.py and drag it into the extensions folder. Once all that is done you can edit the keymap to your liking using KC.STEPS to print out how many steps have been taken and KC.CLEARBT to disconnect and pair to a new bluetooth device. kmk bluetooth can be finicky so if you run into issues you can ask at the [zmk help forum](https://kmkfw.zulipchat.com/#recent).

## Case

## Overview

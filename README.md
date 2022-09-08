Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2022.

## Content

* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `video` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains one or several schematic diagrams in form of JPEG, PNG or PDF of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains code of control software for all components which were programmed to participate in the competition
* `models` is for the files for models used by 3D printers, laser cutting machines and CNC machines to produce the vehicle elements. If there is nothing to add to this location, the directory can be removed.
* `other` is for other files which can be used to understand how to prepare the vehicle for the competition. It may include documentation how to connect to a SBC/SBM and upload files there, datasets, hardware specifications, communication protocols descriptions etc. If there is nothing to add to this location, the directory can be removed.

## Introduction

## The begining
We started originally with lego, as we thought we could do something using lego and since it was the only thing we had near at the moment, we tried using lego, however, after a bit of testing we noticed that lego was really slow and couldn't handle what we were going to do so, after a bit of time reading the rules... we came to the final choice of moving to arduino and using a raspberry pi.

## First 4 Weeks
We started experimenting with the pi and doing our first prototype, that prototype was really flawed, we had voltage issues (mainly because the pi 4b only accepts strictly 5.1 Volts 3 Amperes and wont work if it is decreased a bit, so we tried working with x2 3.7 volt 18650 batteries and accidentally connected the 7 volts it gave to the pi 5 volt pin directly, which resulted on the pi bricking due to raspberry pi foundation's decision to remove the polyfuse that should protect everything on the model 4b.

So after a few weeks of waiting and fixing the block detection software, we managed to get a replacement for the raspberry pi 4b, its name: Rock pi. now, we consulted the rules and were aware that this board had wifi/bluetooth capabilities so we decided to just remove the drivers for those modules as that should make them practically unaccessible from the OS.

We also fixed our power issues using a [REDACTED] which gave enough power to the "pi" to run for 8 hours! and also power up the arduino board we used for controlling motors/actuators, then we focused mainly on finishing the code and the vehicle itself.

## Week #5
We are currently working on programming the AI requognition for the block detection system and building the vehicle base is done by a 75%
The rock pi has booted succesfully and the bluetooth/wifi modules drivers were removed.

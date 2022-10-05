#Future Jam

====

![futurejam](https://user-images.githubusercontent.com/112129112/193986349-58234767-beae-45ed-851f-bba9a4ae4c2f.png)

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

We also fixed our power issues using a SunFounder PiPower which gave enough power to the "pi" to run for 8 hours! and also power up the arduino board we used for controlling motors/actuators, then we focused mainly on finishing the code and the vehicle itself.

## Week #5
We are currently working on programming the AI requognition for the block detection system and building the vehicle base is done by a 75%
The rock pi has booted succesfully and the bluetooth/wifi modules drivers were removed, code is 75% done, we fixed some failures with the actuator for steering and added some cosmetic features like lights, we had a voltage problem with the arduino and had to add x2 9.3V batteries to keep everything stable and have enough power for our 3 servos, it was partially not resolved as we were connecting it on the VIN pin that didn't allow the serial communication to work, we found out that connecting it to the barrel pin that accepts 12 volts fixes it and now the robot is working!

## Week #6 Competition
We went to the 21/09/2022 regional competition, tested till 1:40 AM for failures in our system and we finally managed to narrow most and fix them, we are now awaiting for the competition to start to see how good we go1

after 3 rounds, we classified and ended 5'th we are now going for the nationals.

## Week #7 sunday 8:37 pm
We created the walls for the track, kind of improvised but it works! now we have a better guide to follow. We kept 6 hours trying to fix color detection in open-CV, thank you INTEL, we kept all the weekend focused on how to detect the colors we hope we can fix this fast.

## Week 8 Final days
Finally we find out how to detect colors, so with this advantage we are one step less to complete our project, we are really happy about how is everthing going after months of effort and sacrifices. The programming is complete, we fix problems with the strutucture avoiding any inesperated problem and It works! We do the 3 rounds! Now is time to finally sleep peacefully and hope everthing goes good tomorrow.

## Week 8, 11:45 PM
The robot is now running and did the 3 laps, (actually 4) we are very happy at the moment and are getting ready for the national's this morning!

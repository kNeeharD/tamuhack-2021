# tamuhack-2021
Application for estimating waiting time at Airport security to make air travel easier for passengers.

## Inspiration
During the past year, the COVID-19 pandemic has imposed quite a few restrictions on the lives of most people. One of the few things that most people don't seem to miss due to these restrictions is air travel, mostly because of the hassle and stress that the process of working one's way through an airport and boarding a plane places on a person. While looking for to alleviate such stresses for most travelers, our team realized that the most annoying part of air travel for us was having to overcompensate for airport procedures like check-in and security due to the uncertainty of how long each procedure may take.

## What it does
Our program estimates how long it would take at any given time to complete a procedure at an airport checkpoint by using an overhead camera and a unique crowd-counting algorithm that finds the size of the line at the checkpoint. The algorithm does this by using the camera to count human faces and using a predetermined average time for one person to complete the procedure to provide the time estimate.

## How we built it
We used the computer's inbuilt camera to obtain a video feed, which we processed by using the python openCV library and then processed the data from the camera by constructing an algorithm that used python's dlib library to construct a low-level facial recognition algorithm that identified human faces from the feed and used this data to find the size of the group. This algorithm then used a finite difference approximation for a person to complete a given procedure to find the total time estimate, and used a PHP script to read from the python script and send data to the frontend for any display updates every thirty seconds.

## Challenges we ran into
Initially, we tried to use a cell phone camera along with a React.js script using the [Expo platform](https://docs.expo.io/) to send the video feed from the camera to the server where the algorithm would do its work. However, we were unable to do so due to not being able to figure out a way to reliably stream to the main server, and we did not think that making an application on the cell phone itself to where the camera and the main server were already integrated was the most optimal option. Thus, our only other option was to restart the process of obtaining a consistent camera feed from the computer itself by writing a python script using openCV as mentioned above. At the end, we had to figure out an alternative way to update the frontend since the python script was unable to communicate with the PHP requests.

## Accomplishments that we're proud of
Although we were not able to use Expo camera for providing us with the video feed, getting it to work somewhat reliably with the correct scale factor for the feed despite none of us knowing a sizeable amount of Node.js was a proud moment for us. Despite the setback, we were able to complete the backend part of the program quite rapidly.

## What we learned
A first for some of us was the integration of hardware like computer cameras into an algorithm that purposefully used the data for computation. Others learned about the usage of Javascript languages like Node.js and React.js and the role they filled where the languages we learned in our courses (python, C++, etc) proved ineffective.

## What's next for BeeLine
The next step for BeeLine would be to integrate a map API like Google Maps to broaden the solution base of the program by including travel times to the airport and using a distance calculator in conjunction with the map API to estimate intra-airport walking time.

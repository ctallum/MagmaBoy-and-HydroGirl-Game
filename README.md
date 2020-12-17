
<p align="center">
  <img src=data/readme_images/banner.png alt="Game Logo"/>

  <img src=data/readme_images/full_run.gif alt="Game Demo"/>
</p>

## Website
https://ctallum.github.io/softdes-game-project/

## Description
Grab a friend, and together play as MagmaBoy and HydroGirl, two friends who are exploring and abandoned temple.
But be careful! MagmaBoy can't touch the water puddles, HydroGirl can't touch the lava pools, and neither of them can touch the green goo pools or the level will end! Use the buttons and the platforms to get to the final doors and into the next room. 

## Installation
To download the game, first clone this game repository.
```
git clone https://github.com/ctallum/softdes-game-project.git
```

Before installing MagmaBoy and HydroGirl make sure to have pygame installed.
  To install pygame in Linux run the command:
 ```
 python3 -m pip install -U pygame --user
 ```
 Alternatively, you can run the following to download pygame with all of the needed dependencies.
 ```
sudo apt-get update
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev python3-setuptools python3-dev python3 libportmidi-dev
sudo apt-get build-dep libsdl2 libsdl2-image libsdl2-mixer libsdl2-ttf libfreetype6 python3 libportmidi0
git clone https://github.com/pygame/pygame.git
cd pygame
python3 setup.py -config -auto -sdl2
python3 setup.py install --user
 ```
More in depth installation instructions as well as guides to setting up pygame on Windows and MacOS can be found here:
https://www.pygame.org/wiki/GettingStarted
## Running the game

Running the game is really simple. Once the installation procedure is complete, go to the game directory and run the following line:
```
python main.py
```

Once the game is running, a screen will pop up, showing you the menu and directions. Use the arrow keys to control Magmaboy and WASD keys to control Hydrogirl. While in the level, you can press the escape key at any time to return to the level select screen.

## Sources
The only external sources used were: 

The Fireboy and Watergirl games as a starting idea point.
- https://fireboyand-watergirl.co/

DaFluffyPotato pygame platformer tutorials as starting point to implement jumping physics and collisions.
- https://www.youtube.com/watch?v=xxRhvyZXd8I&list=PLX5fBCkxJmm3nAalPU6gGfRIFLlghRuYy
- https://www.youtube.com/watch?v=Qdeb1iinNtk&list=PLX5fBCkxJmm3nAalPU6gGfRIFLlghRuYy&index=2
- https://www.youtube.com/watch?v=abH2MSBdnWc&list=PLX5fBCkxJmm3nAalPU6gGfRIFLlghRuYy&index=3

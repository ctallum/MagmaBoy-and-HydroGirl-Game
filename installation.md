- [Home](https://ctallum.github.io/softdes-game-project)

- Get the Game

- [Our Inspiration and Sources](sources.md)

- [Meet the Makers](makers.md)

## Get the Game

If you want to play Magmaboy and Hydrogirl for yourself, you'll first need to install the pygame library. To do this in Linux, you can run the following line in your terminal:

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
For more in depth instructions or guides on installing pygame on Windows and MacOS, please refer to: https://www.pygame.org/wiki/GettingStarted

Next, you will need to clone this repository to your computer. This can be done by running the following line:
```
git clone https://github.com/ctallum/softdes-game-project.git
```

Once that is all done, running the game is easy! Just navigate to the directory of the game repository on your terminal and run this line:
```
python main.py
```

And it's as simple as that! Use the up, down, and enter keys to navigate the level select menu. Then, use the arrow keys to control Magmaboy and WASD to control Hydrogirl. At any point during the game, press the escape key to return to the level select menu.

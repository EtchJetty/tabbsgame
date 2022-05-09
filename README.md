# Tabbs
A classic-styled adventure game.

## Instructions for running the game:
To run the game, simply run main.py in Python 3. This takes you to the main menu, where you can select a gamemode. Further instructions can be found in-game.

Python 3 is the only prerequisite, and can be downloaded [here.](https://www.python.org/downloads/)

If you've never run anything in the command line before, the command on UNIX-like systems (MacOS, Linux) is:

```
python3 main.py
```

Of course, this can only be run from the directory with all the other files. Make sure that the filetree is unchanged from after unzipping the code.

On Windows, you'd run something like this:

```
python main.py
```
**BE AWARE! This program *does not work* on the default Windows shell! Please use a shell like Git's Bash shell, or, really, anything that's less terrible and dated.**

## Troubleshooting:
If this does not work, and you're sure you have Python 3 correctly installed, it is possible you are somehow running the game on an unsupported OS. Try running the .py file for your desired gamemode directly.
If you do that, be aware you have to run the files via command line with two paramaters: speed and text width, in that order.
For example, to run drawerGame.py with a text speed of 4 and width of 48, you'd put into a Linux terminal:
```
python3 drawerGame.py 4 48
```
Additionally, the game does not work on certain outdated shells, including the default for Windows. If you get stdin/stdout errors, this is due to your shell.

import os

config = os.environ.get('TREEGAME')

print("init treegame")
if config == None:
    print("Treegame")

if config == "test":
    print("Treegame Test")

if config == "pygame":
    print("Treegame Pygame")
    from pygame import *

if config == "term":
    print("Treegame Term")


class Vector:
    """Vectors are absolutely essential to this game engine.
    Intuitive understanding of them is a prerequisite:
         to comfortable with this game engine"""

    def __init__(self):
        pass

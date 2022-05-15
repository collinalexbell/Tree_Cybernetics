
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
         to comfortable with this game engine



    A Vector represents a direction in a space, along with a scalar that represents magnitude or distance

    common Vector instances include:
      - difference between two points
      - velocity of an object at a particular instant
      - directional force on an object

    An N dimensional vector is abstractly known by N numbers.


    For example, a four-dimensional vector v having components 4,2,6,9 can be written as:

    v = Vector((4,2,6,9))

    In textbooks, vectors are written in bold, scalars are written in italic

    Vectors can be subscripted like so:

    (v[0], v[1], v[2], v[3])

    or indefinitely:

    (v[0], v[1], ... , v[n-1])


    sometimes these vectors are desctructured into subscripted variables.

    vx, vy, vz = v

    One of the most common dimensions of space used in this game engine is the 4th

    vw, vx, vy, vz = vInFourth

    the fourth dimension is generally called the weight

    vx, vy, vz, vweight = v
         """

    def __init__(self):
        pass


class Vector3D(Vector):
    """The vector 3D implements the Vector interface"""

    def __init__(self):
        pass

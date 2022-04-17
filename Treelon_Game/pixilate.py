import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Open the image form working directory
image = Image.open('waypoint_cafe.png')
type(image)
box = (300, 300, 1750, 1400)
image = image.crop(box)
image.save("waypoint_cafe_edited.png")

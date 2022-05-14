
import os

config = os.environ.get('TREEGAME')

print("init treegame")
if config == None:
  print("Treegame")

if config == "test":
  print("Treegame Test")
 
if config == "pygame":
  print("Treegame Pygame")
 
if config == "term":
  print("Treegame Term")


#!usr/bin/python

# Treelon.py

import pygame
import pygame.image
import pygame.display
import time

class Zeus:
    def __init__(self):
        self.sprite = pygame.image.load("Zeus.png")
        self.pos = (20,20)

    def tick(self):
        if(self.pos[0] < 100):
            self.pos = tuple(map(sum, zip(self.pos, (1,1))))
            time.sleep(0.04)

    def get_pos(self):
        return self.pos



class Treelon:
    #         is an adventure game about becoming a world famous billionaire cyberneticist
    #         the aim of Treelon is to augment reality and bring tech genius dreams to life 

    def __init__(self, name, primary_aim):
        # What is the purpose of your character
        self.name = name
        self.primary_aim = primary_aim
        pygame.init()
        self.screen = pygame.display.set_mode([320, 240])
        self.screen.fill((254,254,254))
        self.Collin = pygame.image.load("collin.png")
        self.Zeus = Zeus()
        self.display_zeus()

    def display_zeus(self):
        self.Zeus.tick()
        self.screen.fill((254,254,254))
        collin_position = self.Collin.get_rect()
        moved_position = self.Collin.get_rect().move(150,50)
        print(self.Zeus.get_pos())
        self.screen.blit(self.Collin, moved_position)
        self.screen.blit(self.Zeus.sprite, self.Zeus.get_pos())
        pygame.display.flip()

    def report(self):
        print("sdl version:")
        print(pygame.version.SDL)
        print(self.name + "'s primary aim is " + self.primary_aim)

def kuberlog():
    treelon =  Treelon("\n\nkuberlog", "to become the best software engineer in the world and earn 10e9$ profit by building ethical, benificial, and purposeful cybernetics")

    while(True):
        treelon.display_zeus()

    print("""
                       __
              \ ______/ V`-,
               }        /~~
              /_)^ --,r'
             |b      |b


        Treelon by Tree Inc

        1) install wallpaper

            """)

    selection = input("select option: ")
    print(selection)
    if(selection == "1"):
        import os
        os.system('./wallpaper')

    return treelon
            
    
kuberlog().report()

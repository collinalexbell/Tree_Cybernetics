#!usr/bin/python

# Treelon.py

import pygame
import pygame.image
import pygame.display

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
        self.Zeus = pygame.image.load("Zeus.png")
        self.Collin = pygame.image.load("collin.png")
        self.zeus_pos = self.Zeus.get_rect()
        self.zeus_pos = self.zeus_pos.move(20,20)
        self.display_zeus()

    def display_zeus(self):
        self.screen.fill((254,254,254))
        collin_position = self.Collin.get_rect()
        moved_position = self.Collin.get_rect().move(150,50)
        self.screen.blit(self.Zeus, self.zeus_pos)
        self.screen.blit(self.Collin, moved_position)
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

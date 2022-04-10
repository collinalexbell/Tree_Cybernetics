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
        self.screen.fill((0,0,0))
        self.display_zeus()
        pygame.display.flip()

    def display_zeus(self):
        Zeus = pygame.image.load("Zeus.png")
        Collin = pygame.image.load("collin.png")
        collin_position = Collin.get_rect()
        moved_position = collin_position.move(150,50)
        self.screen.blit(Zeus, Zeus.get_rect())
        self.screen.blit(Collin, moved_position)

    def report(self):
        print("sdl version:")
        print(pygame.version.SDL)
        print(self.name + "'s primary aim is " + self.primary_aim)

def kuberlog():
    treelon =  Treelon("\n\nkuberlog", "to become the best software engineer in the world and earn 10e9$ profit by building ethical, benificial, and purposeful cybernetics")


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

#!usr/bin/python

# Treelon.py

import pygame
import pygame.image
import pygame.display
import time

GAME_HEIGHT = 480
GAME_WIDTH = 640

class Character:
    def __init__(self, sprite_file_name, starting_pos = (20,20), scale=1):
        oversized_image = pygame.image.load(sprite_file_name)
        self.sprite = pygame.transform.scale(oversized_image, (int(oversized_image.get_size()[0] * scale), int(oversized_image.get_size()[1] * scale)))

        self.pos = starting_pos

    def tick(self):
        if(self.pos[0] < 100):
            self.pos = tuple(map(sum, zip(self.pos, (1,1))))

    def get_pos(self):
        return self.pos


    def move(self, x, y):
      self.pos = (self.pos[0]+x, self.pos[1]+y)


class Treelon:
    #         is an adventure game about becoming a world famous billionaire cyberneticist
    #         the aim of Treelon is to augment reality and bring tech genius dreams to life 

    def __init__(self, name, primary_aim):
        # What is the purpose of your character
        self.name = name
        self.party_move_x = 0
        self.party_move_y = 0
        self.primary_aim = primary_aim
        pygame.init()
        self.screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
        self.screen.fill((254,254,254))
        self.Collin = Character("collin.png", (250, 200), 0.05)
        self.Zeus = Character("Zeus.png", (240, 220), 0.3)
        waypoint_img = pygame.image.load("waypoint_cafe.png")
        self.Waypoint_Cafe = waypoint_img
        #self.Waypoint_Cafe = pygame.transform.scale(waypoint_img, (640,420))
        self.tick()

    def tick(self):
        events = pygame.event.get()
        for event in events:
          if event.type == pygame.KEYUP:
            self.party_move_x=0
            self.party_move_y=0
          if event.type == pygame.KEYDOWN:
            print("keydown")
            print(event.key)
            d_move=5
            if event.key == pygame.K_d:
              self.party_move_x=d_move
            if event.key == pygame.K_a:
              self.party_move_x=-d_move
            if event.key == pygame.K_w:
              self.party_move_y=-d_move
            if event.key == pygame.K_s:
              self.party_move_y=d_move
        self.Zeus.move(self.party_move_x, self.party_move_y)
        self.Collin.move(self.party_move_x, self.party_move_y)
        self.Zeus.tick()
        self.screen.fill((254,254,254))
        self.screen.blit(self.Waypoint_Cafe, (0,-150))
        self.screen.blit(self.Collin.sprite, self.Collin.get_pos())
        self.screen.blit(self.Zeus.sprite, self.Zeus.get_pos())

        pygame.display.flip()

    def report(self):
        print("sdl version:")
        print(pygame.version.SDL)
        print(self.name + "'s primary aim is " + self.primary_aim)

def kuberlog():
    treelon =  Treelon("\n\nkuberlog", "to become the best software engineer in the world and earn 10e9$ profit by building ethical, benificial, and purposeful cybernetics")

    while(True):
        treelon.tick()

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

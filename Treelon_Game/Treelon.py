#!usr/bin/python

# Treelon.py

import pygame
import pygame.image
import pygame.font
import pygame.display
import Mechanics
import BuilderMode
import time
from debug import debug

GAME_HEIGHT = 480
GAME_WIDTH = 640

class Character:
    def __init__(self, sprite_file_name, starting_pos = (20,20), scale=1):
        oversized_image = pygame.image.load(sprite_file_name)
        self.sprite = pygame.transform.scale(oversized_image, (int(oversized_image.get_size()[0] * scale), int(oversized_image.get_size()[1] * scale)))

        self.pos = starting_pos

    def tick(self):
      pass

    def get_pos(self):
        return self.pos


    def move(self, x, y):
      self.pos = (self.pos[0]+x, self.pos[1]+y)

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Party:
    def __init__(self, x, y):
        self.setPosition(x, y)
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setPosition(self, x, y):
        self.x = x
        self.y = y
    def getPos(self):
        return Pos(self.x,self.y)

class World:
    # A world is an environment to load into Treelon. 
    # The class invariant is that the World is ready to plug into Treelon and render as soon as load() is called with success
    # 
    # The world dictates the rendering of itself. 
    # It can render using any library it wants to by inheriting from World and overloading the render methods.
    # Subclasses of world implement a generic render method that various world images can be loaded into.

    def __init__(self, name):
        self.name = name

    def render(self):
        # the method that renders this world in Treelon, using whatever library this function needs to use.
        pass

    def load(self, world_image):
        # loads a world image into the World object 
        # return invariant: the World is ready to plug into Treelon and render at this point
        pass

class Grid_World(World):
    def __init__(self, name, screen, n):
        self.screen = screen
        super().__init__(name)
        self.n = n

    def render(self):
        n = self.n
        for i in range(n):
            pygame.draw.line(self.screen, (0,0,0), (0, GAME_HEIGHT/n*i), (GAME_WIDTH,GAME_HEIGHT/n*i))
            pygame.draw.line(self.screen, (0,0,0), (GAME_WIDTH/n*i, 0), (GAME_WIDTH/n*i, GAME_HEIGHT))

    def load(self, world_image):
        pass

class Sprite:
    def __init__(self, screen, sprite_surf, x, y):
        self.sprite_surf = sprite_surf
        self.x = x
        self.y = y
        self.screen = screen
    def render(self):
        self.screen.blit(self.sprite_surf, (self.x*16,self.y*16))

class Tile_World(Grid_World):

    def __init__(self, name, screen, n):
        super().__init__(name, screen, n)
        self.deactivate_grid()
        self.sprite_grid = []
        self.font = pygame.font.Font(None, 24)

    def load_data_file(self, fname):
        ## TODO: implement, this is really bad pseudo code
        f = open(fname, "r")
        lines = f.readlines()
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                letter = lines[y][x]
                if(letter == '<'):
                    sprite = pygame.image.load("Road.png")
                elif(letter == '>'):
                    sprite = pygame.image.load("RoadRight.png")
                elif(letter == '.'):
                    sprite = pygame.image.load("Curb.png")
                elif(letter == '-'):
                    sprite = pygame.image.load("Sidewalk.png")
                elif(letter == '&'):
                    sprite = pygame.image.load("Car.png")
                elif(letter == '$'):
                    sprite = pygame.image.load("Tree.png")
                elif(letter == '+'):
                    sprite = pygame.image.load("TreeBase.png")
                elif(letter == '*'):
                    sprite = pygame.image.load("Bollard.png")
                elif(letter == '|'):
                    sprite = pygame.image.load("BikeRack.png")
                else:
                    sprite = self.font.render(letter, True, (0,0,0))
                self.add_sprite(sprite, x, y)

    def render_sprites(self):
        for sprite in self.sprite_grid:
            sprite.render()

    def add_sprite(self, sprite_surf, x, y):
        sprite = Sprite(self.screen, sprite_surf, x, y)
        self.sprite_grid.append(sprite)

    def deactivate_grid(self):
        self.render_grid = False

    def activate_grid(self):
        self.render_grid = True

    def render(self):
        if(self.render_grid):
            super().render()
        self.render_sprites()

class Treelon:
    #         is an adventure game about becoming a world famous billionaire cyberneticist
    #         the aim of Treelon is to augment reality and bring tech genius dreams to life 
    def init_graphics(self):
        self.reblit_background = True
        pygame.init()
        pygame.display.set_caption("Treelon")
        self.screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
        self.screen.fill((254,254,254))

    def __init__(self, name, primary_aim):
        # What is the purpose of your character
        self.name = name
        self.party = Party(0,0)
        self.primary_aim = primary_aim

        self.init_graphics()
        self.world = Tile_World("Treelon", self.screen, 14)
        self.world.load_data_file("scene1.map")

        characters = self.init_characters()
        self.mechanics = Mechanics.allMechanics(self.screen, characters)
        waypoint_img = pygame.image.load("waypoint_cafe.png")
        self.Waypoint_Cafe = waypoint_img
        self.background = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.background.fill((115,0,0))
        self.screen_x = 0
        self.screen_y = 110 
        #self.Waypoint_Cafe = pygame.transform.scale(waypoint_img, (640,420))
        self.cur_tick = pygame.time.get_ticks()
        self.last_tick = self.cur_tick
        self.tick()

    def init_characters(self):
        self.Collin = Character("Character.png", (250, 200), 1)
        self.Zeus = Character("Zeus.png", (240, 220), 0.3)
        return [self.Collin, self.Zeus]

    def tick(self):
        self.cur_tick = pygame.time.get_ticks()
        wait_time = 1/60 * 1000 - (self.cur_tick - self.last_tick)
        if(wait_time > 0):
            pygame.time.delay(int(wait_time))
        self.last_tick = pygame.time.get_ticks()
        events = pygame.event.get()
        for event in events:
          if event.type == pygame.KEYUP:
            self.party.setPosition(0,0)
          if event.type == pygame.KEYDOWN:
            print("keydown")
            print(event.key)
            d_move=1
            if event.key == pygame.K_d:
              self.party.setX(d_move)
            if event.key == pygame.K_a:
              self.party.setX(-d_move)
            if event.key == pygame.K_w:
              self.party.setY(-d_move)
            if event.key == pygame.K_s:
              self.party.setY(d_move)
        pos = self.party.getPos()
        self.Zeus.move(pos.x, pos.y)
        self.Collin.move(pos.x, pos.y)
        if(self.Collin.get_pos()[0] > GAME_WIDTH):
          self.Collin.move(-GAME_WIDTH, 0)
          self.Zeus.move(-GAME_WIDTH, 0)
          self.screen_x = self.screen_x+GAME_WIDTH
          self.reblit_background = True
        if(self.Collin.get_pos()[0] < 0):
          self.Collin.move(GAME_WIDTH, 0)
          self.Zeus.move(GAME_WIDTH, 0)
          self.screen_x = self.screen_x-GAME_WIDTH
          self.reblit_background = True
        self.Zeus.tick()
        if self.reblit_background:
          self.rebut_background = False
          self.screen.fill((254,254,254))
          self.screen.blit(self.background, (-1*self.screen_x, -1*self.screen_y))
        self.world.render()
        self.screen.blit(self.Collin.sprite, self.Collin.get_pos())
        self.screen.blit(self.Zeus.sprite, self.Zeus.get_pos())
        for mechanic in self.mechanics:
            mechanic.draw()


        pygame.display.flip()

    def report(self):
        print("sdl version:")
        print(pygame.version.SDL)
        print(self.name + "'s primary aim is " + self.primary_aim)

def kuberlog():
    print(BuilderMode.init_builder_mode())
    treelon =  Treelon("\n\nkuberlog", "to become the best software engineer in the world and earn 10e9$ profit by building ethical, benificial, and purposeful cybernetics")
    worlds = [
        World("Waypoint Cafe"),
        World("NYC studio kuberlog's starting"),
        World("Washington DC (politics profession)"),
        World("Yacht"),
        World("EarthShip (rockies)"),
    ]
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

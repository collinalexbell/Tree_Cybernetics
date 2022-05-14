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

TILE_SIZE = 16

class Character:
    # A character implements a pygame specific character class
    # The character class has an internal tick() call back that can be called in the game loop
    # The class also has a position and the ability to move that position.
    # In general, this class is abstract and handles business logic but does contain some pygame specific resources,
    #   such as the pygame image that should be rendered
    def __init__(self, sprite_file_name, starting_pos = (20,20), scale=1):
        oversized_image = pygame.image.load(sprite_file_name)
        self.sprite = pygame.transform.scale(oversized_image, (int(oversized_image.get_size()[0] * scale), int(oversized_image.get_size()[1] * scale)))

        self.pos = starting_pos

    def tick(self):
        # This is where the character's internal logic can be ran during each tick of the game
        pass

    def get_pos(self):
        return self.pos


    def move(self, x, y):
      self.pos = (self.pos[0]+x, self.pos[1]+y)

class Pos:
    # A 2d point data structure
    # 
    # I want to use the same facility to
    # create data structures as I use for objects
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Party:
    # A party is just a container for a position, right now.
    # If this were to remain as the state of things, this class would
    # need a rename, because a party is much more than a position
    def __init__(self, x, y):
        self.setPosition(x, y)
        self.members = []
    def add_member(self, member):
        self.members.append(member)
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
    # This is probably going to become a wrapper for the Pygame sprite. Right now I'm just using Pygame's image load directly
    # The sprite isn't even being used for the character, just for the background and item tiles
    #
    # The sprite uses tile grid coordinates, not pygame coordinates.
    # (16,16) is start of tile[1], (32, 32) is start of tile[2], etc
    def __init__(self, screen, sprite_surf, x, y):
        self.multi_surf = []
        self.multi_loc = []
        if(isinstance(sprite_surf, list)):
            for surf_and_loc in sprite_surf:
                surf = surf_and_loc[0]
                loc = surf_and_loc[1]
                self.multi_surf.append(surf)
                self.multi_loc.append(loc)
        self.sprite_surf = sprite_surf
        self.x = x
        self.y = y
        self.screen = screen
    def render(self):
        if(len(self.multi_surf) > 0):
            # TODO: render the multi_surf
            pass
        else:
            self.screen.blit(self.sprite_surf, (self.x*TILE_SIZE,self.y*TILE_SIZE))

class Tile_World(Grid_World):

    class Tile:
        def __init__(self, letter, file_name):
            self.sprite = pygame.image.load(file_name)
            self.letter = letter

    def __init__(self, name, screen, n):
        super().__init__(name, screen, n)
        self.deactivate_grid()
        self.sprite_grid = []
        self.font = pygame.font.Font(None, 24)

    def load_data_file(self, fname):
        ## TODO: implement, this is really bad pseudo code
        f = open(fname, "r")
        lines = f.readlines()
        tiles = [
            Tile_World.Tile('<', "./imgs/Road.png"),
            Tile_World.Tile('>', "./imgs/RoadRight.png"),
            Tile_World.Tile('.', "./imgs/Curb.png"),
            Tile_World.Tile('-', "./imgs/Sidewalk.png"),
            Tile_World.Tile('&', "./imgs/Car.png"),
            Tile_World.Tile('$', "./imgs/Tree.png"),
            Tile_World.Tile('+', "./imgs/TreeBase.png"),
            Tile_World.Tile('*', "./imgs/Bollard.png"),
            Tile_World.Tile('|', "./imgs/BikeRack.png")
        ]
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                letter = lines[y][x]
                sprites = [tile for tile in tiles if tile.letter == letter]
                if(len(sprites) > 0):
                    self.add_sprite(sprites[0].sprite, x, y)
                else:
                    self.add_sprite(self.font.render(letter, True, (0,0,0)), x, y)

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

    def first_render(self):
        waypoint_img = pygame.image.load("./imgs/waypoint_cafe.png")
        self.Waypoint_Cafe = waypoint_img
        self.background = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.background.fill((115,0,0))
        self.screen_x = 0
        self.screen_y = 110 
        #self.Waypoint_Cafe = pygame.transform.scale(waypoint_img, (640,420))
        self.cur_tick = pygame.time.get_ticks()
        self.last_tick = self.cur_tick
        self.tick()


    def __init__(self, name, primary_aim):
        # What is the purpose of your character
        self.name = name
        self.party = Party(0,0)
        self.primary_aim = primary_aim

        self.init_graphics()
        self.world = Tile_World("Treelon", self.screen, 14)
        self.world.load_data_file("scene1.map")

        characters = self.init_characters()
        for character in characters:
            self.party.add_member(character)
        self.mechanics = Mechanics.allMechanics(self.screen, characters)
        self.first_render()

    def init_characters(self):
        self.Collin = Character("./imgs/Character.png", (250, 200), 1)
        self.Zeus = Character("./imgs/Zeus.png", (237, 215), 1)
        return [self.Collin, self.Zeus]

    def handle_fps(self):
        self.cur_tick = pygame.time.get_ticks()
        wait_time = 1/60 * 1000 - (self.cur_tick - self.last_tick)
        if(wait_time > 0):
            pygame.time.delay(int(wait_time))
        self.last_tick = pygame.time.get_ticks()

    def handle_keypress(self, events):
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

    def tick(self):
        self.handle_fps()
        events = pygame.event.get()
        self.handle_keypress(events)
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
        for character in self.party.members:
            self.screen.blit(character.sprite, character.get_pos())
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

    while(True):
        treelon.tick()

    return treelon

if __name__ == "__main__":
    kuberlog().report()

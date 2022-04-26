import pygame
black = (0,0,0)
class Mechanic():
    def __init__(self):
        pass
    def draw(self):
        pass

class StatisticsMechanic(Mechanic):
    class Statistic():
        def __init__(self, name, value):
            self.name = name
            self.value = value
    class StaticisticSet():
        def __init__(self):
            self.statistics = [
                    StatisticsMechanic.Statistic("speed", 20),
                    StatisticsMechanic.Statistic("endurance", 20),
                    StatisticsMechanic.Statistic("physical attractiveness", 20),
                    StatisticsMechanic.Statistic("physical fitness", 20),
                    StatisticsMechanic.Statistic("software engineering skill", 40 )
                    ]

    def __init__(self):
        pass

class InventoryMechanic(Mechanic):
    def __init__(self, screen):
        self.x = 150
        self.y = 440
        pygame.font.init()
        playerInventories = {}
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 24)


    def draw(self):
        textSurf = self.font.render("Inventory: phone, keys", True, black)
        rect = textSurf.get_rect()
        rect.center = (self.x, self.y)
        self.screen.blit(textSurf, rect)

        


class AttractionMechanic(Mechanic):
    # Use self.attraction as a coefficient in a wave function that deterimines where one holon is relative to the other.
    def __init__(self, holons):
        self.holons = holons
        self.attraction = 0.5
    def increaseAttraction(x):
        self.attraction += x
    def decreaseAttraction(x):
        self.attraction -= x

    def solid(self):
        self.attraction = 0.8
    def liquid(self):
        self.attraction = 0.4
    def gas(self):
        self.attraction = 0.1

def allMechanics(screen, characters):
    return [StatisticsMechanic(), InventoryMechanic(screen), AttractionMechanic(characters)]


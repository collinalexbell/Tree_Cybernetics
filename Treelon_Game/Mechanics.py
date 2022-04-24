import pygame
black = (0,0,0)
class Mechanic():
    def __init__(self):
        pass
    def draw(self):
        pass

class StatisticsMechanic(Mechanic):
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
    def __init__(self):
        pass

def allMechanics(screen):
    return [StatisticsMechanic(), InventoryMechanic(screen), AttractionMechanic()]


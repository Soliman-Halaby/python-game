import pygame

class BigBossEvent:

    def __init__(self, game):
        self.percent = 0
        self.percentSpeed = 100
        self.game = game
        self.bossHere = False

    #Augmentation de la barre de chargement
    def addPercent(self):
        self.percent += self.percentSpeed / 250

    #Methode lorsque la barre de chargement est à 100%
    def isFullLoaded(self):
        return self.percent >= 100

    #Methode pour réinitialiser la barre de chargement
    def resetPercent(self):
        self.percent = 0

    def updateBar(self, surface):

        #Ajout du pourcentage a la barre
        self.addPercent()

        #Barre noire d'arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 10,
            surface.get_width(),
            10
        ])
        #Barre rouge d'evenement
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 10,
            (surface.get_width() / 100) * self.percent, 10 #Epaisseur de la barre d'evenement
        ])


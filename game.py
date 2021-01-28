import pygame

from player import Player
from monster import Monster, Mummy, Slave, Boss, bigPharaon, camel
from bossEvent import BigBossEvent
from arrow import Arrow
import menu
from sounds import manageAudio

#classe qui represente le jeu
class Game:
    def __init__(self):
        #Verifier si le jeu a commencer
        self.isPlaying = False
        self.background = pygame.image.load('assets/background_level1.png')
        #Generation du joueur
        self.allPlayers = pygame.sprite.Group()
        self.player = Player(self)
        self.projectile = Arrow(self.player, 'projectile')
        self.allPlayers.add(self.player)
        #Groupe pour stocker le boss
        self.allBoss = pygame.sprite.Group()
        self.boss = Boss(self)
        #Generation de l'evenement du boss
        self.bossEvent = BigBossEvent(self)
        #Gestion du son
        self.manageSound = manageAudio()
        #Generation du groupe de monster
        self.allMonsters = pygame.sprite.Group()
        self.keyPressed = {}
        self.countMonster = 2

    def startGame(self):
        self.isPlaying = True
        self.createMonster(Mummy)
        self.createMonster(Mummy)

    def checkLevel(self):
        # Condition si l'on est au niveau 2
        if self.player.level == 2:
            # Affichage de l'esclave / momie
            self.createMonster(Slave)
            self.createMonster(Mummy)
            # Changement de fond (débloquage) du projectile du niveau 2
            menu.secondItemButton = pygame.image.load('assets/inventoryMenu/secondItemButton.png')
            # Changemment de background
            self.background = pygame.image.load('assets/background_level2.png')

        if self.player.level == 3:
            self.background = pygame.image.load('assets/background_level3.png')
            menu.thirdItemButton = pygame.image.load('assets/inventoryMenu/thirdItemButton.png')
            self.createMonster(bigPharaon)
            self.createMonster(Slave)
            self.createMonster(Mummy)

        if self.player.level == 4:
            menu.fourthItemButton = pygame.image.load('assets/inventoryMenu/fourthItemButton.png')
            self.background = pygame.image.load('assets/background_level4.png')
            self.createMonster(bigPharaon)
            self.createMonster(Slave)
            self.createMonster(Mummy)
            self.createMonster(camel)

    #Methode lorsque le jeu est terminé
    def gameOver(self):
        #Reinitialisation es monstres
        self.allMonsters = pygame.sprite.Group()
        #Reinitialisation du background
        self.background = pygame.image.load('assets/background_level1.png')
        #Reinitialisation des HP du player
        self.player.health = self.player.maxHealth
        #Reinitialisation de l'asset du projectile de base
        self.player.projectile = 'projectile'
        self.allBoss = pygame.sprite.Group()
        #Réinitialisation des projectiles en route
        self.player.allArrows = pygame.sprite.Group()
        #Reinitialisation de l'xp, du level et du score
        self.player.xp = 0
        self.player.level = 1
        self.player.score = 0
        self.isPlaying = False
        #Reset les backgrounds de l'inventaire
        menu.secondItemButton = pygame.image.load("assets/inventoryMenu/secondItemButtonCrossed.png")
        menu.thirdItemButton = pygame.image.load("assets/inventoryMenu/thirdItemButtonCrossed.png")
        menu.fourthItemButton = pygame.image.load("assets/inventoryMenu/fourthItemButtonCrossed.png")


    def updateComponent(self, gameScreen, pseudo):

        #Application du texte des niveaux
        levelText = pygame.font.SysFont("Courier", 50).render("Niveau {0}".format(self.player.level), 1, (0, 0, 0))
        gameScreen.blit(levelText, (20, 20))

        #Application du nombre de monstre tué
        gameScore = pygame.font.SysFont("Courier", 30).render("Score : {0}".format(self.player.score), 1, (0, 0, 0))
        gameScreen.blit(gameScore, (900, 20))

        # application de l'image du joueur
        gameScreen.blit(self.player.image, self.player.rect)

        # Actualisation de la barre de vie du joueur
        self.player.updateHealth(gameScreen)
        self.player.updatePseudo(gameScreen, pseudo)
        self.player.updateXP(gameScreen)

        #Actualisation de l'animation du joueur
        self.player.updateAnimation()

        #Actualisation de la barre d'evenement du jeu
        self.bossEvent.updateBar(gameScreen)
        # recuperation des projectiles
        for arrow in self.player.allArrows:
            arrow.movement()

        # recuperation des monstres
        for monster in self.allMonsters:
            monster.moveForward()
            monster.updateHealth(gameScreen)
            monster.updateAnimation()

        #Recuperation du boss du jeu
        for Boss in self.allBoss:
            Boss.moveForward()
            Boss.updateHealth(gameScreen)
            Boss.updateAnimation()

        # application des fleches
        self.player.allArrows.draw(gameScreen)

        # Afficher les images des monstres
        self.allMonsters.draw(gameScreen)

        #Appliquer l'image du boss
        self.allBoss.draw(gameScreen)

        # verification des touches du joueur (direction)
        if self.keyPressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < gameScreen.get_width():
            self.player.walkRight()
            #self.player.updateAnimation()

        elif self.keyPressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.walkLeft()
            #self.player.updateAnimation()

    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    #Creation de monstre par nombre
    def createMonster(self, monsterClassName):
        if monsterClassName == Mummy:
            #Affichage du nombre de momie à chaque appel de createMonster selon le nombre défini dans countMonster
            for i in range(self.countMonster):
                self.allMonsters.add(monsterClassName(self))
        if monsterClassName == Slave:
            self.allMonsters.add(monsterClassName(self))
        if monsterClassName == bigPharaon:
            self.allMonsters.add(monsterClassName(self))
        if monsterClassName == camel:
            self.allMonsters.add(monsterClassName(self))

    #Declancher l'appel du boss
    def attemptBoss(self):

        #Si la barre est chargee
        if self.bossEvent.isFullLoaded() and len(self.allMonsters) == 0:
            self.allBoss.add(Boss(self))
            self.bossEvent.bossHere = True #Activation de l'evenement
            #Jeu de l'audio lors de l'apparition du boss
            self.manageSound.play("bossAppear")


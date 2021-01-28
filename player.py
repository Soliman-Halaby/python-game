import pygame
from arrow import Arrow
import animation

#Classe pour definir les elements du joueur principal
class Player(animation.spriteAnimation):

    def __init__(self, game):
        super(Player, self).__init__("mainPlayer1Red")
        self.game = game
        self.health = 100
        self.projectile = 'projectile'
        self.maxHealth = 100
        self.damage = 10
        self.moveSpeed = 5
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 470
        self.allArrows = pygame.sprite.Group()
        self.xp = 0
        self.level = 1
        self.score = 0

    def updateAnimation(self):
        self.animate()

    #Methode qu'on utilisera pour infliger les dégats
    def damageDealt(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #Si le joueur n'a plus de HP
            self.game.manageSound.play("gameOver")
            self.game.gameOver()
    #Mise a jour du pseudo
    def updatePseudo(self, surface, pseudo):
        self.settings = pygame.font.Font("assets/Courier.TTF", 20)
        self.pseudo = self.settings.render(pseudo, False, [0, 0, 0])
        surface.blit(self.pseudo, [self.rect.x - 10, self.rect.y - 50])

    #Ajout de l'XP
    def addXp(self):
        self.xp += 30 / self.level
        if self.xp >= 100:
            self.xp = 0
            self.level += 1

    #Barre de HP du joueur principal
    def updateHealth(self, surface):
        pygame.draw.rect(surface, (63, 60, 60), [self.rect.x - 10, self.rect.y - 35, self.maxHealth, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 10, self.rect.y - 35, self.health, 5])

    #Barre d'XP du joueur principal
    def updateXP(self, surface):
        pygame.draw.rect(surface, (63, 60, 60), [self.rect.x - 10, self.rect.y - 25, 100, 5])
        pygame.draw.rect(surface, (0, 255, 255), [self.rect.x - 10, self.rect.y - 25, self.xp, 5])

    def sendArrow(self):
        self.allArrows.add(Arrow(self, self.projectile))

    #Pour avancer vers la gauche
    def walkLeft(self):
        self.rect.x -= self.moveSpeed
        self.startAnimation()

    #Pour avancer vers la droite
    def walkRight(self):
        #Condition s'il n'y a pas de collision avec le monstre pour pouvoir avancer vers la droite
        if not self.game.checkCollision(self, self.game.allMonsters) and not self.game.checkCollision(self, self.game.allBoss) :
            self.rect.x += self.moveSpeed
            self.startAnimation()




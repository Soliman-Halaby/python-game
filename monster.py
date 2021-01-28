import pygame
import random
import animation


#Clase qui represente le monstre niveau 1
class Monster(animation.spriteAnimation):
    def __init__(self, game, name, offset=0, isBoss=False):
        super().__init__(name)
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.damage = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 980 + random.randint(0, 350)
        self.rect.y = 540 - offset
        self.isBoss = isBoss
        self.startAnimation()

    def setSpeed(self, speed):
        self.defaultSpeed = speed
        self.moveSpeed = random.randint(1, 3)

    def damageDealt(self, amount):
        self.health -= amount

        #Verification du nombre de HP du monstre
        if self.health <= 0:
            #Reapparition comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 350)
            self.moveSpeed = random.randint(1, self.defaultSpeed)
            self.health = self.maxHealth
            self.game.player.addXp()
            self.game.player.score += 1

            #Verification si la barre d'evenement est chargee ou non
            if self.game.bossEvent.isFullLoaded() and self.isBoss==False:
                self.game.allMonsters.remove(self)

                # Appel de la methode pour faire apparaitre le boss
                self.game.attemptBoss()
            if self.isBoss:
                self.game.allBoss.remove(self)
                self.game.checkLevel()
                self.game.bossEvent.resetPercent()


    def updateAnimation(self):
        self.animate(loop=True)

    def updateHealth(self, surface):
        pygame.draw.rect(surface, (63, 60, 60), [self.rect.x + 20, self.rect.y - 20, self.maxHealth, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 20, self.rect.y - 20, self.health, 5])


    def moveForward(self):
        if not self.game.checkCollision(self, self.game.allPlayers):
            self.rect.x -= self.moveSpeed * (self.game.player.level / 1.8)
        #Si collision avec le joueur
        else:
            #Infliger des degats aux joueurs si collision
            self.game.player.damageDealt(self.damage * (self.game.player.level / 1.6))

#Definir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "monster_level1")
        self.setSpeed(3)

#Class pour l'esclave
class Slave(Monster):

    def __init__(self, game):
        super().__init__(game, "slave", 90)
        self.damage = 0.45
        self.setSpeed(1)

class Boss(Monster):
    def __init__(self, game):
        super().__init__(game, "bigBoss", 130, isBoss=True)
        self.health = 100
        self.damage = 0.3
        self.setSpeed(1)

class bigPharaon(Monster):
    def __init__(self, game):
        super().__init__(game, "bigPharaon", 215)
        self.damage = 0.45
        self.setSpeed(1)

class camel(Monster):
    def __init__(self, game):
        super().__init__(game, "camel", 138)
        self.damage = 1.3
        self.setSpeed(2)
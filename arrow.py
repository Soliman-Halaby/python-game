import pygame
from sounds import manageAudio
#classe qui represente notre fleche
class Arrow(pygame.sprite.Sprite):
    def __init__(self, player, projectile):
        super(Arrow, self).__init__()
        self.manageAudio = manageAudio()
        self.speed = 5
        self.player = player
        self.projectile = projectile
        self.image = pygame.image.load('assets/projectile/' + self.projectile + '.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 100
        self.imageOrigin = self.image
        self.angleRotation = 0

    #Methode pour supprimer la flèche
    def removeElements(self):
        self.player.allArrows.remove(self)

    #Methode de rotation de l'élement
    def rotateElements(self):
        self.angleRotation += 15
        self.image = pygame.transform.rotozoom(self.imageOrigin, self.angleRotation, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    #Méthode lorsque la flêche est en mouvement
    def movement(self):
        self.rect.x += self.speed
        if self.projectile == 'projectileLevel2' or self.projectile == 'projectileLevel4':
            self.rotateElements()

        #Lorsqu'il y a une colision entre le projectile et le monstre
        for monster in self.player.game.checkCollision(self, self.player.game.allMonsters):
            #Suppression du projectile
            self.removeElements()
            #Infligation des dégats au monstre selon le niveau du personnage
            monster.damageDealt(self.player.damage / (self.player.level * 1.3))
            self.manageAudio.play("projectileColision")

        for Boss in self.player.game.checkCollision(self, self.player.game.allBoss):
            self.removeElements()
            Boss.damageDealt(self.player.damage / (self.player.level * 1.5))
            self.manageAudio.play("projectileColision")

        #Supprimer le projectile s'il sort de l'ecran
        if self.rect.x > 1080:
            self.removeElements()
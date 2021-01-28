import pygame

#Classe qui s'occupe des animations
class spriteAnimation(pygame.sprite.Sprite):

    def __init__(self, spriteName):
        super(spriteAnimation, self).__init__()
        self.image = pygame.image.load(f"assets/{spriteName}.png")
        self.currentImage = 0
        self.images = animations.get(spriteName)
        self.animation = False

    #Methode pour démarer l'animation
    def startAnimation(self):
        self.animation = True

    #Methode pour animer le sprite
    def animate(self, loop=False):

        #Verifir si l'animation est active
        if self.animation:

            #Passage a l'image suivante
            self.currentImage += 1
            #Verifier si on est a la fin de l'animation
            if self.currentImage >= len(self.images):
                #Remettre l'animation
                self.currentImage = 0

                #Verifier si l'animation n'est pas en boucle
                if loop is False:

                    #Desactivation de l'animation
                    self.animation = False


            #Modifier l'image precedente par la suivante
            self.image = self.images[self.currentImage]


#Fonction qui permet de charger les images d'un sprite
def loadAnimationImages(spriteName):
    #Chargement des images
    images = []
    path = f"assets/{spriteName}/{spriteName}"

    #Boucler sur chaque image dans ce dossier
    for num in range(1, 11):
        imagePath = path + str(num) + ".png"
        images.append(pygame.image.load(imagePath))

    #Renvoyer le contenu de la liste d'image
    return images

#Dictionnaire qui va contenir le chargement d'image de chaque sprite
animations = {
    "monster_level1": loadAnimationImages('monsterLevel1'),
    "slave": loadAnimationImages('slave'),
    "mainPlayer1Red": loadAnimationImages("mainPlayer1Red"),
    "bigBoss": loadAnimationImages("bigBoss"),
    "mainPlayer1Blue": loadAnimationImages("mainPlayer1Blue"),
    "mainPlayer1Yellow": loadAnimationImages("mainPlayer1Yellow"),
    "bigPharaon": loadAnimationImages("bigPharaon"),
    "camel": loadAnimationImages("camel")
}
import pygame

#Class pour gérer les audios
class manageAudio:

    def __init__(self):
        self.audios = {
            #Clefs des différents audios
            'click': pygame.mixer.Sound("assets/sounds/click.mp3"),
            'gameOver': pygame.mixer.Sound("assets/sounds/gameOver.wav"),
            'projectileColision': pygame.mixer.Sound("assets/sounds/projectileColision.wav"),
            'bossAppear': pygame.mixer.Sound("assets/sounds/bossAppear.wav"),
            'keyboardType': pygame.mixer.Sound("assets/sounds/keyboardType.wav"),
            'pseudoValidation': pygame.mixer.Sound("assets/sounds/pseudoValidation.wav"),
            'error': pygame.mixer.Sound("assets/sounds/error.wav"),
            'openInventory': pygame.mixer.Sound("assets/sounds/openInventory.wav"),
        }

    #Methode pour appeler l'audio qui correspond au soundName
    def play(self, soundName):
        self.audios[soundName].play()
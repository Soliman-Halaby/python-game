import pygame
import math

# Importation de la baniere
banner = pygame.image.load('assets/mainMenu/banner.png')
bannerRect = banner.get_rect()
bannerRect.x = 152
bannerRect.y = 40

#Importation du pseudo
pseudoInput = pygame.image.load('assets/mainMenu/pseudo.png')
pseudoInputRect = pseudoInput.get_rect()
pseudoInputRect.x = 350
pseudoInputRect.y = 455

# Importation du boutton play
startButton = pygame.image.load('assets/mainMenu/button.png')
startButtonRect = startButton.get_rect()
startButtonRect.x = 360
startButtonRect.y = 543

#Boutton pour changer le personnage principal
changePlayer = pygame.image.load('assets/mainMenu/menuButton.png')
changePlayerRect = changePlayer.get_rect()
changePlayerRect.x = 870
changePlayerRect.y = 20

#Boutton pour quitter le changement de personnage principal
quitButton = pygame.image.load('assets/choiceMenu/returnButton.png')
quitButtonRect = quitButton.get_rect()
quitButtonRect.x = 50
quitButtonRect.y = 650

#Boutton Joueur principal bleu
mainPlayerBlueButton = pygame.image.load('assets/choiceMenu/mainPlayerBlueButton.png')
mainPlayerBlueButtonRect = mainPlayerBlueButton.get_rect()
mainPlayerBlueButtonRect.x = 70
mainPlayerBlueButtonRect.y = 180

#Boutton Joueur principal jaune
mainPlayerYellowButton = pygame.image.load('assets/choiceMenu/mainPlayer1YellowButton.png')
mainPlayerYellowButtonRect = mainPlayerBlueButton.get_rect()
mainPlayerYellowButtonRect.x = 445
mainPlayerYellowButtonRect.y = 180

#Boutton Joueur principal Rouge
mainPlayerRedButton = pygame.image.load('assets/choiceMenu/mainPlayer1RedButtonSelected.png')
mainPlayerRedButtonRect = mainPlayerRedButton.get_rect()
mainPlayerRedButtonRect.x = 820
mainPlayerRedButtonRect.y = 180

#Affichage des éléments quand le jeu est en pause
gameInventory = pygame.image.load('assets/inventoryMenu/inventory.png')
gameInventoryRect = gameInventory.get_rect()
gameInventoryRect.x = 150
gameInventoryRect.y = 90

#Premier item de l'inventairie
firstItemButton = pygame.image.load('assets/inventoryMenu/firstItemButton.png')
firstItemButtonRect = firstItemButton.get_rect()
firstItemButtonRect.x = 340
firstItemButtonRect.y = 180

#Deuxième item de l'inventairie
secondItemButton = pygame.image.load('assets/inventoryMenu/secondItemButtonCrossed.png')
secondItemButtonRect = firstItemButton.get_rect()
secondItemButtonRect.x = 580
secondItemButtonRect.y = 180

#Troisième item de l'inventairie
thirdItemButton = pygame.image.load('assets/inventoryMenu/thirdItemButtonCrossed.png')
thirdItemButtonRect = thirdItemButton.get_rect()
thirdItemButtonRect.x = 340
thirdItemButtonRect.y = 340

#Quatrième item de l'inventairie
fourthItemButton = pygame.image.load('assets/inventoryMenu/fourthItemButtonCrossed.png')
fourthItemButtonRect = fourthItemButton.get_rect()
fourthItemButtonRect.x = 580
fourthItemButtonRect.y = 340

#Background foncé en arrière plan de l'inventaire
blackBackground = pygame.image.load('assets/inventoryMenu/blackBackground.png')
blackBackgroundRect = blackBackground.get_rect()
blackBackgroundRect.x = 0
blackBackgroundRect.y = 0

#Asset de victoire du jeu
winAsset = pygame.image.load('assets/winMenu/winAsset.png')
winAssetRect = winAsset.get_rect()
winAssetRect.x = 0
winAssetRect.y = 0

#Asset du bouton rejouer
replayButton = pygame.image.load('assets/winMenu/replayButton.png')
replayButtonRect = replayButton.get_rect()
replayButtonRect.x = 500
replayButtonRect.y = 430
import pygame
import menu
import animation

pygame.init()
pygame.font.init()
from game import Game

#Definir une clock
clock = pygame.time.Clock()
FPS = 80

#Creation de notre écran (fenetre de notre jeu)
pygame.display.set_caption(("Un trone poursuivi"))
gameIcon = pygame.image.load("assets/favicon.png")
pygame.display.set_icon(gameIcon)

gameScreen = pygame.display.set_mode((1080, 720))
baseFont = pygame.font.Font(None, 20)
userText = ''
pseudo = ''

#Booléen pour le pseudo
active = False

#Booléen de pause du jeu
gameIsPaused = False

#Booléen de victoire du jeu
gameIsWon = False

#Booléen de démarrage du jeu
isRunning = True

#Booléens pour l'activation des menus (lancement jeu / choix du perso)
mainMenu = True
choiceMenu = False

#Importation de l'arriere plan du jeu
backgroundMenu = pygame.image.load('assets/background_menu.png')


#Chargement de la classe Game
game = Game()

#Boucle qui s'execute tant que le jeu est ouvert
while isRunning:

    #mettre en place le background lorsque le jeu n'a pas commencé et qu'il n'est pas en pause
    if not game.isPlaying and not gameIsPaused:
        gameScreen.blit(backgroundMenu, (0, 0))

    #Condition lorsque le jeu a commencé
    if game.isPlaying:
        #Affichage du packground
        gameScreen.blit(game.background, (0, 0))
        game.updateComponent(gameScreen, pseudo)
        userText = ''

    else:
        # Condition si on est sur le menu principal
        if mainMenu:
            # ajout de la baniere et du bouton play et de l'input pseudo
            gameScreen.blit(menu.pseudoInput, menu.pseudoInputRect)
            gameScreen.blit(menu.startButton, menu.startButtonRect)
            gameScreen.blit(menu.banner, menu.bannerRect)
            #Affichage d'une surface de texte ou l'on va rentrer notre pseudo
            textSurface = baseFont.render(userText, True, (0, 0, 0))
            gameScreen.blit(textSurface, (395, 500))
            gameScreen.blit(menu.changePlayer, menu.changePlayerRect)

        # Condition si on est sur le menu secondaire
        if choiceMenu:
            gameScreen.blit(menu.quitButton, menu.quitButtonRect)
            gameScreen.blit(menu.mainPlayerBlueButton, menu.mainPlayerBlueButtonRect)
            gameScreen.blit(menu.mainPlayerYellowButton, menu.mainPlayerYellowButtonRect)
            gameScreen.blit(menu.mainPlayerRedButton, menu.mainPlayerRedButtonRect)

        #Condition si on est sur l'ecran de l'inventaire
        if gameIsPaused:
            gameScreen.blit(menu.firstItemButton, menu.firstItemButtonRect)
            gameScreen.blit(menu.secondItemButton, menu.secondItemButtonRect)
            gameScreen.blit(menu.thirdItemButton, menu.thirdItemButtonRect)
            gameScreen.blit(menu.fourthItemButton, menu.fourthItemButtonRect)

    #Condition si le joueur arrive au niveau 5
    if game.player.level == 2:
        #Le jeu s'arrête
        game.isPlaying = False
        #Le menu principal ne s'affichage pas
        mainMenu = False
        #Le booléen de gameIsWon devient vrai
        gameIsWon = True
        #Affichage des éléments de la victoire du jeu (l'écran et le bouton rejouer)
        gameScreen.blit(menu.winAsset, menu.winAssetRect)
        gameScreen.blit(menu.replayButton, menu.replayButtonRect)

    # mise a jour de la fenetre
    pygame.display.flip()

    #Pour tout evenement se produisant sur notre fenetre
    for event in pygame.event.get():

        # Verification de la fermeture de la fenetre
        if event.type == pygame.QUIT:
            #Arrêt du jeu lors de la fermeture de la fenetre
            isRunning = False
            #Quitter le jeu
            pygame.quit()

        #Detection lors d'un keydown
        elif event.type == pygame.KEYDOWN:
            game.keyPressed[event.key] = True
            #Si le jeu n'a pas encore commencé et qu'active est vrai
            if active and game.isPlaying == False:
                game.manageSound.play("keyboardType")
                # Suppression d'un caractère écris dans l'input lorsqu'on clique sur backspace
                if event.key == pygame.K_BACKSPACE:
                    #On retire un caractère à chaque fois qu'on utilise backspace
                    userText = userText[: -1]
                #Si l'on appuie sur rentrer
                elif event.key == pygame.K_RETURN:
                    #Pseudo prend la valeur de notre userText
                    pseudo = userText
                    #Jeu de l'audio de validation
                    game.manageSound.play("pseudoValidation")
                else:
                    #Usertext prend la valeur de chaque valeur de la touche utilisée
                    userText += event.unicode
            #Envoie du projectile lorsqu'on appuie sur espace
            if event.key == pygame.K_SPACE:
                game.player.sendArrow()

            # Mettre en pause / reprendre le jeu lorsqu'on ouvre / ferme l'inventaire
            if event.key == pygame.K_h:
                game.manageSound.play("openInventory")
                #On n'affiche pas le menu secondaire
                choiceMenu = False
                #Affichage des elements de l'inventaire
                if game.isPlaying == True:
                    gameScreen.blit(menu.blackBackground, menu.blackBackgroundRect)
                    gameScreen.blit(menu.gameInventory, menu.gameInventoryRect)
                    #On n'affiche pas le menu principal
                    mainMenu = False
                    #On affiche les éléments de gameIsPaused définie au début
                    gameIsPaused = True
                    #On met le jeu en pause
                    game.isPlaying = False
                #Reprise du jeu, inversement de chaque valeur
                elif game.isPlaying == False and gameIsPaused:
                    game.isPlaying = True
                    gameIsPaused = False
                    mainMenu = True

        elif event.type == pygame.KEYUP:
            game.keyPressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Condition si l'on arrive au niveau ou l'on gagne la partie
            if gameIsWon:
                #Si on clique sur le bouton rejouer
                if menu.replayButtonRect.collidepoint(event.pos):
                    game.manageSound.play('click')
                    #La partie n'est plus gagnée
                    gameIsWon = False
                    #Ré affichage des éléments du menu principal
                    mainMenu = True
                    #Reinitialisation des éléments du jeu
                    game.gameOver()

            #Selection de chaque item de l'inventaire
            if gameIsPaused:
                gameScreen.blit(menu.gameInventory, menu.gameInventoryRect)
                gameScreen.blit(menu.firstItemButton, menu.firstItemButtonRect)
                gameScreen.blit(menu.secondItemButton, menu.secondItemButtonRect)
                gameScreen.blit(menu.thirdItemButton, menu.thirdItemButtonRect)
                gameScreen.blit(menu.fourthItemButton, menu.fourthItemButtonRect)
                #Creation du texte de l'inventaire sans contenu
                inventoryTexte = pygame.font.SysFont("Courier", 12).render("", True, (255, 0, 0))

                #S'il y a une collision avec le permier item de l'inventaire
                if menu.firstItemButtonRect.collidepoint(event.pos):
                    #Le projectile change d'asset
                    game.player.projectile = 'projectileLevel1'
                    #Jeu de l'audio lorsqu'on clique
                    game.manageSound.play('click')

                if game.player.level >= 2 and menu.secondItemButtonRect.collidepoint(event.pos):
                    game.player.projectile = 'projectileLevel2'
                    game.manageSound.play('click')

                if game.player.level < 2 and menu.secondItemButtonRect.collidepoint(event.pos):
                    game.manageSound.play("error")
                    #Remplissage d'inventoryTexte par un texte disant que le niveau n'est pas assez haut pour séléctionner cet item
                    inventoryTexte = pygame.font.SysFont("Courier", 12).render("Vous devez être niveau 2 pour séléctionner cet objet", True, (255, 0, 0))

                if game.player.level >= 3 and menu.thirdItemButtonRect.collidepoint(event.pos):
                    game.player.projectile = 'projectileLevel3'
                    game.manageSound.play('click')

                if game.player.level < 3 and menu.thirdItemButtonRect.collidepoint(event.pos):
                    game.manageSound.play("error")
                    inventoryTexte = pygame.font.SysFont("Courier", 12).render("Vous devez être niveau 3 pour séléctionner cet objet", True, (255, 0, 0))

                if game.player.level >= 4 and menu.fourthItemButtonRect.collidepoint(event.pos):
                    game.player.projectile = 'projectileLevel4'
                    game.manageSound.play('click')

                if game.player.level < 4 and menu.fourthItemButtonRect.collidepoint(event.pos):
                    game.manageSound.play("error")
                    inventoryTexte = pygame.font.SysFont("Courier", 12).render("Vous devez être niveau 4 pour séléctionner cet objet", True, (255, 0, 0))
                gameScreen.blit(inventoryTexte, (370, 165))

            #Condition pour éviter la présence du bouton sur le menu de choix des personnages
            if mainMenu:
                #Debut du jeu lorsqu'on appuie sur le bouton start
                if menu.startButtonRect.collidepoint(event.pos) and not game.isPlaying:
                    game.startGame()
                    #Faire jouer le son
                    game.manageSound.play('click')

                if menu.changePlayerRect.collidepoint(event.pos) and not game.isPlaying:
                    #Passage au menu de choix des personnages
                    mainMenu = False
                    choiceMenu = True
                    game.manageSound.play('click')

            #Si l'on est sur le menu du choix des personnages
            if choiceMenu:
                #Si l'on clique sur le bouton retour
                if menu.quitButtonRect.collidepoint(event.pos) and not game.isPlaying:
                    #Apparition de mainMenu (le menu principal)
                    mainMenu = True
                    #On retire le menu de choix des personnages
                    choiceMenu = False
                    game.manageSound.play('click')

                #Conditions pour changer la couleur du personnage selon le choix
                #Si clique sur le bouton bleu
                if menu.mainPlayerBlueButtonRect.collidepoint(event.pos) and not game.isPlaying:
                    game.manageSound.play('click')
                    #Affichage du personnage bleu avec les animations
                    animation.spriteAnimation.__init__(game.player, "mainPlayer1Blue")
                    #Retire l'affichage du personnage bleu
                    menu.mainPlayerBlueButton = pygame.image.load('./assets/choiceMenu/mainPlayer1BlueButtonSelected.png')
                    #Affiche le personnage rouge ou jaune (si jamais ils étaient séléctionnés avant)
                    menu.mainPlayerRedButton = pygame.image.load('./assets/choiceMenu/mainPlayer1RedButton.png')
                    menu.mainPlayerYellowButton = pygame.image.load('./assets/choiceMenu/mainPlayer1YellowButton.png')

                if menu.mainPlayerYellowButtonRect.collidepoint(event.pos) and not game.isPlaying:
                    game.manageSound.play('click')
                    animation.spriteAnimation.__init__(game.player, "mainPlayer1Yellow")
                    menu.mainPlayerBlueButton = pygame.image.load('./assets/choiceMenu/mainPlayerBlueButton.png')
                    menu.mainPlayerYellowButton = pygame.image.load('./assets/choiceMenu/mainPlayer1YellowButtonSelected.png')
                    menu.mainPlayerRedButton = pygame.image.load('./assets/choiceMenu/mainPlayer1RedButton.png')

                if menu.mainPlayerRedButtonRect.collidepoint(event.pos) and not game.isPlaying:
                    game.manageSound.play('click')
                    animation.spriteAnimation.__init__(game.player, "mainPlayer1Red")
                    menu.mainPlayerBlueButton = pygame.image.load('./assets/choiceMenu/mainPlayerBlueButton.png')
                    menu.mainPlayerYellowButton = pygame.image.load('./assets/choiceMenu/mainPlayer1YellowButton.png')
                    menu.mainPlayerRedButton = pygame.image.load('./assets/choiceMenu/mainPlayer1RedButtonSelected.png')

            active = True

    #Fixer le nombre de FPS sur la Clock
    clock.tick(FPS)




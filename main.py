print('1 - Nouvelle partie')
print('2 - Informations')
print('3 - Quitter')

ChoixMenu = int(input())

if ChoixMenu == 1:
    newGame()
    print('Nouvelle partie')

elif ChoixMenu == 2:
    info()

else:
    leave()
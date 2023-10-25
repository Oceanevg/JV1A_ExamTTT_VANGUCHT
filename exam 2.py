#grille = [3][3]  <- cours sur le damier mais ne marche pas

# grille = [0,0,0, #marche pas non plus, ne fais qu'une ligne
#            0,0,0,
#            0,0,0]
# print (grille)

# for i in range (len(grille)):
#     element = int(input("voulez vous jouer un O (tapez 0) ou un X (tapez 1)? \n"))

#     if(element == 0):
#         case = int(input("de 1 à 9 en se basant sur un pad numerique inversé, dans quel case souhaitez vous mettre votre rond ? \n"))
#         grille[case - 1] = 'O'
        

#     else: 
#         case = int(input("de 1 à 9 en se basant sur un pad numerique inversé, dans quel case souhaitez vous mettre votre croix ? \n"))
#         grille[case - 1] = 'X'

#     print (grille)

#marche mais en ligne


def grille(c1,c2,c3,c4,c5,c6,c7,c8,c9):   #malheureusement ce n'est pas un tableau mais c'est tout ce que j'ai
    print (c1,c2,c3)
    print (c4,c5,c6)
    print (c7,c8,c9)

grille("_","_","_","_","_","_","_","_","_")



for i in range(0,9):
    element = int(input("voulez vous jouer un O (tapez 0) ou un X (tapez 1)? \n"))
    if(element == 0):
        case = int(input("de 1 à 9 en se basant sur un pad numerique inversé, dans quel case souhaitez vous mettre votre rond ? \n"))
        if(case ==1):     
            print (grille("O","_","_","_","_","_","_","_","_"))
        if(case ==2):     
            print (grille("_","O","_","_","_","_","_","_","_"))
        if(case ==3):     
            print (grille("_","_","O","_","_","_","_","_","_"))
        if(case ==4):     
            print (grille("_","_","_","O","_","_","_","_","_"))
        if(case ==5):     
            print (grille("_","_","_","_","O","_","_","_","_"))
        if(case ==6):     
            print (grille("_","_","_","_","_","O","_","_","_"))
        if(case ==7):     
            print (grille("_","_","_","_","_","_","O","_","_"))
        if(case ==8):     
            print (grille("_","_","_","_","_","_","_","O","_"))
        if(case ==9):     
            print (grille("_","_","_","_","_","_","_","_","O"))

    else: 
        case = int(input("de 1 à 9 en se basant sur un pad numerique inversé, dans quel case souhaitez vous mettre votre croix ? \n"))
        if(case ==1):     
            print (grille("X","_","_","_","_","_","_","_","_"))
        if(case ==2):     
            print (grille("_","X","_","_","_","_","_","_","_"))
        if(case ==3):     
            print (grille("_","_","X","_","_","_","_","_","_"))
        if(case ==4):     
            print (grille("_","_","_","X","_","_","_","_","_"))
        if(case ==5):     
            print (grille("_","_","_","_","X","_","_","_","_"))
        if(case ==6):     
            print (grille("_","_","_","_","_","X","_","_","_"))
        if(case ==7):     
            print (grille("_","_","_","_","_","_","X","_","_"))
        if(case ==8):     
            print (grille("_","_","_","_","_","_","_","X","_"))
        if(case ==9):     
            print (grille("_","_","_","_","_","_","_","_","X"))
# ya un truc mais le premier reste pas, ça se reinitialise à chaque fois
print (grille)





#3 et 4) je n'ai pas compris la fonction return mais je pense que pour la 3 il faut verifier avec if 1/2/3 , 4/5/6 etc et si ce sont les memes
# alors fin du jeu et print "victoire des ronds/croix".Et ce serait soit avec des and/or ou juste des ==
# et pour la 4 peut etre un while (caseincomplete = true) où caseincomplete detecterai les cases qui n'ont pas de O ou X/ qui sont vides 
#5) surement for i in range(len(grille)) où la question est repétée plusieurs fois jusqu'a la fin de tableau ou la victoire mais sans
# choix possible, on alterne O et X en ne demandant que "quel case ?"



#6) Pour faire un puissance 4 il faudra juste agrandir le tableau pour qu'il ai les bonnes dimensions et faire en sorte que
# la victoire soit donné à la personne qui à 4 pions alignés et non pas 3
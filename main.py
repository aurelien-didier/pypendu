import random   #import des modules  #import of modules
import sys
import time

running = True  #instanciation des variables  #instanciation of variables
win = False
end = False

chance = 14
aigri = 0
lettre = ""
mot = ""
pendu = []
mode = ""
a = False

    #dictionnaire des mots du pendu (par longueur)
    #dictionary of the words for the game (by length)
list_mot = {
    3: ["Ane", "Axe","Bel","Bip","Car","Col","Coq","Cor","Cou","Cri","Gag","Gaz","Gel","Jus","Net","Nul","Val","Ski","Sot","Tas","Tic"],
    4: ["Atre","Beau","Bête","Boxe","Brun","Cerf","Chez","Cire","Dame","Dent","Dock","Dodo","Drap","Dune","Emeu","Fado","Faux","Ibis","Jazz","Joli","Joue","Kaki","Logo","Loin","Long","Lune","Lynx","Mine","Mûre","Ouïe","Ours","Pion","Rhum","Ride","Rock","Seau","Test","Thym","Trou","Truc","User","Vert","Yogi","Watt"],
    5: ["Acces"],
    6: ["Acajou"],
    7: ["Abriter"],
    8: ["Aquarium"],
    9: ["Accordeon"],
    10: ["Acrostiche"],
    "dur": ["Baccalaureat"]
}

def angry(print1 = "", print2 = "", print3 = "", repetitions = 1) :
    print(print1)

    if print3 != "" :
        for i in range(repetitions) :
            time.sleep(0.5)
            print(print3)

    time.sleep(4)

    print(print2)
    time.sleep(1)

    sys.exit()


        #Partie 1 du code : choix du mode de jeu et détermination du mot à deviner
        #Part 1 of the script : choice of the game mode and determining the word to find

while running:

    mode = input("Choisissez un mode (deflet/undeflet/aide) : ")
    mode = mode.lower()

    while mode not in ["deflet","undeflet","exit"]:

        if mode == "aide":
            print("\nVous jouez au pendu."
                "\n\nle but est de trouver le mot a deviner en donnant des lettres avec un compte d'erreurs de 14 maximum"
                "\nsi vous donnez une bonne lettre tous ses emplacement dans le mot y sera indiqué."
                "\n\nLe mode deflet vous permet de choisir le nombre de lettre dans le mot du pendu : "
                "\nil varie de 3 à 10 lettres et vous pouvez choisir l'option mots longs (11 à 13 lettres)."
                "\nle mode undeflet permet de rendre aléatoire le nombre de lettres : \nil varie donc de 3 à 13."
                "\n\nVous pouvez quitter le jeu en écrivant exit dans les zones de réponses avant le lancement d'une "
                  "partie et pouvez arrêter une partie en écrivant stop dans les zones de réponses durant la partie.")

            mode = input("Choisissez un mode (deflet/undeflet/aide) : ")
            mode = mode.lower()

        else :
            mode = input("ERREUR : choisissez un mode (deflet/undeflet/aide) : ")
            mode = mode.lower()


    if mode == "deflet":
        print(">_ Console //: Salut, je serai ton adversaire. Choisis le nombre de lettre... \n")
        choice = input("choisir le nb de lettre (entre 3 et 10 inclus ou 'mot long') : ")
        choice = choice.lower()

        while choice not in ["mot long","3","4","5","6","7","8","9","exit"] :
            aigri += 1
            choice = input(">_ Console //: Choisit entre 3 et 10 inclus ou 'plus' pour le nombre de lettres sinon je "
                           "pourrais pas t'aider : ")
            choice = choice.lower()

            if aigri >= 4 :
                angry(">_ Console //: C'est fou de pas savoir écrire !", ">_ Console //: bah salut !")
            
        if choice == "exit" :
            print(">_ Console //: Tu veux arrêter ? Ok à plus alors.")
            sys.exit()

        elif choice == "mot long" :
            mot = random.choice(list_mot["dur"])

        else :
            while type(choice) != int :
                try :
                    choice = int(choice)
                except :
                    choice = input(">_ Console //: Je suis désolé il y a eu un problème veuillez retaper votre nombre choisi s'il vous plait : ")

            mot = random.choice(list_mot[choice])
            mot = mot.upper()


    elif mode == "undeflet":
        key = random.choice(list(list_mot.keys()))
        mot = random.choice(list_mot[key])
        mot = mot.upper()

    elif mode == "exit" :
        sys.exit()

    print(">_ Console //: Bon et bien bonne chance !")
    print(mot)

    mode = ""
    choice = ""

        #Partie 2 : pendu
        #Part 2 : the game

    pendu = ["_"] * len(mot)


    while not end :

        if "_" in pendu :
            print(" ".join(pendu))
            lettre = input(f"Donnez une lettre (il vous reste {chance} chances) : ")
            lettre = lettre.upper()

        while not a :

            if not "_" in pendu :
                a = True
                win = True

            elif lettre == "STOP" :
                print(">_ Console //: Bon on arrête...")
                end = True
                a = True

            elif not lettre.isalpha() :
                aigri += 1
                print(" ".join(pendu))
                lettre = input(">_ Console //: donnez une lettre s'il vous plait : ")
                lettre = lettre.upper()

                if aigri > 5 :
                    angry(">_ Console //: Mais t'est insupportable a pas savoir mettre UNE SEULE lettre !", ">_ Console //: Au revoir :) ")


            elif chance > 0 and len(lettre) != 1 :
                print(" ".join(pendu))
                lettre = input(">_ Console //: donnez une seule lettre s'il vous plait : ")
                lettre = lettre.upper()
                aigri += 1

                if aigri > 5 :
                    angry(">_ Console //: Mais t'est insupportable a pas savoir mettre UNE SEULE lettre !", ">_ Console //: Au revoir :) ")


            elif len(lettre) == 1  and chance > 0 :
                    if lettre in mot :
                        for i, c in enumerate(mot) :
                            if c == lettre :
                                pendu[i] = c


                        a = True
                    else :
                        chance -= 1
                        print(" ".join(pendu))
                        lettre = input(f"Donnez une lettre (il vous reste {chance} chances) : ")
                        lettre = lettre.upper()


            elif chance > 0 :
                print(" ".join(pendu))
                lettre = input(">_ Console //: donnez une seule lettre s'il vous plait : ")
                lettre = lettre.upper()
                aigri += 1

            else :
                a = True

        if not win and chance > 0 :
            a = False

        if chance <= 0 :
            print("\n>_ Console //: Vous avez perdu...")
            time.sleep(2)
            print(f"\n>_ Console //: La réponse était : {mot}")
            end = True

        elif win :
            print("\n>_ Console //: Bravo ! Vous avez gagné !")
            end = True


    lettre = ""
    pendu = []
    mot = ""
    chance = 14
    end = False
    a = False

    replay = input("\n>_ Console //: On refais une partie ? (oui/non) : ")
    replay = replay.lower()

    while replay not in ["oui","non", "exit"] :

        replay = input("\n>_ Console //: Réponds par oui ou par non... :  ")
        replay = replay.lower()
        aigri += 1

        if aigri > 5 :
            angry("\n>_ Console //: Ma...s c'est pas si compl<UNK>qué de répondre par OUI ou par N§N !", "\n>_ CoN§ole <UNK> /§: ;) ... §!§", "\n...", aigri)


    if replay == "exit" :
        print(">_ Console //: On s'arrête là ? Ok à plus alors.")
        sys.exit()

    elif replay == "oui" :
        aigri = 0

    elif replay == "non" :
        print(">_ Console //: Donc on s'arrête là ? Ok à plus alors.")
        sys.exit()

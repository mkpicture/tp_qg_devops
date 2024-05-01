import random


def jeu_python(choix):
    while choix.upper() == "OUI":

        print("Le joueur mise sur un numero entre 0 et 49")

        # Génération du numero par la machine
        num_aleatoire = random.randrange(0, 50)
        print(num_aleatoire)
        numero_choisi = int(input("Saisir le numero: "))

        mise = int(input("Saisir montant à parier(Doit être un nombre): "))
        montant = 0
        paiement = 0

        # Les conditions pour la victoire du joueur
        if numero_choisi == num_aleatoire:
            mise_double = mise * 2
            montant += mise_double
            print("Gagné!!")
        elif numero_choisi != num_aleatoire:
            if (numero_choisi % 2 == 0 and num_aleatoire % 2 == 0) or (numero_choisi % 2 != 0 and num_aleatoire % 2 != 0):
                mise_moitie = mise + mise / 2
                montant += mise_moitie
                print("Pas mal!!")

            elif (numero_choisi % 2 != 0 and num_aleatoire % 2 == 0) or (numero_choisi % 2 == 0 and num_aleatoire % 2 != 0):
                print("Perdu!! Vous avez perdu votre mise!!")

        paiement += montant

        choix = input("Voulez vous continuer(OUI ou NON): ").upper()
        if choix.upper() == "NON":
            print("Vous avez gagner: ", "$", paiement)
            print("Bye bye")
            quit()


jeu_python("oui")


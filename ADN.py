class BrinADN:
    def __init__(self, brinAdn):
        self.brinADN = str(brinAdn)
        self.composant = "ATGC"

    def sequenceValide(self, sequence):
        for base in sequence:
            if base.upper() in ["A", "T", "G", "C"]:
                pass
            else:
                print("SequenceException")
                break

    def sousSequence(self, sous_sequence):
        pass

    def doubleBrinAdn(self, autreBrin):
        if self.brinADN == autreBrin:
            print("Yes c'est possible")

            for i in self.brinADN:
                print(i, end=" ")

            print()

            for j in autreBrin:
                print(j, end=" ")
        else:
            print("Pas possible!!")

    def pourcentageBase(self, base):
        # creer une liste qui va comprendre toutes les bases du brin
        liste = []
        # la boucle for va separer lettre par lettre et les mettre comme
        # element de la liste
        for i in self.brinADN:
            liste.append(i)

        nombre = liste.count(base.upper())
        nombre_total_base = len(liste)

        # le pourcentage de la base
        pourcentage = int((nombre / nombre_total_base) * 100)
        print(f"{pourcentage}%")


yes = BrinADN("AACATACGTA")
yes.sequenceValide("ATGCED")
yes.doubleBrinAdn("ADCGTACGTU")
yes.pourcentageBase("a")

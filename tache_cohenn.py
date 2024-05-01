class account:
    def __init__(self,firstname,lastname,typee,first_deposit):
        self.firstname = firstname
        self.lastname = lastname
        self.type = typee
        self.first_deposit = first_deposit
    def retrieve(self,montant):
        print(f"Vous avez retiré {montant},merci")
        self.first_deposit -= montant
    def deposit(self,montant):
         print(f"Vous avez deposé {montant},merci")
         self.first_deposit += montant
    def solde(self):
        print(f"votre solde est de{self.first_deposit}")     

Account1 = account("Cohenn","Ossiala-Ngoli","Compte_bancaire",5000000)
Account2 = account("Eddy","Malou","Credit",15000000)

Account1.retrieve(250000)
Account1.solde()    
        
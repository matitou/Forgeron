#Forgeron

class Forgeron:
    
    def welcome(self):
        user_name = str(input("Quel est ton nom de forgeron"))
        print("Alors bienvenue, forgeron",user_name)

    def options(self):
        choice = int(input("Veux-tu...\n1) récolter des ressources ?\n2) acheter des ressources ?\n3) fabriquer de l'équipement ?\n4) démanteler de l'équipement ?\n5) vendre de l'équipement ?"))
    













if __name__ == '__main__':
    initmain = Forgeron()
    initmain.welcome()
    

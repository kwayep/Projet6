class Client:     
    #Le constructeur initialise les attributs de l'objet     
    def __init__(self,nomInit,prenomInit,adresseInit,ageInit):         
    	self.__nom=nomInit         
    	self.__prenom=prenomInit         
    	self.__age=ageInit         
    	self.__adresse=adresseInit    
    	self.__mesComptes=[] 
 
    def donneNom(self):         
        return self.__nom 
 
    def donneAdresse(self):         
        return self.__adresse 
 
    def demenage(self,newAdresse):         
        self.__adresse=newAdresse 
 
    def donneAge(self):  
        return "age: " + str(self.__age) 
 
    def vieillit(self):         
        self.__age+=1 
 
    def __str__(self):        
        return "client: " + self.__prenom + " " + self.__nom
 
    #cette methode rajoute un compte dans la liste du client    
    #elle s'assure egalement que le compte ait bien son client   
 
    def ajouteCompte(self,compte):         
        self.__mesComptes.append(compte)         
        compte.assigneTitulaire(self) 
 
    def identifieCompte(self):         
        print ("Sur quel compte ?")         
        x=input("?") 
	#cette instruction permet de lire un string                      
        #a l'ecran en promptant avec un "?"         
        for c in self.__mesComptes:             
            if c.donneNumero() == x:                                  
                break         
            return c 
    
    def versement(self):
        c = self.identifieCompte()
        print("quel montant !")
        x = int(input(""))
        c.versement(x)
        return x

    def retire(self)
        c = self.identifieCompte()
        print("quel montant ? ")
        x = int(intput(""))
        c.retire(x)


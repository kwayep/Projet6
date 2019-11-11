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
 

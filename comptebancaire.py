# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:18:42 2019

@author: idriss
"""

class CompteBancaire(object):
    _modele="210-"
    _nombreComptes=0
    
    def _init_(self):
        self._solde=0
        self._titulaire=""
        self._numero=CompteBancaire._modele + \
            str(CompteBancaire._nombreComptes)
        CompteBancaire._nombreComptes+=1

    def depot(self,montant):

    	self.solde+=montant

    def retrait(self,montant):
    	self.solde-=montant

    def afficher(self):
    	print("le solde du compte bancaire  %s est de %.2f FRCS " %(self.nom,self.solde))

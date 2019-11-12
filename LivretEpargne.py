# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:14:15 2019

@author: pc
"""

class LivreEpargne(CompteBancaire):
    _soldeMinmal=0
    _interet=0.1
    def calculInteret(self):
       depose(donneSolde()*_interet)
    
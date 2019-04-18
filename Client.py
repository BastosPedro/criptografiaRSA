#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:37:49 2019

@author: pedro
"""

from os.path import getsize 
from User import User
from RSACoding import RSACoding

class Client:
    def __init__(self):
        self.userList = list()
        self.rsamodule = RSACoding()
        print("cliente iniciado, iniciando leitura...")
        self.loadData()
        print("dados carregados")
    
    def addUser(self, usernameInput, passwordInput):
        if self.checkUser(usernameInput) == True:
            raise Exception ("usuario ja existe")
        else:
            newUser = User(usernameInput, passwordInput)
            self.userList.append(newUser)
            return newUser
        
    def removeUser(self, searchedUser):
        for x in self.userList:
            if x.username == searchedUser:
                self.userList.remove(x)
                return
        else:
            raise Exception ("esse usuario nao existe")
            
    def checkUser(self, searchedUser):
        for x in self.userList:
            if x.username == searchedUser:
                return True
        return False
    
    def loadData(self):
        if getsize ("data.txt") > 0:
            file = open("data.txt", "r")
            data = file.read().split()
            publicKey = tuple(map(int,data[0][1:-1].split(',')))
            privateKey = data[1]
            privateKey = privateKey.replace('(', '')
            privateKey = privateKey.replace(')', '')
            privateKey = int(privateKey)
            self.rsamodule.setup(publicKey, privateKey)
            
            for x in range (2, len(data)):
                if x%2 == 0:
                    auxUser = self.rsamodule.decrypto(data[x])
                else:
                    auxPassword = self.rsamodule.decrypto(data[x])
                    self.addUser(auxUser, auxPassword)
                    
                #self.addUser(auxUser, auxPassword)
            return
        else:
            self.rsamodule.setup()
    
    def terminate(self):
        a = self.rsamodule.publicKey
        b = self.rsamodule.privateKey
        file = open("data.txt", "w")
        file.write('('+ str(a[0]) + ',' + str(a[1]) + ') ')
        file.write('(' + str(b) + ')' + '\n')
        for x in self.userList:
            file.write(self.rsamodule.crypto(x.username, a) + '\n')
            file.write(self.rsamodule.crypto(x.password, a) + '\n')
        file.close()
        

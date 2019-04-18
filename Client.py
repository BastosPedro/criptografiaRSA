#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:37:49 2019

@author: pedro
"""

from os.path import isfile
from User import User
from RSACoding import RSACoding

class Client:
    """A classe cliente, a rigor, manipula instancias das classes RSACoding e User"""
    def __init__(self):
        """Instancia a classe, chamando o metodo load para carregar os dados anteriores"""
        self.userList = list()
        self.rsamodule = RSACoding()
        print("cliente iniciado, iniciando leitura...")
        self.loadData()
        print("dados carregados")
    
    def addUser(self, usernameInput, passwordInput):
        """Adiciona uma nova instancia de usuario para a lista de usuarios, se ja nao existir"""
        if self.checkUser(usernameInput) == True:
            raise Exception ("usuario ja existe")
        else:
            newUser = User(usernameInput, passwordInput)
            self.userList.append(newUser)
            return newUser
        
    def removeUser(self, searchedUser):
        """Remove uma instancia de usuario para a lista de usuarios, se ja existir"""
        for x in self.userList:
            if x.username == searchedUser:
                self.userList.remove(x)
                return
        else:
            raise Exception ("esse usuario nao existe")
            
    def checkUser(self, searchedUser):
        """Checa se o usuario ja existe na lista de usuarios"""
        for x in self.userList:
            if x.username == searchedUser:
                return True
        return False
    
    def loadData(self):
        """Carrega o arquivo de dados, descriptografa, e os reinstancia dentro do objeto"""
        if isfile("data.txt") == True: #checa se arquivo existe
            file = open("data.txt", "r") #abre arquivo
            data = file.read().split()
            publicKey = tuple(map(int,data[0][1:-1].split(','))) #tira a chave publica do arquivo
            privateKey = data[1]
            privateKey = privateKey.replace('(', '')
            privateKey = privateKey.replace(')', '')
            privateKey = int(privateKey) #tira a chave privada do arquivo
            self.rsamodule.setup(publicKey, privateKey) #carrega as chaves na instancia
            
            for x in range (2, len(data)): #preenche os dados de volta na lista
                if x%2 == 0:
                    auxUser = self.rsamodule.decrypto(data[x])
                else:
                    auxPassword = self.rsamodule.decrypto(data[x])
                    self.addUser(auxUser, auxPassword)
                    
            return
        else: #se o arquivo estiver em branco, quer dizer que o progama foi rodado pela primeira vez
            self.rsamodule.setup()
    
    def terminate(self):
        """Salva os dados criptografados em um arquivo, de acordo com a formatacao exigida"""
        a = self.rsamodule.publicKey
        b = self.rsamodule.privateKey
        file = open("data.txt", "w")
        file.write('('+ str(a[0]) + ',' + str(a[1]) + ') ')
        file.write('(' + str(b) + ')' + '\n')
        for x in self.userList:
            file.write(self.rsamodule.crypto(x.username, a) + '\n')
            file.write(self.rsamodule.crypto(x.password, a) + '\n')
        file.close()
        

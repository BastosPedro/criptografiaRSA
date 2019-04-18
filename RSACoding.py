#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:54:14 2019

@author: pedro
"""
import support


class RSACoding:
    def __init__(self):
        print("modulo rsa instanciado") 
        self.publicKey = None
        self.privateKey = None

    
    def setup(self, publicKeyInput = None, privateKeyInput = None):                   
        if self.publicKey != None and self.privateKey != None:
            print("ja existem chaves, ze")
            return self.publicKey
        elif publicKeyInput is None and privateKeyInput is None:
            aux = self.create_Keys(100,200)
            self.publicKey = (aux[0],aux[1])
            self.privateKey = (aux[2])
            print("eita, nem existiam chaves, criando!")
        else:
            print("ah, blz, as chaves tao sendo carregadas, tranquilo")
            self.publicKey = publicKeyInput
            self.privateKey = privateKeyInput
            
        return self.publicKey
           
        
    def create_Keys(self, begin,end):
        p = support.randomPrime(begin,end)
        q = support.randomPrime(begin,end)
        n = p*q
        lamb = support.getLambda(p,q)
        e = support.getCoprime(lamb)
        d = support.modInverse(e,lamb)
        return (n,e,d)
    
    def crypto(self, m, pubKey):
        numbers = self.convertToAscii(m)
        aux = list()
        for x in numbers:
            aux.append(pow(x, pubKey[1], pubKey[0]))      
        return self.backToChar(aux)
    
 
    def decrypto(self, c):
        stuff = self.simpleConvertToAscii(c)
        aux = list()
        for x in stuff:
            aux.append(pow(x, self.privateKey, self.publicKey[0]))
        return self.backToChar(aux)
    
    def convertToAscii(self, message): 
        stuff = list()
        for x in range(0, len(message)):
            if ord(message[x]) < 97 and ord(message[x]) != 32:
                raise Exception ("essa mensagem nao rola, man")
            elif ord (message[x]) > 122 and ord(message[x]) != 32:
                raise Exception ("essa mensagem nao rola, man")
            else:
                stuff.append(ord(message[x]))
        return stuff
    
    def simpleConvertToAscii(self, message):
        stuff = list()
        for x in message:
            stuff.append(ord(x))
        return stuff
    
    def backToChar(self, numbers):
        stuff = list()
        for x in range(0, len(numbers)):
            stuff.append(chr(numbers[x]))
        string = ''.join(stuff)
        return string
    

    
    
#teste = RSACoding()
#teste.setup()
#a = teste.publicKey
#b = teste.privateKey
#texto = "feijao com arroz"
#cripto = teste.crypto(texto, a)
#file = open("Chines.txt", "w")
#file.write(cripto + '\n')
#file.write(teste.crypto("arara",a) + '\n')
#file.write(teste.crypto("banana",a) + '\n')
#file.write(teste.crypto("mamao",a) + '\n')
#file.write(teste.crypto("pastel de flango",a) + '\n')
#file.close()
#volta = teste.decrypto(cripto)
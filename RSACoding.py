#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:54:14 2019

@author: pedro
"""
import support


class RSACoding:
    """Reponsavel pela geracao de chaves, criptografia e descriptografia de mensagens"""
    def __init__(self):
        """Instancia a classe"""
        print("modulo rsa instanciado") 
        self.publicKey = None
        self.privateKey = None

    
    def setup(self, publicKeyInput = None, privateKeyInput = None):
        """Checa se ja existem chaves, ou se elas foram fornecidas, caso contrario, chama a funcao de criar chaves"""                
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
        """cria novas chaves aleatorias"""
        p = support.randomPrime(begin,end)
        q = support.randomPrime(begin,end)
        n = p*q
        lamb = support.getLambda(p,q)
        e = support.getCoprime(lamb)
        d = support.modInverse(e,lamb)
        return (n,e,d)
    
    def crypto(self, m, pubKey):
        """criptgrafa a mensagem"""
        numbers = self.convertToAscii(m)
        aux = list()
        for x in numbers:
            aux.append(pow(x, pubKey[1], pubKey[0]))      
        return self.backToChar(aux)
    
 
    def decrypto(self, c):
        """decodifica a mensagem codificada"""
        stuff = self.simpleConvertToAscii(c)
        aux = list()
        for x in stuff:
            aux.append(pow(x, self.privateKey, self.publicKey[0]))
        return self.backToChar(aux)
    
    def convertToAscii(self, message): 
        """metodo auxiliar, converte a mensagem em string para uma lista de valores ascii, fazendo tratamento de erros, usada na codificacao"""
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
        """metodo auxiliar, converte a mensagem de string para uma lista de valores ascii, sem fazer tratamento, usada na decodificacao"""
        stuff = list()
        for x in message:
            stuff.append(ord(x))
        return stuff
    
    def backToChar(self, numbers):
        """metodo auxiliar, transforma a lista de valores ascii de volta para uma string"""
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
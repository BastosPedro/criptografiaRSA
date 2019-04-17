#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:54:14 2019

@author: pedro
"""
import support


class RSACoding:
    def __init__(self, publicKeyInput, privateKeyInput):
        if publicKeyInput is None or privateKeyInput is None:
            aux = self.create_Keys(1000,2000)
            self.publicKey = (aux[0],aux[1])
            self.privateKey = (aux[2])
            print ("rodou")
        else:
            try:
                self.publicKey =  publicKeyInput
                self.privateKey = privateKeyInput
            except 3**(publicKeyInput*privateKeyInput) != 3:
                print("chaves nao funcionam")
            except ValueError:
                print("formato errado parceiro")
                
        
    def create_Keys(self, begin,end):
        p = support.randomPrime(begin,end)
        q = support.randomPrime(begin,end)
        n = p*q
        lamb = support.getLambda(p,q)
        e = support.getCoprime(lamb)
        d = support.modInverse(e,lamb)
        return (n,e,d)

teste = RSACoding(None,None)
a = teste.publicKey
b = teste.privateKey
teste2 = RSACoding(3,2)
#a = teste.create_Keys(1000,10000)
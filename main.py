#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 01:57:08 2019

@author: pedro
"""

from Client import Client

def main ():
    """A main garante que a classe Client seja utilizada corretamente"""
    turnoff = False
    underlying = Client()
    option = 0
    while  turnoff == False:
        if int(option) == 0:
            print("Bem vindo ao progama da criptografia\nEscolha suas opcoes:\n")
            option = input("1)Adicionar usuario\n2)Remover Usuario\n3)Checar se usuario existe\n4)Fechar\n")
        elif int(option) == 1:
            userInput = input("Insira o nome do usuario: ")
            userPassword = input("Insira a senha: ")
            underlying.addUser(userInput, userPassword)
            option = 0
        elif int(option) == 2:
            userInput = input("Insira o nome do usuario: ")
            underlying.removeUser(userInput)
            option = 0
        elif int(option) == 3:
            userInput = input("Insira o nome do usuario: ")
            print(underlying.checkUser(userInput))
            option = 0
        elif int(option) == 4:
            print("Salvando os dados criptografados...")
            underlying.terminate()
            del underlying
            turnoff = True
        else:
            print(print("essa opcao nao existe!"))
            
    print("Fechando...")
    return 
            
            
main()         
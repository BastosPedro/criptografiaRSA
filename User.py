#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:43:15 2019

@author: pedro
"""

class User:
    """essa classe faz nada, suas instancias sao apenas armazenadas na classe client"""
    def __init__(self, nameInput, passwordInput):
        """instancia a classe, de acordo com as informacoes passadas"""
        self.username = nameInput
        self.password = passwordInput
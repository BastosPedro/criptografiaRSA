#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:05:13 2019

@author: pedro
"""
"""Esse codigo tem apenas funcoes de carater auxiliar para o RSACoding"""

from math import gcd
from random import uniform

def lcm (a,b): 
    """minimo multimo comum"""
    return a*b/gcd(a,b)

def isPrime (n): 
    """numero primo ou não"""
    return all(n%i for i in range(2,n))

def randomPrime(a,b): 
    """retorna um numero primo aleatorio dentro de a e b"""
    candidate = 4
    while isPrime(candidate) == False:
        candidate = int(uniform(a,b))
    return candidate

def getLambda(a,b): 
    """retorna o lambda dos numeros aleatorios"""
    return int(lcm(a-1,b-1))

def getCoprime(n): 
    """procura um numero coprimo ao dado"""
    candidate = 0
    while gcd(candidate, n) != 1:
        candidate = int(uniform(2,n-1))
    return candidate

def modInverse(a,m): 
    """calcula o modulo multiplacativo inverso"""
    a = a%m
    for x in range(1,m):
        if((a*x)%m == 1):
            return x
    return x


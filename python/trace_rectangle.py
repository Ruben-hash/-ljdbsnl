# -*- coding: utf-8 -*-
#!/usr/bin/env python3
Longueur = int(input("longueur"))
Largeur = int(input("Largeur"))

from turtle import *
for i in range(2):
    forward(Longueur)
    right(90)
    forward(Largeur)
    right(90)
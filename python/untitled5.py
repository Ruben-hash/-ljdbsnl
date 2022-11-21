# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from turtle import *
pixel_carré = int(input("pixel"))
a = int(input("nombre de carré"))
espace = int(input("eespace"))
b = 0
while b != a:
    for i in range(4):
        forward(pixel_carré*b)
        left(90)
    b +=1





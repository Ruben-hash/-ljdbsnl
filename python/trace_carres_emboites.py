# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from turtle import *
pixel_carré = int(input("pixel"))
a = int(input("nombre de carré"))
espace = int(input("eespace"))
for i in range(a):
    for i in range(4):
        forward(pixel_carré)
        left(90)
    up()
    backward(espace)
    right(90)
    forward(espace)
    left(90)
    down()
    pixel_carré += espace+5
    





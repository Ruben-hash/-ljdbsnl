#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *
pixel = int(input("longueur:"))
augmentation = int(input("up:"))
for i in range(int(pixel/5)):
        forward(pixel)
        right(90)
        pixel += augmentation
        
# -*- coding: utf-8 -*-
"""Homework2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bxf_5gxpazDgNOGilrSzMvXdqPvBey4T
"""

N=int(input("How many sticks (N) in the pile: "))
print("There are ",N,"sticks in the pile.")
name=input("What is your name :")
time=0
while N>0:
  st=int(input(name+", how many sticks you will take (1 or 2): "))
  if st<=0 :
    print("No, you cannot take more less than 1 stick!")
  elif st>2 :
    print("No, you cannot take more than 2 sticks!")
  elif st>N:
    print("There are no enough sticks to take")
  else:
    N=N-st
    time=time+1
    print("There are",N,"sticks in the pile")
print("OK, There is no stick left in the pile. You spent ",time," times")
print("hello")
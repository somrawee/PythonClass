#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:23:54 2022

@author: somrawee
"""

number=""
prex=""


def get_number(n):
    num_list=[]
    for i in range(n):
        num=input('Please enter number: ')
        num_list.append(num)
    print('Your listed number: ',num_list)
    return num_list


    

def findLargestNumber(num_list):
    for x in num_list:
        i=num_list.index(x)
        for j in range(i+1,len(num_list)):
            if num_list[i]+num_list[j] < num_list[j]+num_list[i] and i<len(num_list)-1:
           #     print(num_list[i])
                temp=num_list[i]
                num_list[i]=num_list[j]
                num_list[j]=temp
    #print('Sorted List Number is ', num_list)
    lnum=""
    for x in num_list:
        lnum=lnum+x
    return lnum


    
    
 
#for x in num_list:
#    number=number+x
# Main Program    
print("Welcome to Largest Formed Number")   
num_list=get_number(4)
largestnumber=findLargestNumber(num_list)
print('Your largest formed number is ', largestnumber)
    
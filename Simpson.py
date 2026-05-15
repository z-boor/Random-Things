# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 13:01:09 2025

@author: zacha
"""
def f(x):
    return x**4 -2*x+1
def simpson (a, b, N):
    h = (b-a)/N
    I = 1/3*h*(f(a)+f(b))
    for k in range(1,N,2):
        I += 4/3*h*f(a+k*h)
    for k in range(2,N,2):
        I += 2/3*h*f(a+k*h)
    return I 
print(simpson(0,2,10))

#define your function then solve   

def df4(x):
  return 24

def simpson_err(a,b,N):
    h = (b-a)/N # height of function
    I = 1/3*h*(f(a)+f(b))
    for k in range(1,N,2):
        I += 4/3*h*f(a+k*h)
    for k in range(2,N,2):
        I += 2/3*h*f(a+k*h)
    x = (b+a)/2  #a < x < b     
    err = 1*(b-a)**5/(180*N**4) * abs(df4(x))
    return I, err #returns the simpson value  

print(simpson_err(0,2,10))
#!/usr/bin/python -tt

import sys

def fizz_buzz(input):
  for i in range(1, input+1):
    if (i%3 ==0 and i%5 ==0):
      print "fizz buzz"
    if (i%3 == 0):
      print "fizz"
    elif (i%5==0):
      print "buzz"
    else :
      print i

def main():
  fizz_buzz(int(sys.argv[1]))
  
if __name__=='__main__': main()
  
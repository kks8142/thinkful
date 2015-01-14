#!/usr/bin/python -tt
import sys

def fizz_buzz(input):
 count = input

 for i in range(1, count+1):
   if (i%3 == 0 and i%5 ==0):
      print "fizz buzz"
   elif (i%3 == 0):
      print "fizz"
   elif(i%5==0):
      print "buzz"
   else:
      print i
   
def handle_input():
 while True:
   try:
     usr_input=0
     usr_input = int(raw_input("Enter a number, yo!\n"))
     if (type(usr_input) == int):
       fizz_buzz(usr_input)
     break
   except ValueError:
     print "Oops! not a valid arg"


def main():
 if (len(sys.argv) > 1):
     try:
        usr_input = int(sys.argv[1])
        if (type(usr_input) == int):
            fizz_buzz(usr_input)
     except ValueError:
        print "Oops! not a valid arg"
        handle_input()
 else:
   handle_input()

    
if __name__=='__main__': main()
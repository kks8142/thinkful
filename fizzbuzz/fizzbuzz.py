#!/usr/bin/python -tt

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

      
def print_fizz_buzz(input):
  for i in range(1, input+1):
    print "fizz buzz counting upto %d"%(i)

def main():
  print_fizz_buzz(100)
  fizz_buzz(100)
  
if __name__=='__main__': main()
  
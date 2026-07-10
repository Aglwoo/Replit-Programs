import random
import time
import os
import dice
numero = 5
def login():
  logged_in1 = False
  logged_in2 = False
  un=input("Enter your username: ")
  pw=input("Enter your password: ")
  if un == "admin":
    play()
  with open('Login.txt', 'r') as file:
    for line in file:
      if line==un+","+pw+"\n":
        logged_in1 =True
        print("User 1 logged in...")
        time.sleep(1)
  un2=input("Enter your username: ")
  pw2=input("Enter your password: ")
  with open('Login.txt', 'r') as file:
    for line in file:
      if line==un2+","+pw2+"\n" and un != un2:
        logged_in2 =True
        print("User 2 logged in...")
        time.sleep(1)
        play()
      elif un == un2 or logged_in2 == False:
        print("Error:incorrect_credentials/repeated_username")
        logged_in2 = False
    file.close()
  return logged_in1    
  return logged_in2



def create():
  print("hi")
  nun = input("What do you want your username to be? ")
  npw = input("What do you want your password to be? ")
  f = open("Login.txt","a")
  f.write(nun+","+npw+"\n")
  print("Account has been created...")
  f.close()
  one = input("Does your opponent have a second account? 1= Yes 2= No")
  if one == "1":
    print("Ok... Starting the login process...")
  else:
    print("hi")
    nun = input("What do you want your username to be? ")
    npw = input("What do you want your password to be? ")
    f = open("Login.txt","a")
    f.write(nun+","+npw+"\n")
    print("Account has been created...")
    f.close()
  print("thank you...now login and let the games begin")
    
  login()

def menu():
  choice=int(input("\n1. Create account \n2. Login "))
  if  choice == 1:
    create()
  elif choice ==2:
    logged_in = login()

def play():
  bob= 5
  point1 = 0
  #player 1 roll
  while bob == True:
    for i in range(5):
    print("Roll number: ",i+1)
    dice.dicerolled(i,point1,bob)


  


  
menu()

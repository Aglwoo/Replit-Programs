def login():
  user = input("Username: ")
  password = input("Password: ")
  file = open("logins.txt","r")
  for i in range(100):
    #print(file.readline(i))
    line = file.readline(i)
    split = line.split(",")
    print(split)
    if split[0]==user:
      if (split[1].split("\n"))[0]==password:
        print("login successful buddy")
        break
def scores():
  string= input("Name: ")
  scoreyyy=input("Score: ")
  file = open("scores.txt","r")
  for i in range(100):
    line = file.readline(i)
    split = line.split(",")
    if int((split[1].split("\n"))[0])<int(scoreyyy):
      print("updating score at postition",i)
      break
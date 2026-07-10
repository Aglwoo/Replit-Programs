import readline
"""
for i in range(1,10):
  var = input()
  file = open(var+".txt","a")
  file.write("ran_command")
  file.close()
"""
while True:
  line = readline.get_current_history_length()
  file = open("log.txt","a")
  file.close()
  print(line)
  print("hi")
  
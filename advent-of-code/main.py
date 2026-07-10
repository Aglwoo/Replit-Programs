#calories = []
#with open("elf.txt","r") as file:
 # bob = "0"
 # for line in file:
 #   if line != "\n":
#      bob = int(line)+bob
#      print(bob)
      
prev_entry = measurements[0]
increases = 0
for entry in measurements[1:]:
    if entry > prev_entry:
        increases += 1
    prev_entry = entry
    sliding_windows = np.convolve(measurements, np.ones(3), 'valid')
              
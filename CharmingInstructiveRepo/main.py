nums=[23,54,62,16,91,53,78,91]
nums = [16,23,52,54,76,97]
bob= int(input("Num"))
def binsearch(bob):
  halflen = len(nums)/2 + 0.5
  halflen = int(halflen)
  print(halflen)
  if nums[halflen] >bob:
    print("bottom")
    half2 = int(halflen /2 + 0.5)
    
  elif nums[halflen] <bob:
    print("top")


binsearch(bob)
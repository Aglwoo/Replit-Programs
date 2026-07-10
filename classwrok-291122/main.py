  def largest(n1,n2,n3):
  if n1 > n2 and n2>n3:
    print(n1,n2,n3)
  elif n1 > n3 and n3>n2:
    print(n2,n1,n3)

    
  elif n2 > n1 and n1>n3:
    print(n2,n1,n1)
  elif n2 > n3 and n3>n1:
    print(n2,n1,n3)
    
  elif n3 > n2 and n2>n1:
    print(n3,n2,n1)
  elif n3 > n1 and n1>n2:
    print(n3,n1,n2)

largest(13,15,19)
largest(10,2,19)
def book(name,year):
  year = str(year)
  x = name[:3].upper()+year[-2:]
  print(x)
  return x
book("poetry of war", 2012)

discountcodes = [["PVSC",10],["CPU5",5],["BGF2",15]]
def discount():
  for i in discountcodes:
    if i == code:
      
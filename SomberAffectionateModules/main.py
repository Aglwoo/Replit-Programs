scorelist=[1,212152,23,4,13465,63,67]
def bubble(scorelist):
  swap = True
  while swap ==True:
    swap =False
    for i in range(len(scorelist)-1):
      if scorelist[i]>scorelist[i+1]:
        temp = scorelist[i]
        scorelist[i] = scorelist[i+1]
        scorelist[i+1]=temp
        swap=True
    print(scorelist)
    print("bob")



#bubble(scorelist)





def insertion(scorelist):
      for i in range(1, len(scorelist)):
 
        key = scorelist[i]
        temp = i-1
        while temp >=0 and key < scorelist[temp] :
                scorelist[temp+1] = scorelist[temp]
                temp -= 1
        scorelist[temp+1] = key
        print(scorelist)

insertion(scorelist)
print(scorelist)
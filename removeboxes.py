
boxes=[]
for i in range(4):
     n = int(input('enter number'))
     boxes.append(n)

c=[]
   
print( boxes)
for i in boxes:
     if boxes.count(i)>1:
          c.append(i)
          boxes.remove(i)
          print(boxes)
print(c)

    


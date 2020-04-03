# Create - Define a Tuple

mytuple =("c","Java","Python","C+","Mi","Vivo","Samsung")
print("\nTuple Content:")
print(mytuple)



#Tuple with diff.items

print("Tuple Content:")
print(mytuple)



#Traverse tuple using loop


print("All item of the tuple:")
for item in mytuple:
 print(item)



#Access an item using index
  
print("\nTuple Content:")
print(mytuple)

print("Item at index3 is:")
print(mytuple[4])


#Access item using index range
#Specifying a range, the return value will be
#a new tuple with the specified items
#[2:5]>>index 2 to 4(5 not included)

print("Tuple Content:")
print(mytuple)

print("item in range [2:5] is :")
print(mytuple[2:5])



#Access items using neg.index range
#specifying a range, the return value will
#be a new Tuple with the specified items
#Negative indexing > beginning from the end,
#-1 refers to the last item
#-2 refers to the second last item etc
#[-5:1]>>-1 not included

print("Tuple COntent:")
print(mytuple)

print("Item in range[-5:-1] is :")
print(mytuple[-5:-1])



#Tuple Length

print("Tuple content:")
print(mytuple)

print("Length of tuple>>",len(mytuple))



#Search item

search = input("Enter item to be searched:")


if search in mytuple:
  print("Yes",search,"is in the tuple")
else:
  print("No",search,"is not in the tuple")
  




















































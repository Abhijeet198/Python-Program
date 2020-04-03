# Create and define Set

myset= {"C","C++","Java","Python","50","L#@12","@@@@","1","A","a"}
print("\nSet Content:",myset)


# set with different items

print("Set content:")
print(myset)


# Traverse set using loop

print("All items of the set:")
for item in myset:
    print(item)



# Length of Set

print("Set Content:")
print(myset)
print("Length of set>>",len(myset))

# Add Item - add()
# add()>> add item, one at a time

myset.add("Apple Mac")
print("\nmyset(after add()):")
print(myset)



# Add multiple Items - update()
#add()>>add item, multiple at a time

myset.update(["JS","Query","Sublime","Linux"])
print("\nmyset(after update()):")
print(myset)



# Remove item - remove()
#remove()>> remove the specified item

myset.remove("Query")
print("set content(after remove()):")
print(myset)


#Remove an item randomly - pop()
#pop()>> removes the last item,but as the set is unordered so any
# random item will be deleted


x= myset.pop()
print("Item removed from the set:")
print(x)
print("Set Content(after pop()):")
print(myset)


# reomve all(empty) - clear()
#clear()>> remove all items
#write : myset.clear()
#write : print("Set Contetn(after clear()):")


# Delete Set - del keyword
#del>> delete Set
#write : del myset
#write : print("Set is deleted.")



# Add(join) two sets - union()
# union()>> perofrm union(),return a new
#set with all item from both sets
#(excluding duplicate items)

mybit = ("Dog","Cow","Hen","Lion")

My = myset.union(mybit)

print("myset:")
print(myset)
print("mybit:")
print(mybit)
print("My:")
print(My)


# Add(join) two sets - update()
#update()>> insert mybit in myset
#(exclude duplicate items)
# write : myset.update(mybit)
# write : print("myset(after update()):")
# write : print(myset)



# Copy Set -copy()

setA = myset.copy()
print("setA:")
print(setA)





























































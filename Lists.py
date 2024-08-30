
#Functions available in Python for List

# append = adds an element at the end of the list
my_list= [2,5,7]  
my_list.append(4)
print(f"New List= {my_list}")

# extend(iterable) = extends the list by appending all the items from the iterable
my_list= [1,2,3]
my_list.extend([2,4,9])
print(f"Extended List= {my_list}")

# insert(i,x) = inserts the element x at position i
my_list= [4,5,3]
my_list.insert(1,7)
print(f"List after insertion= {my_list}")

# remove(x) = removes the first occurence of the element x from the list
my_list = [3,4,3,6,5,4,9]
my_list.remove(4)
print(f"New List= {my_list}")

# pop([i]) = removes and returns the element at position i
my_list =[3,5,12,78]
pop_element =my_list.pop(2)
print(f"REmoved element= {pop_element}") # removed element
print(f"List after removal= {my_list}")

# pop() = removes and return the last element from the list
my_list =[3,5,12,78]
last_element = my_list.pop() 
print(f"Last element of the list= {last_element}")
print(f"New list= {my_list}")

# clear() = removes all the element from the list
my_list =[3,5,12,78]
my_list.clear()
print(f"Cleared List = {my_list}")

# index(x,[, start[, end]]) = returns the index of the first occurence of the element x (within optional start and end)
my_list = [3,4,3,6,5,4,9]
print(f"First position of 3 is: {my_list.index(3)}")
index_element = my_list.index(3,1)
print(f"First position of 3 after 1 index = {index_element}")

# count(x) = returns the number of times x appears in the list
my_list = [3,4,3,6,5,4,9]
print(f"Number of 3's in list = {my_list.count(3)}")

# sort(key= None, reverse = False) = sorts the list in ascending order. The key is an optional argument that can be used to customize the sort order
my_list= [3,4,3,6,5,4,9]
my_list.sort(reverse= True)
print(f"Sorted List= {my_list}")

# sorted = returns a new list containing all the items from the original list in ascending order
my_list= [3,4,3,6,5,4,9]
new_list= sorted(my_list)
print(f"Sorted List= {new_list}")

# reverse() = reverses the elements of the list
my_list = [3,4,3,6,5,4,9]
my_list.reverse()
print(f"Reversed list = {my_list}")

# copy() = returns a shallow copy of the list
my_list = [3,4,5,4,9]
copy_list = my_list.copy()
print(f"Copied list= {copy_list}")

# len() = returns  the number of elements in the list
my_list = [3,4,5,4,9]
print(f"Length of list = {len(my_list)}")

# min() = returns the smallest item in the list
my_list = [3,4,5,4,9]
print(f"Smallest element = {min(my_list)}")

# max() = returns the largest item in the list
my_list = [3,4,5,4,9]
print(f"Largest element = {max(my_list)}")

# sum() = returns the sum of all items in the list
my_list = [3,4,5,4,9]
print(f"Sum of elements = {sum(my_list)}")

# any() = returns true if any element of the lsit is true
my_list = [0,1,4,7]
print(f"Truth Value= {any(my_list)}")

# all() = returns true if all elements of the lsit is true
my_list = [0,1,4,7]
print(f"Truth Value= {all(my_list)}")



""" Lists Comprehension"""
#Lists comprehension offers shorter syntax when we need to create a new list based on the values of an existing list 

list1 = ['apple','mango','cherry','banana','guava','melon']
newlist = [x for x in list1 ]   # will include all the elements in list1
print(newlist)

newlist = [x for x in list1 if 'a' in x]  # will include elements having character 'a'
print(newlist)

newlist = [x for x in list1 if x=='apple']  # will include if element is equal to apple
print(newlist)

list2 = [1,2,3,4,5,6]
newlist = [x for x in list2 if x in range(4)]
print(newlist)



"""List Copying"""
 # 1. use copy() method

list1 = [1,2,3,4]
list2 = list1.copy()
print(list2)

# 2. use list() method 
list1 = [1,2,3]
list2 = list(list1)
print(list2)

# 3. use slice operator(:)
list1 = [2,3]
list2 = list1[:]
print(list2)


""" List Joining"""
# 1. use append() function
list1= [1,2]
list2 = [8,7,8,6]
for x in list2:
    list1.append(x)
print(list1)


# 2. use + operator
list1= [1,2]
list2 = [8,6]
newlist = list1 + list2
print(newlist)
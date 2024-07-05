
#Functions available in Python

# append = adds an element at the end of the list
my_list= [2,5,7]  
my_list.append(4)
print(my_list)

# extend(iterable) = extends the list by appending all the items from the iterable
my_list= [1,2,3]
my_list.extend([2,4,9])
print(my_list)

# insert(i,x) = inserts the element x at position i
my_list= [4,5,3]
my_list.insert(1,7)
print(my_list)

# remove(x) = removes the first occurence of the element x from the list
my_list = [3,4,3,6,5,4,9]
my_list.remove(4)
print(my_list)

# pop([i]) = removes and returns the element at position i
my_list =[3,5,12,78]
pop_element =my_list.pop(2)
print(pop_element)
print(my_list)

# pop() = removes and return the last element from the list
my_list =[3,5,12,78]
last_element = my_list.pop()
print(last_element)
print(my_list)

# clear() = removes all the element from the list
my_list =[3,5,12,78]
my_list.clear()
print(my_list)

# index(x,[, start[, end]]) = returns the index of the first occurence of the element x (within optional start and end)
my_list = [3,4,3,6,5,4,9]
print(my_list.index(3))

# count(x) = returns the number of times x appears in the list
my_list = [3,4,3,6,5,4,9]
print(my_list.count(3))

# sort(key= None, reverse = False) = sorts the list in ascending order. The key is an optional argument that can be used to customize the sort order
my_list= [3,4,3,6,5,4,9]
my_list.sort(reverse= True)
print(my_list)

# sorted = returns a new list containing all the items from the original list in ascending order
my_list= [3,4,3,6,5,4,9]
new_list= sorted(my_list)
print(new_list)

# reverse() = reversews the elements of the list
my_list = [3,4,3,6,5,4,9]
my_list.reverse()
print(my_list)

# copy() = returns a shallow copy of the list
my_list = [3,4,5,4,9]
copy_list = my_list.copy()
print(copy_list)

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
print(any(my_list))

# all() = returns true if all elements of the lsit is true
my_list = [0,1,4,7]
print(all(my_list))
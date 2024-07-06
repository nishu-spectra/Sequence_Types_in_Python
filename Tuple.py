
"""Tuples are an immutable data types, meaning their elements cannot be changed after they are generted . Each element in a tuple has a specific order that will never change because tuples are ordered sequence. They can be declared with or without paranthesis "()". """
# craetion of tuple
my_tuple = [1,2,3]
print(my_tuple) 
my_tuple = 1,2,3
print(my_tuple)
my_tuple= [1,"nishu",21.34]
print(my_tuple)

#Methods available in Tuple

# count(x) = returns the number of times 'x' appears in the tuple
my_tuple = [2,3,5,2,6,7,8,2]
count= my_tuple.count(2)
print(f"Number of 2's in the tuple= {count}")

# index(x,start,end) = returns the index of the first occurence of 'x' in the tuple(with the optional start and end )
my_tuple = [2,3,5,2,6,7,8,2]
print(f"First positionn of 2 = f{my_tuple.index(2)}")
index = my_tuple.index(2,2)
print(f"First position of 2 after index 2 = {index}")

# tuple()= converts tuple into tuple
my_list = (2,3,4,5,6,1)
my_tuple = tuple(my_list)
print(f"Tuple = {my_tuple}")

# len() = returns  the number of elements in the tuple
my_tuple = [3,4,5,4,9]
print(f"Length of tuple = {len(my_tuple)}")

# min() = returns the smallest item in the tuple
my_tuple = [3,4,5,4,9]
print(f"Smallest element = {min(my_tuple)}")

# max() = returns the largest item in the tuple
my_tuple = [3,4,5,4,9]
print(f"Largest element = {max(my_tuple)}")

# sum() = returns the sum of all items in the tuple
my_tuple = [3,4,5,4,9]
print(f"Sum of elements = {sum(my_tuple)}")

# any() = returns true if any element of the tuple is true
my_tuple = [0,1,4,7]
print(f"Truth Value= {any(my_tuple)}")

# all() = returns true if all elements of the tuple is true
my_tuple = [0,1,4,7]
print(f"Truth Value= {all(my_tuple)}")

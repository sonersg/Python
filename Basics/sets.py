#SETS

nums = {1,2,3,4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicate allowed
nums = {1,2,2,2,3}
print(nums)

# true is a dupe of 1
# false is a dupe of 0
nums = {1,True, 0, False}
print(nums)

# check if a value is in a set 
print(2 in nums)

# but we cannot refer to an
# element in the set with an 
# index position

# add a new element to a set
nums.add(5)
print(nums)

# add elements from one set to another
morenums = {6,7,8}
nums.update(morenums)
print(nums)

# we can use update function with.
# lists
# tuples
# dictionaries

# merge two sets
one = {1,3,5}
two = {2,4,6}
mergedSet = one.union(two)
print(mergedSet)

# keep only duplicates
one = {1,3,5}
two = {3,5,7}
one.intersection_update(two)
print(one)

# keep everything except duplicates
one = {1,3,5}
two = {3,5,7}
one.symmetric_difference_update(two)
print(one)

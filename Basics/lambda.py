# if it receives a function as an argument
# or returnes a function, it is callled
# higher order function.

squared = lambda num: num * num
print(squared(2))

summation = lambda a, b : a + b
print(summation(4, 5))



def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(5))
print(addTwenty(5))

# similar to closures

############# MAP ###############
numbers = [1, 2, 3, 4, 5, 6]
squared_nums = map(lambda num: num*num, numbers)
print(list(squared_nums))

############# FILTER ###############
numbers = [1, 2, 3, 4, 5, 6]
odd_nums = filter(lambda num: num%2 != 0, numbers)
print(list(odd_nums))

############# REDUCE ###############
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)

print(sum(numbers))

# more complex example for reduce
names = ["Lost", "fish", "Memo"]
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)


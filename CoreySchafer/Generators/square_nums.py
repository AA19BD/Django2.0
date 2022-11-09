def square_nums(nums):
    # result = []
    for i in nums:
        yield (i * i) #<class 'generator'>
        # result.append(i * i)
    # return result


my_nums = square_nums([1,2,3,4,5])
#

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

my_nums = (x * x for x in [1,2,3,4,5])

print(dir(my_nums)) #<class 'generator'>

for num in my_nums:
    print(num)
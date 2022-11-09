nums =  [1, 2, 3]

# iter_nums = nums.__iter__()

iter_nums = iter(nums)

print(dir(iter_nums))

while True:
    try:
        item = next(iter_nums)
        print(item)
    except StopIteration:
        break


print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))


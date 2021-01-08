nums = ['4', '6', '4', '6', '7']


def star_func(s):
    return '*=*'+s+'*=*'

nums2 = map(star_func, nums)
print(*nums, sep='-----', end='')
print(*nums2)

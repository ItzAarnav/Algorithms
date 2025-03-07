

def two_sum(nums, target):
  num_dict = {}
  for i, num in enumerate(nums):
    needed_num = target - num
    if needed_num in num_dict:
      return [num_dict[needed_num], i]
    num_dict[num] = i
  return []


array = (3,2,4)

print(two_sum(array, 6))
nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums_partial = nums[0::2]
nums_partial1 = nums[0:8]
print(nums_partial)
print(nums_partial1)
print(len(nums))
print(max(nums))
print(min(nums))

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors_partial = colors[3:6]
print(colors_partial)

my_string = 'john'
print(len(my_string))
print(max(my_string))
print(min(my_string))

student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]
length = len(student_gpas)
max_gpa = max(student_gpas)
min_gpa = min(student_gpas)
print(length)
print(max_gpa)
print(min_gpa)
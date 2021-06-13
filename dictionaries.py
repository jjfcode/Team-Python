course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

# print(course['teacher'])
# course.keys()
# course.values()
# sorted(course.keys())
# sorted(course.values())
# course['teacher'] = 'Treasure'
# course['level'] = 'intermediate'
# course['stages'] = 2
# del(course['stages'])

for key, value in course.items():
    print(key)
    print(value)
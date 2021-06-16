# Step 1
# Ask the user for their name and the year they were born.
name = input('Enter your name: ')
year = int(input('What Year you were born? '))
current_year = int(input('Today Year? '))
# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
today_age = current_year - year
print(today_age)
if today_age <= 25:
    print(name, 'On', year + 25, 'you will have 25 years')
    print(name, 'On', year + 50, 'you will have 50 years')
    print(name, 'On', year + 75, 'you will have 75 years')
    print(name, 'On', year + 100, 'you will have 100 years')
elif today_age <= 50: 
    print(name, 'On', year + 50, 'you will have 50 years')
    print(name, 'On', year + 75, 'you will have 75 years')
    print(name, 'On', year + 100, 'you will have 100 years')
elif today_age <= 75:
    print(name, 'On', year + 75, 'you will have 75 years')
    print(name, 'On', year + 100, 'you will have 100 years')
else:
    print(name, 'On', year + 100, 'you will have 100 years')
# Step 3
# If they're already past any of these ages, skip them.
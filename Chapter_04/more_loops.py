my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("I am using a for loop for my favorite foods:")
for my_food in my_foods:
    print(my_food)

print("\nI am using a for loop my friend's favorite foods:")
for friend_food in friend_foods:
    print(friend_food)
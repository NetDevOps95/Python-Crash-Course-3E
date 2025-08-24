motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles[0])

print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcylces = ['honda', 'yamaha', 'suzuki']
print(motorcylces)

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcylces.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcylces.pop(0)
print(f"The first motorcylce I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
print(motorcycles)
print(f"\nA {too_expensive.title()} motorcycle is too expensive for me.")
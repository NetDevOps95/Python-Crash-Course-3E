first_name = " John "
last_name = " Smith "
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


print(f"Hello, {last_name.title().lstrip()}!")
print(f"Hello, {last_name.title().rstrip()}!")
print(f"Hello, {full_name.title().strip()}!")


import os


# Make working directory this file's location
# such that `input.txt` is in path
# https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Converts string of "newline seperated integers" into its sum as int
# E.g. '1\n\2\n3' -> 1 + 2 + 3 = 6
def sum_elf(calorie_list: str) -> int:
    calorie_list_as_strings = calorie_list.split('\n')
    calorie_list_as_integers = [int(i.strip()) for i in calorie_list_as_strings if len(i) > 0]
    return sum(calorie_list_as_integers)

# Read the file and split into list of each elf
with open('./input.txt', 'r') as file:
    data = file.read().split('\n\n')

# For each elf, sum its calories using `sum_elf()`
sums = [sum_elf(i) for i in data]

# Print the biggest sum, solution A
most_calories1 = max(sums)

# Get the biggest sum, remove that value from the sums list,
# then find the next biggest sum
# doing this 3 times
most_calories3 = 0
for i in range(3):
    most_calories = max(sums)
    most_calories3 += most_calories
    sums.remove(most_calories)

print(f'Solution A = {most_calories1}')
print(f'Solution B = {most_calories3}')

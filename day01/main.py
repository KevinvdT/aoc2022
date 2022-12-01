import os


# Make working directory this file's location
# such that `input.txt` is in path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Converts string of "newline seperated integers" into its sum as int
def sum_elf(calorie_list: str) -> int:
    calorie_list_as_strings = calorie_list.split('\n')
    calorie_list_as_integers = [int(i.strip()) for i in calorie_list_as_strings if len(i) > 0]
    return sum(calorie_list_as_integers)

# Read the file and split into list of each elf
with open('./input.txt', 'r') as file:
    data = file.read().split('\n\n')

# For each elf, sum its calories using `sum_elf()`
sums = [sum_elf(i) for i in data]

# Print the biggest sum, the solution
most_calories = max(sums)
print(most_calories)

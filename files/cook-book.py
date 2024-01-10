from pprint import pprint
##task1
def make_cook_book(file):
    recipes = {}
    with open(file, "r") as f:
        while True:
            title = f.readline().strip()
            if not title:
                break
            num = int(f.readline())
            ingredients = []
            for i in range(num):
                ingredient, quantity, measure = [item.strip() for item in f.readline().split("|")]
                ingredient_dict = {"ingredient_name": ingredient, "quantity": quantity, "measure": measure}
                ingredients.append(ingredient_dict)
            recipes[title] = ingredients
            f.readline()
    return recipes

recipes = make_cook_book('recipes.txt')
print(recipes)
print()
##task2
def get_shop_list_by_dishes(dishes, persons):
    shopping_list = {}
    for dish in dishes:
        ingredients = recipes.get(dish)
        if ingredients:
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * persons
                measure = ingredient['measure']
                if ingredient_name in shopping_list:
                    shopping_list[ingredient_name]['quantity'] += quantity
                else:
                    shopping_list[ingredient_name] = {'quantity': quantity, 'measure': measure}

    return shopping_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()

##task3

input_files = ["1.txt", "2.txt", "3.txt"]

output_file = "sorted-files.txt"

data = []

for input_file in input_files:
    with open(input_file, 'r') as file:
        lines = file.readlines()
        data.append((input_file, len(lines), lines))


data.sort(key=lambda x: x[2], reverse=True)

with open(output_file, 'w') as file:
    for filename, line_count, lines in data:
        file.write(f'{filename}\n{line_count}\n')
        file.writelines(lines)
        file.write('\n')

with open(output_file) as file:
    for line in file:
        print(line.strip())
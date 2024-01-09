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

##task3
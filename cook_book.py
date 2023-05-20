from pprint import pprint
#Задача №1
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        count_ingredient = int(file.readline())
        ingredient_list = []
        for _ in range(count_ingredient):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredient_dict = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredient_list.append(ingredient_dict)
        file.readline()
        cook_book[dish_name] = ingredient_list

    pprint(cook_book, sort_dicts=False)

print()
print()

#Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ingredient in recipe:
            key = ingredient['ingredient_name']
            if key not in result:
                new_dict = {
                    'measure': ingredient['measure'],
                    'quantity': int(ingredient['quantity']) * person_count

                }
                result[key] = new_dict
            else:
                result[key]['quantity'] += int(ingredient['quantity']) * person_count

    pprint(result, sort_dicts=False)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)



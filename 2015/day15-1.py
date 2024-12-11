from common import get_input_lines

def calc_score(elems:dict, frost:int, candy:int, bscotch:int, sugar:int)->int:
    capacity = frost * elems['F'][0] + candy * elems['C'][0] + bscotch * elems['B'][0] + sugar * elems['S'][0]
    if capacity <= 0: return 0
    durability = frost * elems['F'][1] + candy * elems['C'][1] + bscotch * elems['B'][1] + sugar * elems['S'][1]
    if durability <= 0: return 0
    flavor = frost * elems['F'][2] + candy * elems['C'][2] + bscotch * elems['B'][2] + sugar * elems['S'][2]
    if flavor <= 0: return 0
    texture = frost * elems['F'][3] + candy * elems['C'][3] + bscotch * elems['B'][3] + sugar * elems['S'][3]
    if texture <= 0: return 0
    return capacity * durability * flavor * texture

def main():
    input = get_input_lines('day15.txt')
    ingredients = dict()
    top_score = 0

    for line in input:
        parts = line.split()
        ingredient, capacity, durability = parts[0][0], int(parts[2][:-1]), int(parts[4][:-1])
        flavor, texture, calories = int(parts[6][:-1]), int(parts[8][:-1]), int(parts[10])
        ingredients[ingredient] = (capacity, durability, flavor, texture, calories)
    
    for frost_amt in range(0, 101):
        for candy_amt in range(0, 101 - frost_amt):
            for bscotch_amt in range(0, 101 - candy_amt - frost_amt):
                sug_amt = 100 - bscotch_amt - candy_amt - frost_amt
                recipe_score = calc_score(ingredients, frost_amt, candy_amt, bscotch_amt, sug_amt)
                if recipe_score > top_score:
                    top_score = recipe_score
    
    print(f'Top scoring cookie has a score of {top_score}')

if __name__ == '__main__':
    main()
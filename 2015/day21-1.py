from functools import reduce

def win_battle(boss:dict, player:dict)->bool:
    print(f'Boss {boss} vs Player {player}')
    while boss['hp'] > 0 and player['hp'] > 0:
        boss['hp'] -= max(1, player['dmg'] - boss['ac'])
        if boss['hp'] > 0:
            player['hp'] -= max(1, boss['dmg'] - player['ac'])
    if player['hp'] > 0:
        print(f'Player wins!')
        return True

def main():
    weapons = [(8,4), (10,5), (25,6), (40,7), (74,8)]
    armors = [(0,0), (13,1), (31,2), (53,3), (75,4), (102,5)]
    rings = [(0,0,0), (0,0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]
    min_cost = 360

    for weapon in weapons:
        for armor in armors:
            for ring1_idx in range(len(rings)):
                for ring2_idx in range(ring1_idx + 1, len(rings)):
                    cost = weapon[0] + armor[0] + rings[ring1_idx][0] + rings[ring2_idx][0]
                    boss = {'hp': 104, 'dmg': 8, 'ac': 1}
                    player = {'hp': 100, 'dmg': 0, 'ac': 0}
                    player['dmg'] += weapon[1] + rings[ring1_idx][1] + rings[ring2_idx][1]
                    player['ac'] += armor[1] + rings[ring1_idx][2] + rings[ring2_idx][2]
                    if win_battle(boss, player):
                        print(f'Player wins for {cost}')
                        if cost < min_cost:
                            min_cost = cost
                    
    print(f'Player can win for {min_cost}')

if __name__ == '__main__':
    main()
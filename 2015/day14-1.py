from common import get_input_lines

def main():
    input = get_input_lines('day14.txt')
    race_time = 2503
    
    reindeer = dict()
    for line in input:
        (name, _, _, veloc, _, _, duration, _, _, _, _, _, _, rest, _) = line.split()
        reindeer[name] = (int(veloc), int(duration), int(rest))
    
    distance = 0
    winner = ''

    for racer in reindeer.keys():
        dist_per_cycle = reindeer[racer][0] * reindeer[racer][1]
        cycle_time = reindeer[racer][1] + reindeer[racer][2]

        racer_dist = (race_time // cycle_time) * dist_per_cycle
        if race_time % cycle_time >= reindeer[racer][1]:
            racer_dist += dist_per_cycle
        else:
            racer_dist += (race_time % cycle_time) * reindeer[racer][0]
        
        if racer_dist > distance:
            winner = racer
            distance = racer_dist
    
    print(f'The winner is {winner} with a distance of {distance}')

if __name__ == '__main__':
    main()
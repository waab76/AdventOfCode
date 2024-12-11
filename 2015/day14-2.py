from common import get_input_lines
import json

def in_first(racers:dict, race_time:int)->list:
    winning_dist = 0
    winners = list()

    for racer in racers.keys():
        dist_per_cycle = racers[racer][0] * racers[racer][1]
        cycle_time = racers[racer][1] + racers[racer][2]

        racer_dist = (race_time // cycle_time) * dist_per_cycle
        if race_time % cycle_time >= racers[racer][1]:
            racer_dist += dist_per_cycle
        else:
            racer_dist += (race_time % cycle_time) * racers[racer][0]
        
        if racer_dist > winning_dist:
            winners = list()
            winners.append(racer)
            winning_dist = racer_dist
        elif racer_dist == winning_dist:
            winners.append(racer)

    return winners

def main():
    input = get_input_lines('day14.txt')
    race_time = 2503
    
    reindeer = dict()
    for line in input:
        (name, _, _, veloc, _, _, duration, _, _, _, _, _, _, rest, _) = line.split()
        reindeer[name] = (int(veloc), int(duration), int(rest))
    
    scores = dict()
    for time in range(race_time):
        leaders = in_first(reindeer, time + 1)
        for leader in leaders:
            if leader not in scores:
                scores[leader] = 1
            else:
                scores[leader] += 1

    print(json.dumps(scores, indent=2))

if __name__ == '__main__':
    main()
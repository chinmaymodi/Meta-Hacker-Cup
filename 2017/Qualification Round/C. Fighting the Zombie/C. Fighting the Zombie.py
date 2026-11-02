import time
start = time.time()

file = "fighting_the_zombie_input.txt"

ans = []

frequency_dict = {}

def get_dist(dice, sides):
    if (dice, sides) in frequency_dict:
        return frequency_dict[(dice, sides)]

    if dice == 1:
        dist = [0] * (sides + 1)
        for face in range(1, sides + 1):
            dist[face] = 1
    else:
        prev = get_dist(dice - 1, sides)

        dist = [0] * (dice * sides + 1)

        for total, count in enumerate(prev):
            if count:
                for face in range(1, sides + 1):
                    dist[total + face] += count

    frequency_dict[(dice, sides)] = dist
    return dist

for sides in (4, 6, 8, 10, 12, 20):
    for dice in range(1, 21):
        get_dist(dice, sides)

prob_dict = {}

for sides in (4, 6, 8, 10, 12, 20):
    for dice in range(1, 21):
        dist = frequency_dict[(dice, sides)]
        total = sum(dist)
        suffix = [0] * len(dist)
        running = 0

        for i in range(len(dist) - 1, -1, -1):
            running += dist[i]
            suffix[i] = running

        prob_dict[(dice, sides)] = (total, suffix)

with (open(file, 'r') as f):
    t = int(f.readline())
    for case in range(t):
        health, spell_count = map(int, f.readline().split())
        spells = f.readline().split()
        val = 0
        for i in range(spell_count):
            attempt = spells[i]
            bonus = 0
            if '+' in attempt:
                remnant, bonus = attempt.split('+')
                attempt = remnant
                bonus = int(bonus)
            elif '-' in attempt:
                remnant, bonus = attempt.split('-')
                attempt = remnant
                bonus = -int(bonus)
            rolls, die = map(int, attempt.split('d'))
            if bonus + rolls >= health:
                val = 1.0
                break

            current_health = health - bonus

            total, suffix = prob_dict[(rolls, die)]

            max_damage = rolls * die

            min_damage = rolls

            if current_health <= min_damage:
                probability = 1.0

            elif current_health > max_damage:
                probability = 0.0

            else:
                probability = suffix[current_health] / total
            val = max(val, probability)
        ans.append(f"{val:.6f}")

outputfile = "fighting_the_zombie_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')

from collections import defaultdict


input_file = open('./2/input', 'r')
colors = ['green', 'blue', 'red']
games_dict = defaultdict(list)




for line in input_file:
    game_num_str = line.split(':')[0].split(' ')[1]
    games = line.split(':')[1].split(';')

    for game in games:
        items = [item.strip() for item in game.split(',')]
        vals = {}

        for item in items:
            count = item.split()[0]
            color = item.split()[1]
            vals[color] = int(count)

        games_dict[int(game_num_str)].append(vals)


def is_game_allowed(game, allowed):
    for key in game:
        if key not in allowed or game[key] > allowed[key]:
            return False

    return True



allowed = {'blue' : 14 , 'red' : 12 , 'green' : 13 }
ans = 0
ans_mult = 0

for game_num, games in games_dict.items():
    smallest_red = 1
    smallest_blue = 1
    smallest_green = 1

    is_good_game = True

    for game in games:
        if not(is_game_allowed(game, allowed)):
            is_good_game = False

        smallest_red = max(game.get('red', 1), smallest_red)
        smallest_blue =  max(game.get('blue', 1), smallest_blue)
        smallest_green =  max(game.get('green', 1), smallest_green)

    games_power = smallest_red * smallest_blue * smallest_green
    ans_mult += games_power
    if is_good_game:
        ans += game_num
        
print(ans, ans_mult)
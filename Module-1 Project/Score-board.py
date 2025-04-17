# London played = 8 matches
# won = 4 matches
# loss = 3 matches
# drew = 1 match

def calulate_score (win, draw):
    # 3x points for win
    # 1x point for draw

    result = (3*win) + (1*draw)
    return result

total_points = calulate_score(4, 1)

print (f"Total points earned by team London: {total_points}")
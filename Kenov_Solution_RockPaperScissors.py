# Kenov: Solution to the HySci Task on Rock, Paper, Scissors in Python

def next_move(player_moves):
    if player_moves[0] == "O":
        return player_moves[0], player_moves[1:]
    elif player_moves[0:2] == "[]":
        return player_moves[0:2], player_moves[2:]
    elif player_moves[0:2] == "8<":
        return player_moves[0:2], player_moves[2:]
    else:
        return "X", ""


def determine_winner(move_p1, move_p2):
    if move_p1 == "O" and move_p2 == "8<" \
            or move_p1 == "8<" and move_p2 == "[]" \
            or move_p1 == "[]" and move_p2 == "O":
        return 2, 0
    if move_p1 == "8<" and move_p2 == "O" \
            or move_p1 == "[]" and move_p2 == "8<" \
            or move_p1 == "O" and move_p2 == "[]":
        return 0, 2
    elif move_p1 == move_p2:
        return 1, 1
    else:
        return 0, 0


def solution(george, john):
    score_board = {"george": 0, "john": 0}
    games_map = dict()

    while george or john:
        move_george, george = next_move(george)
        move_john, john = next_move(john)

        score_george, score_john = determine_winner(move_george, move_john)
        score_board["george"] += score_george
        score_board["john"] += score_john

        game_type = move_george + move_john
        if game_type in games_map.keys():
            games_map[game_type] += 1
        else:
            games_map[game_type] = 1

    max_games_name = max(games_map, key=games_map.get)
    max_games_score = games_map[max_games_name]

    return "George " + str(score_board["george"]) + " John " + str(score_board["john"]) + \
           " " + max_games_name + " " + str(max_games_score)


if __name__ == "__main__":
    george_moves = "OOOOOO[][]8<"
    john_moves = "[][]8<8<8<O[]O[]"

    print(solution("OOOOOO[][]8<", "[][]8<8<8<O[]O[]"))

# main.py

from game_module import run_game, get_player_name, greet_player

if __name__ == "__main__":
    player_name = get_player_name()
    greet_player(player_name)
    run_game()

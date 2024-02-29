from TicTacToe import TicTacToe


def main():
    # Test: Horizontal victory
    print("Case 1: Horizontal connection")
    game = TicTacToe(3)
    game.display_board()
    game.coin_flip_check()
    game.place_marker(game.game_result, 0, 0)
    game.place_marker(game.game_result, 1, 0)
    game.place_marker(game.game_result, 0, 1)
    game.place_marker(game.game_result, 1, 1)
    game.place_marker(game.game_result, 0, 2)

    # Test: Vertical victory
    print("Case 2: Vertical connection")
    game = TicTacToe(3)
    game.display_board()
    game.coin_flip_check()
    game.place_marker(game.game_result, 0, 1)
    game.place_marker(game.game_result, 1, 0)
    game.place_marker(game.game_result, 1, 2)
    game.place_marker(game.game_result, 2, 0)
    game.place_marker(game.game_result, 0, 2)
    game.place_marker(game.game_result, 0, 0)

    # Test: Diagonal victory
    print("Case 3: Diagonal connection")
    game = TicTacToe(3)
    game.display_board()
    game.coin_flip_check()
    game.place_marker(game.game_result, 0, 0)
    game.place_marker(game.game_result, 1, 0)
    game.place_marker(game.game_result, 1, 1)
    game.place_marker(game.game_result, 2, 0)
    game.place_marker(game.game_result, 2, 2)

    # Test: 5x5 grid: Game allows for any size grid and completes the same tasks in the same manner
    print("Case 4: nxn Grid")
    game = TicTacToe(5)
    game.display_board()
    game.coin_flip_check()
    game.place_marker(game.game_result, 0, 0)
    game.place_marker(game.game_result, 1, 0)
    game.place_marker(game.game_result, 1, 1)
    game.place_marker(game.game_result, 2, 0)
    game.place_marker(game.game_result, 2, 2)
    game.place_marker(game.game_result, 3, 0)
    game.place_marker(game.game_result, 3, 3)
    game.place_marker(game.game_result, 4, 0)
    game.place_marker(game.game_result, 4, 4)

    game.place_marker(game.game_result, 6, 0)


    # Custom Game
    # This code chunk allows two players to battle in real time by taking in their coordinate inputs
    game = TicTacToe(3)
    print("Case 5: 1v1 Tic Tac Toe Game using keyboard inputs\n")
    print("To terminate game, input -1 as a coordinate\n")
    game.display_board()
    game.coin_flip_check()

    while game.check_winner() == "continue":
        print("input x coordinate")

        try:
            x_input = int(input())
            if x_input == -1:
                break
        except TypeError:
            print("You terminated the game, make sure to use proper integer input next time")
            break
        except ValueError:
            print("Input not an integer, Please try not to break the game again")
            break

        try:
            print("input y coordinate")
            y_input = int(input())
            if y_input == -1:
                break
        except TypeError:
            print("You terminated the game, make sure to use proper integer input next time")
            break
        except ValueError:
            print("Input not an integer, Please try not to break the game again")
            break

        if (0 <= x_input <= len(game.board) - 1) and (0 <= y_input <= len(game.board) - 1):
            game.place_marker(game.game_result, x_input, y_input)
        else:
            print("input valid coordinates 0 - Grid length or grid height")


if __name__ == "__main__":
    main()



import Player
import Console
import Board
import GameRunner
if __name__ == '__main__':
    board1=Board.Board()
    console1=Console.Console()
    player1=Player.Player(1,500)
    game1=GameRunner.GameRunner()
    game1.Run(player1,board1,console1)


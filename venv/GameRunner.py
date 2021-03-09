class GameRunner:
    def Run(self,player, board, console):
        while (board.GameStatus(player) == "PLAYING"):
            console.DisplayPosition(player)
            rolled_number = console.GetDiceRoll()
            board.Play(player, rolled_number)

        status = board.GameStatus(player)
        if (status == "WON"):
            console.DisplayWinningTheGame()
            return
        elif (status == "LOST"):
            console.DisplayLosingTheGame()
            return
        else:
            raise Exception("This is not supposed to happen")
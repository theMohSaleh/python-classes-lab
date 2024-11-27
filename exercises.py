class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        
    def play_game(self):
        print("Shall we play a game?")
        # While there is no winner or tie
        while True:
            # render
            self.render()
            # get player input
            self.get_move()
            # check for a winner
            self.check_for_winner()
            # check for a tie
            self.check_for_tie()
            # switch turns
            self.switch_turn()
            # ...repeat until there is a winner or tie
            if (self.winner != None or self.tie != False):
                break
        # Outside the loop, render state at the end of a game
        self.render()
    
    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    
    def print_message(self):
        ## If there is a tie: print("Tie game!")
        if self.tie:
            print("Tie game!")
        ## If there is a winner: print(f"{self.winner} wins the game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        ## Otherwise: print(f"It's player {self.turn}'s turn!")
        else:
            print(f"It's player {self.turn}'s turn!")
    
    def render(self):
        # Call upon print_board
        self.print_board()
        ## Call upon print_message
        self.print_message()
    
    def get_move(self):
        while True:
            # prompt user for input
            move = input(f"Enter a valid move (example: A1): ").lower()
            # If the input is valid and board piece is not taken, update the board and break the loop
            if move in self.board and not self.board[move]:
                self.board[move] = self.turn
                return
            else:
            # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
                print("Invalid entry")
                self.print_board()
    
    def check_for_winner(self):
        if (
            # top row
            self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']) or
            # middle row
            self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']) or
            # bottom row
            self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']) or
            # top column
            self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']) or
            # middle column
            self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']) or
            # bottom column
            self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']) or
            # diagonal a1 to c3
            self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']) or
            # diagonal a3 to c1
            self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1'])
        ):
            # set winner
            self.winner = self.turn
    
    def check_for_tie(self):
        # if board has no empty fields and no winner is decided, set tie to True
        if not self.winner and None not in self.board.values():
            self.tie = True
    
    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
            
        
game = Game()
game.play_game()
import tkinter as tk
from tkinter import messagebox
import random


class TicTacToeGame:
    def __init__(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.player_score = 0
        self.bot_score = 0

        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')
        self.root.configure(bg='dark red')

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.root,
                text='',
                width=10,
                height=5,
                command=lambda idx=i: self.make_move(idx),
                font=('Arial', 20),
                bg='dark red',
                fg='white',
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.reset_button = tk.Button(
            self.root,
            text='Reset',
            command=self.reset_game,
            width=10,
            bg='dark red',
            fg='white',
            font=('Arial', 12, 'bold'),
        )
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.score_label = tk.Label(
            self.root,
            text=f'Player: {self.player_score} | Bot: {self.bot_score}',
            bg='dark red',
            fg='white',
            font=('Arial', 12, 'bold')
        )
        self.score_label.grid(row=4, column=0, columnspan=3)

        self.root.mainloop()

    def reset_game(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.update_board()
        self.score_label.config(text=f'Player: {self.player_score} | Bot: {self.bot_score}')

    def make_move(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)

            if self.check_win(self.current_player):
                messagebox.showinfo('Game Over', f'Player {self.current_player} wins!')
                if self.current_player == 'X':
                    self.player_score += 1
                else:
                    self.bot_score += 1
                self.reset_game()
            elif not any(move == '' for move in self.board):
                messagebox.showinfo('Game Over', 'It\'s a draw!')
                self.reset_game()
            else:
                self.current_player = 'O'
                
    def make_bot_move(self):
        available_moves = [i for i, cell in enumerate(self.board) if cell == '']
        if available_moves:
            # Check if the bot can win
            for move in available_moves:
                copy_board = self.board[:]
                copy_board[move] = 'O'
                if self.check_win('O', copy_board):
                    self.board[move] = 'O'
                    self.buttons[move].config(text='O', state=tk.DISABLED)
                    if self.check_win('O'):
                        messagebox.showinfo('Game Over', 'Bot wins!')
                        self.bot_score += 1
                        self.reset_game()
                    return

            # Check if the player can win and block them
            for move in available_moves:
                copy_board = self.board[:]
                copy_board[move] = 'X'
                if self.check_win('X', copy_board):
                    self.board[move] = 'O'
                    self.buttons[move].config(text='O', state=tk.DISABLED)
                    return

            # Choose a random move
            move = random.choice(available_moves)
            self.board[move] = 'O'
            self.buttons[move].config(text='O', state=tk.DISABLED)

            if self.check_win('O'):
                messagebox.showinfo('Game Over', 'Bot wins!')
                self.bot_score += 1
                self.reset_game()

            self.current_player = 'X'

    def check_win(self, player, board=None):
        if board is None:
            board = self.board
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        return any(all(board[i] == player for i in condition) for condition in win_conditions)

    def update_board(self):
        for i, cell in enumerate(self.board):
            self.buttons[i].config(text=cell, state=tk.DISABLED if cell != '' else tk.NORMAL)


TicTacToeGame()

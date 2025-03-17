from PIL import Image, ImageTk 
import tkinter as tk
import random
import pygame
import time

class Sal:
    def __init__(self, board_size: int, snakes: dict, ladders: dict):
        self.board_size = board_size
        self.snakes = snakes
        self.ladders = ladders

    def get_next_position(self, current_pos: int) -> int:
        if current_pos in self.ladders:
            return self.ladders[current_pos]
        elif current_pos in self.snakes:
            return self.snakes[current_pos]
        return current_pos

class salGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Let's Play")

        self.board_size = 100
        self.grid_size = 10
        self.cell_size = 50

        self.snakes = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}
        self.ladders = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}

        self.game = Sal(self.board_size, self.snakes, self.ladders)
        self.player_position = 1
        
        pygame.mixer.init()
        
        self.load_images()
        self.setup_ui()
        self.create_board()

    def load_images(self):
        self.board_image = Image.open("Assingnment 8/board_image.png")
        self.board_image = self.board_image.resize((self.grid_size * self.cell_size, self.grid_size * self.cell_size))
        self.board_photo = ImageTk.PhotoImage(self.board_image)
        
        self.player_avatar = Image.open("Assingnment 8/player_avatar.png")
        self.player_avatar = self.player_avatar.resize((45, 45))  # Slightly smaller than cell
        self.player_photo = ImageTk.PhotoImage(self.player_avatar)

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=self.grid_size * self.cell_size, height=self.grid_size * self.cell_size)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.board_photo)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        self.roll_button = tk.Button(button_frame, text="🎲 Roll Dice", command=self.roll_dice, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10)
        self.roll_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.reset_button = tk.Button(button_frame, text="🔄 Reset", command=self.reset_game, font=("Arial", 14, "bold"), bg="#FF5733", fg="white", padx=20, pady=10)
        self.reset_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.dice_label = tk.Label(self.root, text="Dice: ", font=("Arial", 14))
        self.dice_label.pack()
        
        self.create_board()

    def roll_dice(self):
        self.roll_button.config(state=tk.DISABLED)  # Disable rolling during movement
        dice_roll = random.randint(1, 6)
        self.dice_label.config(text=f"Dice: {dice_roll}")
        new_position = self.player_position + dice_roll
        
        if new_position <= self.board_size:
            self.animate_movement(new_position, dice_roll)
        else:
            self.roll_button.config(state=tk.NORMAL)  # Enable roll again if move is invalid

    def animate_movement(self, new_position, dice_roll):
        step = 1 if new_position > self.player_position else -1
        for pos in range(self.player_position + step, new_position + step, step):
            self.player_position = pos
            self.create_board()
            self.root.update()
            time.sleep(0.3)  # Smooth movement delay

        # Handle Snakes, Ladders & Winning
        final_position = self.game.get_next_position(self.player_position)
        if final_position < self.player_position:
            pygame.mixer.Sound("Assingnment 8/snake_hiss.wav").play()
            time.sleep(0.5)  # Wait before moving down
            self.player_position = final_position
            self.create_board()
            self.root.update()
        elif final_position > self.player_position:
            self.player_position = final_position
            self.create_board()
            self.root.update()

        if self.player_position == 100:
            pygame.mixer.Sound("Assingnment 8/celebration.wav").play()
        
        self.roll_button.after(1000, lambda: self.roll_button.config(state=tk.NORMAL))  # 1-sec delay before enabling roll

    def reset_game(self):
        self.player_position = 1
        self.create_board()
        self.roll_button.config(state=tk.NORMAL)

    def create_board(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.board_photo)
        self.draw_player()

    def draw_player(self):
        x, y = self.get_position_coordinates(self.player_position)
        self.canvas.create_image(x, y, anchor=tk.CENTER, image=self.player_photo)

    def get_position_coordinates(self, position):
        row = (position - 1) // self.grid_size
        if row % 2 == 0:
            col = (position - 1) % self.grid_size
        else:
            col = self.grid_size - 1 - (position - 1) % self.grid_size
        x = col * self.cell_size + self.cell_size // 2
        y = (self.grid_size - 1 - row) * self.cell_size + self.cell_size // 2
        return x, y

def main():
    root = tk.Tk()
    app = salGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()

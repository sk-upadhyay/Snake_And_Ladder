# 🎲 Snakes and Ladders Game (Python GUI)

An exciting digital version of Snakes & Ladders built with Python (Tkinter & Pygame), featuring animations and sound effects!

## 🌜 Overview
This is a fun, interactive Snakes & Ladders game built using:

- **Tkinter** for the Graphical User Interface
- **Pygame** for sound effects
- **PIL (Pillow)** for handling image assets
- **Random module** for dice rolls
- **Smooth animations** to enhance the gameplay

🎮 Experience the thrill of climbing ladders and escaping from snakes! The game board follows the traditional 10x10 Snakes & Ladders layout.

## 🔥 Features
- ✅ Beautiful GUI with a realistic board layout
- ✅ Player avatar moves smoothly with animations
- ✅ Sound effects 🎵 for rolling dice, snake bites 🐍, ladder climbs 🪜, and winning celebrations 🎉
- ✅ Realistic dice roll mechanics 🎲
- ✅ Easy-to-use controls - just click a button to roll the dice
- ✅ Reset button to restart the game instantly

## 🎥 Game Demo
🎬 Check out the gameplay preview:
*(Add a GIF or video showcasing the game in action)*

## 🚀 Installation

### 1️⃣ Prerequisites
Ensure you have Python 3.x installed.
Then, install the required libraries using:

```sh
pip install pillow pygame tk
```

### 2️⃣ Run the Game
Clone or download the repository, then navigate to the folder and run:

```sh
python snakes_and_ladders.py
```

## 🌜 How to Play?
1. Click on "🎲 Roll Dice" to roll the dice
2. Your player avatar moves according to the dice number
3. If you land on a ladder, you move up! 🪜
4. If you land on a snake, you slide down! 🐍
5. First to reach **100** wins! 🎉

## 🖼️ Visual Elements

### 🎨 Game Board
![Game Board](Assingnment%208/board_image.png)
The board follows a standard 10x10 grid with numbered positions.

### 🎭 Player Avatar
![Player Token](Assingnment%208/player_avatar.png)
This is the player's token that moves across the board.

### 🔊 Sound Effects
- 🎲 **Rolling Dice** - A short dice sound when rolling
- 🐍 **Snake Hiss** - When landing on a snake
- 🪜 **Climbing Sound** - When going up a ladder
- 🎉 **Victory Music** - When reaching 100

## 🛠️ Code Explanation
### Main Components
- **Sal (Logic Class)** – Handles snakes, ladders, and movement
- **salGui (GUI Class)** – Manages game visuals, dice rolling, and animations
- **Tkinter Canvas** – Used to render the game board and player
- **Pygame Mixer** – Plays sound effects

### Key Functions
- `roll_dice()`: Rolls the dice and updates player position
- `animate_movement()`: Moves the player smoothly
- `get_next_position()`: Checks if the player lands on a snake or ladder
- `create_board()`: Draws the game board and player

## 🔄 Resetting the Game
Click the "🔄 Reset" button anytime to restart!

## 🌟 Future Enhancements
- **Multiplayer Mode** 🎭
- **Themed Boards** 🎨
- **Custom Player Avatars** 🏆

## 💼 Feedback & Contributions
Found a bug or have an idea? Feel free to contribute! 🚀

## 👨‍💻 Developer
**Shivam Kumar**  
📧 Email: [shivamws2003@gmail.com](mailto:shivamws2003@gmail.com)  
🔗 LinkedIn: [Shivam Kumar](https://www.linkedin.com/in/28sku/)

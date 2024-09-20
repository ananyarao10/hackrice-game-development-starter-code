# 🎮 **Game Development Track Starter Code** 🎮

## 🎯 **Introduction** 🎯

This repository provides the foundational code for creating a simple 2D game with Pygame. It includes essential components like game loops, collision detection, player and enemy handling, image rendering, addition of sound, and user interface elements. Use this starter code as a launchpad for your project and build upon it to create your own unique game!

## 🚀 **Getting Started** 🚀

### 📦 **Prerequisites** 📦

Before you begin, ensure that your system meets the following requirements:

1. **Python**: Python 3.7 or higher should be installed on your machine. Verify your Python version by running:
   ```bash
   python --version
   ```
   If Python is not installed, download and install it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   
3. **Pygame Library**: This project requires the Pygame library, which will be installed during the setup process.

   Link to Pygame documentation: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)

### 🔧 **Setup**

1. IDE setup: Some popular options include Visual Studio Code (VS Code) and PyCharm.
   
After installing your chosen IDE or editor, ensure that it's properly configured to work with Python and Pygame:
- For VS Code: Install the Pygame Snippets extension for additional Pygame support.
- For PyCharm: Ensure the project interpreter is set to the correct Python version. You can manage libraries like Pygame directly from the PyCharm interface.
  
2. Clone the repository:

    ```bash
    git clone https://github.com/ananyarao10/hackrice-game-development-starter-code.git
    ```
    
3. Navigate into the project directory:
   ```bash
    cd hackrice-game-development-starter-code
    ```

4. Install the required dependencies:

   ```bash
    pip install pygame
    pip install pygame_ui
    ```

After completing these steps, you're ready to start developing your game!

## 📂 **File Descriptions** 📂

Each file in this project is designed to showcase a specific feature of Pygame. Here’s a brief overview of each one:

### 💥 **collision_detection.py** 💥

This file is responsible for the functionality related to detecting and managing collisions between different game objects, such as the player, enemies, and obstacles. It ensures that the game responds appropriately when objects interact with each other.

### 🏃 **player_enemy.py** 🏃

This file sets up a simple Pygame environment for player character movement within a defined screen space. It initializes the game window, creates a player character, and handles basic player input to move the character around the screen. Note that this file uses the game loop.

### 🔄 **game_loop.py** 🔄

This file contains the main game loop which is the core functionality of any game. It handles the overall flow of the game, including initializing game components, processing player input and events, updating game logic (like movement and collisions), and rendering the game visuals on the screen. 

### 🖼️ **image.py** 🖼️

This file is responsible for the functionality of loading, managing, and rendering images and sprites in the game. 

### 🎵 **sound.py** 🎵

This file is responsible for the functionality that manages all audio aspects of the game, including sound effects and background music. It loads, plays, and controls the volume of different sounds.

### 🖥️ **ui.py** 🖥️

This file is responsible for the game's user interface (UI) elements. It manages the display and updates of health bars, score counters, menus, and other visual indicators that help the player navigate and understand the game. 

## 📖 **Usage** 📖

Plan Your Game Concept: Before diving into the code, decide on the type of game you want to create and consider what the player is trying to achieve, what players/enemies/objects will be in the game, and what are the rules of the game.

The starter code provided includes multiple files, each demonstrating a specific feature of Pygame. Each file is a fully functional standalone example, showcasing different aspects of game development with Pygame. To create a more complex and fully functional game, you can combine the features from these separate files into a single file, which we will refer to as main.py.

Creating main.py:
- Create a file called main.py in your project directory
- Import necessary modules and initialize Pygame and set up the game window and other basic configurations (as seen in the beginning of each provided file)
- Use image.py as a reference for how to load and manage game images and use sound.py as a reference for how to load and manage audio assets
- Initialize player and enemy objects and set their initial positions (as seen in player_enemy.py)
- Implement player movement logic as seen in player_enemy.py, handle interactions between game objects as seen in collision_detection.py, render game objects, backgrounds, and UI elements on the screen as seen in ui.py, and play background music and sound effects as seen in sound.py
- Adapt the game loop from game_loop.py to include event handling, game updates, and rendering.
- Test the combined functionality to ensure everything works together seamlessly. Adjust and debug as needed to create a cohesive game experience.

## 🧑‍🎨 **Ways to get creative** 🧑‍🎨

- The current file uses arrow keys for movement, you can modify this to use other keys or add new actions (could also add a way to switch between different weapons or tools)
- The player loses health when colliding with an enemy
- Incorporate new game mechanics, such as power-ups or level progression
- Modify how health bars, score counters, and other indicators are displayed and updated
- Design start screens, pause menus, and game-over screens
- Implement a save and load feature that allows players to save their progress and resume the game

By exploring different ways to level up your game, you can create a more engaging and dynamic experience for players. Use these suggestions as a starting point to experiment and build upon the features in your game and don't forget to have fun!

## ❓ **Questions?** ❓

If you have any questions about using the starter code or any of the tracks here is the contact info of the tracks & workshops committee:
- Ananya Rao (ar156@rice.edu)
- Hannah Watkins (hw76@rice.edu)
- Xinze Feng (xf15@rice.edu)

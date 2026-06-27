# Minesweeper

A classic Minesweeper game built in Python.

## Features
- Classic Minesweeper gameplay
- Toggle between placing mines and clicking tiles with the s key
- Timer and mine counter
- Win/lose detection including the clicked mine and falsely planted flags
- Zero-spreading
- If there are at least 9 free spaces on the board and less than 1/3rd of your cells are mines you are guaranteed to start on a zero tile
- You may chord by clicking on a revealed tile if there are the requisite amount of flags surrounding it

## How to Play
1. Click on a cell while in tile clicking mode to reveal it
2. Click on a cell while in flag planting mode to flag a potential mine
3. Reveal all non-mine cells to win
4. Clicking a mine ends the game
5. Press the smiley to restart the same board size
6. Return to go back to the menu

## Requirements
- Python 3.x

## Installation
```bash
git clone https://github.com/branpower/Minesweeper.git
cd Minesweeper
python Minesweeper.py
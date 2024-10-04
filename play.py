from minesweeper import Minesweeper

'''
Main UI code.
'''
if __name__ == "__main__":
    while True:
        width = int(input("Enter the width of the grid: "))
        height = int(input("Enter the height of the grid: "))
        if width > 1 and height > 1:
            break
        else:
            print("The grid must be at least 2x2. Please enter valid dimensions.")
    diff = int(input("Choose your difficulty Easy:1, Medium:2, Hard:3 : "))
    game = Minesweeper(width=width, height=height, difficulty=diff)
    game.play()

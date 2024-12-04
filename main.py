import os
import random
import time

# Clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Matrix effect
def matrix_emulator():
    # Get terminal size
    columns, rows = os.get_terminal_size()

    # Generate a list for column states
    drops = [random.randint(0, rows) for _ in range(columns)]

    try:
        while True:
            # Clear the screen (refresh frame)
            clear_screen()

            # Print Matrix rain
            for i in range(rows):
                line = ''.join(
                    random.choice([' ', '1', '0', '#', '$', '@', '!']) if i < drops[j] else ' '
                    for j in range(columns)
                )
                print(line)

            # Randomly reset some drops
            drops = [
                drop + 1 if drop < rows and random.random() > 0.05 else random.randint(0, rows)
                for drop in drops
            ]

            time.sleep(0.2)  # Control speed of animation

    except KeyboardInterrupt:
        # Exit on Ctrl+C
        clear_screen()
        print("Matrix Emulator Exited.")

# Run the emulator
if __name__ == "__main__":
    matrix_emulator()

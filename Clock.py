import tkinter as tk
import math
from datetime import datetime

def update_time():
    now = datetime.now()
    hour, minute, second = now.hour % 12, now.minute, now.second

    # Clear the previous text and drawings
    canvas.delete("all")

    # Draw the clock frame
    draw_clock_frame()

    # Create the numeric 'hands'
    hour_hand = str(hour if hour else 12).zfill(2) * 3  # Pad and repeat the hour
    minute_hand = str(minute).zfill(2) * 4  # Pad and repeat the minute
    second_hand = str(second).zfill(2) * 6  # Pad and repeat the second

    # Calculate the angle for each hand
    hour_angle = (hour / 12) * 360
    minute_angle = (minute / 60) * 360
    second_angle = (second / 60) * 360

    # Draw each hand on the clock
    draw_hand(hour_hand, hour_angle, 5, "black", 13, 60)  # Hour hand, closer to center
    draw_hand(minute_hand, minute_angle, 10, "green", 13, 80)  # Minute hand, reversed
    draw_hand(second_hand, second_angle, 14, "red", 13, 100)  # Second hand, closer to center
    root.after(1000, update_time)

def draw_hand(hand_text, angle, radius, color, font_size, total_length, reverse=False):
    angle_rad = math.radians(angle - 90)
    step = total_length / (len(hand_text) // 2)  # Adjust step for paired characters
    if reverse:
        # Start from the end of the hand (near center) going outward
        start_radius = radius + total_length
        step = -step  # Negative to move towards the center
    else:
        start_radius = radius
    for i in range(0, len(hand_text), 2):  # Increment by 2 to handle characters in pairs
        char_pair = hand_text[i:i+2]  # Get character pairs
        x = center_x + (start_radius + (i // 2) * step) * math.cos(angle_rad)
        y = center_y + (start_radius + (i // 2) * step) * math.sin(angle_rad)
        canvas.create_text(x, y, text=char_pair, font=('Helvetica', font_size), fill=color, tags="hand")

def draw_clock_frame():
    # Drawing a circle for the clock frame
    diameter = 220
    canvas.create_oval(center_x - diameter / 2, center_y - diameter / 2,
                       center_x + diameter / 2, center_y + diameter / 2, outline='black', width=2)

root = tk.Tk()
root.title("Digilog Clock")

canvas = tk.Canvas(root, width=222, height=222, bg="white")
canvas.pack()

center_x, center_y = 111, 111   # Center of the canvas

# Set window always on top
root.attributes('-topmost', True)

update_time()  # Initialize the clock

root.mainloop()

## Make to .EXE on terminal
# pip install pyinstaller
# pyinstaller --onefile --icon=clock_icon.ico --noconsole Clock.py


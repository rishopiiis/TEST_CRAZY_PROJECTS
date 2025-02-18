#pip install matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

def draw_clock(hour, minute, second):
    plt.clf()
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)
    plt.axis("off")

    # Draw clock face
    circle = plt.Circle((0, 0), 1, color="black", fill=False, linewidth=2)
    plt.gca().add_patch(circle)

    # Draw hour markers
    for i in range(12):
        angle = np.deg2rad(i * 30)
        x1, y1 = np.cos(angle) * 0.9, np.sin(angle) * 0.9
        x2, y2 = np.cos(angle) * 1.0, np.sin(angle) * 1.0
        plt.plot([x1, x2], [y1, y2], color="black", linewidth=2)

    # Calculate angles
    second_angle = np.deg2rad(90 - second * 6)
    minute_angle = np.deg2rad(90 - minute * 6)
    hour_angle = np.deg2rad(90 - (hour % 12) * 30 - minute * 0.5)

    # Draw hands with printed values
    draw_hand(hour_angle, 0.5, "red", hour)
    draw_hand(minute_angle, 0.7, "blue", minute)
    draw_hand(second_angle, 0.9, "green", second)

    plt.pause(1)

def draw_hand(angle, length, color, value):
    x, y = np.cos(angle) * length, np.sin(angle) * length
    plt.plot([0, x], [0, y], color=color, linewidth=3)
    plt.text(x * 1.1, y * 1.1, str(value), fontsize=12, ha="center", va="center", color=color)

# Run the clock
plt.figure(figsize=(5, 5))
while True:
    now = datetime.datetime.now()
    draw_clock(now.hour, now.minute, now.second)

#pip install astral matplotlib numpy
from astral import LocationInfo
from astral.sun import sun
import datetime
import numpy as np
import matplotlib.pyplot as plt

city = LocationInfo("New York", "USA", "America/New_York", 40.7128, -74.0060)

while True:
    now = datetime.datetime.now()
    s = sun(city.observer, date=now)

    angle = ((now - s['sunrise']).seconds / (s['sunset'] - s['sunrise']).seconds) * 180
    angle = np.deg2rad(angle)

    plt.clf()
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)
    plt.axis("off")

    x, y = np.cos(angle), np.sin(angle)
    plt.plot([0, x], [0, y], color="orange", linewidth=3)
    plt.text(x * 1.1, y * 1.1, "☀", fontsize=15, color="gold")

    plt.pause(60)

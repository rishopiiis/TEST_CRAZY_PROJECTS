#pip install windows-curses


import curses
import time
import random
import datetime

def matrix_clock(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    cols = curses.COLS
    rows = curses.LINES
    drops = [0] * cols

    while True:
        stdscr.clear()

        # Get current time
        now = datetime.datetime.now().strftime("%H:%M:%S")
        stdscr.addstr(rows // 2, (cols - len(now)) // 2, now, curses.A_BOLD)

        for i in range(cols):
            if random.random() < 0.05:
                drops[i] = 0

            if drops[i] < rows:
                char = str(random.randint(0, 9))
                stdscr.addstr(drops[i], i, char, curses.color_pair(1))
                drops[i] += 1

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(matrix_clock)


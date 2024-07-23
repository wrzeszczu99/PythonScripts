import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to typing speed test!")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey() 

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, target, curses.color_pair(3))
    for i, char in enumerate(current):
            correct_char = target[i]
            colour = curses.color_pair(1)
            if char != correct_char:
                colour = curses.color_pair(2)
            
            stdscr.addstr(0, i, char, colour)

    stdscr.addstr(1, 0, f"Current Words per minute: {wpm}")
    return

def game_loop(stdscr):
    target_text = "Hello world is a typical phrase you use, when you starting to learn a new programming language."
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / (time_elapsed/60))/5
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key) == 27:
            break
        if key in ("KEY_BAKCSPACE", '\b', '\x7f'):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    while True:
        game_loop(stdscr)
        stdscr.addstr(2, 0, "You compleated the test! Press any key to continue...\n Or esc to end, if you want so")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)

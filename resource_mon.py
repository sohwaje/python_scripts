import atexit
import sys
import time
try:
    import curses
except ImportError:
    sys.exit('platform not supported')

import psutil
from psutil._common import bytes2human


# --- curses stuff

def tear_down():
    win.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


win = curses.initscr()
atexit.register(tear_down)
curses.endwin()
lineno = 0


def print_line(line, highlight=False):
    """A thin wrapper around curses's addstr()."""
    global lineno
    try:
        if highlight:
            line += " " * (win.getmaxyx()[1] - len(line))
            win.addstr(lineno, 0, line, curses.A_REVERSE)
        else:
            win.addstr(lineno, 0, line, 0)
    except curses.error:
        lineno = 0
        win.refresh()
        raise
    else:
        lineno += 1

# --- /curses stuff


def poll(interval):
    # sleep some time
    time.sleep(interval)

def print_header():
    """Print system-related info, above the process list."""

    def get_dashes(perc):
        dashes = "|" * int((float(perc) / 10 * 4))
        empty_dashes = " " * (40 - len(dashes))
        return dashes, empty_dashes

    # cpu usage
    percs = psutil.cpu_percent(interval=0, percpu=True)
    for cpu_num, perc in enumerate(percs):
        dashes, empty_dashes = get_dashes(perc)
        line= (" CPU%-2s [%s%s] %5s%%" % (cpu_num, dashes, empty_dashes,
                                              perc))
        print_line(line)

    # cpu usage
    mem = psutil.virtual_memory()
    dashes, empty_dashes = get_dashes(mem.percent)
    line = " Mem   [%s%s] %5s%% %6s / %s" % (
        dashes, empty_dashes,
        mem.percent,
        str(int(mem.used / 1024 / 1024)) + "M",
        str(int(mem.total / 1024 / 1024)) + "M"
    )
    print_line(line)

    # swap usage
    swap = psutil.swap_memory()
    dashes, empty_dashes = get_dashes(swap.percent)
    line = " Swap  [%s%s] %5s%% %6s / %s" % (
        dashes, empty_dashes,
        swap.percent,
        str(int(swap.used / 1024 / 1024)) + "M",
        str(int(swap.total / 1024 / 1024)) + "M"
    )
    print_line(line)

def refresh_window():
    """Print results on screen by using curses."""
    curses.endwin()
    win.erase()
    print_header()

    for p in range(1, 100):
        try:
            print_line("")
        except curses.error:
            break
        win.refresh()


def main():
    try:
        interval = 0
        while True:
            poll(interval)
            refresh_window()
            interval = 1
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()

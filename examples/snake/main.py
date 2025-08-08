import curses
import random


def main(stdscr):
    """Run a simple terminal-based Snake game."""
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2],
    ]
    food = [sh // 2, sw // 2]
    stdscr.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT
    while True:
        next_key = stdscr.getch()
        if next_key != -1:
            key = next_key

        head = snake[0].copy()
        if key == curses.KEY_RIGHT:
            head[1] += 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_DOWN:
            head[0] += 1
        else:
            continue

        snake.insert(0, head)

        if (
            head[0] in [0, sh]
            or head[1] in [0, sw]
            or head in snake[1:]
        ):
            msg = "Game Over!"
            stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            stdscr.nodelay(False)
            stdscr.getch()
            break

        if head == food:
            food = None
            while food is None:
                nf = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
                if nf not in snake:
                    food = nf
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(head[0], head[1], '#')


if __name__ == "__main__":
    curses.wrapper(main)

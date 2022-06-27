import curses
from miscclasses import *

screen = curses.initscr()
screen.clear()
curses.noecho()
screen.keypad(True)
curses.cbreak()
curses.curs_set(0)

player = Player()

def endApp():
	curses.nocbreak()
	screen.keypad(False)
	curses.echo()
	curses.endwin()
	quit()
def draw():
	screen.addch(player.y, player.x, str(player))
def doEvents():
	key=screen.getch()
	if key == ord('q'):
		endApp()

while 1:
	screen.clear()
	draw()
	doEvents()
	screen.refresh()
endApp()
import curses
from miscclasses import *

screen = curses.initscr()
screen.clear()
curses.noecho()
screen.keypad(True)
curses.cbreak()
curses.curs_set(0)
player = Player()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

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

	if key == curses.KEY_UP:
		player.y -= 1

	if key == curses.KEY_DOWN:
		player.y += 1
	
	if key == curses.KEY_LEFT:
		player.x -= 1
	
	if key == curses.KEY_RIGHT:
		player.x += 1

while 1:
	screen.clear()
	try:
		draw()
	except:
		doEvents()
	doEvents()
	screen.refresh()
endApp()
import curses
from miscclasses import *

screen = curses.initscr()
screen.clear()
#curses.noecho()
screen.keypad(True)
curses.cbreak()

curses.start_color()
curses.curs_set(0)
player = Player()

curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

def endApp():
	curses.nocbreak()
	screen.keypad(False)
	curses.echo()
	curses.endwin()
	quit()
def draw():
	height, width = screen.getmaxyx()
	for y in range(height):
		for x in range(width):
			if x == player.x and y == player.y:	
				screen.addch(player.y, player.x, "π", curses.color_pair(2))
			else:
				screen.addch(y, x, "#", curses.color_pair(1))
def doEvents():
	key=screen.getch()

	#TODO: fix player movement glitch
	if key == ord('q'):
		endApp()

	elif key == curses.KEY_UP:
		player.y -= 1
		return

	elif key == curses.KEY_DOWN:
		player.y += 1
		return
	
	elif key == curses.KEY_LEFT:
		player.x -= 1
		return
	elif key == curses.KEY_RIGHT:
		player.x += 1
		return
while 1:
	doEvents()
	screen.clear()
	try:
		draw()
	except:
		continue
	screen.refresh()
endApp()
import curses
from miscclasses import *

screen = curses.initscr()
#curses.noecho()
screen.keypad(True)
curses.cbreak()
Map = dict()
curses.start_color()
curses.curs_set(0)
page = 0
player = Player()
height, width = screen.getmaxyx()

curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

screen.addstr(height//2, width//2, "Press any key to start.")
def initMap():
	Map = dict()
	for i in range(1, 5):
		Map[i] = []
		for y in range(height):
			for x in range(width):
				Map[i].append(0)
def endApp():
	curses.nocbreak()
	screen.keypad(False)
	curses.echo()
	curses.endwin()
	quit()
def draw():
	for y in range(height):
		for x in range(width):
			if x == player.x and y == player.y:	
				screen.addch(player.y, player.x, "λ", curses.color_pair(2))
			else:
				screen.addch(y, x, "-", curses.color_pair(1))
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
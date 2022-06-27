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
	#TODO: replace this with arrow keys
	if key == ord('w'):
		player.y -= 1
	
	if key == ord('s'):
		player.y += 1
	
	if key == ord('a'):
		player.x -= 1
	
	if key == ord('d'):
		player.x += 1
while 1:
	screen.clear()
	draw()
	doEvents()
	screen.refresh()
endApp()
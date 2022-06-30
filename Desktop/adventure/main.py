import curses
from miscclasses import *
import random

#TODO: add page support

screen = curses.initscr()
#curses.noecho()
screen.keypad(True)
curses.cbreak()
nonPassables = [1]
Map = None

screen.scrollok(0)
curses.start_color()
curses.curs_set(0)
page = 0
player = Player()
height, width = screen.getmaxyx()

curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

screen.addstr(height//2, width//2, "Press any key to start.")
def initMap():
	global Map
	Map = list()
	# Must be a perfect square
	for i in range(0, 8):
		Map.append([]) # append a page
		for y in range(0, height):
			Map[i].append([]) #append a y-axis
			for x in range(0, width):
				if random.randint(0, 150) != 3:
					Map[i][y].append(0)
				else:
					Map[i][y].append(1)
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
				try:
					screen.addch(player.y, player.x, str(player), curses.color_pair(2))
				except:
					pass
			else:
				try:
					if Map[page][y][x] == 0:
						screen.addch(y, x, "-", curses.color_pair(1))
					elif Map[page][y][x] == 1:
						screen.addch(y, x, "@")
				except:
					pass
def isNonPassable():
	if Map[page][player.y][player.x] in nonPassables:
		return True
	return False
def doEvents():
	global page
	key=screen.getch()

	if key == ord('q'):
		endApp()
	elif key == ord('a'):
		initMap()
	elif key == ord('s'):
		page += 1
		if page == 8:
			page = 0

	elif key == curses.KEY_UP:
		player.y -= 1
		if player.y <= -1:
			player.y += 1
		if isNonPassable():
			player.y += 1

	elif key == curses.KEY_DOWN:
		player.y += 1
		
		if player.y >= height:
			player.y -= 1

		if isNonPassable():
			player.y -= 1
	
	elif key == curses.KEY_LEFT:
		player.x -= 1
		
		if player.x <= -1:
			player.x += 1
		if isNonPassable():
			player.x += 1
	elif key == curses.KEY_RIGHT:
		player.x += 1
		if player.x >= width:
			player.x -= 1
		if isNonPassable():
			player.x -= 1
	return
initMap()
while 1:
	doEvents()
	screen.clear()
	draw()
	screen.refresh()
endApp()
# This module is in charge of all mathematics in the game. A few conventions to note:
# point = (x, y)
# hitbox/rect = (width, height)
# The combination of the two above gives us an absolute rectangle on the screen.

# Returns true if the two given rectangles converge
def boxes_converging(pos1, hitbox1, pos2, hitbox2):
	converging = False
	for point in rect_to_points(pos1, hitbox1):
		converging = converging or point_in_rect(point, pos2, hitbox2)
	return converging
	
# Returns true if point is within the boundaries of the hitbox
def point_in_rect(point, pos, hitbox):
	tl, tr, bl, br = rect_to_points(pos, hitbox)
	return (point[0] >= tl[0] and point[0] <= br[0]) and ((point[1] >= tl[1] and point[1] <= br[1]))
	
# Turns (x, y) and (width, height) to four points - (topleft, topright, bottomleft, bottomright)
def rect_to_points(point, rect):
	return point, (point[0]+rect[0], point[1]), (point[0], point[1]+rect[1]), (point[0]+rect[0], point[1]+rect[1])

# Recieves two points and returns values of m and b in the function: y = mx + b	that passws through both points
def interpolate_line(point1, point2):
	m = (point1[1]-point2[1])/(point1[0]-point2[0])
	b = m*(-point1[0]) + point1[1]
	return m, b
import sys,pygame
class archer():
	def __init__(self,x,y):
		self.health = 120
		self.damage = 45
		self.range = 5
		self.target = ['Air','Ground']
		self.type = 'Ground'
		self.speed = 60
		self.cost = 3
		self.position = (x,y)

class baloon():
	def __init__(self,x,y):
		self.health = 1050
		self.damage = 600
		self.range = 'Melee'
		self.type = 'Air'
		self.target = ['Buildings']
		self.speed = 60
		self.cost = 5
		self.position = (x,y)

class bomber():
	def __init__(self,x,y):
		self.health = 147
		self.damage = 128
		self.range = 4.5
		self.type = 'Ground'
		self.target = ['Ground']
		self.speed = 60
		self.cost = 3
		self.position = (x,y)

class fireball():
	def __init__(self, x, y):
		self.damage = 325
		self.type = 'Air'
		self.target = ['Air','Ground']
		self.cost=4
		self.position=(x,y)
class giant():
	def __init__(self, x, y):
		self.health = 1900
		self.damage = 120
		self.range = 'Melee'
		self.type = 'Ground'
		self.target = ['Buildings']
		self.speed = 45
		self.cost = 5
		self.position = (x, y)
class hog_rider():
	def __init__(self, x, y):
		self.health = 800
		self.damage = 150
		self.range = 'Melee'
		self.type = 'Ground'
		self.target = ['Buildings']
		self.speed = 120
		self.cost = 4
		self.position = (x, y)
class lava_hound():
	def __init__(self, x, y):
		self.health = 3150
		self.damage = 45
		self.range = 2
		self.type = 'Air'
		self.target = ['Buildings']
		self.speed = 60
		self.cost = 7
		self.position = (x, y)
class witch():
	def __init__(self, x, y):
		self.health = 524
		self.damage = 52
		self.range = 5
		self.type = 'Ground'
		self.target = ['Air', 'Ground']
		self.speed = 60
		self.cost = 5
		self.position = (x, y)
class wizard():
	def __init__(self, x, y):
		self.health = 340
		self.damage = 130
		self.range = 5.5
		self.type = 'Ground'
		self.target = ['Air', 'Ground']
		self.speed = 60
		self.cost = 5
		self.position = (x, y)






pygame.init()
windowWidth = 360
windowHeight = 640
first_X = 200
first_Y = 590
reverse_V = 10
card_position = [200,590]
screen = pygame.display.set_mode((windowWidth, windowHeight))


background_img = pygame.image.load('Screenshot_20180124-152631.jpg')
player_img = pygame.image.load('giant.png')



'''while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill((255,255,255))
	screen.blit(image,(0,0))
	pygame.display.update()'''
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP and card_position[1]<300:
			available_area = False 
	screen.fill((255,255,255))
	screen.blit(background_img,(0,0))
	if pygame.mouse.get_pressed()[0] and card_position[0]<pygame.mouse.get_pos()[0]<card_position[0]+50 and card_position[1]<pygame.mouse.get_pos()[1]<card_position[1]+50:
		onclick = True
		diffs = [card_position[0]-pygame.mouse.get_pos()[0],card_position[1]-pygame.mouse.get_pos()[1]]
	if not pygame.mouse.get_pressed()[0]:
		onclick = False
	if onclick:
		card_position = [pygame.mouse.get_pos()[0]+diffs[0],pygame.mouse.get_pos()[1]+diffs[1]]
	if not onclick and  first_X-5<=card_position[0] <= first_X+5 and first_Y-5<=card_position[1] <= first_Y+5:
		available_area = True
	elif not onclick and not(card_position[0] == first_X and card_position[1] == first_Y) and not available_area:
		card_position[0] = card_position[0] + reverse_V*(first_X - card_position[0])/((first_X - card_position[0])**2 + (first_Y - card_position[1])**2)**0.5
		card_position[1] = card_position[1] + reverse_V*(first_Y - card_position[1])/((first_X - card_position[0])**2 + (first_Y - card_position[1])**2)**0.5
	screen.blit(player_img,(card_position[0],card_position[1]))
	pygame.display.update()












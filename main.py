import pygame,sys
Card_List = []
select_card = True

def get_event(Giant,Witch,Wizard,Fireball,Lava,Bomber,Balloon):
	global Card_List,select_card
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP and 25<pygame.mouse.get_pos()[0]<95 and 220<pygame.mouse.get_pos()[1]<300 and Giant not in Card_List:
			Card_List.append(Giant)
		elif event.type == pygame.MOUSEBUTTONUP and 25<pygame.mouse.get_pos()[0]<95 and 220<pygame.mouse.get_pos()[1]<300 and Giant  in Card_List:
			Card_List.remove(Giant)
		if event.type == pygame.MOUSEBUTTONUP and 105<pygame.mouse.get_pos()[0]<175 and 220<pygame.mouse.get_pos()[1]<300 and Wizard not in Card_List:
			Card_List.append(Wizard)
		elif event.type == pygame.MOUSEBUTTONUP and 105<pygame.mouse.get_pos()[0]<175 and 220<pygame.mouse.get_pos()[1]<300 and Wizard in Card_List:
			Card_List.remove(Wizard)
		if event.type == pygame.MOUSEBUTTONUP and 185<pygame.mouse.get_pos()[0]<255 and 220<pygame.mouse.get_pos()[1]<300 and Witch not in Card_List:
			Card_List.append(Witch)
		elif event.type == pygame.MOUSEBUTTONUP and 185<pygame.mouse.get_pos()[0]<255 and 220<pygame.mouse.get_pos()[1]<300 and Witch in Card_List:
			Card_List.remove(Witch)
		if event.type == pygame.MOUSEBUTTONUP and 265<pygame.mouse.get_pos()[0]<335 and 220<pygame.mouse.get_pos()[1]<300 and Fireball not in Card_List:
			Card_List.append(Fireball)
		elif event.type == pygame.MOUSEBUTTONUP and 265<pygame.mouse.get_pos()[0]<335 and 220<pygame.mouse.get_pos()[1]<300 and Fireball in Card_List:
			Card_List.remove(Fireball)
		if event.type == pygame.MOUSEBUTTONUP and 70<pygame.mouse.get_pos()[0]<140 and 360<pygame.mouse.get_pos()[1]<440 and Lava not in Card_List:
			Card_List.append(Lava)
		elif event.type == pygame.MOUSEBUTTONUP and 70<pygame.mouse.get_pos()[0]<140 and 360<pygame.mouse.get_pos()[1]<440 and Lava in Card_List:
			Card_List.remove(Lava)
		if event.type == pygame.MOUSEBUTTONUP and 150<pygame.mouse.get_pos()[0]<220 and 360<pygame.mouse.get_pos()[1]<440 and Balloon not in Card_List:
			Card_List.append(Balloon)
		elif event.type == pygame.MOUSEBUTTONUP and 150<pygame.mouse.get_pos()[0]<220 and 360<pygame.mouse.get_pos()[1]<440 and Balloon in Card_List:
			Card_List.remove(Balloon)
		if event.type == pygame.MOUSEBUTTONUP and 230<pygame.mouse.get_pos()[0]<300 and 360<pygame.mouse.get_pos()[1]<440 and Bomber not in Card_List:
			Card_List.append(Bomber)
		elif event.type == pygame.MOUSEBUTTONUP and 230<pygame.mouse.get_pos()[0]<300 and 360<pygame.mouse.get_pos()[1]<440 and Bomber in Card_List:
			Card_List.remove(Bomber)
		if event.type == pygame.MOUSEBUTTONUP and 130<pygame.mouse.get_pos()[0]<230 and 500<pygame.mouse.get_pos()[1]<550 and 2<len(Card_List)<6:
			select_card = False
			print("i am fucking here",select_card)

class Card:
	def __init__(self,picture_address):
		self.picture = pygame.image.load(picture_address)
		self.power = 0
		self.max_health = 0
		self.health = 0
		self.status = ""
		self.att_status = ""
		self.position = (0,0)
		self.cost = 0
		self.speed = 0
	def move(self,Destination):
		position = (position[0] + self.speed*(Destination[0] - position[0])/((Destination[0] - position[0])**2 + (Destination[1] - position[1])**2)**0.5,position[1] + self.speed*(Destination[1] - position[1])/((Destination[0] - position[0])**2 + (Destination[1] - position[1])**2)**0.5)
	def attack(self,enemy):
		enemy.set_health(get_health - self.power)
	def get_position(self):
		return self.position
	def set_health(self,new_health):
		self.health = new_health
	def get_health(self):
		return self.health
	def set_position(self,new_position):
		self.position = new_position
	def set_pic(self,new_pic_add):
		self.picture = pygame.image.load(new_pic_add)
	def get_pic(self):
		return self.picture



'''class Giant(Card):
	def __init__(picture_address):
		self.image = pygame.image.load (picture)
		self.power = 10
		self.health = 100
		self.status = "Ground"
		self.att_status = "Tower"
		self.position = (0,0)
		self.cost = 5
		self.speed = 5'''



class Tower:
	def __init__(self,picture_address,health,position,range):
		self.img = pygame.image.load(picture_address)
		self.health = health
		self.position = position
		self.range = range
		self.power = 10
	def attack(self,enemy):
		enemy.set_health(enemy.get_health - self.power)
	def set_health(self,new_health):
		self.health = new_health
	def get_health(self):
		return self.health

# class GameRuntime():
# 	def __init__(self):
# 		self.card_list= []
# 		pass

# 	def setup_game(self):
# 		pygame.init()
# 		windowWidth = 360
# 		windowHeight = 640


# 	def init_cards(self):
# 		self.Giant = Card("GiantCard copy.png")
# 		Witch = Card("WitchCard copy.png")
# 		Fireball = Card("FireballCard copy.png")
# 		Wizard = Card("WizardCard copy.png")
# 		Bomber = Card("BomberCard copy.png")
# 		Balloon = Card("BalloonCard copy.png")
# 		Archer = Card("archers copy.png")
# 		Lava = Card("LavaHoundCard copy.png")

# 	def start_game(self):





def main():
	global Card_List,select_card
	pygame.init()
	windowWidth = 360
	windowHeight = 640
	Giant=Card("GiantCard copy.png")
	Witch=Card("WitchCard copy.png")
	Fireball=Card("FireballCard copy.png")
	Wizard=Card("WizardCard copy.png")
	Bomber = Card("BomberCard copy.png")
	Balloon = Card("BalloonCard copy.png")
	Archer = Card("archers copy.png")
	Lava = Card("LavaHoundCard copy.png")

	screen = pygame.display.set_mode((windowWidth,windowHeight))

	while select_card:

		screen.fill((255,255,255))
		get_event(Giant,Witch,Wizard,Fireball,Lava,Bomber,Balloon)
		#print(select_card)
		screen.blit(Giant.picture,(25,220))
		screen.blit(Wizard.picture,(105,220))
		screen.blit(Witch.picture,(185,220))
		screen.blit(Fireball.picture,(265,220))
		screen.blit(Lava.picture,(70,360))
		screen.blit(Balloon.picture,(150,360))
		screen.blit(Bomber.picture,(230,360))
		if Giant in Card_List:
			screen.blit(pygame.image.load("CheckMark.png"),(45,190))
		if Wizard in Card_List:
			screen.blit(pygame.image.load("CheckMark.png"),(120,190))
		if Witch in Card_List:
			screen.blit(pygame.image.load("CheckMark.png"),(200,190))
		if Fireball in Card_List:
			screen.blit(pygame.image.load("CheckMark.png"),(280,190))
		if Lava in Card_List:
			screen.blit(pygame.image.load("CheckMark.png"),(88,330))
		if Balloon in Card_List:
			screen.blit(pygame.image.load("CheckMark.png"),(165,330))
		if Bomber in Card_List:
			screen.blit(pygame.image.load("CheckMark.png"),(245,330)) 
		if not(130<pygame.mouse.get_pos()[0]<230 and 500<pygame.mouse.get_pos()[1]<550 and pygame.mouse.get_pressed()[0]):	
			pygame.draw.rect(screen,(0,255,0),(130,500,100,50))
		elif 130<pygame.mouse.get_pos()[0]<230 and 500<pygame.mouse.get_pos()[1]<550 and pygame.mouse.get_pressed()[0]:
			pygame.draw.rect(screen,(0,200,0),(130,500,100,50))
		pygame.display.update()

main()






































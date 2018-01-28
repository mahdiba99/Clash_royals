
import pygame,sys,time
from pygame import mouse as m
InGameCards=[]
Card_List = []
select_card = True
card = None
budget = 5
prev_diff = 0

def intial():
    carts_distance = int((360 - len(Card_List) * 60) / (len(Card_List) + 1))
    distance = carts_distance
    for card in Card_List:
        card.set_position((distance, 530))
        # screen.blit(card.picture, (distance, 530))
        card.first_x = distance
        distance = distance + carts_distance + 60

        if card.id == 1:
            # card.picture = pygame.image.load("GiantCard_ingame.png")
            card.max_health = 800
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.2
            card.att_status = 'building'
            card.range = 5 + 42
            card.damage = 120
        if card.id == 2:
            # card.picture = pygame.image.load("WitchCard_ingame.png")
            card.max_health = 500
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 50
        if card.id == 3:
            # card.picture = pygame.image.load("WizardCard_ingame.png")
            card.max_health = 350
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 80
        if card.id == 4:
            # card.picture = pygame.image.load("FireballCard_ingame.png")
            card.max_health = 350
            card.health = card.max_health
            card.status = 'Air'
            card.cost = 4
            card.available_area = 50
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 50
        if card.id == 5:
            # card.picture = pygame.image.load("BomberCard_ingame.png")
            card.max_health = 150
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 3
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 50
        if card.id == 6:
            # card.picture = pygame.image.load("BalloonCard_ingame.png")
            card.max_health = 600
            card.health = card.max_health
            card.status = 'Air'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'building'
            card.range = 42 + 5
            card.damage = 100
        if card.id == 7:
            # card.picture = pygame.image.load("archers_ingame.png")
            card.max_health = 300
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 3
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 50
        if card.id == 8:
            # card.picture = pygame.image.load("LavaHoundCard_ingame.png")
            card.max_health = 1000
            card.health = card.max_health
            card.status = 'Air'
            card.cost = 7
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'building'
            card.range = 42 + 15
            card.damage = 50


def get_event(Giant, Witch, Wizard, Fireball, Archer, Bomber, Balloon):
    global Card_List, select_card
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and 25 < pygame.mouse.get_pos()[0] < 95 and 220 < pygame.mouse.get_pos()[
            1] < 300 and Giant not in Card_List:
            Card_List.append(Giant)
        elif event.type == pygame.MOUSEBUTTONUP and 25 < pygame.mouse.get_pos()[0] < 95 and 220 < \
                pygame.mouse.get_pos()[1] < 300 and Giant in Card_List:
            Card_List.remove(Giant)
        if event.type == pygame.MOUSEBUTTONUP and 105 < pygame.mouse.get_pos()[0] < 175 and 220 < \
                pygame.mouse.get_pos()[1] < 300 and Wizard not in Card_List:
            Card_List.append(Wizard)
        elif event.type == pygame.MOUSEBUTTONUP and 105 < pygame.mouse.get_pos()[0] < 175 and 220 < \
                pygame.mouse.get_pos()[1] < 300 and Wizard in Card_List:
            Card_List.remove(Wizard)
        if event.type == pygame.MOUSEBUTTONUP and 185 < pygame.mouse.get_pos()[0] < 255 and 220 < \
                pygame.mouse.get_pos()[1] < 300 and Witch not in Card_List:
            Card_List.append(Witch)
        elif event.type == pygame.MOUSEBUTTONUP and 185 < pygame.mouse.get_pos()[0] < 255 and 220 < \
                pygame.mouse.get_pos()[1] < 300 and Witch in Card_List:
            Card_List.remove(Witch)
        if event.type == pygame.MOUSEBUTTONUP and 265 < pygame.mouse.get_pos()[0] < 335 and 220 < \
                pygame.mouse.get_pos()[1] < 300 and Fireball not in Card_List:
            Card_List.append(Fireball)
        elif event.type == pygame.MOUSEBUTTONUP and 265 < pygame.mouse.get_pos()[0] < 335 and 220 < \
                pygame.mouse.get_pos()[1] < 300 and Fireball in Card_List:
            Card_List.remove(Fireball)
        if event.type == pygame.MOUSEBUTTONUP and 70 < pygame.mouse.get_pos()[0] < 140 and 360 < pygame.mouse.get_pos()[
            1] < 440 and Archer not in Card_List:
            Card_List.append(Archer)
        elif event.type == pygame.MOUSEBUTTONUP and 70 < pygame.mouse.get_pos()[0] < 140 and 360 < \
                pygame.mouse.get_pos()[1] < 440 and Archer in Card_List:
            Card_List.remove(Archer)
        if event.type == pygame.MOUSEBUTTONUP and 150 < pygame.mouse.get_pos()[0] < 220 and 360 < \
                pygame.mouse.get_pos()[1] < 440 and Balloon not in Card_List:
            Card_List.append(Balloon)
        elif event.type == pygame.MOUSEBUTTONUP and 150 < pygame.mouse.get_pos()[0] < 220 and 360 < \
                pygame.mouse.get_pos()[1] < 440 and Balloon in Card_List:
            Card_List.remove(Balloon)
        if event.type == pygame.MOUSEBUTTONUP and 230 < pygame.mouse.get_pos()[0] < 300 and 360 < \
                pygame.mouse.get_pos()[1] < 440 and Bomber not in Card_List:
            Card_List.append(Bomber)
        elif event.type == pygame.MOUSEBUTTONUP and 230 < pygame.mouse.get_pos()[0] < 300 and 360 < \
                pygame.mouse.get_pos()[1] < 440 and Bomber in Card_List:
            Card_List.remove(Bomber)
        if event.type == pygame.MOUSEBUTTONUP and 130 < pygame.mouse.get_pos()[0] < 230 and 500 < \
                pygame.mouse.get_pos()[1] < 550 and 2 < len(Card_List) < 6:
            select_card = False


def main_get_event():
    global card,InGameCards,Card_List,budget
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if card:
            if event.type == pygame.MOUSEBUTTONUP and card.get_position()[1] > card.available_area and card.get_cost() <= budget and card.get_position()[1] < 440:
                next_card = Card('background.jpg')
                next_card.picture=card.picture
                next_card.position = (card.first_x , 530)
                next_card.damage = card.damage
                next_card.max_health = card.max_health
                next_card.health = card.health
                next_card.status = card.status
                next_card.att_status = card.att_status
                next_card.cost = card.cost
                next_card.speed = card.speed
                next_card.id = card.id
                next_card.range = card.range
                next_card.available_area = card.available_area
                next_card.first_x = card.first_x
                Card_List.append(next_card)
                if card.id == 1:
                    card.picture = pygame.image.load("GiantCard_ingame.png")
                elif card.id == 2:
                    card.picture = pygame.image.load("WitchCard_ingame.png")
                elif card.id == 3:
                    card.picture = pygame.image.load("WizardCard_ingame.png")
                elif card.id == 4:
                    card.picture = pygame.image.load("FireballCard_ingame.png")
                elif card.id == 5:
                    card.picture = pygame.image.load("BomberCard_ingame.png")
                elif card.id == 6:
                    card.picture = pygame.image.load("BalloonCard_ingame.png")
                elif card.id == 7:
                    card.picture = pygame.image.load("archers_ingame.png")
                elif card.id == 8:
                    card.picture = pygame.image.load("LavaHoundCard_ingame.png")

                InGameCards.append(card)
                Card_List.remove(card)
                budget-=card.cost
                card = None
            elif event.type == pygame.MOUSEBUTTONUP:

                card.position = (card.first_x , 530)
                card = None


class Card:
    def __init__(self, picture_address):
        self.picture = pygame.image.load(picture_address)
        self.damage = 0
        self.max_health = 0
        self.health = 0
        self.status = ""
        self.att_status = ""
        self.position = (0, 0)
        self.cost = 0
        self.speed = 0
        self.id = 0
        self.range = 0
        self.available_area = 0
        self.first_x = 0
    def move(self, Destination):
        self.position = (self.position[0] + self.speed * (Destination[0] - self.position[0]) / (
                    (Destination[0] - self.position[0]) ** 2 + (Destination[1] - self.position[1]) ** 2) ** 0.5,
                         self.position[1] + self.speed * (Destination[1] - self.position[1]) / (
                                (Destination[0] - self.position[0]) ** 2 + (Destination[1] - self.position[1]) ** 2) ** 0.5)

    def attack(self, enemy):
        enemy.set_health(enemy.get_health - self.damage)

    def get_position(self):
        return self.position

    def set_health(self, new_health):
        self.health = new_health

    def get_health(self):
        return self.health

    def set_position(self, new_position):
        self.position = new_position

    def set_pic(self, new_pic_add):
        self.picture = pygame.image.load(new_pic_add)

    def get_pic(self):
        return self.picture

    def get_cost(self):
        return self.cost

    def get_id(self):
        return self.id


def ShowCards(Card_List, screen):
    for card in Card_List:
        screen.blit(card.picture, card.get_position())
    for card in InGameCards:
        screen.blit(card.picture, card.get_position())



'''class Giant(Card):
    5022-2910-6143-1597
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
    def __init__(self, picture_address, health, position, range):
        self.img = pygame.image.load(picture_address)
        self.health = health
        self.position = position
        self.range = range
        self.power = 10

    def attack(self, enemy):
        enemy.set_health(enemy.get_health - self.power)

    def set_health(self, new_health):
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


# def deposit(budget):
#     if budget < 10:
#         budget += 1
#         T(2.0, deposit(budget))
#     else:
#         budget_need = False


# def clock(watch):
#     watch -= 1
#     if watch > 0:
#         T(1.0, clock(watch)).start()
# def deposit(time_need_begin):
#     global budget,prev_diff
#     diff = int((time.time() - time))
def deposit(time_need_begin):
    global budget,prev_diff
    diff = int((time.time()-time_need_begin))
    print(budget)
    if budget<10 and prev_diff!=diff and diff%2==0 :
        budget+=1
        prev_diff = diff
        return False
    elif budget==10:
        prev_diff = diff
        return True

def chosen_card(pos, Card_List):
    for card in Card_List:
        if card.get_position()[0] < pos[0] < card.get_position()[0] + 68 and card.get_position()[1] < pos[1] < \
                card.get_position()[1] + 80:
            return card
    return None


def main():
    time_need_begin = None
    game_end = None
    game_begin = None
    budget_need = True
    global Card_List, select_card, card , budget , prev_diff
    InGameCards = []
    pygame.init()
    windowWidth = 360
    windowHeight = 640
    Giant = Card("GiantCard copy.png")
    Giant.id = 1
    Witch = Card("WitchCard copy.png")
    Witch.id = 2
    Fireball = Card("FireballCard copy.png")
    Fireball.id = 4
    Wizard = Card("WizardCard copy.png")
    Wizard.id = 3
    Bomber = Card("BomberCard copy.png")
    Bomber.id = 5
    Balloon = Card("BalloonCard copy.png")
    Balloon.id = 6
    Archer = Card("archers copy.png")
    Archer.id = 7
    Lava = Card("LavaHoundCard copy.png")
    Lava.id = 8
    screen = pygame.display.set_mode((windowWidth, windowHeight))

    while select_card:

        screen.fill((255, 255, 255))
        get_event(Giant, Witch, Wizard, Fireball, Archer, Bomber, Balloon)
        screen.blit(Giant.picture, (25, 220))
        screen.blit(Wizard.picture, (105, 220))
        screen.blit(Witch.picture, (185, 220))
        screen.blit(Fireball.picture, (265, 220))
        screen.blit(Archer.picture, (70, 360))
        screen.blit(Balloon.picture, (150, 360))
        screen.blit(Bomber.picture, (230, 360))
        if Giant in Card_List:
            screen.blit(pygame.image.load("CheckMark.png"), (45, 190))
        if Wizard in Card_List:
            screen.blit(pygame.image.load("CheckMark.png"), (120, 190))
        if Witch in Card_List:
            screen.blit(pygame.image.load("CheckMark.png"), (200, 190))
        if Fireball in Card_List:
            screen.blit(pygame.image.load("CheckMark.png"), (280, 190))
        if Archer in Card_List:
            screen.blit(pygame.image.load("CheckMark.png"), (88, 330))
        if Balloon in Card_List:
            screen.blit(pygame.image.load("CheckMark.png"), (165, 330))
        if Bomber in Card_List:
            screen.blit(pygame.image.load("CheckMark.png"), (245, 330))
        if not (130 < pygame.mouse.get_pos()[0] < 230 and 500 < pygame.mouse.get_pos()[1] < 550 and
                pygame.mouse.get_pressed()[0]):
            pygame.draw.rect(screen, (0, 255, 0), (130, 500, 100, 50))
        elif 130 < pygame.mouse.get_pos()[0] < 230 and 500 < pygame.mouse.get_pos()[1] < 550 and \
                pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, (0, 200, 0), (130, 500, 100, 50))
        pygame.display.update()
    intial()
    game_begin = time.time()
    while True:
        game_end = time.time()
        if int(game_end - game_begin) == 120:
            break
        main_get_event()
        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load("background.jpg"), (0, 0))
        ShowCards(Card_List, screen)
        if budget_need and budget!=10:
            time_need_begin = time.time()
            budget_need = False
        budget_need = deposit(time_need_begin)
        if m.get_pressed()[0] and m.get_pos()[1] > 400 and not card:
            card = chosen_card(m.get_pos(), Card_List)
        if card:
            card.set_position(m.get_pos())

        pygame.display.update()


main()
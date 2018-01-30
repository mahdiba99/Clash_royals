import pygame,sys,time,random
from pygame import mouse as m
InGameCards=[]
Card_List = []
Tower_List = []
Other_Towers = []
in_range_enmy = []
select_card = True
card = None
budget = 5
prev_diff = 0
Ingame_enm_cards = []

def intial():
    global Card_List,Tower_List
    carts_distance = int((360 - len(Card_List) * 60) / (len(Card_List) + 1))
    distance = carts_distance
    for card in Card_List:
        card.set_position((distance, 530))
        card.first_x = distance
        distance = distance + carts_distance + 60
        if card.id == 1:
            card.max_health = 800.0
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.2
            card.att_status = 'building'
            card.range = 5 + 42
            card.damage = 250/50
        if card.id == 2:
            card.max_health = 500.0
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 150/50
        if card.id == 3:
            card.max_health = 350.0
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 300/50
        if card.id == 4:
            card.max_health = 350.0
            card.health = card.max_health
            card.status = 'Air'
            card.cost = 4
            card.available_area = 50
            card.speed = 0
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 300
        if card.id == 5:
            card.max_health = 150.0
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 3
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = 200/50
        if card.id == 6:
            card.max_health = 600.0
            card.health = card.max_health
            card.status = 'Air'
            card.cost = 5
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'building'
            card.range = 42 + 5
            card.damage = 400/50
        if card.id == 7:
            card.max_health = 300.0
            card.health = card.max_health
            card.status = 'Ground'
            card.cost = 3
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'Air,Ground'
            card.range = 30 + 42
            card.damage = float(120.0/50.0)
        if card.id == 8:
            card.max_health = 100.0
            card.health = card.max_health
            card.status = 'Air'
            card.cost = 7
            card.available_area = 280
            card.speed = 0.3
            card.att_status = 'building'
            card.range = 42 + 15
            card.damage = 50/50
    for tower in Tower_List:
        if tower.id == 1:
            tower.max_health = 2000.0
            tower.health = tower.max_health
            tower.position = (149,406)
            tower.range = 65
            tower.damage = 80
            tower.size = (57,78)
        if tower.id == 2:
            tower.max_health = 1500.0
            tower.health = tower.max_health
            tower.position = (68,370)
            tower.range = 65
            tower.damage = 65
            tower.size = (40,51)
        if tower.id == 3:
            tower.max_health = 1500.0
            tower.health = tower.max_health
            tower.position = (258,370)
            tower.range = 65
            tower.damage = 65
            tower.size = (40,51)
    for tower in Other_Towers:
        if tower.id == 1:
            tower.max_health = 2000.0
            tower.health = tower.max_health
            tower.position = (149,56)
            tower.range = 65
            tower.damage = 80
            tower.size = (60,81)
        if tower.id == 2:
            tower.max_health = 1500.0
            tower.health = tower.max_health
            tower.position = (68,110)
            tower.range = 65
            tower.damage = 65
            tower.size = (40,54)
        if tower.id == 3:
            tower.max_health = 1500.0
            tower.health = tower.max_health
            tower.position = (258,110)
            tower.range = 65
            tower.damage = 65
            tower.size = (40,54)



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
        self.Destination = (None,None)
    def move(self, Destination):
        self.position = (self.position[0] + self.speed * (Destination[0] - self.position[0]) / (
                    (Destination[0] - self.position[0]) ** 2 + (Destination[1] - self.position[1]) ** 2) ** 0.5,
                         self.position[1] + self.speed * (Destination[1] - self.position[1]) / (
                                (Destination[0] - self.position[0]) ** 2 + (Destination[1] - self.position[1]) ** 2) ** 0.5)
    def attack(self, enemy):
        enemy.set_health(enemy.get_health() - self.damage)
        if self.id == 4:
            self.set_health(-1)

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


def ShowCards(Card_List, screen , Ingame_enm_cards):
    global budget,Tower_List,Other_Towers
    for tower in Tower_List:
        screen.blit(tower.img,tower.position)
        health = int(float(tower.health/tower.max_health)*tower.size[0])+1
        if tower.health == tower.max_health:
            health -=1
        if tower.id!=1:
            pygame.draw.rect(screen,(30,144,255),(tower.position[0]+6,tower.position[1]+66,health,5))
        else:
            pygame.draw.rect(screen,(30,144,255),(tower.position[0]+4,tower.position[1]+76,health,5))

        # for i in range(health):
        #     if tower.id!=1:
        #         pygame.draw.rect(screen,(30,144,255),(tower.position[0]+i*10+6,tower.position[1]+66,9,5))
        #     else:
        #         pygame.draw.rect(screen,(30,144,255),(tower.position[0]+i*14+4,tower.position[1]+76,12,5))

    for tower in Other_Towers:
        screen.blit(tower.img,tower.position)
        health = int(float(tower.health/tower.max_health)*tower.size[0])+1
        if tower.health == tower.max_health:
            health -= 1
        
        if tower.id!=1:
            pygame.draw.rect(screen,(255,69,0),(tower.position[0]+8,tower.position[1]-5,health,5))
        else:
            pygame.draw.rect(screen,(255,69,0),(tower.position[0]+10,tower.position[1]-3,health,5))


    for card in Card_List:
        screen.blit(card.picture, card.get_position())

    for card in InGameCards:
        screen.blit(card.picture, card.get_position())
        health = int(float(card.health/card.max_health)*40)+1
        if card.health == card.max_health:
            health -=1
        pygame.draw.rect(screen,(30,144,255),(card.get_position()[0],card.get_position()[1]-7,health,5))
    for i in range(budget):
        pygame.draw.rect(screen,(255,0,255),(12+i*(30+4),617,30,20))
    
    if Ingame_enm_cards: 
        for card in Ingame_enm_cards:
            screen.blit(card.picture, card.get_position())
            health = int(float(card.health/card.max_health)*40)+1
            if card.health == card.max_health:
                health -=1            
            pygame.draw.rect(screen,(255,69,0),(card.get_position()[0],card.get_position()[1]-7,health,5))



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
    def __init__(self,picture_address):
        self.img = pygame.image.load(picture_address)
        self.health = None
        self.max_health = 0
        self.position = None
        self.range = 0
        self.damage = 10
        self.size = 0
        self.id = 0

    def attack(self, enemy):
        enemy.set_health(enemy.get_health - self.power)

    def set_health(self, new_health):
        self.health = new_health

    def get_health(self):
        return self.health
def closest_target(M_card):
    c_distance = 2000
    if M_card in InGameCards:
        for tower in Other_Towers:
            distance = ((tower.position[0] - M_card.position[0])**2 + (tower.position[1] - M_card.position[1])**2)**0.5
            if c_distance> distance:
                c_distance = distance
                c_tower = tower
        return c_tower
    else:
        for tower in Tower_List:
            distance = ((tower.position[0] - M_card.position[0])**2 + (tower.position[1] - M_card.position[1])**2)**0.5
            if c_distance>= distance:
                c_distance = distance
                c_tower = tower
        return c_tower



def find_destination(M_card):

    if M_card in InGameCards:
        if M_card.id != 6:
            if 0<M_card.position[0]<180 and M_card.position[1]>270:
                #print((70,270))
                #print(M_card.position)
                return (70,270)
            if 180<M_card.position[0] and M_card.position[1]>270:
                print((255,270))
                return (255,270)
            else:
               target=closest_target(M_card)
               return target.position
        else:
            target=closest_target(M_card)
            return target.position
    else:
        if M_card.id != 6:
            if 0<M_card.position[0]<180 and M_card.position[1]<260:
                return (70,260)
            if 180<M_card.position[0] and M_card.position[1]<260:
                return (255,260)
            else:
               target=closest_target(M_card)
               return target.position
        else:
            target=closest_target(M_card)
            return target.position
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
    if budget<10 and prev_diff!=diff and diff%2==0 :
        budget+=1
        prev_diff = diff
        return False
    elif budget==10:
        prev_diff = diff
        return True
def add_enemy(time_left,pre_time_left):
    if time_left!=pre_time_left:
        return True
    else:
        return False


def chosen_card(pos, Card_List):
    for card in Card_List:
        if card.get_position()[0] < pos[0] < card.get_position()[0] + 68 and card.get_position()[1] < pos[1] < \
                card.get_position()[1] + 80:
            return card
    return None
def in_range(card , other_cards , other_towers=Other_Towers):
    if not other_cards or (card.att_status == "building" and other_cards[0] not in other_towers):
        return []
    in_range_enemy=[]
    for enemy in other_cards:
        if enemy in other_towers or enemy.status in card.att_status:
            if (((enemy.position[0]-20)-(card.position[0]-20))**2 + ((enemy.position[1]-23.5)-(card.position[1]-23.5))**2)**0.5 <= card.range:
                in_range_enemy.append(enemy)

    return(in_range_enemy)
def random_cards(Giant, Witch, Wizard, Fireball, Archer, Bomber, Balloon):
    enemy_id = []
    enm_cards = []
    while True:
        if len(enemy_id)==5:
            break
        else:
            a = random.randrange(1,8)
            if a not in enemy_id and a!=4:
                enemy_id.append(a)
    for i in enemy_id:
        if i == 1:
            enm_cards.append(Giant)
        if i == 2:
            enm_cards.append(Witch)
        if i ==3:
            enm_cards.append(Wizard)
        if i == 4:
            enm_cards.append(Fireball)
        if i == 5:
            enm_cards.append(Bomber)
        if i == 6:
            enm_cards.append(Balloon)
        if i == 7:
            enm_cards.append(Archer)
    return enm_cards
def new_enemy(enm_cards):
    enm_id = enm_cards[random.randrange(0,5)].id
    new_enm = Card("background.jpg")
    new_enm.position = (random.randrange(90,220), random.randrange(120,200))
    if enm_id == 1:
        new_enm.id = 1
        new_enm.max_health = 800.0
        new_enm.health = new_enm.max_health
        new_enm.status = 'Ground'
        new_enm.cost = 5
        new_enm.available_area = 280
        new_enm.speed = 0.2
        new_enm.att_status = 'building'
        new_enm.range = 5 + 42
        new_enm.damage = 250/50
    if enm_id == 2:
        new_enm.id = 2
        new_enm.max_health = 500.0
        new_enm.health = new_enm.max_health
        new_enm.status = 'Ground'
        new_enm.cost = 5
        new_enm.available_area = 280
        new_enm.speed = 0.3
        new_enm.att_status = 'Air,Ground'
        new_enm.range = 30 + 42
        new_enm.damage = 150/50
    if enm_id == 3:
        new_enm.id = 3
        new_enm.max_health = 350.0
        new_enm.health = new_enm.max_health
        new_enm.status = 'Ground'
        new_enm.cost = 5
        new_enm.available_area = 280
        new_enm.speed = 0.3
        new_enm.att_status = 'Air,Ground'
        new_enm.range = 30 + 42
        new_enm.damage = 300/50
    if enm_id == 4:
        new_enm.id = 4
        new_enm.max_health = 350.0
        new_enm.health = new_enm.max_health
        new_enm.status = 'Air'
        new_enm.cost = 4
        new_enm.available_area = 50
        new_enm.speed = 0.3
        new_enm.att_status = 'Air,Ground'
        new_enm.range = 30 + 42
        new_enm.damage = 500/50
    if enm_id == 5:
        new_enm.id =5
        new_enm.max_health = 150.0
        new_enm.health = new_enm.max_health
        new_enm.status = 'Ground'
        new_enm.cost = 3
        new_enm.available_area = 280
        new_enm.speed = 0.3
        new_enm.att_status = 'Air,Ground'
        new_enm.range = 30 + 42
        new_enm.damage = 200/50
    if enm_id == 6:
        new_enm.id = 6
        new_enm.max_health = 600.0
        new_enm.health = new_enm.max_health
        new_enm.status = 'Air'
        new_enm.cost = 5
        new_enm.available_area = 280
        new_enm.speed = 0.3
        new_enm.att_status = 'building'
        new_enm.range = 42 + 5
        new_enm.damage = 400/50
    if enm_id == 7:
        new_enm.id = 7
        new_enm.max_health = 300.0
        new_enm.health = new_enm.max_health
        new_enm.status = 'Ground'
        new_enm.cost = 3
        new_enm.available_area = 280
        new_enm.speed = 0.3
        new_enm.att_status = 'Air,Ground'
        new_enm.range = 30 + 42
        new_enm.damage = float(120.0/50.0)
    if new_enm.id == 1:
        new_enm.picture = pygame.image.load("GiantCard_ingame.png")
    elif new_enm.id == 2:
        new_enm.picture = pygame.image.load("WitchCard_ingame.png")
    elif new_enm.id == 3:
        new_enm.picture = pygame.image.load("WizardCard_ingame.png")
    elif new_enm.id == 4:
        new_enm.picture = pygame.image.load("FireballCard_ingame.png")
    elif new_enm.id == 5:
        new_enm.picture = pygame.image.load("BomberCard_ingame.png")
    elif new_enm.id == 6:
        new_enm.picture = pygame.image.load("BalloonCard_ingame.png")
    elif new_enm.id == 7:
        new_enm.picture = pygame.image.load("archers_ingame.png")
    elif new_enm.id == 8:
        new_enm.picture = pygame.image.load("LavaHoundCard_ingame.png")
    return new_enm

def main():
    pre_time_left = None
    result = None
    time_need_begin = None
    game_end = None
    game_begin = None
    budget_need = True
    global Card_List, select_card, card , budget , prev_diff , Tower_List , Other_Towers,InGameCards, Ingame_enm_cards
    pygame.init()
    Clash_Font = pygame.font.SysFont("Chalkduster",25)
    Clash_Font1 = pygame.font.SysFont("Chalkduster",30)
    Clash_Font2 = pygame.font.SysFont("Chalkduster",18)
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
    Main_Tower = Tower("main_tower.png")
    Main_Tower.id = 1
    Side_Tower1 = Tower("side_tower.png")
    Side_Tower1.id = 2
    Side_Tower2 = Tower("side_tower.png")
    Side_Tower2.id = 3
    Tower_List.extend([Main_Tower,Side_Tower1,Side_Tower2])
    Enm_Main_Tower = Tower("tower2.png")
    Enm_Main_Tower.id = 1
    Enm_Side_Tower1 = Tower("tower1.png")
    Enm_Side_Tower1.id = 2
    Enm_Side_Tower2 = Tower("tower1.png")
    Enm_Side_Tower2.id = 3
    Other_Towers.extend([Enm_Main_Tower,Enm_Side_Tower1,Enm_Side_Tower2])
    enm_cards = random_cards(Giant, Witch, Wizard, Fireball, Archer, Bomber, Balloon)
    screen = pygame.display.set_mode((windowWidth, windowHeight))

    while select_card:
        lable = Clash_Font1.render("Choose Your Cards",True,(255,215,0))
        screen.fill((255, 255, 255))
        screen.blit(lable,(17,100))
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
        lable = Clash_Font2.render("Ready",True,(0,0,0))
        screen.blit(lable,(150,510))
        pygame.display.update()
    intial()
    extra_time = False
    game_begin = time.time()
    while True:
        for i in InGameCards:
            if i.health<=0:
                InGameCards.remove(i)
        for i in Ingame_enm_cards:
            if i.health<=0:
                Ingame_enm_cards.remove(i)
        for i in Tower_List:
            if i.health<=0:
                Tower_List.remove(i)
        for i in Other_Towers:
            if i.health<=0:
                Other_Towers.remove(i)

        game_end = time.time()
        time_left = 180 - int(game_end - game_begin)
        if time_left>30:
            if time_left%60<10: 
                lable = Clash_Font.render(str(time_left//60)+':'+'0'+str(time_left%60),True,(255,255,255))
            else:
                lable = Clash_Font.render(str(time_left//60)+':'+str(time_left%60),True,(255,255,255))
        else:
            if time_left%60<10: 
                lable = Clash_Font.render(str(time_left//60)+':'+'0'+str(time_left%60),True,(255,0,0))
            else:
                lable = Clash_Font.render(str(time_left//60)+':'+str(time_left%60),True,(255,0,0))
        if Main_Tower not in Tower_List:
            result = -1
            break
        if Enm_Main_Tower not in Other_Towers:
            result = 1
            break
        if int(game_end - game_begin) == 180:
            if len (Other_Towers) > len(Tower_List):
                result = -1
                break
            elif len (Other_Towers) == len(Tower_List) and not extra_time:
                game_begin+=60
                extra_time = True
            elif len (Other_Towers) < len(Tower_List):
                result = 1
                break
            elif len (Other_Towers) == len(Tower_List) and extra_time:
                result = 0
                break
        if time_left%7 == 0 and add_enemy(time_left,pre_time_left):
            enemy = new_enemy(enm_cards)
            Ingame_enm_cards.append(enemy)
        pre_time_left = time_left

        main_get_event()
        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load("background.jpg"), (0, 0))
        screen.blit(lable,(300,10))
        ShowCards(Card_List, screen ,Ingame_enm_cards)
        if budget_need and budget!=10:
            time_need_begin = time.time()
            budget_need = False
        budget_need = deposit(time_need_begin)
        if m.get_pressed()[0] and m.get_pos()[1] > 400 and not card:
            card = chosen_card(m.get_pos(), Card_List)
        if card:
            card.set_position(m.get_pos())
        for ingamecard in InGameCards:
            in_range_tower = in_range(ingamecard, Other_Towers)
            in_range_enmy = in_range(ingamecard, Ingame_enm_cards)
            if in_range_tower:
                closest_distance = (640 ** 2 + 360 ** 2) ** 0.5
                for tower in in_range_tower:
                    distance = (((tower.position[0] - tower.size[0] / 2) - (ingamecard.position[0] - 20)) ** 2 + (
                                (tower.position[1] - tower.size[1] / 2) - (ingamecard.position[1] - 23.5)) ** 2) ** 0.5
                    if distance < closest_distance:
                        closest_tower = tower
                        closest_distance = distance
                ingamecard.attack(closest_tower)
            elif in_range_enmy and ingamecard.att_status != 'building':
                closest_distance = (640 ** 2 + 360 ** 2) ** 0.5
                for enemy in in_range_enmy:
                    distance = (((enemy.position[0] - 20) - (ingamecard.position[0] - 20)) ** 2 + (
                            (enemy.position[1] - 23.5) - (ingamecard.position[1] - 23.5)) ** 2) ** 0.5
                    if distance < closest_distance:
                        closest_enemy = enemy
                        closest_distance = distance
                ingamecard.attack(closest_enemy)
            else:
                destination = find_destination(ingamecard)
                ingamecard.move(destination)

        for enm_card in Ingame_enm_cards:
            in_range_tower = in_range(enm_card, Tower_List , Tower_List)
            in_range_enmy = in_range(enm_card, InGameCards ,Tower_List)
            if in_range_tower:
                closest_distance = (640 ** 2 + 360 ** 2) ** 0.5
                for tower in in_range_tower:
                    distance = (((tower.position[0] - tower.size[0] / 2) - (enm_card.position[0] - 20)) ** 2 + (
                            (tower.position[1] - tower.size[1] / 2) - (enm_card.position[1] - 23.5)) ** 2) ** 0.5
                    if distance < closest_distance:
                        closest_tower = tower
                        closest_distance = distance
                enm_card.attack(closest_tower)
            elif in_range_enmy and enm_card.att_status != 'building':
                closest_distance = (640 ** 2 + 360 ** 2) ** 0.5
                closest_enemy = None
                for enemy in in_range_enmy:
                    if enemy.status in enm_card.att_status:
                        distance = (((enemy.position[0] - 20) - (enm_card.position[0] - 20)) ** 2 + (
                                (enemy.position[1] - 23.5) - (enm_card.position[1] - 23.5)) ** 2) ** 0.5
                        if distance < closest_distance:
                            closest_enemy = enemy
                            closest_distance = distance
                if not closest_enemy == None:
                    enm_card.attack(closest_enemy)
                else:
                    destination = find_destination(enm_card)
                    enm_card.move(destination)
            else:
                destination = find_destination(enm_card)
                enm_card.move(destination)

        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if  result == -1:
            screen.fill((255,0,0))
            lable = Clash_Font1.render("You lost",True,(0,0,0))
            screen.blit(lable,(100,300))
        if  result == 1:
            screen.fill((0,255,0))
            lable = Clash_Font1.render("You Win",True,(0,0,0))
            screen.blit(lable,(100,300))
        if  result == 0:
            screen.fill((255,255,255))
            lable = Clash_Font1.render("Draw",True,(0,0,0))
            screen.blit(lable,(130,300))
        pygame.display.update()



main()
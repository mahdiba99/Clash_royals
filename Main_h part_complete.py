import pygame,sys,time
from pygame import mouse as m
InGameCards=[]
Card_List = []
Tower_List = []
Other_Towers = []
select_card = True
card = None
budget = 5
prev_diff = 0

def intial():
    global Card_List,Tower_List
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
    for tower in Tower_List:
        if tower.id == 1:
            tower.max_health = 2000
            tower.health = tower.max_health
            tower.position = (149,406)
            tower.range = 65
            tower.damage = 80
            tower.size = (57,78)
        if tower.id == 2:
            tower.max_health = 1500
            tower.health = tower.max_health
            tower.position = (68,370)
            tower.range = 65
            tower.damage = 65
            tower.size = (40,51)
        if tower.id == 3:
            tower.max_health = 1500
            tower.health = tower.max_health
            tower.position = (258,370)
            tower.range = 65
            tower.damage = 65
            tower.size = (40,51)
    for tower in Other_Towers:
        if tower.id == 1:
            tower.max_health = 2000
            tower.health = tower.max_health
            tower.position = (149,56)
            tower.range = 65
            tower.damage = 80
            tower.size = (60,81)
        if tower.id == 2:
            tower.max_health = 1500
            tower.health = tower.max_health
            tower.position = (68,110)
            tower.range = 65
            tower.damage = 65
            tower.size = (40,54)
        if tower.id == 3:
            tower.max_health = 1500
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
    global budget,Tower_List,Other_Towers
    for tower in Tower_List:
        screen.blit(tower.img,tower.position)
        health = int(tower.health/tower.max_health)*4+1
        if tower.health == tower.max_health:
            health = 4
        for i in range(health):
            if tower.id!=1:
                pygame.draw.rect(screen,(30,144,255),(tower.position[0]+i*10+6,tower.position[1]+66,9,5))
            else:
                pygame.draw.rect(screen,(30,144,255),(tower.position[0]+i*14+4,tower.position[1]+76,12,5))

    for tower in Other_Towers:
        screen.blit(tower.img,tower.position)
        health = int(tower.health/tower.max_health)*4+1
        if tower.health == tower.max_health:
            health = 4
        for i in range(health):
            if tower.id!=1:
                pygame.draw.rect(screen,(255,69,0),(tower.position[0]+i*10+8,tower.position[1]-5,9,5))
            else:
                pygame.draw.rect(screen,(255,69,0),(tower.position[0]+i*14+10,tower.position[1]-3,12,5))


    for card in Card_List:
        screen.blit(card.picture, card.get_position())

    for card in InGameCards:
        screen.blit(card.picture, card.get_position())
        health = int(card.health/card.max_health)*4+1
        if card.health == card.max_health:
            health = 4
        for i in range(health):
            pygame.draw.rect(screen,(30,144,255),(card.get_position()[0]+i*10,card.get_position()[1]-7,9,5))
    for i in range(budget):
        pygame.draw.rect(screen,(255,0,255),(12+i*(30+4),617,30,20))



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
    global Card_List, select_card, card , budget , prev_diff , Tower_List , Other_Towers
    InGameCards = []
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
    game_begin = time.time()
    while True:
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
        if int(game_end - game_begin) == 180:
            break
        main_get_event()
        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load("background.jpg"), (0, 0))
        screen.blit(lable,(300,10))


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
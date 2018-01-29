import pygame,sys,time
pygame.init()
windowWidth = 360
windowHeight = 640
screen = pygame.display.set_mode((windowWidth,windowHeight))
card_list=[]
available_area=[]

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
    def get_position(self):
        return self.position
    def set_health(self,new_health):
        self.health = new_health
    def get_health(self):
        return self.health
    def attack(self, enemy):
        enemy.set_health(self.get_health() - self.power)
    def set_position(self,new_position):
        self.position = new_position
    def set_pic(self,new_pic_add):
        self.picture = pygame.image.load(new_pic_add)
    def get_pic(self):
        return self.picture

Giant=Card("GiantCard copy.png")
Witch=Card("WitchCard copy.png")
Fireball=Card("FireballCard copy.png")
Wizard=Card("WizardCard copy.png")
Bomber = Card("BomberCard copy.png")
Balloon = Card("BalloonCard copy.png")
Archer = Card("archers copy.png")
Lava = Card("LavaHoundCard copy.png")
card_list=[Wizard,Archer,Lava,Balloon,Bomber]
available_area={str(i):False for i in card_list}
onclick={str(i):False for i in card_list}

def intial():
    carts_distance = int((360-len(card_list)*60)/(len(card_list)+1))
    distance=carts_distance
    for card in card_list:
        card.set_position((distance,530))
        screen.blit(card.picture, (distance, 530))
        distance = distance + carts_distance + 60

intial()


def move(card, position):
    print('im in move')
    card.set_position((card.position[0] + card.speed / 500 * (position[0] - card.position[0]) / ((position[0] - card.position[0]) ** 2 + (position[1] - card.position[1]) ** 2) ** 0.5 ,card.position[1] + card.speed / 500 * (position[1] - card.position[1]) / ((position[0] - card.position[0]) ** 2 + (position[1] - card.position[1]) ** 2) ** 0.5))

reverse_V = 10
carts_distance = int((360 - len(card_list) * 60) / (len(card_list) + 1))
bg_image = pygame.image.load('1.jpg')
while True:
    first_X = carts_distance


    screen.blit(bg_image, (0, 0))
    for card in card_list:
        first_Y = 530
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and (card.position[1] < 260 or card.position[1]>480) :
                available_area[card] = False
        if pygame.mouse.get_pressed()[0] and card.position[0] < pygame.mouse.get_pos()[0] < card.position[0] + 50 and card.position[1] < pygame.mouse.get_pos()[1] < card.position[1] + 50 and card.position[1]>520 :
            onclick[card] = True
            diffs = [card.position[0] - pygame.mouse.get_pos()[0],
                     card.position[1] - pygame.mouse.get_pos()[1]]
        if not pygame.mouse.get_pressed()[0]:
            onclick[card] = False
        if onclick[card]:
            card.set_position((pygame.mouse.get_pos()[0] + diffs[0], pygame.mouse.get_pos()[1] + diffs[1]))
        if not onclick[card] and first_X - 5 <= card.position[0] <= first_X + 5 and first_Y - 5 <= card.position[1] <= first_Y + 5:
            available_area[card] = True
            print(1)
        elif not onclick[card] and not (card.position[0] == first_X and card.position[1] == first_Y) and not available_area[card]:
            card.set_position((card.position[0] + reverse_V * (first_X - card.position[0]) / ((first_X - card.position[0]) ** 2 + (first_Y - card.position[1]) ** 2) ** 0.5,card.position[1] + reverse_V * (first_Y - card.position[1]) / ((first_X - card.position[0]) ** 2 + (first_Y - card.position[1]) ** 2) ** 0.5))
        elif card.position[1] < 500 and not pygame.mouse.get_pressed()[0]:
            if card.position[0] < 180-30 and card.position[1] <= 300 :
                move(card,(60,175))
            elif card.position[0] > 180-30 and card.position[1] <= 300 :
                move(card,(240,175))
            elif  58+50>=card.position[0]>= 58 and 245 <= card.position[1] <= 300 :
                move(card,(58,245))
            elif card.position[0] < 180-30 and card.position[1] > 260 :
                move(card, (58, 291))
            elif card.position[0] > 240 and card.position[1] > 260:
                move(card, (243, 291))
            else:
                move(card,(243,245))

        first_X = first_X + carts_distance + 60
        screen.blit(card.picture, (card.position[0], card.position[1]))

    pygame.display.update()






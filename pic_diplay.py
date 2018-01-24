import sys,pygame

pygame.init()
windowWidth = 480
windowHeight = 640
first_X = 200
first_Y = 590
reverse_V = 10
card_position = [200,590]
screen = pygame.display.set_mode((windowWidth, windowHeight))


background_img = pygame.image.load('fuck.jpg')
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












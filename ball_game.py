import pygame
import random

pygame.init()

display_width,display_height=1000,600
paddle_x,paddle_y=5,5
x,y=random.randint(100,900),random.randint(100,500)
radius=10
dx,dy=3,3
paddle_width,paddle_height=5,50
speed,score=50,0

def start_Screen():
	display=pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption("Ball Game ...")
	display.fill((0,0,0))
	start=pygame.font.Font(None,36)
	instruct=pygame.font.Font(None,24)
	start=start.render("Welcome to the Game ...",True,(255,255,255))
	instruct=instruct.render("Press 'S' to Start the Game, otherwise it will automatically start in 10 seconds",True,(255,255,255))
	start_rect=start.get_rect(center=(int(display_width/2),int(display_height/2)))
	instruct_rect=instruct.get_rect(center=(int(display_width/2),2*int(display_height/3)))
	display.blit(start,start_rect)
	display.blit(instruct,instruct_rect)
	pygame.display.flip()

def hit_back(x):
	if x+radius>=display_width:
		return True
	return False

def hit_sides(x):
	if y+radius>=display_height or y-radius<0:
		return True
	return False

def hit_paddle(x,y):
	global speed,score
	if y>=paddle_y and y<=paddle_y+paddle_height and x<=paddle_x+paddle_width:
		speed+=1
		score+=25
		return True
	return False

def out(x):
	if x-radius<=0:
		return True
	return False

def end_Screen():
	global score
	global display_height,display_width
	display=pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption("Ball Game ...")
	display.fill((0,0,0))
	end=pygame.font.Font(None,36)
	end=end.render("Game Ended ...",True,(255,255,255))
	end_rect=end.get_rect(center=(int(display_width/2),int(display_height/3)))
	display.blit(end,end_rect)
	final="Final Score : "+str(score)
	end=pygame.font.Font(None,36)
	end=end.render(final,True,(255,255,255))
	end_rect=end.get_rect(center=(int(display_width/2),int(display_height/2)))
	display.blit(end,end_rect)
	instruct=pygame.font.Font(None,24)
	instruct=instruct.render("Press Q to Quit",True,(255,255,255))
	instruct_rect=instruct.get_rect(center=(int(display_width/2),int(0.65*display_height)))
	display.blit(instruct,instruct_rect)
	instruct=pygame.font.Font(None,24)
	instruct=instruct.render("Press R to Restart",True,(255,255,255))
	instruct_rect=instruct.get_rect(center=(int(display_width/2),int(0.75*display_height)))
	display.blit(instruct,instruct_rect)
	pygame.display.flip()	

def game():
	global x,y,paddle_y,paddle_x,paddle_width,paddle_height,radius,dx,dy,speed
	clock=pygame.time.Clock()
	display=pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption("Ball Game ...")
	display.fill((0,0,0))
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					end()
			elif event.type==pygame.QUIT:
				end()
		pressed=pygame.key.get_pressed()
		if pressed[pygame.K_UP] or pressed[pygame.K_w]:
			if paddle_y-5>=0:
				paddle_y-=5
		elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
			if paddle_y+paddle_height+5<display_height:
				paddle_y+=5
		display.fill((0,0,0))
		clock.tick(speed)
		if hit_back(x) or hit_paddle(x,y):
			dx*=-1
		if hit_sides(x):
			dy*=-1
		if out(x):
			end()
			exit()
		x+=dx
		y+=dy
		pygame.draw.circle(display,(255,255,255),(x,y),radius)
		pygame.draw.rect(display,(255,255,255),(paddle_x,paddle_y,paddle_width,paddle_height))
		pygame.display.update()

def end():
	end=True
	while end==True:
		end_Screen()
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_r:
					main()
					end=False
				elif event.key==pygame.K_q:
					pygame.quit()
					end=False
def main():
	global x,y,dx,dy,paddle_x,paddle_y,display_height,display_width,speed,score,radius,paddle_width,paddle_height
	display_width,display_height=1000,600
	paddle_x,paddle_y=5,5
	x,y=random.randint(100,900),random.randint(100,500)
	radius=10
	dx,dy=3,3
	paddle_width,paddle_height=5,50
	speed,score=50,0
	start=True
	speed,score=50,0
	wait=pygame.USEREVENT+1
	pygame.time.set_timer(wait,10000)	
	while start==True:
		start_Screen()
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_s:
					start=False
			elif event.type==wait:
				start=False
	game()	

if __name__=='__main__':
	main()

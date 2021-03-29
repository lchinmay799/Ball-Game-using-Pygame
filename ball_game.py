import pygame
import random

pygame.init()

def start_screen():
	display=pygame.display.set_mode((display_length,display_width))
	pygame.display.set_caption("Ball Game ...")
	display.fill((0,0,0))

	start_msg=pygame.font.Font(None,36)
	start_msg=start_msg.render("Press 'S' to Start the Game and 'Q' to Quit the Game",True,(255,255,255))
	start_rect=display.get_rect(center=(0.7*display_length,display_width))
	display.blit(start_msg,start_rect)

	instruct_msg=pygame.font.Font(None,24)
	instruct_msg=instruct_msg.render("Game will Automatically Start in 10 Seconds ...",True,(255,255,255))
	instruct_rect=display.get_rect(center=(0.85*display_length,1.15*display_width))
	display.blit(instruct_msg,instruct_rect)

	pygame.display.update()

def end_screen():
	global score

	display=pygame.display.set_mode((display_length,display_width))
	pygame.display.set_caption("Ball Game ...")
	display.fill((0,0,0))

	score_msg=pygame.font.Font(None,36)
	score_msg=score_msg.render("You Scored : "+str(score),True,(255,255,255))
	score_rect=display.get_rect(center=(0.85*display_length,display_width))
	display.blit(score_msg,score_rect)

	restart_msg=pygame.font.Font(None,36)
	restart_msg=restart_msg.render("Press 'R' to Restart the Game and 'Q' to Quit the Game",True,(255,255,255))
	restart_rect=display.get_rect(center=(0.7*display_length,1.15*display_width))
	display.blit(restart_msg,restart_rect)

	pygame.display.update()

def game():
	global speed,score,paddle_length,paddle_width,paddle_x,paddle_y
	global display_length,display_width,dx,dy,x,y

	while True:
		clock=pygame.time.Clock()

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					end()
					pygame.quit()
					break

			elif event.type==pygame.QUIT:
				end()
				pygame.quit()
				break

		pressed=pygame.key.get_pressed()
		
		if pressed[pygame.K_UP] or pressed[pygame.K_w]:
			if paddle_y-5>=5:
				paddle_y-=5

		elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
			if paddle_y+paddle_length+55<=display_width:
				paddle_y+=5

		if hit_back():
			dx*=-1

		if hit_side():
			dy*=-1

		if hit_paddle():
			dx*=-1
			speed+=25
			score+=25

		if out():
			end()
			break
		
		x+=dx
		y+=dy

		clock.tick(speed)

		display=pygame.display.set_mode((display_length,display_width))
		pygame.display.set_caption("Ball Game ...")
		display.fill((0,0,0))

		pygame.draw.rect(display,(255,255,255),pygame.Rect(paddle_x,paddle_y,paddle_length,paddle_width))
		pygame.draw.circle(display,(255,255,255),(x,y),radius)

		pygame.display.update()

def end():
	end=True

	while end==True:
		end_screen()
		
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					end=False
					exit()

				elif event.key==pygame.K_r:
					main()
					break

			elif event.type==pygame.QUIT:
				end=False
				exit()

def hit_back():
	return x+radius>=display_length

def hit_side():
	return y-radius<=0 or y+radius>=display_width

def hit_paddle():
	return x-radius<paddle_x+paddle_length and y>=paddle_y and y<=paddle_y+paddle_width

def out():
	return x<=0 and (y<paddle_y or y>paddle_y+paddle_length) 

def main():
	global display_length,display_width,paddle_length,paddle_width
	global paddle_x,paddle_y,x,y,radius,speed,score,dx,dy

	display_length,display_width=1000,600
	paddle_length,paddle_width=5,50
	paddle_x,paddle_y=5,5
	x,y=random.randint(100,900),random.randint(100,500)
	radius=10
	speed=250
	dx,dy=1,1
	score=0

	start=True
	wait=pygame.USEREVENT+1
	pygame.time.set_timer(wait,10000)

	while start==True:
		start_screen()

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_s:
					start=False
				elif event.key==pygame.K_q:
					pygame.quit()
					start=False
					exit()
			elif event.type==pygame.QUIT:
				start=False
				pygame.quit()
				exit()
			elif event.type==wait:
				start=False

	game()

if __name__=='__main__':
	main()
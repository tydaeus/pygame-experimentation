import sys, pygame, time
pygame.init()

size = width, height = 1024, 768
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
screen.fill(black)

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    # mod: increase speed with each collision
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        if speed[0] < 0:
            speed[0] -= 1 
        else:
            speed[0] += 1
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if speed[1] < 0:
            speed[1] -= 1
        else:
            speed[1] += 1
    
    # mod: skip screen clear between draws
    # screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    # Fix: delay between draws (otherwise too fast)
    # time.sleep(1/60)
    clock.tick(60)
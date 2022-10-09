import pygame
import random
import math
pygame.init()
WHITE = (255, 255, 255)
DARKBLUE = (0, 0, 0)
LIGHTBLUE = (0,22,126)
RED = (235, 54, 1)
score = 0
hexagonImg = pygame.image.load('hexagon1.png')
bg_img = pygame.image.load('bg_1.jpg')
bg_img = pygame.transform.scale(bg_img,(600,600))
bombImg = pygame.image.load('sign.png')

velocity = [1, 1]
paddle_size = 100

size = (600, 600)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Bricks Game")

ball_x = random.randint(10,590 )
ball_y = random.randint(230,300)
paddle = pygame.Rect(100, 550, paddle_size, 10)
ball = pygame.Rect(ball_x, ball_y,10, 10 )
brick_coordinate = []
for j in range(3):
    for i in range (7):
        if j == 1:
            brick_coordinate.append((100+ 65*i,50 + 60*j))
        else:
            brick_coordinate.append((65+ 65*i,50 + 60*j))
bomb_coordinates_x=[]
bomb_coordinates_y=[]
for i in brick_coordinate:
     bomb_coordinates_x.append(i[0])
     bomb_coordinates_y.append(i[1])
def brick():
    for i in brick_coordinate:
        screen.blit(hexagonImg,i)
def collision():
    global score
    for i in brick_coordinate:
        x = i[0]
        y = i[1]
        dist = math.sqrt(pow((x-ball.x),2)+pow((y-ball.y),2))
        # print (dist)
        # print (x)
        # print (y)
        if dist <= 50:
            brick_coordinate.remove(i)
            print (brick_coordinate)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score + 1 
def bomb_spawn():
    global random_bomb_y
    global random_bomb_x
    random_bomb_x= bomb_coordinates_x[random.randint(0,20)]
    random_bomb_y= bomb_coordinates_y[random.randint(0,20)]
   
def bomb_draw(b_x,b_y):
    screen.blit(bombImg,(b_x,b_y))

running = True
bomb_spawn()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(DARKBLUE)
    screen.blit(bg_img,(0,0))
    pygame.draw.rect(screen, LIGHTBLUE, paddle)

    font = pygame.font.Font(None, 34)

    text = font.render("SCORE " + str(score), 1, WHITE)

    screen.blit(text, (20, 10))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
            if paddle.x < 540:
                paddle.x = paddle.x + 5

    if keys[pygame.K_a]:
            if paddle.x > 0:
                paddle.x = paddle.x - 5

        
    brick()
    ball.x = ball.x + velocity[0]
    ball.y = ball.y + velocity[1]

    if ball.x > 590 or ball.x < 0:
        velocity[0] = -velocity[0]

    if ball.y <= 3:
        velocity[1] = -velocity[1]

    if paddle.collidepoint(ball.x, ball.y):
        velocity[1] = -velocity[1]
    bomb_draw(random_bomb_x,random_bomb_y)
    dist = math.sqrt(pow((random_bomb_x-ball.x),2)+pow((random_bomb_y-ball.y),2))
    if dist <= 50:
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score-1
            bomb_spawn()

    if ball.y >= 590  or score==-1:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over ", 1, RED)
        screen.blit(text, (150, 350))
        
        pygame.display.flip()

        pygame.time.wait(2000)

        break;
    collision()
    if score == 21:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON ", 1, RED)
        screen.blit(text, (150, 350))
        pygame.display.flip()

        pygame.time.wait(3000)
        break;
    pygame.draw.rect(screen, WHITE, ball)
    pygame.display.update()        
import pygame

pygame.init()

###########################################################
#화면크기 설정
screen_width = 720
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("game")

#Fps
clock = pygame.time.Clock()
###########################################################

#사용자 게임 초기화
player = pygame.image.load("images/player.png")
player = pygame.transform.scale(player, (128,128))
player_X = screen_width/2
player_Y = screen_height - 128
fire = False
ball_Y = 5
ballXY = []
global i
i = 0

j = 0
On = False

bg = pygame.image.load("images/bg.jpg")
bg = pygame.transform.scale(bg, (720,960))

def ball_fire():
    global i
    ball = pygame.image.load("images/ball.png")
    ball = pygame.transform.scale(ball, (128,64))
    ball = pygame.transform.rotate(ball, -90)
    ballXY.append([player_X + 32,player_Y - 128])
    On = True
    i += 1

'''enemy = pygame.image.load('images/enemy')
enemy = pygame.transform.scale(enemy, (64,64))'''

running = True
while running:
    dt = clock.tick(60)
    #이동구현
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        player_X -= 20
    elif key[pygame.K_RIGHT]:
        player_X += 20
    if key[pygame.K_SPACE]:
        fire = True

    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #배경그리기
    screen.blit(bg, (0,0))
    screen.blit(player, (player_X,player_Y))
    

    #충돌처리

    #세로
    if player_Y > screen_height - 128:
        player_Y = screen_height - 128
    elif player_Y < 0:
        player_Y = 0
    #가로
    if player_X > screen_width - 128:
        player_X = screen_width - 128
    elif player_X < 0:
        player_X = 0

    #미사일 발사
    if fire == True:
        ball_fire()

    if On == True:
        for j in range(i+1):
            ballXY[j][1] = -100
            screen.blit(ball, (ballXY[j][0], ballXY[j][1]))


    pygame.display.update()

pygame.quit()

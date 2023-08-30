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

global i, On, ballXY

ball_Y = 5
ballXY = []
i = 0
j = 0
On = False

bg = pygame.image.load("images/bg.jpg")
bg = pygame.transform.scale(bg, (720,960))

ball = pygame.image.load("images/ball.png")
ball = pygame.transform.scale(ball, (128,64))
ball = pygame.transform.rotate(ball, -90)

def ball_fire():
    global i, On, ballXY
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

    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                fire = False
    
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
        fire = False

    if On == True:
        for j in range(0, i):
            ballXY[j][1] -= 10
            screen.blit(ball, (ballXY[j][0], ballXY[j][1]))


    pygame.display.update()

pygame.quit()

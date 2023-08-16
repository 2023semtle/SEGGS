import pygame

pygame.init()

###########################################################
#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("game")

#Fps
clock = pygame.time.Clock()
###########################################################

#사용자 게임 초기화
player = pygame.image.load("images/player.png")
player = pygame.transform.scale(player, (64,64))
player_X = 0
player_Y = 0

bg = pygame.image.load("images/bg.jpg")
bg = pygame.transform.scale(bg, (480,640))

'''ball = pygame.image.load("images/ball.png")
ball = pygame.transform.scale(ball, (16,16))'''

running = True
while running:
    dt = clock.tick(30)
    #이동구현
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        player_X -= 10
    elif key[pygame.K_RIGHT]:
        player_X += 10
    if key[pygame.K_UP]:
        player_Y -= 10
    elif key[pygame.K_DOWN]:
        player_Y += 10
    if key[pygame.K_SPACE]:
        pass

    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #게임캐릭터 위치정의

    #충돌처리
    #세로
    if player_Y > 640 - 64:
        player_Y = 640 - 64
    elif player_Y < 0:
        player_Y = 0
    #가로
    if player_X > 480 - 64:
        player_X = 480 - 64
    elif player_X < 0:
        player_X = 0

    #배경그리기
    screen.blit(bg, (0,0))
    screen.blit(player, (player_X,player_Y))
    pygame.display.update()

pygame.quit()

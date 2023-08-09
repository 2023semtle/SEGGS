import pygame

pygame.init()

###########################################################
#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("")

#Fps
clock = pygame.time.Clock()
###########################################################

#사용자 게임 초기화

running = True
while running:
    dt = clock.tick(30)

    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #게임캐릭터 위치정의

    #충돌처리

    #배경그리기

    pygame.display.update()

pygame.quit()

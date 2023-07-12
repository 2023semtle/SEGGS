import pygame

pygame.init()

###########################################################
#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("AVOID")

#Fps
clock = pygame.time.Clock()
###########################################################

#사용자 게임 초기화
background = pygame.image.load("C:/Users/user/Desktop/pythonworksapce/lets_avoid/background.png")

character = pygame.image.load("C:/Users/user/Desktop/pythonworksapce/lets_avoid/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = (screen_width/2) - (character_width/2)
character_ypos = screen_height -  character_height

#이동위치
character_speed = 10
to_x = 0

#이동좌표


running = True
while running:
    dt = clock.tick(30)

    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x = -character_speed
            elif event.key == pygame.K_RIGHT:
                to_x = character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    #게임캐릭터 위치정의
    character_xpos += to_x

    
    #충돌처리

    #화면그리기
    screen.blit(background, (0,0))

    screen.blit(character, (character_xpos,character_ypos))

    pygame.display.update()

pygame.quit()

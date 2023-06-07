import pygame

pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("THE GAME")

#FPS
clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/user/Desktop/pythonworksapce/pygame/background.jpg")

green_ch = pygame.image.load("C:/Users/user/Desktop/pythonworksapce/pygame/green.png")
green_ch_size = green_ch.get_rect().size
green_ch_width = green_ch_size[0]
green_ch_height = green_ch_size[1]
green_ch_x_pos = (screen_width/2) - (green_ch_width/2)
green_ch_y_pos = screen_height - green_ch_height

#이동할 좌표
to_x = 0
to_y = 0

#이동속도
green_speed = 0.6

#적
enemy = pygame.image.load("C:/Users/user/Desktop/pythonworksapce/pygame/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)

running = True
while running:

    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= green_speed
            elif event.key == pygame.K_RIGHT:
                to_x += green_speed
            elif event.key == pygame.K_UP:
                to_y -= green_speed
            elif event.key == pygame.K_DOWN:
                to_y += green_speed
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    green_ch_x_pos += to_x * dt
    green_ch_y_pos += to_y * dt

    #가로 경계
    if green_ch_x_pos < 0:
        green_ch_x_pos = 0
    elif green_ch_x_pos > screen_width - green_ch_width:
         green_ch_x_pos = screen_width - green_ch_width

    #세로경계
    if green_ch_y_pos < 0:
        green_ch_y_pos = 0
    elif green_ch_y_pos > screen_height - green_ch_height:
        green_ch_y_pos = screen_height - green_ch_height

    #충돌처리
    
    
        

    screen.blit(background, (0,0))

    screen.blit(green_ch, (green_ch_x_pos, green_ch_y_pos))
    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()
        

pygame.quit()

import pygame
pygame.init()
screen_width = 500
screen_height = 600
#color
white =(255,255,255)
black=(0,0,0)
red=(0,255,0)
screen = pygame.display.set_mode((screen_width,screen_height))
screen_caption = pygame.display.set_caption("Snakes")
velocity_x_snake=30
velocity_y_snake=30

game_exit=False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x_snake+=5
            if event.key == pygame.K_LEFT:
                velocity_x_snake-=5
            if event.key == pygame.K_DOWN:
                velocity_y_snake+=5
            if event.key == pygame.K_UP:
                velocity_y_snake-=5

    bg_img=screen.fill(white)
    snake_rect=pygame.draw.rect(screen,black,[100,100,velocity_x_snake,velocity_y_snake])
    
    pygame.display.update()
    pygame.quit
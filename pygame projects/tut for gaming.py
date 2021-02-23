import pygame
pygame.init()
screen = pygame.display.set_mode((500,600))
caption = pygame.display.set_caption("My First Game tut")
white=(255,255,255)
black=(0, 0, 0)
blc_len=30
blc_wdt=30
game_over=True
blc_x=100
blc_y=100
bg=pygame.image.load("images/jungle.png").convert()
clock=pygame.time.Clock()
fps=30
while game_over:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                blc_x = blc_x -10
            if event.key==pygame.K_RIGHT:
                blc_x += 10
            if event.key==pygame.K_UP:
                blc_y = blc_x -10
            if event.key==pygame.K_DOWN:
                blc_y += 10

    screen.fill(white)
    screen.blit(bg, [0, 0])
    pygame.draw.rect(screen,black ,[blc_x,blc_y,blc_len,blc_wdt])
    clock.tick(fps)
    pygame.display.update()




quit()

import pygame
pygame.init()
import random


screen_width = 500

screen_height = 500
white = (255,255,255)
red=(255,0,0)
black=(0,0,0)
game_window=pygame.display.set_mode((screen_width,screen_height))
game_caption=pygame.display.set_caption("Snake Game By Rohit Narwal")
font = pygame.font.SysFont('arial', 30)



clock=pygame.time.Clock()

snk_list = []

def len_inc(game_window, color, snk_lst, snake_width, snake_length):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_width, snake_length])


def screen_text(text, color, x, y):
    text_screen = font.render(text, True, color)
    game_window.blit(text_screen, [x, y])

def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill(white)
        screen_text("Welcome To Snakes",black,100,150)
        screen_text("Press Space to Play", black, 102, 200)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()
        pygame.display.update()

def game_loop():
    snk_length = 1
    exit_game = False
    screen_width = 500

    screen_height = 500

    snake_length = 10
    snake_width = 10
    snake_x = 100
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(50, 250)
    food_y = random.randint(50, 250)
    score = 0
    fps = 30


    with open("Hiscore.txt", "r") as r:
        Hiscore = r.read()

    def gameover_condition():
        with open("Hiscore.txt", "w") as w:
             w.write(str(Hiscore))
        if snake_x > screen_width or snake_x < 0 or snake_y > screen_height or snake_y < 0:
            game_window.fill(white)
            screen_text("Game Over,Press Space to Continue", red, 0, 200)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    velocity_x=5
                    velocity_y=0
                if event.key==pygame.K_LEFT:
                    velocity_x = -5
                    velocity_y = 0
                if event.key==pygame.K_UP:
                    velocity_x = 0
                    velocity_y = -5
                if event.key==pygame.K_DOWN:
                    velocity_x = 0
                    velocity_y = 5
                if event.key==pygame.K_q:
                    score+=50

            if event.type==pygame.QUIT:
                exit_game=True
        if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
            score+=1
            food_x = random.randint(50, 250)
            food_y = random.randint(50, 250)
            snk_length +=1
            print(str(Hiscore))
            if score > int(Hiscore):
                 Hiscore=score

        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y

        game_window.fill(white )

        pygame.display.flip()
        screen_text("Score : "+ str(score)+"     HiScore : "+ str( Hiscore),red,5,5)
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)
        pygame.draw.rect(game_window, black, [food_x, food_y, snake_width, snake_length])
        len_inc(game_window, red, snk_list, snake_width, snake_length)




        if len(snk_list)>int(snk_length):
            del snk_list[0]

        if head in snk_list[:-1]:
            gameover_condition()
        event=pygame.QUIT
        gameover_condition()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

    quit()
welcome()



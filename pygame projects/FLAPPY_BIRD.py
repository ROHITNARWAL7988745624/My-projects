import pygame,sys,random
pygame.init()
# Global variable
FPS = 32
screen_length = 650
screen_width = 480
white=(255,255,255)
black=(0,0,0)
bird_x=100
bird_y=270
screen = pygame.display.set_mode((screen_width,screen_length))
screen_caption = pygame.display.set_caption("Flappy Bird By Rohit Narwal")
clock=pygame.time.Clock()
# bg Images
bg_surface = pygame.image.load("images/bg for flappy.png").convert()
base_surface = pygame.image.load("images/base.png").convert()
base_surface = pygame.transform.scale2x(base_surface)
# bird images
down_bird = pygame.image.load("images/down_bird.png").convert_alpha()
up_bird = pygame.image.load("images/up_bird.png").convert_alpha()
mid_bird = pygame.image.load("images/mid bird.png").convert_alpha()


#color
red=(0,0,255)

#pipe images
pipe_img =pygame.image.load("gallery/sprites/pipe.png").convert_alpha()




game_font = pygame.font.SysFont('04B_19.ttf', 40)

#functions
def screen_text(text, color, x, y):
    text_screen = game_font.render(text, True, color)
    screen.blit(text_screen, [x, y])

def main_screen():
    exit_game=False
    while not exit_game:
        screen.fill(white)
        screen_text("Welcome To Flappy Bird",black,70,150)
        screen_text("Press Space to Play", black, 102, 200)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_second_screen()
        pygame.display.update()

game_exit = False

def game_second_screen():
    bird_images=[mid_bird,down_bird,up_bird]
    bird_index=1
    bird_surface=bird_images[bird_index]
    bird_rect=bird_surface.get_rect(center =(100,240))
    BIRDFLAP=pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP,200)
    white=(255,255,255)
    black=(0,0,0)
    # game variables
    score=0
    hiscore=0

    
    gravity=1
    pipe_height=[400,300,350,420,280,320]
    bird_motion=0
    pipe_list=[]
    game_work=True
    SPAWNPIPE =pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE,1200)
    base_x=0
    def draw_floor():
        screen.blit(base_surface, [base_x, 550])
        screen.blit(base_surface, [base_x-483, 550])
    def create_pipe():
        pipe_height_possible=random.choice(pipe_height)

        down_pipe= pipe_img.get_rect(midtop=(500,pipe_height_possible))
        up_pipe= pipe_img.get_rect(midbottom=(500,pipe_height_possible-200))
        return up_pipe,down_pipe
    def pipe_move(pipes):
        for pipe in pipes:
            pipe.centerx -=9
        return pipes
    def draw_pipes(pipes):
        for pipe in pipes:
            if pipe.bottom>=300:
                screen.blit(pipe_img,pipe)
            else:
                flip_pipe=pygame.transform.flip(pipe_img,False,True)
                screen.blit(flip_pipe,pipe)

    def check_collision(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                screen_text("Game Over", black, 200, 200)
                return False

        if bird_rect.centery<0 or bird_rect.centery>550:
            screen_text("Game Over", black, 0, 0)
            return False
        return True


    def bird_rotation(bird):
        bird_new=pygame.transform.rotozoom(bird,-bird_motion,1)
        return bird_new
    def bird_animation():
        new_bird=bird_images[bird_index]
        new_bird_rect=new_bird.get_rect(center=(100,bird_rect.centery))
        return new_bird,new_bird_rect
    def score_for_screen():
        score_surface=game_font.render(str(int(score)),True,(0,0,255))
        score_rect= score_surface.get_rect(center=(200,50))
        screen.blit(score_surface,score_rect)
    
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and game_work:
                    bird_motion=0
                    bird_motion-=17
                if event.key == pygame.K_SPACE and game_work==False:
        
                    game_work=True
                    pipe_list.clear()
                    bird_rect.center =(100,240)
                    bird_motion=0
            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())
            if event.type == BIRDFLAP:
                if bird_index<2:
                    bird_index+=1
                else:
                    bird_index=0
            bird_surface,bird_rect=bird_animation()
        base_x -= 7

        #backgroung
        screen.blit(bg_surface, [0, -110])
        if game_work:
            #bird
            bird_motion += gravity
            bird_rotate = bird_rotation(bird_surface)
            bird_rect.centery += bird_motion
            screen.blit(bird_rotate, bird_rect)
            game_work=check_collision(pipe_list)
            #pipes
            pipe_list=pipe_move(pipe_list)
            draw_pipes(pipe_list)
            score += 0.014
            score_for_screen()

        #floor
        base_x +=1
        draw_floor()
        if base_x<0:
            base_x=480

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
main_screen()
game_second_screen()
    
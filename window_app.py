import pygame
import Button
import time

pygame.init()

#create game window
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("VTB-S Counter")

def draw_text (text, font, text_col, x, y) :
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
#Game variables
game_paused = False
menu_state = "main"
#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colors
TEXT_COL = (255,255,255)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load("images/button_video.png").convert_alpha()
audio_img = pygame.image.load("images/button_audio.png").convert_alpha()
keys_img = pygame.image.load("images/button_keys.png").convert_alpha()
back_img = pygame.image.load("images/button_back.png").convert_alpha()


#create button instances
resume_button = Button.Button((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), resume_img, 1)
quit_button = Button.Button(336, 375, quit_img, 1)
options_button = Button.Button(297, 250, options_img, 1)
keys_button = Button.Button(246, 325, keys_img, 1)
video_button = Button.Button(226, 75, video_img, 1)
back_button = Button.Button(332, 450, back_img, 1)
audio_button = Button.Button(225, 200, audio_img, 1)
# game loop
run = True
while run:

    screen.fill((52,78,91))

    #check if the game is paused
    if game_paused == True:
        #check menu state
        if menu_state == "main":

            if resume_button.draw(screen):
                game_paused = False
            if quit_button.draw(screen):
                run = False
            if options_button.draw(screen):
                menu_state = "options"
       # if menu_state == "options":

            # draw the different options buttons

    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #print("Pause")
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
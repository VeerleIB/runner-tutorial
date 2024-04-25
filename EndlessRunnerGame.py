#2024/30/03 started
#2024/24/04 finished

import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite): #PLAYER
    def __init__(self):
        super().__init__()
        
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
    
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,ground_X))
        self.gravity = 0
        
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and self.rect.bottom >= ground_X:
            self.gravity = -20
            self.jump_sound.play()
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= ground_X:
            self.rect.bottom = ground_X
            
    def animation_state(self):
        if self.rect.bottom <ground_X:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle (pygame.sprite.Sprite): #OBSTACLES
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            self.frames = [fly_frame_1,fly_frame_2]
            y_pos = 210
        else:
            self.frames = [snail_frame_1,snail_frame_2]
            y_pos = ground_X
            
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        else:
            self.image = self.frames[int(self.animation_index)]
                
    def update(self):
        self.destroy()
        self.animation_state()
        self.rect.x -= 5

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, score_colors)
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        death_sound.play(0)
        obstacle_group.empty()
        return False
    else:
        return True

#SETTINGS
pygame.init()
score_colors = (255,255,255)
screen_X = 800
screen_Y = 400
ground_X = 300

#SET BASICS
screen = pygame.display.set_mode((screen_X,screen_Y))
pygame.display.set_caption('Runner Tutorial')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.2)
bg_music.play(loops = -1)
death_sound = pygame.mixer.Sound('audio/death.mp3')

#PLAYER GROUP
player = pygame.sprite.GroupSingle()
player.add(Player())

#OBSTACLES
fly_frame_1 = pygame.image.load('graphics/Fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/Fly/fly2.png').convert_alpha()
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()

obstacle_group = pygame.sprite.Group()

#TEXTURE IMPORTS
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale_by(player_stand,2)
player_stand_rect = player_stand.get_rect(center = (screen_X/2,200))

#OBSTACLE TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

#EVENT LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == obstacle_timer and game_active == True:
            obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_active == False:
            game_active = True
            start_time = int(pygame.time.get_ticks()/1000)
        
    if game_active == True:
        #Sky+Groun
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,ground_X))

        #Score
        score = display_score()
         
        #Player
        player.draw(screen)
        player.update()
        
        #Obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        #Collisions
        game_active = collision_sprite()
        
    else: #GAMEOVER       
        screen.fill((7,0,30))
        
        #Title
        game_title_surf = test_font.render('Runner Sim',False,score_colors)
        game_title_rect = game_title_surf.get_rect(center = (screen_X/2,75))
        
        #Instructions
        instruction_surf = test_font.render('Press space to start',False, score_colors)
        instruction_rect = instruction_surf.get_rect(center = (screen_X/2,330))
        screen.blit(instruction_surf,instruction_rect)
        
        #Score
        score_message_surf = test_font.render(f'Score: {score}', False, score_colors)
        score_message_rect = score_message_surf.get_rect(center = (screen_X/2,50))
        
        if score == 0:
            screen.blit(game_title_surf,game_title_rect)
        else:
            screen.blit(score_message_surf,score_message_rect)
            
        screen.blit(player_stand, player_stand_rect)
        
        
    pygame.display.update()
    clock.tick(60)
#EndlessRunnerGame.py before general clean up and with old notes and methods.

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
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            
    def anim_state(self):
        if self.rect.bottom <300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]       
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.anim_state()

class Obstacle (pygame.sprite.Sprite): #OBSTACLES
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            fly_frame_1 = pygame.image.load ('graphics/Fly/fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load ('graphics/Fly/fly2.png').convert_alpha()
            self.frames = [fly_frame_1,fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1,snail_frame_2]
            y_pos = 300
            
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
        
    def anim_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        else:
            self.image = self.frames[int(self.animation_index)]
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
                
    def update(self):
        self.anim_state()
        self.destroy()
        self.rect.x -= 5

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5
            
#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surf,obstacle_rect)
#             else:
#                 screen.blit(fly_surf,obstacle_rect)
            
#             obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] #Only copy obstacle if item on 
            
#         return obstacle_list
#     else: 
#         return []

# def collisions (player,obstacles):
#     if obstacles:
#         for obstacle_rect in obstacles:
#             if player.colliderect(obstacle_rect):
#                 print(game_active)
#                 return False
#     return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True
    

# def player_animation():
#     global player_surf, player_index
    
#     if player_rect.bottom <300:
#         player_surf = player_jump
#     else:
#         player_index +=0.1
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surf = player_walk[int(player_index)]

#SET BASICS    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner Tutorial')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
game_active = False
start_time = 0
score = 0

#PLAYER GROUP
player = pygame.sprite.GroupSingle()
player.add(Player())

#OBSTACE GROUP
obstacle_group = pygame.sprite.Group()

#TEXTURE IMPORTS
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

# #Snail
# snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1,snail_frame_2]
# snail_index = 0
# snail_surf = snail_frames [snail_index]

# #Fly
# fly_frame_1 = pygame.image.load ('graphics/Fly/fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load ('graphics/Fly/fly2.png').convert_alpha()
# fly_frames = [fly_frame_1,fly_frame_2]
# fly_index = 0
# fly_surf = fly_frames [fly_index]

obstacle_rect_list = []

# #Player
# player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk_1,player_walk_2]
# player_index = 0
# player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

# player_surf = player_walk[player_index]

# player_rect = player_surf.get_rect(midbottom = (80,300))
# player_gravity = 0

#OBSTACLE TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

# #Snail anim timer
# snail_animation_timer = pygame.USEREVENT +2
# pygame.time.set_timer(snail_animation_timer,500)

# #Fly anim timer
# fly_animation_timer = pygame.USEREVENT +3
# pygame.time.set_timer(fly_animation_timer,200)
 
#Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == obstacle_timer:
            obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
            # if randint (0,2):
            #     obstacle_group.add(Obstacle('fly'))
            #     obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
            # else:
            #     obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),200)))
                
        # if event.type == snail_animation_timer:
        #     if snail_index == 0:
        #         snail_index = 1
        #     else:
        #         snail_index = 0
        #     snail_surf = snail_frames[snail_index]
            
        # if event.type == fly_animation_timer:
        #     if fly_index == 0:
        #         fly_index = 1
        #     else:
        #         fly_index = 0
        #     fly_surf = fly_frames[fly_index]
            
        # if game_active:
        #     if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
        #         if player_rect.collidepoint(event.pos):
        #             player_gravity = -20
                    
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
        #                 player_gravity = -20
        # else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            start_time = int(pygame.time.get_ticks()/1000)
                
    if game_active == True:
        #Sky+Ground show           
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        #Score show
        score = display_score()
        
        #Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
            
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # player_animation()
        # screen.blit(player_surf,player_rect)
        
        #Collisions
        game_active = collision_sprite()
        # game_active = collisions(player_rect,obstacle_rect_list)
        
        # #Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
    else: #Game over screen         
        screen.fill((94,129,162))
        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80,300)
        # player_gravity = 0
        #Title game
        game_title_surf = test_font.render('Runner Sim',False,(111,196,169))
        game_title_rect = game_title_surf.get_rect(center = (400,75))
        #Instructions
        instruc_surf = test_font.render('Press space to start',False, (111,196,169))
        instruc_rect = instruc_surf.get_rect(center = (400,330))
        screen.blit(instruc_surf,instruc_rect)
        #Score
        score_message_surf = test_font.render(f'Score: {score}', False, (111,196,169))
        score_message_rect = score_message_surf.get_rect(center = (400,50))
        
        if score == 0:
            screen.blit(game_title_surf,game_title_rect)
        else:
            screen.blit(score_message_surf,score_message_rect)
            
        screen.blit(player_stand, player_stand_rect)
        
        
    pygame.display.update()
    clock.tick(60)
import pygame,sys,time,random,platform
pygame.init()

win_width = 1270
win_height = 800
running = True
text_fount = pygame.font.SysFont("Arial", 40, bold=True)
ount = pygame.font.SysFont("Arial", 50, bold=False)
text = pygame.font.SysFont("Arial", 80, bold=True)
random_text = pygame.font.SysFont("georgia", 70, bold=False)
arrow_positions = []
ground = 650
monke_y = ground + 180
orangutan_y = ground + 180
pooper_y = ground + 180
bloboon_y = ground + 18888
lvl = 0
monkes_caught = 0
speed = 4
restarted = False
slave = False
boss_catch = False
boss_catch_started = False
boss_catching_cooldown = 0
collision_detected = False 
on_menu = False
on_controls = False
on_monkeys = False
on_map = False
on_beach = True
windows = pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
pygame.display.set_caption("Monkey Catchers")
#COLORS
white = (255, 255, 255)
gray = (128, 128, 128)
green = (5, 200, 0)
yellow = (250, 255, 0)
red = (255, 0, 0)
black = (0,0,0)
orange = (255,165,0)
blue = (200,0,255)
dark_blue = (0,0,50)
dark_green = (0,60,0)
peach_brown = (90,60,0)
x = 350

Jungle_Background = pygame.image.load("MonkeyCatchers/jungle.jpg").convert_alpha()
poo_effect = pygame.image.load("MonkeyCatchers/diarhe.png").convert_alpha()
poo_effect_rez = pygame.transform.scale(poo_effect,(1400,900))
banana_img = pygame.image.load("MonkeyCatchers/banana.png").convert_alpha()
monke_img = pygame.image.load("MonkeyCatchers/Monkey.png").convert_alpha()
oran_img = pygame.image.load("MonkeyCatchers/Orangutan.png").convert_alpha()
pooper_img = pygame.image.load("MonkeyCatchers/Poomonkey.png").convert_alpha()
bloboon_img = pygame.image.load("MonkeyCatchers/Bloboon.png").convert_alpha()
slime_img = pygame.image.load("MonkeyCatchers/Slime.png").convert_alpha()
arrow = pygame.transform.scale(pygame.image.load("MonkeyCatchers/arrow.png"),(30,30)).convert_alpha()
poop_img = pygame.image.load("MonkeyCatchers/Poop.png").convert_alpha()
Rock = pygame.image.load("MonkeyCatchers/Rock.png").convert_alpha()
slime = pygame.image.load("MonkeyCatchers/Slime.png").convert_alpha()
gorilla = pygame.image.load("MonkeyCatchers/Gorilla.png").convert_alpha()
gorilla_frames = [pygame.image.load("MonkeyCatchers/Gorilla.png").convert_alpha(),
                  pygame.image.load("MonkeyCatchers/Gorilla2.png").convert_alpha(),
                  pygame.image.load("MonkeyCatchers/Gorilla3.png").convert_alpha()]
menu = pygame.transform.scale(pygame.image.load("MonkeyCatchers/Monkey Catchers menu.png"),(1300,800))

beach_map = pygame.image.load("MonkeyCatchers/BeachMap.png").convert_alpha()
beach_x,beach2_x,beach_y = 0,1740,-140
log = pygame.transform.scale(pygame.image.load("MonkeyCatchers/Log.png"),(250,120))
log_width = log.get_width()
log_x_list,log_x_list2 = [250,1700,1500],[2400,1000,2900]
log_x,log_x2 = random.choice(log_x_list),random.choice(log_x_list2)
log_rect,log2_rect = pygame.Rect(log_x,650,log_width,log_width),pygame.Rect(log_x2,650,log_width,log_width)

rock_width = Rock.get_width()
rock_x_list = [250,1700,1500]
rock_x_list2 = [2400,1000,2900]
rock_x = random.choice(rock_x_list)
rock_x2 = random.choice(rock_x_list2)
rock_rect = pygame.Rect(rock_x,650,rock_width,rock_width)
rock2_rect = pygame.Rect(rock_x2,650,rock_width,rock_width)

Jungle_x, Jungle_y = 0, -180
Jungle2_x = 1740
background_width = Jungle_Background.get_width()

Leaste_x, Leaste_y = 0, 650
monkes = []
bananas = []
bullets = []
left_bullets = []
orangutans = []
poopers = []
bloboons = []
poops = []
slimes = []

poop_effect_time = 0  # Initialize with a default value

#BEACH
surf_monkey_img = pygame.image.load("MonkeyCatchers/Surf_Monkey.png").convert_alpha()
anxey_img = pygame.image.load("MonkeyCatchers/Anxey.png").convert_alpha()
surf_img = pygame.image.load("MonkeyCatchers/Surf.png").convert_alpha()
surf_monkeys = []
anxeys = []
surfs = []

def is_near(A_rect, B_rect, distance=45):
    return A_rect.colliderect(B_rect.inflate(distance, distance))
win_width = 1270
win_height = 800
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.frames = [pygame.image.load('MonkeyCatchers/MonJ.png').convert_alpha(),
                       pygame.image.load('MonkeyCatchers/MonJ2.png').convert_alpha(),
                       pygame.image.load('MonkeyCatchers/MonJ3.png').convert_alpha()]
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.y_velocity = 0
        self.jump_strength = -2
        self.gravity = 0.3
        self.is_jumping = False
        self.flying = False
        self.img = pygame.image.load("MonkeyCatchers/MonJ.png").convert_alpha()
        self.fuel = 0
        self.res_time = None 
        self.mov_sped = 0.1 
        self.waiting = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

    def draw(self):
        windows.blit(pygame.transform.scale(self.current_frame, (self.width, self.height)), (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if not boss_catch:
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and not boss_catch:
                self.x -= self.mov_sped
                self.moving = True
                self.flipped = True  # Set flipped to True when moving left
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x += self.mov_sped
                self.moving = True
                self.flipped = False  # Set flipped to False when moving right
            else:
                self.moving = False
                if self.flipped:
                    self.current_frame = self.flipped_frames[0]  # Use flipped image if last direction was left
                else:
                    self.current_frame = self.frames[0]

        if self.x < 0:
            self.x = 0

        elif self.x + self.width > win_width:
            self.x = win_width - self.width

        if keys[pygame.K_w] and not self.is_jumping:
            self.y_velocity = self.jump_strength
            self.is_jumping = True
            self.flying = True
        
        if keys[pygame.K_w] and self.flying and self.is_jumping:
            self.fuel += 1

        if self.fuel <= 300 and self.flying and not self.waiting:
            if self.flying and keys[pygame.K_w]:
                self.y_velocity += -0.4

            if keys[pygame.K_d] and self.flying and self.is_jumping:
                self.fuel += 1
                self.x -= -1.5

            if keys[pygame.K_a] and self.flying and self.is_jumping:
                self.fuel += 1
                self.x += -1.5

        elif self.fuel >= 300 and not self.waiting:
            self.waiting = True
            self.res_time = time.time()

        self.y_velocity += self.gravity
        self.y += self.y_velocity

        if self.y >= ground:
            if self.waiting and time.time() - self.res_time >= 3:
                self.fuel = 0  # Reset number back to 0
                self.waiting = False  # Stop waiting
            self.y = ground
            self.y_velocity = 0
            self.is_jumping = False 

    def update(self):
        global boss_catch  # Access the global boss_catch variable
        # Always play animation during boss_catch
        if boss_catch and not gorilla_boss.caught and not gorilla_boss.escaped:
            self.speed += 1
            if self.speed >= 7:  # Adjust animation speed as needed
                self.index = (self.index + 1) % len(self.frames)  # Cycle through frames
                if self.flipped:
                    self.current_frame = self.flipped_frames[self.index]  # Use flipped frame
                else:
                    self.current_frame = self.frames[self.index]  # Use normal frame
                self.speed = 0  # Reset speed counter
        else:
            # Default animation logic (based on movement)
            if self.moving:
                self.speed += 1
                if self.speed >= 7:
                    self.index = (self.index + 1) % len(self.frames)
                    self.current_frame = self.flipped_frames[self.index] if self.flipped else self.frames[self.index]
                    self.speed = 0
            else:
                # Reset to idle frame when not moving
                self.current_frame = self.flipped_frames[0] if self.flipped else self.frames[0]

    def set_flipped(self, flipped):
        self.flipped = flipped

class Banana(pygame.sprite.Sprite):
    def __init__(self,img_pth,x,y,width,height):
        super().__init__()
        self.img_pth = img_pth
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spawned = False

    def spawn(self,player):
         keys = pygame.key.get_pressed()
         if keys[pygame.K_SPACE] and not self.spawned and not Leaste.is_jumping:
            self.spawned = True
            if player.flipped:
                self.x = player.x - self.width 
            else:
                self.x = player.x + player.width
            self.y = ground + 35
         if self.spawned:
            windows.blit(pygame.transform.scale(self.img_pth, (self.width, self.height)), (self.x,self.y))

class Monkey(pygame.sprite.Sprite):
    def __init__(self,img_pth,x, y, width, height):
        super().__init__()
        self.frames = [pygame.image.load("MonkeyCatchers/Monkey.png").convert_alpha(),
                       pygame.image.load("MonkeyCatchers/Monkey2.png").convert_alpha(),
                       pygame.image.load("MonkeyCatchers/Monkey3.png").convert_alpha()]
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.img_pth = img_pth
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.spawned = False
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.jump_strength = -7  # Negative to move upwards
        self.gravity = 1  # Pulls down
        self.velocity_y = 0  # Current vertical velocity
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.caugth_monke = pygame.transform.rotate(pygame.transform.scale(self.frames[0],(self.width,self.height)),(90))
        self.caught = False
        self.flipped_caught = pygame.transform.flip(self.caugth_monke,True, False)

    def spawn(self, arrow_positions, bananas):
        global banana
        player_rect = Leaste.rect
        banana_rect = pygame.Rect(banana.x, banana.y, banana.width, banana.height)
        if self.spawned:
            if not self.caught:
               self.y -= 5.5
            self.rect.topleft = (self.x, self.y)
            if not self.caught:
               windows.blit(pygame.transform.scale(self.current_frame, (self.width, self.height)), (self.x, self.y))
            else:
                if not slave and restarted or not restarted:
                    if not self.flipped:
                        windows.blit(self.caugth_monke,(self.x, ground))
                    else:
                        windows.blit(self.flipped_caught,(self.x, ground))
        for banana in bananas:
            if banana.spawned and not is_near(player_rect, banana_rect, distance=400):
                for arrow_x in arrow_positions[:]:
                    # Check if the banana's x position is within a small range of the arrow's position
                    if abs(banana.x - arrow_x) < 60:
                        new_monke = Monkey("MonkeyCatchers/Monkey.png",arrow_x, self.y, self.width, self.height)
                        new_oran = Orangutan("MonkeyCatchers/Orangutan.png",arrow_x, self.y, orangutan.width, orangutan.height)
                        new_pooper = Pooper("MonkeyCatchers/Poomonkey.png",arrow_x,self.y,pooper.width,pooper.height)
                        new_bloboon = Bloboon("MonkeyCatchers/Bloboon.png",arrow_x,bloboon.y,bloboon.width,bloboon.height)
                        animal_type = random.choice(['monkey', 'orangutan', 'pooper', 'bloboon'])
                        if animal_type == 'monkey':
                            monkes.append(new_monke)
                            new_monke.spawned = True
                        elif animal_type == 'orangutan' and lvl >= 2:
                            orangutans.append(new_oran)
                            new_oran.spawned = True
                        elif animal_type == 'pooper' and lvl >= 3:
                            poopers.append(new_pooper)
                            poops.append(Poop(poop_img, new_pooper.x + 100, ground, 40, 40))
                            new_pooper.spawned = True
                        elif animal_type == 'bloboon' and lvl >= 4.5:
                            bloboons.append(new_bloboon)
                            slimes.append(Slime(slime_img,new_bloboon.x + 10, slime.y, slime.width, slime.height))
                            new_bloboon.spawned = True
                        else:
                            monkes.append(new_monke)
                            new_monke.spawned = True
                        arrow_positions.remove(arrow_x)
                        banana.spawned = False
                        bananas.remove(banana)
                        break
            for arrow_x in arrow_positions[:]:
                if abs(banana.x - arrow_x) < 60:
                    if not self.spawned and is_near(player_rect, banana_rect, distance=400):
                        dis_txt("Must be further away", text_fount, red, 0, 350)
    def update(self):
        if not self.caught:
            if self.moving:
                self.speed += 1
                if self.speed >= 7:
                    self.index += 1
                    if self.index >= len(self.frames):
                        self.index = 0
                    if self.flipped:
                        self.current_frame = self.flipped_frames[self.index]
                    else:
                        self.current_frame = self.frames[self.index]
                    self.img_path = self.frames[self.index]
                    self.speed = 0

    def jump(self):
        if not self.caught:
            if self.spawned:
                self.y -= 4
                self.moving = True
                # Check if the monkey is on the ground
                if self.y < ground - 40:
                    self.gravity = 1
                    self.y += self.velocity_y - 1
                    self.velocity_y += 1  # Apply gravity to pull down
                    self.x += 4
                else:
                    self.x += 4
                    self.y = ground - 40
                    self.is_jumping = False
                    self.velocity_y = 0  # Reset the velocity
                # Start jumping if the monkey is on the ground
                if not self.is_jumping and (is_near(self.rect, rock_rect) or is_near(self.rect, rock2_rect)):
                    self.moving = False
                    self.is_jumping = True
                    self.velocity_y = self.jump_strength  # Set the upward velocity

class Orangutan(pygame.sprite.Sprite):
    def __init__(self,img_pth,x, y, width, height):
        super().__init__()
        self.frames = [pygame.image.load("MonkeyCatchers/Orangutan.png").convert_alpha(),
                       pygame.image.load("MonkeyCatchers/Orangutan2.png").convert_alpha(),
                       pygame.image.load("MonkeyCatchers/Orangutan3.png").convert_alpha()]
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.img_pth = img_pth
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.spawned = False
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.jump_strength = -7  # Negative to move upwards
        self.gravity = 1  # Pulls down
        self.velocity_y = 0  # Current vertical velocity
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.width - 40,self.height - 50)
        self.caugth_monke = pygame.transform.rotate(pygame.transform.scale(self.frames[1],(self.width,self.height)),(180))
        self.caught = False
        self.flipped_caught = pygame.transform.flip(self.caugth_monke,True, False)

    def spawn(self, arrow_positions, bananas):
        global banana, lvl
        player_rect = Leaste.rect
        banana_rect = pygame.Rect(banana.x, banana.y, banana.width, banana.height)
        if lvl >= 2:
            if self.spawned:
                if not self.caught:
                    self.y -= 5.5
                    self.rect.topleft = (self.x, self.y)
                if not self.caught:
                    windows.blit(pygame.transform.scale(self.current_frame, (self.width, self.height)), (self.x, self.y))
                else:
                    if not self.flipped:
                        windows.blit(self.caugth_monke,(self.x, ground - 80))
                    else:
                        windows.blit(self.flipped_caught,(self.x, ground - 80))
                return
            for banana in bananas:
                if banana.spawned and not is_near(player_rect, banana_rect, distance=400):
                    for arrow_x in arrow_positions[:]:
                        # Check if the banana's x position is within a small range of the arrow's position
                        if abs(banana.x - arrow_x) < 60:
                            new_monke = Monkey("MonkeyCatchers/Monkey.png",arrow_x, self.y, monke.width, monke.height)
                            new_oran = Orangutan("MonkeyCatchers/Orangutan.png",arrow_x, self.y, self.width, self.height)
                            new_pooper = Pooper("MonkeyCatchers/Poomonkey.png",arrow_x,self.y,pooper.width,pooper.height)
                            new_bloboon = Bloboon("MonkeyCatchers/Bloboon.png",arrow_x,bloboon.y,bloboon.width,bloboon.height)
                            animal_type = random.choice(['monkey', 'orangutan', 'pooper', 'bloboon'])
                            if animal_type == 'monkey':
                                monkes.append(new_monke)
                                new_monke.spawned = True
                            elif animal_type == 'orangutan' and lvl >= 2:
                                orangutans.append(new_oran)
                                new_oran.spawned = True
                            elif animal_type == 'pooper' and lvl >= 3:
                                poopers.append(new_pooper)
                                poops.append(Poop(poop_img, new_pooper.x + 100, ground, 40, 40))
                                new_pooper.spawned = True
                            elif animal_type == 'bloboon' and lvl >= 4.5:
                                bloboons.append(new_bloboon)
                                slimes.append(Slime(slime_img,new_bloboon.x + 10, slime.y, slime.width, slime.height))
                                new_bloboon.spawned = True
                            else:
                                monkes.append(new_monke)
                                new_monke.spawned = True
                            arrow_positions.remove(arrow_x)
                            banana.spawned = False
                            bananas.remove(banana)
                            break
                for arrow_x in arrow_positions[:]:
                    if abs(banana.x - arrow_x) < 60:
                        if not self.spawned and is_near(player_rect, banana_rect, distance=400):
                            dis_txt("It can sense you", text_fount, red, 0, 350)

    def update(self):
        if not self.caught:
            if self.moving:
                self.speed += 1
                if self.speed >= 7:
                    self.index += 1
                    if self.index >= len(self.frames):
                        self.index = 0
                    if self.flipped:
                        self.current_frame = self.flipped_frames[self.index]
                    else:
                        self.current_frame = self.frames[self.index]
                    self.img_path = self.frames[self.index]
                    self.speed = 0

    def jump(self):
        if not self.caught:
            if self.spawned:
                self.y -= 4
                self.moving = True
                # Check if the monkey is on the ground
                if self.y < ground - 80:
                    self.gravity = 1
                    self.y += self.velocity_y - 2
                    self.velocity_y += 1  # Apply gravity to pull down
                    self.x += 4
                else:
                    self.x += 4
                    self.y = ground - 80
                    self.is_jumping = False
                    self.velocity_y = 0  # Reset the velocity
                # Start jumping if the monkey is on the ground
                if not self.is_jumping and (is_near(self.rect, rock_rect) or is_near(self.rect, rock2_rect)):
                    self.moving = False
                    self.is_jumping = True
                    self.velocity_y = self.jump_strength  # Set the upward velocity

class Pooper(pygame.sprite.Sprite):
    def __init__(self,img_pth,x, y, width, height):
        super().__init__()
        self.frames = [pygame.image.load("MonkeyCatchers/Poomonkey.png").convert_alpha(),
                       pygame.image.load("MonkeyCatchers/Poomonkey2.png").convert_alpha(),]
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.img_pth = img_pth
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.spawned = False
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.jump_strength = -7  # Negative to move upwards
        self.gravity = 1  # Pulls down
        self.velocity_y = 0  # Current vertical velocity
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.caugth_monke = pygame.transform.rotate(pygame.transform.scale(self.frames[0],(60,110)),(90))
        self.caught = False
        self.flipped_caught = pygame.transform.flip(self.caugth_monke,True, False)
        self.glid = False
        self.pooped = False
        self.mov_sped = 4
    def spawn(self, arrow_positions, bananas):
        global banana, lvl
        player_rect = Leaste.rect
        banana_rect = pygame.Rect(banana.x, banana.y, banana.width, banana.height)
        if lvl >= 3:
            if self.spawned:
                if not self.caught:
                    self.y -= 5.5
                    self.rect.topleft = (self.x, self.y)
                if not self.caught and self.glid:
                    windows.blit(pygame.transform.scale(self.current_frame, (130, 50)), (self.x, self.y))
                elif not self.caught and not self.glid:
                    windows.blit(pygame.transform.scale(self.current_frame, (60, 110)), (self.x, self.y))
                else:
                    if not self.flipped:
                        windows.blit(self.caugth_monke,(self.x, self.y))
                    else:
                        windows.blit(self.flipped_caught,(self.x, self.y))
                    self.y += 10
                    if self.y >= ground + 10:
                        self.y = ground + 10
                return
            for banana in bananas:
                if banana.spawned and not is_near(player_rect, banana_rect, distance=400):
                    for arrow_x in arrow_positions[:]:
                        # Check if the banana's x position is within a small range of the arrow's position
                        if abs(banana.x - arrow_x) < 60:
                            new_monke = Monkey("MonkeyCatchers/Monkey.png",arrow_x, self.y, monke.width, monke.height)
                            new_oran = Orangutan("MonkeyCatchers/Orangutan.png",arrow_x, self.y, self.width, self.height)
                            new_pooper = Pooper("MonkeyCatchers/Poomonkey.png",arrow_x,self.y,self.width,self.height)
                            new_bloboon = Bloboon("MonkeyCatchers/Bloboon.png",arrow_x,bloboon.y,bloboon.width,bloboon.height)
                            animal_type = random.choice(['monkey', 'orangutan','pooper','bloboon'])
                            if animal_type == 'monkey':
                                monkes.append(new_monke)
                                new_monke.spawned = True
                            elif animal_type == 'orangutan' and lvl >= 2:
                                orangutans.append(new_oran)
                                new_oran.spawned = True
                            elif animal_type == 'pooper' and lvl >= 3:
                                poopers.append(new_pooper)
                                poops.append(Poop(poop_img, new_pooper.x + 100, ground, 40, 40))
                                new_pooper.spawned = True
                            elif animal_type == 'bloboon' and lvl >= 4.5:
                                bloboons.append(new_bloboon)
                                slimes.append(Slime(slime_img,new_bloboon.x + 10, slime.y, slime.width, slime.height))
                                new_bloboon.spawned = True
                            else:
                                monkes.append(new_monke)
                                new_monke.spawned = True
                            arrow_positions.remove(arrow_x)
                            banana.spawned = False
                            bananas.remove(banana)
                            break
                for arrow_x in arrow_positions[:]:
                    if abs(banana.x - arrow_x) < 60:
                        if not self.spawned and is_near(player_rect, banana_rect, distance=400):
                            dis_txt("It can sense you", text_fount, red, 0, 350)
    def update(self):
        if not self.caught:
            if self.moving:
                if not self.flipped:
                    if self.glid:
                        self.current_frame = self.frames[1]
                    else:
                        self.current_frame = self.frames[0]
                else:
                    if self.glid:
                        self.current_frame = self.flipped_frames[1]
                    else:
                        self.current_frame = self.flipped_frames[0]
    def jump(self):
        global collision_detected
        if not self.caught:
            if self.spawned:
                self.y -= 1
                self.moving = True
                # Check if the monkey is on the ground
                if self.y < ground - 80:
                    self.gravity = 1
                    self.y += 1.5
                    self.x += 4
                else:
                    self.x += 4
                    self.y = ground - 80
                    self.is_jumping = False
                if self.y <= 350:
                    self.y = 350
                    self.glid = True
                # Start jumping if the monkey is on the ground
                if not self.is_jumping and (is_near(self.rect, rock_rect) or is_near(self.rect, rock2_rect)):
                    self.moving = False
                    self.is_jumping = True
                    self.velocity_y = self.jump_strength
        else:
            keys = pygame.key.get_pressed()
            Leaste.rect = pygame.Rect(Leaste.x,Leaste.y,Leaste.width,Leaste.height)
            slime.rect = pygame.Rect(slime.x + 100,slime.y,slime.width - 150,slime.height)
            if not collision_detected and Jungle_x < 0 and Jungle2_x > -background_width + win_width:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.x += self.mov_sped
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.x -= self.mov_sped

class Poop(pygame.sprite.Sprite):
    def __init__(self,img,x,y,width,height):
        super().__init__()
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.flipped = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.collided = False
    def blit(self):
        global poops
        windows.blit(pygame.transform.scale(self.img,(self.width,self.height)),(self.x,self.y))
        if not pooper.flipped:
            self.x -= 10
        else:
            self.x += 10

class Bloboon(pygame.sprite.Sprite):
    def __init__(self,img_pth,x, y, width, height):
        super().__init__()
        self.frames = [pygame.image.load("MonkeyCatchers/Bloboon.png").convert_alpha(),
                       pygame.image.load("MonkeyCatchers/Bloboon2.png").convert_alpha(),
                       pygame.image.load("MonkeyCatchers/Bloboon3.png").convert_alpha()]
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.img_pth = img_pth
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.spawned = False
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.hits = 0
        self.jump_strength = -7  # Negative to move upwards
        self.gravity = 1  # Pulls down
        self.velocity_y = 0  # Current vertical velocity
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.caugth_monke = pygame.transform.rotate(pygame.transform.scale(self.frames[0],(self.width,self.height)),(90))
        self.caught = False
        self.flipped_caught = pygame.transform.flip(self.caugth_monke,True, False)

    def spawn(self, arrow_positions, bananas):
        global banana
        player_rect = Leaste.rect
        banana_rect = pygame.Rect(banana.x, banana.y, banana.width, banana.height)
        if self.spawned:
            if not self.caught:
               self.y -= 5.5
            self.rect.topleft = (self.x, self.y)
            if not self.caught:
               windows.blit(pygame.transform.scale(self.current_frame, (self.width, self.height)), (self.x, self.y))
            else: 
                if not slave and restarted or not restarted:
                    if not self.flipped:
                        windows.blit(self.caugth_monke,(self.x, ground))
                    else:
                        windows.blit(self.flipped_caught,(self.x, ground))

        for banana in bananas:
            if banana.spawned and not is_near(player_rect, banana_rect, distance=400):
                for arrow_x in arrow_positions[:]:
                    # Check if the banana's x position is within a small range of the arrow's position
                    if abs(banana.x - arrow_x) < 60:
                        new_monke = Monkey("MonkeyCatchers/Monkey.png",arrow_x, monke.y, monke.width, monke.height)
                        new_oran = Orangutan("MonkeyCatchers/Orangutan.png",arrow_x, orangutan.y, orangutan.width, orangutan.height)
                        new_pooper = Pooper("MonkeyCatchers/Poomonkey.png",arrow_x,pooper.y,pooper.width,pooper.height)
                        new_bloboon = Bloboon("MonkeyCatchers/Bloboon.png",arrow_x,self.y,self.width,self.height)
                        animal_type = random.choice(['monkey', 'orangutan', 'pooper','bloboon'])
                        if animal_type == 'monkey':
                            monkes.append(new_monke)
                            new_monke.spawned = True
                        elif animal_type == 'orangutan' and lvl >= 2:
                            orangutans.append(new_oran)
                            new_oran.spawned = True
                        elif animal_type == 'pooper' and lvl >= 3:
                            poopers.append(new_pooper)
                            poops.append(Poop(poop_img, new_pooper.x + 100, ground, 40, 40))
                            new_pooper.spawned = True
                        elif animal_type == 'bloboon' and lvl >= 4.5:
                            bloboons.append(new_bloboon)
                            slimes.append(Slime(slime_img,new_bloboon.x + 10, slime.y, slime.width, slime.height))
                            new_bloboon.spawned = True
                        else:
                            monkes.append(new_monke)
                            new_monke.spawned = True
                        arrow_positions.remove(arrow_x)
                        banana.spawned = False
                        bananas.remove(banana)
                        break
            for arrow_x in arrow_positions[:]:
                if abs(banana.x - arrow_x) < 60:
                    if not self.spawned and is_near(player_rect, banana_rect, distance=400):
                        dis_txt("Must be further away", text_fount, red, 0, 350)
    def update(self):
        if not self.caught:
            if self.moving:
                self.speed += 1
                if self.speed >= 7:
                    self.index += 1
                    if self.index >= len(self.frames):
                        self.index = 0
                    if self.flipped:
                        self.current_frame = self.flipped_frames[self.index]
                    else:
                        self.current_frame = self.frames[self.index]

                    self.img_path = self.frames[self.index]
                    self.speed = 0

    def jump(self):
        if not self.caught:
            if self.spawned:
                self.y -= 4
                self.moving = True
                # Check if the monkey is on the ground
                if self.y < ground - 70:
                    self.gravity = 1
                    self.y += self.velocity_y - 1
                    self.velocity_y += 1  # Apply gravity to pull down
                    self.x += 4

                else:
                    self.x += 4
                    self.y = ground - 70
                    self.is_jumping = False
                    self.velocity_y = 0  # Reset the velocity

                # Start jumping if the monkey is on the ground
                if not self.is_jumping and (is_near(self.rect, rock_rect) or is_near(self.rect, rock2_rect)):
                    self.moving = False
                    self.is_jumping = True
                    self.velocity_y = self.jump_strength

class Slime(pygame.sprite.Sprite):
    def __init__(self,img,x,y,width,height):
        super().__init__()
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spawned = False
        self.flipped = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.collided = False
        self.colliding_slimes = 0
    def blit(self):
        windows.blit(pygame.transform.scale(self.img,(self.width,self.height)),(self.x,self.y))

class Boss(pygame.sprite.Sprite):
    def __init__(self,frames,img_pth,x, y, width, height):
        super().__init__()
        self.frames = frames
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.img_pth = img_pth
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.spawned = True
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.hits = 0
        self.mov_sped = 0.3
        self.jump_strength = -7  # Negative to move upwards
        self.gravity = 1  # Pulls down
        self.velocity_y = 0  # Current vertical velocity
        self.health, self.max_health = 18,18
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.caugth_monke = pygame.transform.rotate(pygame.transform.scale(self.frames[0],(self.width,self.height)),(180))
        self.caught = False
        self.escaped = False
        self.flipped_caught = pygame.transform.flip(self.caugth_monke,True, False)
    def update(self):
        if not self.caught:
            if self.moving:
                self.speed += 1
                if self.speed >= 7:  # Adjust animation speed as needed
                    self.index = (self.index + 1) % len(self.frames)  # Cycle through frames
                    if self.flipped:
                        self.current_frame = self.flipped_frames[self.index]  # Use flipped frame
                    else:
                        self.current_frame = self.frames[self.index]  # Use normal frame
                    self.speed = 0  # Reset speed counter
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        if not self.caught:
            if self.spawned:
                self.y -= 1
                self.moving = True
                # Check if the monkey is on the ground
                if self.y < ground - 60:
                    self.x += self.mov_sped
                    self.gravity = 100
                    self.y += self.velocity_y - 10
                    self.velocity_y += 1  # Apply gravity to pull down
                else:
                    self.x += 4
                    self.y = ground - 70
                    self.is_jumping = False
                    self.velocity_y = 0  # Reset the velocity
                # Start jumping if the monkey is on the ground
                if boss_catch:
                    if not self.is_jumping and (is_near(self.rect, rock_rect) or is_near(self.rect, rock2_rect)):
                        self.moving = False
                        self.is_jumping = True
                        self.velocity_y = self.jump_strength
    def blit(self):
        if not self.caught:
            windows.blit(pygame.transform.scale(self.current_frame,(self.width,self.height)),(self.x,self.y))
        else:
            windows.blit(self.caugth_monke,(self.x,ground - 35))

class Button(pygame.sprite.Sprite):
    def __init__(self,text,text_col,text_font,rect_col,w,h,x,y,x_text,y_text):
        super().__init__()
        self.text = text
        self.text_col = text_col
        self.text_font = text_font
        self.rect_col = rect_col
        self.w,self.h = w,h
        self.x,self.y = x,y
        self.x_text,self.y_text = x_text, y_text
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def blit(self):
        pygame.draw.rect(windows,self.rect_col,self.rect)
        dis_txt(self.text,self.text_font,self.text_col,self.x_text,self.y_text)

#BEACH CLASS
class SurfMonkey(pygame.sprite.Sprite):
    def __init__(self,img_pth,x, y, width, height):
        super().__init__()
        self.frames = [pygame.image.load("MonkeyCatchers/Surf_Monkey.png").convert_alpha(),
                      pygame.image.load("MonkeyCatchers/Surf_Monkey2.png").convert_alpha(),
                      pygame.image.load("MonkeyCatchers/Surf_Monkey3.png").convert_alpha()]
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.img_pth = img_pth
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.spawned = False
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.jump_strength = -7  # Negative to move upwards
        self.gravity = 1  # Pulls down
        self.velocity_y = 0  # Current vertical velocity
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.caugth_monke = pygame.transform.rotate(pygame.transform.scale(self.frames[0],(self.width,self.height)),(90))
        self.caught = False
        self.flipped_caught = pygame.transform.flip(self.caugth_monke,True, False)

    def spawn(self, arrow_positions, bananas):
        global banana
        player_rect = Leaste.rect
        banana_rect = pygame.Rect(banana.x, banana.y, banana.width, banana.height)
        if self.spawned:
            if not self.caught:
               self.y -= 5.5
            self.rect.topleft = (self.x, self.y)
            if not self.caught:
               windows.blit(pygame.transform.scale(self.current_frame, (self.width, self.height)), (self.x, self.y))
            else:
                if not slave and restarted or not restarted:
                    if not self.flipped:
                        windows.blit(self.caugth_monke,(self.x, ground))
                    else:
                        windows.blit(self.flipped_caught,(self.x, ground))
        for banana in bananas:
            if banana.spawned and not is_near(player_rect, banana_rect, distance=400):
                for arrow_x in arrow_positions[:]:
                    # Check if the banana's x position is within a small range of the arrow's position
                    if abs(banana.x - arrow_x) < 60:
                        new_surf = Surf(surf_img,surfmonke.x,surfmonke.y,80,170)
                        new_surfmonke = SurfMonkey("MonkeyCatchers/Surf_Monkey.png",arrow_x, self.y, self.width, self.height)
                        new_anxey = Anxey("MonkeyCatchers/Anxey.png",arrow_x,self.y,self.width,self.height)
                        animal_type = random.choice(['surfmonke', 'anxey'])
                        if animal_type == 'surfmonke':
                            surf_monkeys.append(new_surfmonke)
                            surfs.append(new_surf)
                            new_surfmonke.spawned = True
                        elif animal_type == 'anxey':
                            anxeys.append(new_anxey)
                            new_anxey.spawned = True
                        arrow_positions.remove(arrow_x)
                        banana.spawned = False
                        bananas.remove(banana)
                        break
            for arrow_x in arrow_positions[:]:
                if abs(banana.x - arrow_x) < 60:
                    if not self.spawned and is_near(player_rect, banana_rect, distance=400):
                        dis_txt("Must be further away", text_fount, red, 0, 350)
    def update(self):
        if not self.caught:
            if self.moving:
                self.speed += 1
                if self.speed >= 7:
                    self.index += 1
                    if self.index >= len(self.frames):
                        self.index = 0
                    if self.flipped:
                        self.current_frame = self.flipped_frames[self.index]
                    else:
                        self.current_frame = self.frames[self.index]
                    self.img_path = self.frames[self.index]
                    self.speed = 0

    def jump(self):
        if not self.caught:
            if self.spawned:
                self.y -= 4
                self.moving = True
                # Check if the monkey is on the ground
                if self.y < ground - 70:
                    self.gravity = 1
                    self.y += self.velocity_y - 1
                    self.velocity_y += 1  # Apply gravity to pull down
                    self.x += 4
                else:
                    self.x += 4
                    self.y = ground - 70
                    self.is_jumping = False
                    self.velocity_y = 0  # Reset the velocity
                # Start jumping if the monkey is on the ground
                if not self.is_jumping and (is_near(self.rect, log_rect) or is_near(self.rect, log2_rect)):
                    self.moving = False
                    self.is_jumping = True
                    self.velocity_y = self.jump_strength  # Set the upward velocity

class Anxey(pygame.sprite.Sprite):
    def __init__(self,img_pth,x, y, width, height):
        super().__init__()
        self.frames = [pygame.image.load("MonkeyCatchers/Anxey.png").convert_alpha(),
                      pygame.image.load("MonkeyCatchers/Anxey2.png").convert_alpha()]
        self.flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.img_pth = img_pth
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.spawned = False
        self.index = 0
        self.current_frame = self.frames[self.index]
        self.flipped = False
        self.moving = False
        self.speed = 0
        self.jump_strength = -7  # Negative to move upwards
        self.gravity = 1  # Pulls down
        self.velocity_y = 0  # Current vertical velocity
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.caugth_monke = pygame.transform.rotate(pygame.transform.scale(self.frames[0],(self.width,self.height)),(90))
        self.caught = False
        self.flipped_caught = pygame.transform.flip(self.caugth_monke,True, False)
        self.walked = False
        self.sped = 4
        self.hits = 0

    def spawn(self, arrow_positions, bananas):
        global banana
        player_rect = Leaste.rect
        banana_rect = pygame.Rect(banana.x, banana.y, banana.width, banana.height)
        if self.spawned:
            if not self.caught:
               self.y -= 5.5
            self.rect.topleft = (self.x, self.y)
            if not self.caught and self.walked:
                windows.blit(pygame.transform.scale(self.current_frame, (105, 130)), (self.x, self.y))
            elif not self.caught and not self.walked:
                windows.blit(pygame.transform.scale(self.current_frame, (90,135)), (self.x, self.y))
            else:
                if not slave and restarted or not restarted:
                    if not self.flipped:
                        windows.blit(self.caugth_monke,(self.x, ground))
                    else:
                        windows.blit(self.flipped_caught,(self.x, ground))
        for banana in bananas:
            if banana.spawned and not is_near(player_rect, banana_rect, distance=400):
                for arrow_x in arrow_positions[:]:
                    # Check if the banana's x position is within a small range of the arrow's position
                    if abs(banana.x - arrow_x) < 60:
                        new_surf = Surf(surf_img,surfmonke.x,surfmonke.y,80,170)
                        new_surfmonke = SurfMonkey("MonkeyCatchers/Surf_Monkey.png",arrow_x, self.y, self.width, self.height)
                        new_anxey = Anxey("MonkeyCatchers/Anxey.png",arrow_x,self.y,self.width,self.height)
                        animal_type = random.choice(['surfmonke', 'anxey'])
                        if animal_type == 'surfmonke':
                            surf_monkeys.append(new_surfmonke)
                            surfs.append(new_surf)
                            new_surfmonke.spawned = True
                        elif animal_type == 'anxey':
                            anxeys.append(new_anxey)
                            new_anxey.spawned = True
                        arrow_positions.remove(arrow_x)
                        banana.spawned = False
                        bananas.remove(banana)
                        break
            for arrow_x in arrow_positions[:]:
                if abs(banana.x - arrow_x) < 60:
                    if not self.spawned and is_near(player_rect, banana_rect, distance=400):
                        dis_txt("Must be further away", text_fount, red, 0, 350)
    def update(self):
        if self.current_frame == self.frames[0]:
            self.walked = True
        else:
            self.walked = False
        if not self.caught:
            if self.moving:
                self.speed += 1
                if self.speed >= 7:
                    self.index += 1
                    if self.index >= len(self.frames):
                        self.index = 0
                    if self.flipped:
                        self.current_frame = self.flipped_frames[self.index]
                    else:
                        self.current_frame = self.frames[self.index]
                    self.img_path = self.frames[self.index]
                    self.speed = 0

    def jump(self):
        if not self.caught:
            if self.spawned:
                self.y -= 4
                self.moving = True
                # Check if the monkey is on the ground
                if self.y < ground - 70:
                    self.gravity = 1
                    self.y += self.velocity_y - 1
                    self.velocity_y += 1  # Apply gravity to pull down
                    self.x += self.sped
                else:
                    self.x += 4
                    self.y = ground - 70
                    self.is_jumping = False
                    self.velocity_y = 0  # Reset the velocity
                # Start jumping if the monkey is on the ground
                if not self.is_jumping and (is_near(self.rect, log_rect) or is_near(self.rect, log2_rect)):
                    self.moving = False
                    self.is_jumping = True
                    self.velocity_y = self.jump_strength  # Set the upward velocity

class Surf(pygame.sprite.Sprite):
    def __init__(self,img,x,y,width,height):
        super().__init__()
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spawned = False
        self.flipped = False
        self.hits = 0
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.flipped_img = pygame.transform.flip(self.img, True, False)
    def align_with_monkey(self, monkey):
        if not self.flipped:
            self.x = monkey.x - 20
        else:
            self.x = monkey.x + 40
        self.y = monkey.y - 30
    def blit(self):
        self.rect.topleft = (self.x, self.y)
        if not self.flipped:
            windows.blit(pygame.transform.scale(self.img,(self.width,self.height)),(self.x,self.y))
        else:
            windows.blit(pygame.transform.scale(self.flipped_img,(self.width,self.height)),(self.x,self.y))

playS,jungleS,ControlS,MonkeyS= None,None,None,None

# ADJUSTING SIZE
if "Laptop" in platform.node() or platform.system() == "Windows" or platform.system() == "Darwin":  # Adjust condition for laptops
    playS,jungleS,ControlS,MonkeyS= 330,340,480,230
else:  # monitor/desktop
    playS,jungleS,ControlS,MonkeyS = 300,300,400,200

Leaste = Player(Leaste_x, Leaste_y, 70, 70)
clock = pygame.time.Clock()
banana = Banana(banana_img,Leaste.x,ground + 27,30,30)
monke = Monkey(monke_img, banana.x + 180, monke_y, 90, 120)
orangutan = Orangutan(oran_img, banana.x + 180, orangutan_y, 190, 190)
pooper = Pooper(pooper_img, banana.x + 180, pooper_y, 100,100)
bloboon = Bloboon(bloboon_img,banana.x + 180,bloboon_y,110,130)
poop = Poop(poop_img,pooper.x + 100, ground,40,40) 
slime = Slime(slime_img,bloboon.x,ground + 65,230,20)
gorilla_boss = Boss(gorilla_frames,gorilla,550,ground - 55,120,120)
play = Button("PLAY",white,text,orange,playS,100,500,400,560,400)
jungle_btn = Button("JUNGLE",white,text,green,jungleS,260,285,230,300,300)
tutorial_btn = Button("CONTROLS",white,text,orange,ControlS,100,460,540,480,540)
back_btn = Button("BACK",white,text,orange,300,100,30,680,90,680)
back2_btn = Button("BACK",white,text,orange,300,100,930,680,990,680)
monkeys_btn = Button("MONKEYS",white,text_fount,dark_blue,MonkeyS,50,555,660,575,660)
menu_btn = Button("MENU",white,ount,orange,150,60,560,400,575,400)
menu_pressed = False
beach_btn = Button("BEACH",white,text,green,jungleS,260,685,230,720,300)

#BEACH
surfmonke = SurfMonkey("MonkeyCatchers/Surf_Monkey.png",banana.x + 180, ground + 180, 100, 130)
anxey = Anxey("MonkeyCatchers/Anxey.png",banana.x + 180, ground + 180, 100, 130)
surf = Surf(surf_img,500,500,80,170)

def dis_txt(text, font,text_col, x, y):
    img = font.render(text, True, text_col)
    windows.blit(img, (x, y))

def is_arrow_near_rocks(arrow_x, rocks, min_distance):
    return any(abs(arrow_x - rock_x) < min_distance for rock_x in rocks)

def show_loading_screen():
    start_time = pygame.time.get_ticks()  # Record the start time
    loading_duration = 3000  # 3000 milliseconds (3 seconds)
    loading_text = text.render("Loading...", True, white)
    loading_rect = loading_text.get_rect(center=(win_width // 2, win_height // 2))

    while pygame.time.get_ticks() - start_time < loading_duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display the loading screen
        windows.fill(black)
        windows.blit(loading_text, loading_rect)
        pygame.display.update()  # Ensure the display is updated
        pygame.time.delay(10)  # Small delay to prevent 100% CPU usage

def draw_health_bar(surface, x, y, health, max_health):
    # Define the width and height of the health bar
    bar_length = 150
    bar_height = 20
    # Calculate health bar fill ratio
    fill = (health / max_health) * bar_length
    # Outline of the bar
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    pygame.draw.rect(surface, red, outline_rect, 10)
    # Fill rectangle representing current health
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surface, green, fill_rect)

min_distance = 2000  # You can adjust this distance as needed
rocks = rock_x_list + rock_x_list2  # Combine both rock lists

arrow_x = random.uniform(400, 1500)
arrow_rect = pygame.Rect(arrow_x,ground,60,60)

if arrow_x == rock_x or arrow_x == rock_x2:
    for arrow_x in arrow_positions[:]:
        arrow_positions.remove(arrow_x)

def main_game():
    global Jungle_x, Jungle_y, Jungle2_x, Leaste_x, rock_x, rock_x2, rock_rect, banana, arrow_X, arrow_positions, monkes, bananas, bullets, orangutans, lvl, monkes_caught, num_arrows, collision_detected, poop_x, poop_y
    global restarted, slave, poop, pooper, poops, speed, boss_catch, boss_catching_cooldown, boss_catch_started
    global menu_pressed,poop_effect_time,on_beach
    banums = 7
    banana_spawned = False
    min_distance_between_arrows = 150  # Set the minimum distance between arrows
    arrow_speed = 4
    poop_x, poop_y = pooper.x + 100, ground
    y,al_y, an_y = 300, 370, 440
    boss_display_start = None 
    keys = pygame.key.get_pressed()
    x,xx,xxx = 100,-100,-100
    lvl = 4.5
    lvl_inc = False
    texted = False
    boss_catching_cooldown = 8.5 
    bullet_limit = 20
    red_rect = pygame.Rect(500,500,215,42)
    if lvl >= 3:
        num_arrows = random.randint(5,7)
    elif lvl < 3:
        num_arrows = random.randint(3,5)
    while len(arrow_positions) < num_arrows:
        pos = random.uniform(400, 1500)
        if all(abs(pos - existing_pos) >= min_distance_between_arrows for existing_pos in arrow_positions):
            arrow_positions.append(pos)
    show_loading_screen()
    while running:
        if not lvl_inc and monkes_caught >= num_arrows:
            lvl += 1
            lvl_inc = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not boss_catch:
                        new_bullet = pygame.Rect(Leaste.x + Leaste.rect.width // 2 - 5, Leaste.y - -48, 7, 3)
                        bullets.append(new_bullet)
                    else:
                        bullet_limit -= 1
                        if bullet_limit >= 0:
                            new_bullet = pygame.Rect(Leaste.x + Leaste.rect.width // 2 - 5, Leaste.y - -48, 7, 3)
                            bullets.append(new_bullet)
                        else:
                            bullet_limit = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and Leaste.flipped:
                    new_bullet = pygame.Rect(Leaste.x + Leaste.rect.width // 2 - 5, Leaste.y - -48, 7, 3)
                    left_bullets.append(new_bullet)
                if event.button == 1 and boss_catch_started:
                    if red_rect.collidepoint(event.pos) and not boss_catch:
                        boss_catch = True
                        texted = True
                        Jungle_x, Jungle2_x = 0, 1740
                        Leaste.x, Leaste.y, Leaste.fuel = 0, ground, 0
                        rock_x = random.choice(rock_x_list)
                        rock_x2 = random.choice(rock_x_list2)
                        show_loading_screen()
                if event.button == 1:
                    if menu_btn.rect.collidepoint(event.pos) and gorilla_boss.escaped or gorilla_boss.caught:
                        print("DABBBB")
                        poop_effect_time = pygame.time.get_ticks()
                        menu_pressed = True
                        arrow_positions.clear()  # Clear the arrow positions
                        monkes.clear()  # Clear the monkeys
                        bananas.clear()  # Clear the bananas
                        bullets.clear()  # Clear the bullets
                        left_bullets.clear()  # Clear the left bullets
                        orangutans.clear()  # Clear the orangutans
                        poopers.clear()
                        bloboons.clear()
                        slimes.clear()
                        Jungle_x, Jungle2_x = 0, 1740
                        Leaste.x, Leaste.y, Leaste.fuel = 0, ground, 0
                        rock_x = random.choice(rock_x_list)
                        rock_x2 = random.choice(rock_x_list2)
                        boss_catch = False
                        boss_catching_cooldown = 0
                        main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and monkes_caught >= num_arrows and not restarted and not boss_catch:
                    restarted = True
                    monkes_caught = 0
                    if lvl < 3:
                        num_arrows = random.randint(3, 5)
                    else:
                        num_arrows = random.randint(5, 7)
                    arrow_positions.clear()  # Clear the arrow positions
                    monkes.clear()  # Clear the monkeys
                    bananas.clear()  # Clear the bananas
                    bullets.clear()  # Clear the bullets
                    left_bullets.clear()  # Clear the left bullets
                    orangutans.clear()  # Clear the orangutans
                    poopers.clear()
                    bloboons.clear()
                    slimes.clear()
                    Jungle_x, Jungle2_x = 0, 1740
                    Leaste.x, Leaste.y, Leaste.fuel = 0, ground, 0
                    rock_x = random.choice(rock_x_list)
                    rock_x2 = random.choice(rock_x_list2)
                    y,al_y, an_y = 300, 370, 440
                    banums = 7
                    for monkey in monkes:
                        monkey.caught = False
                    for orangutan in orangutans:
                        orangutan.caught = False
                    while len(arrow_positions) < num_arrows:
                        pos = random.uniform(400, 1500)
                        if all(abs(pos - existing_pos) >= min_distance_between_arrows for existing_pos in arrow_positions):
                            arrow_positions.append(pos)
                    restarted = False
                    slave = True
                    lvl += 0.5
                    show_loading_screen()
        if not boss_catch:
            for monkeys in monkes:
                if Leaste.x > monkeys.x:
                    if not monkeys.caught:
                        monkeys.x -= 7.5
                        monkeys.flipped = True
                else:
                    if not monkeys.caught:
                        monkeys.flipped = False
            for orans in orangutans:
                if Leaste.x > orans.x:
                    if not orans.caught:
                        orans.x -= 7.5
                        orans.flipped = True
                else:
                    if not orans.caught:
                        orans.flipped = False
        windows.blit(Jungle_Background, (Jungle_x, Jungle_y))
        windows.blit(Jungle_Background, (Jungle2_x, Jungle_y))
        windows.blit(Rock, (rock_x, ground - 20))
        windows.blit(Rock, (rock_x2, ground - 20))
        if not boss_catch:
            windows.blit(banana_img, (0, 0))
        for bullet in bullets:
            bullet.x += 18
        for left_bullet in left_bullets:
            left_bullet.x -= 18
        for left_bullet in left_bullets:
            pygame.draw.rect(windows, yellow, left_bullet)
            for bullet in bullets:
                if Leaste.flipped:
                    bullets.remove(bullet)

        for bullet in bullets:
            pygame.draw.rect(windows, yellow, bullet)
        for bullet in bullets:
            if bullet.colliderect(rock_rect) or bullet.colliderect(rock2_rect):
                bullets.remove(bullet)
        for left_bullet in left_bullets:
            if left_bullet.colliderect(rock_rect) or left_bullet.colliderect(rock2_rect):
                left_bullets.remove(left_bullet)

        if not boss_catch:
            for bullet in bullets:
                for monkeys in monkes:
                    if bullet.colliderect(monkeys.rect) and not monkeys.caught:
                        monkeys.caught = True
                        monkes_caught += 1
                        bullets.remove(bullet)

            for bullet in bullets:
                if lvl >= 2:
                    for orans in orangutans:
                        if bullet.colliderect(orans.rect) and not orans.caught:
                            orans.caught = True
                            monkes_caught += 1
                            bullets.remove(bullet)

            for left_bullet in left_bullets:
                if lvl >= 2:
                    for orans in orangutans:
                        if left_bullet.colliderect(orans.rect) and not orans.caught:
                            orans.caught = True
                            monkes_caught += 1
                            left_bullets.remove(left_bullet)

            for left_bullet in left_bullets:
                for monkeys in monkes:
                    if left_bullet.colliderect(monkeys.rect) and not monkeys.caught:
                        monkeys.caught = True
                        monkes_caught += 1
                        left_bullets.remove(left_bullet)

            for monkeys in monkes:
                if monkeys.x > Jungle2_x - -1800:
                    monkes.remove(monkeys)
                    num_arrows -= 1
                elif monkeys.x < Jungle_x - 100:
                    monkes.remove(monkeys)
                    num_arrows -= 1
            if lvl >= 2:
                for orans in orangutans:
                    if orans.x > Jungle2_x - -1800:
                        orangutans.remove(orans)
                        num_arrows -= 1
                    elif orans.x < Jungle_x - 100:
                        orangutans.remove(orans)
                        num_arrows -= 1
            keys = pygame.key.get_pressed()

            banana.spawn(Leaste)
            monke.spawn(arrow_positions, bananas)
            monke.update()
            dis_txt(f": {banums}", ount, blue, 100, 30)

            for monke_instance in monkes:
                monke_instance.spawn(arrow_positions, bananas)
                monke_instance.update()
                monke_instance.jump()
            if lvl >= 2:
                for oran_instance in orangutans:
                    oran_instance.spawn(arrow_positions, bananas)
                    oran_instance.update()
                    oran_instance.jump()
            if lvl >= 3:
                for pooper_instance in poopers:
                    pooper_instance.spawn(arrow_positions, bananas)
                    pooper_instance.update()
                    pooper_instance.jump()
                for pooper in poopers:
                    if pooper.x > Jungle2_x - -1800:
                        poopers.remove(pooper)
                        num_arrows -= 1
                    elif pooper.x < Jungle_x - 100:
                        poopers.remove(pooper)
                        num_arrows -= 1
            if lvl >= 3:
                for bullet in bullets:
                    for pooper in poopers:
                        if bullet.colliderect(pooper.rect) and not pooper.caught:
                            pooper.caught = True
                            monkes_caught += 1
                            bullets.remove(bullet)
                for left_bullet in left_bullets:
                    for pooper in poopers:
                        if left_bullet.colliderect(pooper.rect) and not pooper.caught:
                            pooper.caught = True
                            monkes_caught += 1
                            left_bullets.remove(left_bullet)
                for pooper in poopers:
                    if Leaste.x > pooper.x:
                        if not pooper.caught:
                            pooper.x -= 7.5
                            pooper.flipped = True
                    else:
                        if not pooper.caught:
                            pooper.flipped = False
                for poo in poops:
                    poo.blit()
            if lvl >= 4.5:
                for blob in bloboons:
                    blob.spawn(arrow_positions, bananas)
                    blob.update()
                    blob.jump()
                for bullet in bullets:
                    for blob in bloboons:
                        if bullet.colliderect(blob.rect) and not blob.caught:
                            blob.hits += 1
                            bullets.remove(bullet)
                        if blob.hits >= 5 and not blob.caught:
                            blob.caught = True
                            monkes_caught += 1
                for left_bullet in left_bullets:
                    for blob in bloboons:
                        if left_bullet.colliderect(blob.rect) and not blob.caught:
                            blob.hits += 1
                            left_bullets.remove(left_bullet)
                        if blob.hits >= 5 and not blob.caught:
                            blob.caught = True
                            monkes_caught += 1
                for blob in bloboons:
                    if blob.x > Jungle2_x - -1800:
                        bloboons.remove(blob)
                        for slime in slimes:
                            slimes.remove(slime)
                        num_arrows -= 1
                    elif blob.x < Jungle_x - 100:
                        bloboons.remove(blob)
                        for slime in slimes:
                            slimes.remove(slime)
                        num_arrows -= 1
                for blob in bloboons:
                    if Leaste.x > blob.x:
                        if not blob.caught:
                            blob.x -= 7.5
                            blob.flipped = True
                    else:
                        if not blob.caught:
                            blob.flipped = False
                for blob in bloboons:
                    for slime in slimes:
                        slime.blit()
        Leaste.rect.topleft = (Leaste.x, Leaste.y)
        rock_rect.topleft = (rock_x, 635)  
        rock2_rect.topleft = (rock_x2, 635)

        if Leaste.rect.colliderect(rock_rect):
            if Leaste.rect.right > rock_rect.left and Leaste.rect.left < rock_rect.left:
                Leaste.x = rock_rect.left - Leaste.width 
            elif Leaste.rect.left < rock_rect.right and Leaste.rect.right > rock_rect.right:
                Leaste.x = rock_rect.right 
            elif Leaste.rect.bottom > rock_rect.top and Leaste.rect.top < rock_rect.top:
                Leaste.y = rock_rect.top - Leaste.height 
                Leaste.y_velocity = 0  
            collision_detected = True 
          
        elif Leaste.rect.colliderect(rock2_rect):
           if Leaste.rect.right > rock2_rect.left and Leaste.rect.left < rock2_rect.left:
                Leaste.x = rock2_rect.left - Leaste.width
           elif Leaste.rect.left < rock2_rect.right and Leaste.rect.right > rock2_rect.right:
                Leaste.x = rock2_rect.right
           elif Leaste.rect.bottom > rock2_rect.top and Leaste.rect.top < rock2_rect.top:
                Leaste.y = rock2_rect.top - Leaste.height 
                Leaste.y_velocity = 0  
           collision_detected = True 
        else:
            collision_detected = False 

        if keys[pygame.K_SPACE] and not banana_spawned and banums > 0 and not Leaste.is_jumping and banana.spawned and not monkes_caught >= num_arrows:
            if not Leaste.flipped:
                new_banana = Banana(banana_img, Leaste.x + Leaste.width // 2 - 22, Leaste.y, 38, 38)
            else:
                new_banana = Banana(banana_img, Leaste.x - Leaste.width // 2 - 22, Leaste.y, 38, 38)  
            bananas.append(new_banana)
            banums -= 1  # Decrease banana count
            banana_spawned = True  # Mark banana as spawned
        if not keys[pygame.K_SPACE]:
            banana_spawned = False
        for banana in bananas:
            banana.spawn(Leaste) 
        if not boss_catch:
            if not collision_detected:
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                    if Jungle_x < 0:
                        if not boss_catch:
                            Leaste.set_flipped(True)
                        Jungle_x += speed
                        Jungle2_x += speed
                        rock_x += speed
                        rock_x2 += speed
                        arrow_positions = [(pos + arrow_speed) for pos in arrow_positions]
                        for banana in bananas:
                            banana.x += speed
                        if monke.y < ground:
                            monke.x += speed
                        for monkeys in monkes:
                            if monkeys.y < ground:
                                monkeys.x += speed
                        if lvl >= 2:
                            for orans in orangutans:
                                if orans.y < ground:
                                    orans.x += speed
                        if lvl >= 3: 
                            for pooper in poopers:
                                if pooper.y < ground:
                                    pooper.x += speed
                        if lvl >= 4.5:
                            for blob in bloboons:
                                if blob.y < ground:
                                    blob.x += speed
                            for slime in slimes:
                                slime.x += speed
                    else:
                        Jungle_x = 0
                        Leaste.x = max(Leaste.x - 3, 0)

                if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                    if Jungle2_x > -background_width + win_width:
                        if not boss_catch:
                            Leaste.set_flipped(False)
                        Jungle_x -= speed
                        Jungle2_x -= speed
                        rock_x -= speed
                        rock_x2 -= speed
                        arrow_positions = [(pos - arrow_speed) for pos in arrow_positions]
                        for banana in bananas:
                            banana.x -= speed
                        if monke.y < ground:
                            monke.x -= speed
                        for monkeys in monkes:
                            if monkeys.y < ground:
                                monkeys.x -= speed
                        if lvl >= 2:
                            for orans in orangutans:
                                if orans.y < ground:
                                    orans.x -= speed
                        if lvl >= 3:
                            for pooper in poopers:
                                if pooper.y < ground:
                                    pooper.x -= speed
                        if lvl >= 4.5:
                            for blob in bloboons:
                                if blob.y < ground:
                                    blob.x -= speed
                            for slime in slimes:
                                slime.x -= speed
                    else:
                        max_position_x = Jungle2_x + background_width - Leaste.width
                        Leaste.x = min(Leaste.x + 3, max_position_x)
        if not boss_catch:
            for monkeys in monkes:
                if monkeys.rect.colliderect(rock_rect):
                    if monkeys.rect.right > rock_rect.left and monkeys.rect.left < rock_rect.left:
                        monkeys.x = rock_rect.left - monkeys.width
                    elif monkeys.rect.left < rock_rect.right and monkeys.rect.right > rock_rect.right:
                        monkeys.x = rock_rect.right
                    elif monkeys.rect.bottom > rock_rect.top and monkeys.rect.top < rock_rect.top:
                        monkeys.y = rock_rect.top - monkeys.height
                        monkeys.y_velocity = 0   
                        monkeys.is_jumping = False
                
                elif monkeys.rect.colliderect(rock2_rect):
                    if monkeys.rect.right > rock2_rect.left and monkeys.rect.left < rock2_rect.left:
                            monkeys.x = rock2_rect.left - monkeys.width
                    elif monkeys.rect.left < rock2_rect.right and monkeys.rect.right > rock2_rect.right:
                            monkeys.x = rock2_rect.right
                    elif monkeys.rect.bottom > rock2_rect.top and monkeys.rect.top < rock2_rect.top:
                            monkeys.y = rock2_rect.top - monkeys.height
                            monkeys.y_velocity = 0 
                            monkeys.is_jumping = False
            if lvl >= 2:
                for orans in orangutans:
                    if not orans.caught:
                        if orans.rect.colliderect(rock_rect):
                            if orans.rect.right > rock_rect.left + 100 and orans.rect.left < rock_rect.left:
                                orans.x = 100 + rock_rect.left - orans.width 
                            elif orans.rect.left < rock_rect.right and orans.rect.right > rock_rect.right:
                                orans.x = rock_rect.right
                            elif orans.rect.bottom > rock_rect.top and orans.rect.top < rock_rect.top:
                                orans.y = rock_rect.top - orans.height
                                orans.y_velocity = 0   
                                orans.is_jumping = False
                        
                        elif orans.rect.colliderect(rock2_rect):
                            if orans.rect.right > rock2_rect.left + 100 and orans.rect.left < rock2_rect.left:
                                    orans.x = 100 + rock2_rect.left - orans.width
                            elif orans.rect.left < rock2_rect.right and orans.rect.right > rock2_rect.right:
                                    orans.x = rock2_rect.right
                            elif orans.rect.bottom > rock2_rect.top and orans.rect.top < rock2_rect.top:
                                    orans.y = rock2_rect.top - orans.height
                                    orans.y_velocity = 0 
                                    orans.is_jumping = False
            if lvl >= 4.5:
                for blob in bloboons:
                    if blob.rect.colliderect(rock_rect):
                        if blob.rect.right > rock_rect.left and blob.rect.left < rock_rect.left:
                            blob.x = rock_rect.left - blob.width
                        elif blob.rect.left < rock_rect.right and blob.rect.right > rock_rect.right:
                            blob.x = rock_rect.right
                        elif blob.rect.bottom > rock_rect.top and blob.rect.top < rock_rect.top:
                            blob.y = rock_rect.top - blob.height
                            blob.y_velocity = 0   
                            blob.is_jumping = False
                    
                    elif blob.rect.colliderect(rock2_rect):
                        if blob.rect.right > rock2_rect.left and blob.rect.left < rock2_rect.left:
                                blob.x = rock2_rect.left - blob.width
                        elif blob.rect.left < rock2_rect.right and blob.rect.right > rock2_rect.right:
                                blob.x = rock2_rect.right
                        elif blob.rect.bottom > rock2_rect.top and blob.rect.top < rock2_rect.top:
                                blob.y = rock2_rect.top - blob.height
                                blob.y_velocity = 0 
                                blob.is_jumping = False
        if boss_catch:
            if gorilla_boss.rect.colliderect(rock_rect):
                if gorilla_boss.rect.right > rock_rect.left and gorilla_boss.rect.left < rock_rect.left:
                    gorilla_boss.x = rock_rect.left - gorilla_boss.width
                elif gorilla_boss.rect.left < rock_rect.right and gorilla_boss.rect.right > rock_rect.right:
                    gorilla_boss.x = rock_rect.right
                elif gorilla_boss.rect.bottom > rock_rect.top and gorilla_boss.rect.top < rock_rect.top:
                    gorilla_boss.y = rock_rect.top - gorilla_boss.height
                    gorilla_boss.y_velocity = 0   
                    gorilla_boss.is_jumping = False
                
            elif gorilla_boss.rect.colliderect(rock2_rect):
                if gorilla_boss.rect.right > rock2_rect.left and gorilla_boss.rect.left < rock2_rect.left:
                    gorilla_boss.x = rock2_rect.left - gorilla_boss.width
                elif gorilla_boss.rect.left < rock2_rect.right and gorilla_boss.rect.right > rock2_rect.right:
                    gorilla_boss.x = rock2_rect.right
                elif gorilla_boss.rect.bottom > rock2_rect.top and gorilla_boss.rect.top < rock2_rect.top:
                    gorilla_boss.y = rock2_rect.top - gorilla_boss.height
                    gorilla_boss.y_velocity = 0 
                    gorilla_boss.is_jumping = False
        if monkes_caught >= num_arrows:
            banums = 0
            slave = True
            if slave:
                if not boss_catch:
                    dis_txt(f"-Monkeys Catched-: {monkes_caught}",random_text,white,355,y)
                    dis_txt(f"Level: {lvl}",ount,white,350,al_y)
                    dis_txt("Press 'R' to catch monkeys", text_fount,white,350, an_y)
        if not lvl_inc and monkes_caught >= num_arrows:
            lvl += 1
            lvl_inc = True
            boss_catching_cooldown += 1
        else:
            None
        if monkes_caught >= num_arrows:
            for banana in bananas:
                banana.spawned = False  
        Leaste.move()
        Leaste.draw()
        Leaste.update()
        monke.jump()
        dis_txt(f"{monkes_caught}/{num_arrows}", ount , white, 10, 730)
        if boss_catching_cooldown >= 8.5 and monkes_caught >= num_arrows and lvl >= 5.5:
            boss_catch_started = True
            if not boss_catch:
                pygame.draw.rect(windows,red,red_rect)
                dis_txt("BOSS CATCH",text_fount,white,500,500)
        if texted:
            if boss_display_start is None:
                boss_display_start = pygame.time.get_ticks()  # Set the start time once
            # Check if 3 seconds have passed since the start
            if pygame.time.get_ticks() - boss_display_start < 3000:
                teext = text.render("BOSS CATCH", True, red)
                text_rect = teext.get_rect(center=(x, win_height // 2))
                windows.blit(teext, text_rect)
            else:
                texted = False
                boss_display_start = None  # Reset for future use
            text_rect = teext.get_rect(center=(x, win_height // 2))
            if x >= win_width // 2:
                x = win_width // 2
            x += 5
            pygame.display.flip()
        if not boss_catch:
            for pos in arrow_positions:
                windows.blit(arrow, (pos, ground + 30))
            for poo in poops:
                Leaste.rect = pygame.Rect(Leaste.x,Leaste.y,Leaste.width,Leaste.height)
                poo.rect = pygame.Rect(poo.x,poo.y,poo.width,poo.height)
                if poo.rect.colliderect(Leaste.rect) or Leaste.rect.colliderect(poo.rect):
                    poo.collided = True
                    poo.y = 1000
                    poop_effect_time = pygame.time.get_ticks()
                if poo.collided and (pygame.time.get_ticks() - poop_effect_time < 4000):
                    windows.blit(poo_effect_rez,(-50,-50))
            for slime in slimes:
                Leaste.rect = pygame.Rect(Leaste.x, Leaste.y, Leaste.width, Leaste.height)
                slime.rect = pygame.Rect(slime.x, ground, slime.width, slime.height) 
                if slime.rect.colliderect(Leaste.rect):  # Check collision
                    if not slime.collided:
                        slime.collided = True
                        slime.colliding_slimes += 1  # Increment collision count
                else:
                    if slime.collided:
                        slime.collided = False
                        if slime.colliding_slimes > 0:
                            slime.colliding_slimes -= 1  # Decrement collision count if resolved
            # Apply slow effect based on aggregate collision state
            if any(slime.collided for slime in slimes):
                speed = 2
                arrow_speed = 2
                Leaste.mov_sped = 0
                for pooper in poopers:
                    pooper.mov_sped = 2
            else:
                speed = 4
                arrow_speed = 4
                Leaste.mov_sped = 0.1
                for pooper in poopers:
                    pooper.mov_sped = 4
        if boss_catch:
            if not gorilla_boss.caught:
                monkes_caught = 0
            num_arrows = 1
            if not gorilla_boss.caught:
                draw_health_bar(windows,gorilla_boss.x,gorilla_boss.y - 30,gorilla_boss.health,gorilla_boss.max_health)
            dis_txt(f"Bullets : {bullet_limit}",ount,blue,0,30)
            gorilla_boss.moving = True
            gorilla_boss.update()
            gorilla_boss.jump()
            gorilla_boss.blit()
            Leaste.set_flipped(False)
            Leaste.mov_sped = 0
            if not collision_detected and not gorilla_boss.caught:
                if not gorilla_boss.escaped:
                    Jungle_x -= 4
                    Jungle2_x -= 4
                    rock_x -= 4
                    rock_x2 -= 4
            if collision_detected:
                gorilla_boss.mov_sped = 3.5
                collision_detected = False
            else:
                gorilla_boss.mov_sped = 0.4
            if Jungle_x == -1748:
                Jungle_x = 1272
            elif Jungle2_x == -1748:
                Jungle2_x = 1272
            if rock_x == -1748:
                rock_x = 1276
            elif rock_x2 == -1748:
                rock_x2 = 1280
            for bullet in bullets:
                if bullet.colliderect(gorilla_boss.rect):
                    gorilla_boss.health -= 1
                    bullets.remove(bullet)
            if gorilla_boss.health <= 0 and not gorilla_boss.caught:
                monkes_caught += 1
                gorilla_boss.caught = True
            if gorilla_boss.health <= 0:
                dis_txt("BOSS CATCHED",text,red,xx, 300)
                menu
                if xx >= 370:
                    menu_btn.blit()
                    xx = 370
                xx += 5
            if gorilla_boss.x >= 1300:
                gorilla_boss.escaped = True
            if gorilla_boss.escaped:
                dis_txt("MISSION FAILED",text,red,xxx, 300)
                if xxx >= 370:
                    menu_btn.blit()
                    xxx = 370
                xxx += 5
        print(f"cooldown:{boss_catching_cooldown}")
        if gorilla_boss.caught or gorilla_boss.escaped:
            boss_catching_cooldown = 0  # Reset cooldown to restart counting
            if menu_pressed:
                boss_catch = False
        # Reset the boss_catch flag
        pygame.display.flip()
        clock.tick(60)

def beach_game():
    global beach2_x,beach_x,arrow_positions,banana,bananas,log_x,log_x2,log_rect,log2_rect,surf,anxey
    min_distance_between_arrows = 200
    num_arrows = random.randint(3,5)
    banana_spawned = False
    lvl = 2
    bullets = []
    banums = 7
    collision_detected = False
    surf.x = surfmonke.x
    surf.y = surfmonke.y
    monkes_caught = 0
    arrow_speed = 4
    while len(arrow_positions) < num_arrows:
        pos = random.uniform(400, 1500)
        if all(abs(pos - existing_pos) >= min_distance_between_arrows for existing_pos in arrow_positions):
            arrow_positions.append(pos)
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_bullet = pygame.Rect(Leaste.x + Leaste.rect.width // 2 - 5, Leaste.y - -48, 7, 3)
                    bullets.append(new_bullet)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and Leaste.flipped:
                    new_bullet = pygame.Rect(Leaste.x + Leaste.rect.width // 2 - 5, Leaste.y - -48, 7, 3)
                    left_bullets.append(new_bullet)
        windows.blit(beach_map,(beach_x,beach_y))
        windows.blit(beach_map,(beach2_x,beach_y))
        dis_txt(f": {banums}", ount, blue, 100, 30)
        dis_txt(f"{monkes_caught}/{num_arrows}", ount , white, 10, 730)
        Leaste.move()
        Leaste.draw()
        Leaste.update()
        windows.blit(banana_img, (0, 0))
        windows.blit(log,(log_x,ground - 40))
        windows.blit(log,(log_x2,ground - 40))
        for pos in arrow_positions:
            windows.blit(arrow, (pos, ground + 30))
        if not collision_detected:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                if beach_x < 0:
                    for banana in bananas:
                        banana.x += speed
                    Leaste.set_flipped(True)
                    beach_x += 4
                    beach2_x += 4
                    log_x += 4
                    log_x2 += 4
                    for surfreys in surf_monkeys:
                        surfreys.x += 4
                    if lvl >= 2:
                        for anxey in anxeys:
                            anxey.x += 4
                    arrow_positions = [(pos + arrow_speed) for pos in arrow_positions]
                else:
                    beach_x = 0
                    Leaste.x = max(Leaste.x - 3, 0)
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                if beach2_x > -background_width + win_width:
                    for banana in bananas:
                        banana.x -= speed
                    Leaste.set_flipped(False)
                    beach_x -= 4
                    beach2_x -= 4
                    log_x -= 4
                    log_x2 -= 4
                    for surfreys in surf_monkeys:
                        surfreys.x -= 4
                    if lvl >= 2:
                        for anxey in anxeys:
                            anxey.x -= 4
                    arrow_positions = [(pos - arrow_speed) for pos in arrow_positions]
                else:
                    max_position_x = beach2_x + background_width - Leaste.width
                    Leaste.x = min(Leaste.x + 3, max_position_x)
        if keys[pygame.K_SPACE] and not banana_spawned and banums > 0 and not Leaste.is_jumping and banana.spawned and not monkes_caught >= num_arrows:
            if not Leaste.flipped:
                new_banana = Banana(banana_img, Leaste.x + Leaste.width // 2 - 22, Leaste.y, 38, 38)
            else:
                new_banana = Banana(banana_img, Leaste.x - Leaste.width // 2 - 22, Leaste.y, 38, 38)  
            bananas.append(new_banana)
            banums -= 1  # Decrease banana count
            banana_spawned = True  # Mark banana as spawned
        if not keys[pygame.K_SPACE]:
            banana_spawned = False
        for banana in bananas:
            banana.spawn(Leaste) 
        for bullet in bullets:
            pygame.draw.rect(windows, yellow, bullet)
        for bullet in bullets:
            bullet.x += 18
        for left_bullet in left_bullets:
            left_bullet.x -= 18
        for left_bullet in left_bullets:
            pygame.draw.rect(windows, yellow, left_bullet)
            for bullet in bullets:
                if Leaste.flipped:
                    bullets.remove(bullet)
        banana.spawn(Leaste)
        Leaste.rect.topleft = (Leaste.x, Leaste.y)
        log_rect.topleft = (log_x, 612)  
        log2_rect.topleft = (log_x2, 612)
        if Leaste.rect.colliderect(log_rect):
            if Leaste.rect.right > log_rect.left and Leaste.rect.left < log_rect.left:
                Leaste.x = log_rect.left - Leaste.width 
            elif Leaste.rect.left < log_rect.right and Leaste.rect.right > log_rect.right:
                Leaste.x = log_rect.right 
            elif Leaste.rect.bottom > log_rect.top and Leaste.rect.top < log_rect.top:
                Leaste.y = log_rect.top - Leaste.height 
                Leaste.y_velocity = 0  
            collision_detected = True 
          
        elif Leaste.rect.colliderect(log2_rect):
           if Leaste.rect.right > log2_rect.left and Leaste.rect.left < log2_rect.left:
                Leaste.x = log2_rect.left - Leaste.width
           elif Leaste.rect.left < log2_rect.right and Leaste.rect.right > log2_rect.right:
                Leaste.x = log2_rect.right
           elif Leaste.rect.bottom > log2_rect.top and Leaste.rect.top < log2_rect.top:
                Leaste.y = log2_rect.top - Leaste.height 
                Leaste.y_velocity = 0  
           collision_detected = True 
        else:
            collision_detected = False 
        for bullet in bullets:
            if bullet.colliderect(log_rect) or bullet.colliderect(log2_rect):
                bullets.remove(bullet)
        for left_bullet in left_bullets:
            if left_bullet.colliderect(log_rect) or left_bullet.colliderect(log2_rect):
                left_bullets.remove(left_bullet)
        for surfreys in surf_monkeys:
            if not surfreys.caught:
                for surf in surfs:
                    surf.align_with_monkey(surfreys)
                    surf.blit()
        for surfrey in surf_monkeys:
            surfrey.spawn(arrow_positions, bananas)
            surfrey.update()
            surfrey.jump()
        surfmonke.spawn(arrow_positions, bananas)
        surfmonke.update()
        surfmonke.jump()
        for surfreys in surf_monkeys:
            if surfreys.rect.colliderect(log_rect):
                if surfreys.rect.right > log_rect.left and surfreys.rect.left < log_rect.left:
                    surfreys.x = log_rect.left - surfreys.width
                elif surfreys.rect.left < log_rect.right and surfreys.rect.right > log_rect.right:
                    surfreys.x = log_rect.right
                elif surfreys.rect.bottom > log_rect.top and surfreys.rect.top < log_rect.top:
                    surfreys.y = log_rect.top - surfreys.height
                    surfreys.y_velocity = 0   
                    surfreys.is_jumping = False
            
            elif surfreys.rect.colliderect(log2_rect):
                if surfreys.rect.right > log2_rect.left and surfreys.rect.left < log2_rect.left:
                        surfreys.x = log2_rect.left - surfreys.width
                elif surfreys.rect.left < log2_rect.right and surfreys.rect.right > log2_rect.right:
                        surfreys.x = log2_rect.right
                elif surfreys.rect.bottom > log2_rect.top and surfreys.rect.top < log2_rect.top:
                        surfreys.y = log2_rect.top - surfreys.height
                        surfreys.y_velocity = 0 
                        surfreys.is_jumping = False
        for surfreys in surf_monkeys:
            if surfreys.x > beach2_x - -1800:
                surf_monkeys.remove(surfreys)
                num_arrows -= 1
            elif surfreys.x < beach_x - 100:
                surf_monkeys.remove(surfreys)
                num_arrows -= 1
        for surfreys in surf_monkeys:
            if Leaste.x >= surfreys.x:
                if not surfreys.caught:
                    surfreys.x -= 7.5
                    surfreys.flipped = True
                for surf in surfs:
                    surf.flipped = True
            else:
                if not surfreys.caught:
                    surfreys.flipped = False
                for surf in surfs:
                    surf.flipped = False
        for surf in surfs:
            print(f"hits:{surf.hits}")
            for bullet in bullets:
                if bullet.colliderect(surf.rect):
                    bullets.remove(bullet)
                    surf.hits += 1
            for left_bullet in left_bullets:
                if left_bullet.colliderect(surf.rect):
                    left_bullets.remove(left_bullet)
                    surf.hits += 1
            if surf.hits >= 10:
                surfs.remove(surf)
        for bullet in bullets:
            for surfreys in surf_monkeys:
                if bullet.colliderect(surfreys.rect) and not surfreys.caught:
                    surfreys.caught = True
                    monkes_caught += 1
                    bullets.remove(bullet)
        for left_bullet in left_bullets:
            for surfreys in surf_monkeys:
                if left_bullet.colliderect(surfreys.rect) and not surfreys.caught:
                    surfreys.caught = True
                    monkes_caught += 1
                    left_bullets.remove(left_bullet)
        if lvl >= 2:
            for anxey in anxeys:
                anxey.spawn(arrow_positions, bananas)
                anxey.update()
                anxey.jump()
            for anxey in anxeys:
                if anxey.x > beach2_x - -1800:
                    anxeys.remove(anxey)
                    num_arrows -= 1
                elif anxey.x < beach_x - 100:
                    anxeys.remove(anxey)
                    num_arrows -= 1
            for anxey in anxeys:
                if Leaste.x >= anxey.x:
                    if not anxey.caught:
                        anxey.x -= 7.5
                        anxey.flipped = True
                else:
                    if not anxey.caught:
                        anxey.flipped = False
            for anxey in anxeys:
                if anxey.rect.colliderect(log_rect):
                    if anxey.rect.right > log_rect.left and anxey.rect.left < log_rect.left:
                        anxey.x = log_rect.left - anxey.width
                    elif anxey.rect.left < log_rect.right and anxey.rect.right > log_rect.right:
                        anxey.x = log_rect.right
                    elif anxey.rect.bottom > log_rect.top and anxey.rect.top < log_rect.top:
                        anxey.y = log_rect.top - anxey.height
                        anxey.y_velocity = 0   
                        anxey.is_jumping = False
                
                elif anxey.rect.colliderect(log2_rect):
                    if anxey.rect.right > log2_rect.left and anxey.rect.left < log2_rect.left:
                            anxey.x = log2_rect.left - anxey.width
                    elif anxey.rect.left < log2_rect.right and anxey.rect.right > log2_rect.right:
                            anxey.x = log2_rect.right
                    elif anxey.rect.bottom > log2_rect.top and anxey.rect.top < log2_rect.top:
                            anxey.y = log2_rect.top - anxey.height
                            anxey.y_velocity = 0 
                            anxey.is_jumping = False
            for bullet in bullets:
                for anxey in anxeys:
                    if bullet.colliderect(anxey.rect) and not anxey.caught:
                        anxey.hits += 1
                        bullets.remove(bullet)
                    if anxey.hits == 1:
                        anxey.sped = 7.5
                    elif anxey.hits >= 2 and not anxey.caught:
                        anxey.caught = True
                        monkes_caught += 1
            for left_bullet in left_bullets:
                for anxey in anxeys:
                    if left_bullet.colliderect(anxey.rect) and not anxey.caught:
                        anxey.hits += 1
                        left_bullets.remove(left_bullet)
                    if anxey.hits == 1:
                        anxey.sped = 7.5
                    elif anxey.hits >= 2 and not anxey.caught:
                        anxey.caught = True
                        monkes_caught += 1
            pygame.display.flip()
        clock.tick(60)
def map():
    global on_menu,on_controls,on_map,on_monkeys,poop_effect_time,on_beach
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if jungle_btn.rect.collidepoint(event.pos):
                        show_loading_screen()
                        main_game()
                    elif back_btn.rect.collidepoint(event.pos):
                        on_monkeys = False
                        on_controls = False
                        on_menu = True
                        on_map = False
                        main_menu()
                    elif beach_btn.rect.collidepoint(event.pos):
                        on_beach = True
                        show_loading_screen()
                        beach_game()
        if on_map:
            windows.fill(dark_blue)
            back_btn.blit()
            jungle_btn.blit()
            beach_btn.blit()
        on_map = True
        pygame.display.flip()
def show_controls():
    global on_menu,on_controls,on_map,on_monkeys,poop_effect_time
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_btn.rect.collidepoint(event.pos):
                        main_menu()
                        on_monkeys = False
                        on_controls = False
                        on_menu = True
                        on_map = False
        if on_controls:
            windows.fill(dark_green)
            back_btn.blit()
            dis_txt("A > Left move",random_text,white,50,100) 
            dis_txt("D > Right move",random_text,white,50,180) 
            dis_txt("W > Fly",random_text,white,50,260) 
            dis_txt("SPACE > Spawn bananas",random_text,white,50,340) 
        on_controls = True
        pygame.display.flip()
def show_monkeys():
    global on_menu,on_controls,on_map,on_monkeys,poop_effect_time
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back2_btn.rect.collidepoint(event.pos):
                        main_menu()
                        on_monkeys = False
                        on_controls = False
                        on_menu = True
                        on_map = False
        if on_monkeys:
            windows.fill(peach_brown)
            windows.blit(pygame.transform.scale(monke_img,(90,110)),(0,30))
            windows.blit(pygame.transform.scale(oran_img,(210,190)),(-40,190))
            windows.blit(pygame.transform.scale(pooper_img,(60,100)),(0,450))
            windows.blit(pygame.transform.scale(bloboon_img,(110,130)),(0,650))
            dis_txt("MONKEY > Regular monkey you can see in your jungle.",text_fount,white,100,50)
            dis_txt("ORANGOG > Weird orangutan but friendly.",text_fount,white,140,240)
            dis_txt("POOPER > Likes pooping and has a fast jetpack.",text_fount,white,100,480)
            dis_txt("BLOBOON > Extremely durable and likes blobs.",text_fount,white,140,670)
            back2_btn.blit()
        on_monkeys = True
        pygame.display.flip()
def main_menu():
    global on_menu,on_controls,on_map,on_monkeys,poop_effect_time
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play.rect.collidepoint(event.pos):
                        map()
                        on_map = True
                        on_menu = False
                        on_controls = False
                        on_monkeys = False
                    elif tutorial_btn.rect.collidepoint(event.pos):
                        show_controls()
                        on_controls = True
                        on_map = False
                        on_menu = False
                        on_monkeys = False
                    elif monkeys_btn.rect.collidepoint(event.pos):
                        show_monkeys()
                        on_monkeys = True
                        on_controls = False
                        on_menu = False
                        on_map = False
        on_menu = True
        if on_menu:
            windows.blit(menu,(0,0))
            monkeys_btn.blit()
            tutorial_btn.blit()
            play.blit()
        pygame.display.flip()
beach_game()
pygame.quit()

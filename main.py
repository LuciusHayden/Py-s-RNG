import pygame
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 40)

screen_width = 1600
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

MythicList = []
RareList = []
UncommonList = []
CommonList = []

class aura:
    def __init__(self, x, y, colorX, colorY, colorZ, aura_name, rarity):
        self.x = 800
        self.y = 500
        self.colorX = colorX
        self.colorY = colorY
        self.colorZ = colorZ
        self.color = (self.colorX, self.colorY, self.colorZ)
        self.radius = 200
        self.aura_name = font.render(aura_name, True, (255, 255, 255))
        self.rarity = font.render(rarity, True, (255, 255, 255))
        self.backgroundX = colorX - 120
        self.backgroundY = colorY - 120
        self.backgroundZ = colorZ - 120
        
    def draw(self):
        global wait
        global wait_time
        
        wait = False
        if self.backgroundX  <= 0:
            self.backgroundX = 0
        if self.backgroundY <= 0:
            self.backgroundY = 0
        if self.backgroundZ <= 0:
            self.backgroundZ = 0
        if not wait and self.backgroundX <= self.colorX-70:
            self.backgroundX += 3
            wait_time = pygame.time.get_ticks()
            wait = True
        if not wait and self.backgroundY <= self.colorY-70:
            self.backgroundY += 3
            wait_time = pygame.time.get_ticks()
            wait = True
        if not wait and self.backgroundZ <= self.colorZ-70:
            self.backgroundZ += 3
            wait_time = pygame.time.get_ticks()
            wait = True
        if wait and pygame.time.get_ticks() - wait_time > 75:  
            wait = False
        screen.fill((self.backgroundX, self.backgroundY, self.backgroundZ))
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        screen.blit(self.aura_name, ((screen_width // 2 - self.aura_name.get_width() // 2, screen_height // 2 - self.aura_name.get_height() // 2)))
        screen.blit(self.rarity, (screen_width // 2 - self.rarity.get_width() // 2, screen_height // 2 - self.rarity.get_height() // 2 + 250))

def roll():
    global dice
    global rolled
    global show_aura
    global selected
    rolled = False
    roll = random.randint(0, 1000)
    if roll > 900 and roll < 1000 and not rolled:
        i = len(MythicList)
        dice2 = random.randint(0, i-1)
        selected = MythicList[dice2]
        show_aura = True
        rolled = True
    if roll > 800 and roll < 900 and not rolled:
        i = len(RareList)
        dice2 = random.randint(0, i-1)
        selected = RareList[dice2]
        show_aura = True
        rolled = True
    if roll > 500 and roll < 800 and not rolled:
        i = len(UncommonList)
        dice2 = random.randint(0, i-1)
        selected = UncommonList[dice2]
        show_aura = True
        rolled = True
    if roll > 0 and roll < 500 and not rolled:
        i = len(CommonList)
        dice2 = random.randint(0, i-1)
        selected = CommonList[dice2]
        show_aura = True
        rolled = True
    print(selected)


BloodLust = aura(700, 475, 130, 0, 0,  "BloodLust", "Mythical")
Impeached = aura(700, 475, 0, 70,0, "Impeached", "Mythical")
ArchAngle = aura(700, 475, 250, 241, 147, "ArchAngle", "Mythical")
Genesis = aura(700, 475, 200, 200, 255, "Genesis", "Mythical")
StarScourge = aura(700, 475, 169, 20, 199, "StarScourge", "Mythical")

MythicList.append(Impeached)
MythicList.append(BloodLust)
MythicList.append(ArchAngle)
MythicList.append(Genesis)
MythicList.append(StarScourge)

Undead = aura(700, 475, 0, 0, 70, "Undead", "Rare")
Lunar = aura(700, 475, 50, 70, 200, "Lunar", "Rare")
StarLight = aura(700, 475, 70, 70, 150, "Starlight", "Rare")
Eclipse = aura(700, 475, 200, 70, 70, "Eclipse", "Rare")
Comet = aura(700, 475, 150, 70, 70, "Comet", "Rare")
Solar = aura(700, 475, 255, 140, 0, "Solar", "Rare")

RareList.append(Undead)
RareList.append(Lunar)
RareList.append(StarLight)
RareList.append(Eclipse)
RareList.append(Comet)
RareList.append(Solar)


Natural = aura(700, 475, 70, 200, 70, "Natural", "Uncommon")
Uncommon = aura(700, 475, 70, 70, 70, "Uncommon", "Uncommon")
Rage = aura(700, 475, 150, 70, 70, "Rage", "Uncommon")
Ruby = aura(700, 475, 255, 70, 70, "Ruby", "Uncommon")
Gilded = aura(700, 475, 181, 201, 26, "Gilded", "Uncommon")

UncommonList.append(Natural)
UncommonList.append(Uncommon)
UncommonList.append(Rage)
UncommonList.append(Ruby)
UncommonList.append(Gilded)

Common = aura(700, 475, 70, 70, 70, "Common", "Common")
Good = aura(700, 475, 70, 70, 70, "Good", "Common")
Crystal = aura(700, 475, 144, 0, 255, "Crystal", "Common")
Evil = aura(700, 475, 144, 70, 70, "Evil", "Common")

CommonList.append(Common)
CommonList.append(Good)
CommonList.append(Crystal)
CommonList.append(Evil)

run = True
rolled = False 
show_aura = False
remaining_cooldown = 0
total_cooldown = 2000
show_guide = True
guide = font.render("Press space to start rolling!", True, (255, 255, 255))



while run:
    screen.fill((0, 0, 0))
    
    roll_cooldown = font.render(f"Your on cooldown for {remaining_cooldown}", True, (255, 255, 255))
    
    key = pygame.key.get_pressed()

    if show_guide:
        screen.blit(guide, (screen_width // 2 - guide.get_width() // 2, screen_height // 2 - guide.get_height() // 2))
    if not rolled and key[pygame.K_SPACE]:
        roll()
        cd_start = pygame.time.get_ticks()
        show_guide = False
        
    if show_aura:
        selected.draw()
    if rolled:
        remaining_cooldown = total_cooldown - (pygame.time.get_ticks() - cd_start)
        screen.blit(roll_cooldown, (screen_width // 2 - guide.get_width() // 2, screen_height // 2 - guide.get_height() // 2 + 400))
        if pygame.time.get_ticks() - cd_start > total_cooldown:
            rolled = False
    print(f"Rolled: {rolled} Show Aura: {show_aura} Remaining Cooldown: {remaining_cooldown}" )
    print(MythicList, CommonList)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False 
    pygame.display.update()

pygame.quit()
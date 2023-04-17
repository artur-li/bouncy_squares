import pygame, sys, random
pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
score = 0

class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        self.rect = self.image.get_rect(center = (random.randint(10,590), -10))
        self.x_movement = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        self.y_movement = random.randint(1,3)
    def collisions(self):
        if self.rect.centerx >= 595 or self.rect.centerx <= 5:
            self.x_movement = self.x_movement * -1
    def update(self):
        if self.rect.centery > 605:
            global score
            score += 1
            self.kill()
        else:
            self.collisions()
            self.rect.centerx += self.x_movement
            self.rect.centery += self.y_movement
rect_group = pygame.sprite.Group()
def spawn_rect():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        rect = Rect()
        rect_group.add(rect)
def spawn_score():
        global score
        score_surf = font.render(str(score), False, "Grey")
        score_rect = score_surf.get_rect(center=(300,20))
        screen.blit(score_surf,score_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    spawn_rect()
    rect_group.update()
    rect_group.draw(screen)
    spawn_score()
    pygame.display.update()
    clock.tick(60)

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spider Shooter")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Spider:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.size = 20
        self.web_trail = [(x, y)]
        
    def update(self):
        self.y += self.speed
        self.web_trail.append((self.x, self.y))
        
    def draw(self, screen):
        for i in range(len(self.web_trail) - 1):
            pygame.draw.line(screen, (200, 200, 200), self.web_trail[i], self.web_trail[i + 1], 1)
        
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.size)
        pygame.draw.circle(screen, RED, (self.x, self.y), self.size-2)
        
        for i in range(8):
            angle = i * 45
            end_x = self.x + self.size * 1.5 * pygame.math.Vector2(1, 0).rotate(angle).x
            end_y = self.y + self.size * 1.5 * pygame.math.Vector2(1, 0).rotate(angle).y
            pygame.draw.line(screen, BLACK, (self.x, self.y), (end_x, end_y), 2)

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.width = 40
        self.height = 20
        self.speed = 5
        
    def move_left(self):
        self.x = max(0, self.x - self.speed)
        
    def move_right(self):
        self.x = min(WIDTH - self.width, self.x + self.speed)
        
    def draw(self, screen):
        points = [
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ]
        pygame.draw.polygon(screen, BLUE, points)
        pygame.draw.polygon(screen, GREEN, points, 2)

class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
        self.width = 3
        self.height = 15
        
    def update(self):
        self.y -= self.speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x - self.width//2, self.y, self.width, self.height))

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.reset_game()
        
    def reset_game(self):
        self.player = Player()
        self.spiders = []
        self.lasers = []
        self.score = 0
        self.level = 1
        self.game_over = False
        self.paused = False
        self.spider_spawn_timer = 0
        self.spider_spawn_delay = 60
        
    def spawn_spider(self):
        x = random.randint(20, WIDTH - 20)
        spider = Spider(x, 0)
        spider.speed = int(1 + (self.level - 1) * 0.5)
        self.spiders.append(spider)
        
    def shoot_laser(self):
        laser = Laser(self.player.x + self.player.width // 2, self.player.y)
        self.lasers.append(laser)
        
    def check_collisions(self):
        for laser in self.lasers[:]:
            for spider in self.spiders[:]:
                distance = ((laser.x - spider.x)**2 + (laser.y - spider.y)**2)**0.5
                if distance < spider.size:
                    if laser in self.lasers:
                        self.lasers.remove(laser)
                    if spider in self.spiders:
                        self.spiders.remove(spider)
                    self.score += 10
                    if self.score % 50 == 0:
                        self.level += 1
                    break
                    
        for spider in self.spiders:
            if spider.y >= HEIGHT - 50:
                self.game_over = True
                
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_over and not self.paused:
                        self.shoot_laser()
                    elif event.key == pygame.K_p:
                        self.paused = not self.paused
                    elif event.key == pygame.K_r and self.game_over:
                        self.reset_game()
                        
            if not self.game_over and not self.paused:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.player.move_left()
                if keys[pygame.K_RIGHT]:
                    self.player.move_right()
                    
                self.spider_spawn_timer += 1
                if self.spider_spawn_timer >= self.spider_spawn_delay:
                    self.spawn_spider()
                    self.spider_spawn_timer = 0
                    self.spider_spawn_delay = max(20, 60 - self.level * 5)
                    
                for spider in self.spiders:
                    spider.update()
                    
                for laser in self.lasers[:]:
                    laser.update()
                    if laser.y < 0:
                        self.lasers.remove(laser)
                        
                self.check_collisions()
                
            screen.fill(WHITE)
            
            for spider in self.spiders:
                spider.draw(screen)
                
            self.player.draw(screen)
            
            for laser in self.lasers:
                laser.draw(screen)
                
            score_text = self.font.render(f"Score: {self.score}", True, BLACK)
            level_text = self.font.render(f"Level: {self.level}", True, BLACK)
            screen.blit(score_text, (10, 10))
            screen.blit(level_text, (WIDTH - 150, 10))
            
            if self.paused:
                pause_text = self.font.render("PAUSED - Press P to continue", True, RED)
                text_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.blit(pause_text, text_rect)
                
            if self.game_over:
                game_over_text = self.font.render("GAME OVER!", True, RED)
                restart_text = self.small_font.render("Press R to restart", True, BLACK)
                score_final_text = self.font.render(f"Final Score: {self.score}", True, BLACK)
                
                screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//2 - 60))
                screen.blit(restart_text, (WIDTH//2 - 100, HEIGHT//2))
                screen.blit(score_final_text, (WIDTH//2 - 120, HEIGHT//2 + 40))
                
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
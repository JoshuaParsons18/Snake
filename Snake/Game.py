import pygame
import sys 

from Snake import Snake
from Food import Food

class Game:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)
        self.deadly_food = []


    def update(self, dt):
        '''responsible for updating the game state and objects on each iteration of the loop.'''
        self.snake.update()
        self.food.update()
        for deadly_food in self.deadly_food:
            deadly_food.update()
        self.draw()


    def draw(self):
        '''handles drawing to the screen. Called from game.update()'''
        self.snake.draw()
        self.food.draw()
        for deadly_food in self.deadly_food:
            deadly_food.draw()


    def run(self):
        '''handles the main game loop and runs continuously until the game is exited'''
        running = True

        clock = pygame.time.Clock()

        # Game loop
        while(running):
            dt = clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

            keys = pygame.key.get_pressed()

            if(self.snake.rect.colliderect(self.food.rect)):
                print(f"Snake Length = {self.snake.length}")
                self.snake.add_segment()
                self.food.destroy_food()
                new_deadly_food = Food(self.screen, color=(83,6,97), total_food=0)
                self.deadly_food.append(new_deadly_food)
                

            # Lose conditions
            for deadly_food in self.deadly_food:
                if self.snake.rect.colliderect(deadly_food.rect):
                    print(f"You lose")
                    self.food.destroy_food()
                    running = False
                    sys.exit()


            self.snake.input_handler(keys, dt)

            self.screen.fill((0, 255, 255))
            self.update(dt)
            pygame.display.update()

    pygame.quit()




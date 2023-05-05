import pygame
import random

class Food:
    def __init__(self, screen, width=16, height=16, color=(255,0,0), total_food=0):
        
        # dynamic attributes
        self.width = width
        self.height = height
        self.color = color
        self.total_food = total_food

        # static attributes
        self.screen = screen
        self.win_dimensions = self.screen.get_size()
        self.screen_width = self.win_dimensions[0]
        self.screen_height = self.win_dimensions[1]
        self.xPos = 0 
        self.yPos = 0
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def update(self):
        # check how many food are in the game. If 0 spawn_food
        if(self.total_food < 1):
            self.spawn_food()


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


    def spawn_food(self):
        self.xPos = random.randint(0, self.screen_width-20)
        self.yPos = random.randint(0, self.screen_height-20)
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        self.total_food += 1


    def destroy_food(self):
        self.total_food -= 1


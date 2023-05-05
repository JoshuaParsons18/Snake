import pygame
import sys

class Snake:
    def __init__(self, screen, xPos=400, yPos=300, width=16, height=16, speed=250, length=0, color=(0,0,255)):

        # dyanamic attributes
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.speed = speed
        self.length = length
        self.color = color

        # static attributes
        self.screen = screen
        self.win_dimensions = self.screen.get_size()
        self.screen_width = self.win_dimensions[0]
        self.screen_height = self.win_dimensions[1]
        self.score = 0
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        self.segments = []

    
    def update(self):
        if self.segments:
            # Move the tail segment to the front of the list
            tail = self.segments.pop()
            tail.x, tail.y = self.rect.x, self.rect.y
            self.segments.insert(0, tail)

        if self.rect.top < 0:
            print("player collided with wall. You lose")
            sys.exit()
        elif self.rect.bottom > self.screen_height:
            print("player collided with wall. You lose")
            sys.exit()
        elif self.rect.left < 0:
            print("player collided with wall. You lose")
            sys.exit()
        elif self.rect.right > self.screen_width:
            print("player collided with wall. You lose")
            sys.exit()

    def draw(self):
        # Draw the snake head
        pygame.draw.rect(self.screen, self.color, self.rect)

        # Draw the segments
        for segment in self.segments:
            pygame.draw.rect(self.screen, self.color, segment)

    
    def input_handler(self, keys, dt):
        '''Takes in a list of keys and checks which were pressed. Then updates position using dt'''
        dt = dt / 1000

        if(keys[pygame.K_w]):
            self.rect.y -= int(self.speed * dt)
        elif(keys[pygame.K_s]):
            self.rect.y += int(self.speed * dt)
        elif(keys[pygame.K_a]):
            self.rect.x -= int(self.speed * dt)
        elif(keys[pygame.K_d]):
            self.rect.x += int(self.speed * dt)

    def add_segment(self):
        self.length += 1
        if self.segments:
            last_segment = self.segments[-1]
            new_segment = pygame.Rect(last_segment.x, last_segment.y, self.width, self.height)
            self.segments.append(new_segment)
        else:
            new_segment = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
            self.segments.append(new_segment)
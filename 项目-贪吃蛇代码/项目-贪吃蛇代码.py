# My Name:Oliver Mao   Student ID:185084   Massey ID:19029837
print("My Name:Oliver Mao   Student ID:185084   Massey ID:19029837")

import pygame
import random

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)

# Screen size
height = 600
width = 600

# set a score
score = 0

# Margin between each segment
segment_margin = 3

# Set the width and height of each snake segment
segment_width = min(height, width) / 40 - segment_margin
segment_height = min(height, width) / 40 - segment_margin

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0


class Snake():
    """ Class to represent one snake. """

    # Constructor
    def __init__(self):
        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(5):
            x = (segment_width + segment_margin) * 30 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 2
            segment = Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)

    def grow(self):
        # Insert new segment into the list
        global old_segment
        self.spriteslist.add(old_segment)
        self.segments.insert(-1, old_segment)

    def move(self):
        global old_segment
        # Figure out where new segment will be
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change

        # Insert new segment into the list
        segment = Segment(x, y)
        self.segments.insert(0, segment)
        self.spriteslist.add(segment)

        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        old_segment = self.segments.pop()
        self.spriteslist.remove(old_segment)
        self.dead()

    def dead(self):
        global game_ended
        # snake reach the edge
        if (self.segments[0].rect.x < 0) or (self.segments[0].rect.x > width - segment_width) or (self.segments[0].rect.y < 0) or (self.segments[0].rect.y > 600):
            game_ended = True

        # snake reach itself
        for i in self.segments[1:]:
            if (self.segments[0].rect.x == i.rect.x) and (self.segments[0].rect.y == i.rect.y):
                game_ended = True

        # snake reach the obstacle
        obstacle_hit = pygame.sprite.spritecollide(self.segments[0],my_obstacle.spriteslist,True)
        if obstacle_hit != []:
            game_ended = True

        # snake reach AIsnake
        obstacle_hit0 = pygame.sprite.spritecollide(self.segments[0], ai_snake.spriteslist, True)
        if obstacle_hit0 != []:
            game_ended = True

class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Food():
    """ Class to represent one food. """

    # Constructor
    def __init__(self):
        self.foods = []
        self.spriteslist = pygame.sprite.Group()
        x = random.randrange(0, 600, 15)
        y = random.randrange(0, 600, 15)
        food = Food_item(x, y)
        self.foods.append(food)
        self.spriteslist.add(food)

    # for creating new food
    def create_food(self):
        x = random.randrange(0, 600, 15)
        y = random.randrange(0, 600, 15)
        while (x,y) in my_snake.segments[:]:
            x = random.randrange(0, 600, 15)
            y = random.randrange(0, 600, 15)
        food = Food_item(x, y)
        self.foods.append(food)
        self.spriteslist.add(food)


class Food_item(pygame.sprite.Sprite):
    """ Class to represent the item of the food. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Obstacle():

    def __init__(self):
        self.obstacles = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(10):
            x = random.randrange(0, 600, 15)
            y = random.randrange(0, 600, 15)
            obstacle = Obstacle_item(x, y)
            self.obstacles.append(obstacle)
            self.spriteslist.add(obstacle)

    # for creating the new obstacle
    def create_obstacle(self):
        x = random.randrange(0, 600, 15)
        y = random.randrange(0, 600, 15)
        obstacle = Obstacle_item(x, y)
        self.obstacles.append(obstacle)
        self.spriteslist.add(obstacle)

class Obstacle_item(pygame.sprite.Sprite):
    def __init__(self, x, y):

        super().__init__()

        # Set height, width
        width = random.randrange(15,150,15)
        height = random.randrange(15,150,15)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class AISnake():
    """ Class to represent one AIsnake. """

    # Constructor
    def __init__(self):
        self.segments2 = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(5):
            x = (segment_width + segment_margin) * 30 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 30
            segment2 = AISnake_item(x, y)
            self.segments2.append(segment2)
            self.spriteslist.add(segment2)


    def move(self):
        # Figure out where new segment will be
        x = self.segments2[0].rect.x + y_change*random.randrange(-1,1)
        y = self.segments2[0].rect.y + x_change*random.randrange(-1,1)

        # Don't move off the screen
        if 0 <= x <= width - segment_width and 0 <= y <= height - segment_height:
        # Insert new segment into the list
            segment2 = AISnake_item(x, y)
            self.segments2.insert(0, segment2)
            self.spriteslist.add(segment2)

            # Get rid of last segment of the snake
            # .pop() command removes last item in list
            old_segment2 = self.segments2.pop()
            self.spriteslist.remove(old_segment2)


class AISnake_item(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# reset the pygame
pygame.init()

# Create a 600x600 sized screen
screen = pygame.display.set_mode([width, height])

# Set the title of the window
pygame.display.set_caption('SNAKE')

my_snake = Snake()
food = Food()
my_obstacle = Obstacle()
ai_snake = AISnake()

clock = pygame.time.Clock()


# create the "game over" screen
def Gameover():
    screen2 = pygame.display.set_mode([width, height])
    screen2.fill(WHITE)
    font2 = pygame.font.SysFont("comicsansms", 48)
    text2 = font2.render('Game Over', True, (0, 100, 255))
    textrect2 = text2.get_rect()
    textrect2.centerx = 300
    textrect2.centery = 500
    screen2 = pygame.display.get_surface()
    screen2.blit(text2, textrect2)


done = False
game_ended = False

while not done:
    # control moving
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Set the direction based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change != (segment_width + segment_margin) :
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT and x_change != (segment_width + segment_margin) * -1:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP and y_change != (segment_height + segment_margin):
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN and y_change != (segment_height + segment_margin) * -1:
                x_change = 0
                y_change = (segment_height + segment_margin)



    # snake eat the food
    if my_snake.segments[0].rect == food.foods[-1].rect:
        hit_list = pygame.sprite.spritecollide(my_snake.segments[0], food.spriteslist, True)
        food.create_food()
        my_snake.grow()
        score += 1

    # let the food not appear on the snake
    for i in range(len(my_snake.segments)):
        hit_list2 = pygame.sprite.spritecollide(my_snake.segments[i], food.spriteslist, True)
        if hit_list2 != []:
            food.create_food()

    # let the food not appear on the obstacles
    for i in range(len(my_obstacle.obstacles)):
        hit_list3 = pygame.sprite.spritecollide(my_obstacle.obstacles[i], food.spriteslist, True)
        if hit_list3 != []:
            food.create_food()

    # let the obstacles not on the snake's body
    for i in range(len(my_snake.segments)):
        hit_list4 = pygame.sprite.spritecollide(my_snake.segments[i], my_obstacle.spriteslist, True)
        if hit_list4 != []:
            my_obstacle.create_obstacle()

    # move snake one step
    my_snake.move()
    ai_snake.move()

    # -- Draw everything
    screen.fill(BLACK)
    my_snake.spriteslist.draw(screen)
    food.spriteslist.draw(screen)
    my_obstacle.spriteslist.draw(screen)
    ai_snake.spriteslist.draw(screen)

    # draw the 'score' on the screen
    font = pygame.font.SysFont("comicsansms", 48)
    text = font.render('Score = ' + str(score), True, (180, 180, 0))
    textrect = text.get_rect()
    textrect.centerx = 120
    textrect.centery = 40
    screen.blit(text, textrect)

    # game_ended()
    if game_ended:
        Gameover()
    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(12)

pygame.quit()
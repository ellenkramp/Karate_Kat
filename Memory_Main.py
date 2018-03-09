import random, time, pickle
import pygame
pygame.init()

screen_width = 960
screen_height = 540

black = (0, 0, 0)
teal = (44, 245, 235)
white = (255, 255, 255)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        (self.rect.left, self.rect.top) = location

background_pic = Background('assets/dojo.png', (0, 0))

image_list = [
    'assets/karate_kick_1.png',
    'assets/karate_punch.png',
    'assets/karate_split.png',
    'assets/karate_kick3.png',
    'assets/karate_kick4.png',
    'assets/karate_kick6.png',
    'assets/karate_kick7.png',
    'assets/karate_kick8.png',
    'assets/karate_kick9.png',
    'assets/karate_kick10.png'
]

image_dict = {
    1: 'assets/karate_stance.png',
    2: 'assets/karate_kick2.png',
    3: 'assets/karate_split.png',
    4: 'assets/karate_kick3.png',
    5: 'assets/karate_kick4.png',
    6: 'assets/karate_kick6.png',
    7: 'assets/karate_kick7.png',
    8: 'assets/karate_kick8.png',
    9: 'assets/karate_punch.png',
    10: 'assets/karate_kick10.png'
}

coordinates = [
    (5, 300),
    (95, 390),
    (160, 320),
    (300, 370),
    (400, 310),
    (500, 350),
    (600, 300),
    (680, 370),
    (750, 390),
    (840, 350)
]

dead_pic = 'assets/karate_dead.png'

user_list = []
game_list = []

def kat(i):
    karatePic = pygame.image.load(image_dict[i])
    screen.blit(karatePic,coordinates[i-1])

def kat_to_memorize():
    rand_num = random.randint(1,11)
    game_list.append(rand_num)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Karate Kat')
clock = pygame.time.Clock()
screen.fill(teal)
screen.blit(background_pic.image, background_pic.rect)
for i in range(1, 11):
    kat(i)

lostGame = False

while not lostGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lostGame = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print position

    pygame.display.update()
    clock.tick()
    
pygame.quit()
quit()

score = 0 #track points here. points per turn = length of array, while user array == game array

    ####gameplay
    #start menu options, 1 - play game 2 - see high scores 3 - quit
    #while user array == game array, 
 
    ####game structure
    #1) randomly generate one number between 1-10
    #2) store randomly generated number in game array
    
    #3) call upon a dictionary, which houses each number, paired with its associated image in the game. if x, then have structure dictionary[x] enlarge, etc. to
    #exhibit to the player that this is the chosen object. 

#4) have the user *click* on the image(s) representing the array
#5) store user's answers in a separate array
    

#6) while user input array matches the game array, restart at #1, continuing to add to the 
#store lives in a number variable, decrement each time the user selects wrong memory string
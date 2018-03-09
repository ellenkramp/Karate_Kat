import random, time, pickle
import pygame
pygame.init()
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption('Karate Kat')
clock = pygame.time.Clock()

lostGame = False
#initialize a user array and a game array
user_list = []
game_list = []
#initialize images in sequence
image_dict = {
    1: 'assets/karate_kick_1',
    2: 'assets/karate_kick_2',
    3: 'assets/karate_kick_3',
    4: 'assets/karate_kick_4',
    5: 'assets/karate_kick_5',
    6: 'assets/karate_kick_6',
    7: 'assets/karate_kick_7',
    8: 'assets/karate_kick_8',
    9: 'assets/karate_kick_9',
    10: 'assets/karate_kick_10'
}

#color definitions
black = (0, 0, 0)
teal = (44, 245, 235)
white = (255, 255, 255)
score = 0 #track points here. points per turn = length of array, while user array == game array

def main():
    ####gameplay
    #start menu options, 1 - play game 2 - see high scores 3 - quit
    pygame.draw.rect(screen, teal, [55, 200, 100, 70], 0)
    #while user array == game array, 
while user_list == game_list:
    ####game structure
    #1) randomly generate one number between 1-10
    rand_num = random.randint(1,11)
    #2) store randomly generated number in game array
    game_list.append(rand_num)
    #3) call upon a dictionary, which houses each number, paired with its associated image in the game. if x, then have structure dictionary[x] enlarge, etc. to
    #exhibit to the player that this is the chosen object.      
    
    done = False
    while not done:
        screen.fill(black) #colors defined above
        for event in pygame.event.get(): #user action
            if event.type == pygame.QUIT: #user closes window
                done = True
        pygame.display.update() #update screen
        clock.tick(60) # set to 60 fps
pygame.quit()




#4) have the user *click* on the image(s) representing the array
#5) store user's answers in a separate array
    

#6) while user input array matches the game array, restart at #1, continuing to add to the 
#store lives in a number variable, decrement each time the user selects wrong memory string
main()
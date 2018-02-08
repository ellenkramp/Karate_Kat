import random
# sound.main(file_path=None)

#start menu options, 1 - play game 2 - see high scores 3 - quit

#initialize a user array and a game array
user_list = []
game_list = []
image1 = 
image_dict = {
    1: 'image1',
    2: 'image2',
    3: 'image3',
    4: 'image4',
    5: 'image5',
    6: 'image6',
    7: 'image7',
    8: 'image8',
    9: 'image9',
    10: 'image10'
}
####gameplay
#while user array == game array

####game structure
#1) randomly generate one number between 1-10
rand_num = random.randint(1,11)
#2) store randomly generated number in game array
game_list.append(rand_num)
print game_list
#3) call upon a dictionary, which houses each number, paired with its associated image in the game. if x, then have structure dictionary[x] enlarge, etc. to
#exhibit to the player that this is the chosen object.
print image_dict[rand_num]

#4) have the user *click* on the image(s) representing the array
#5) store user's answers in a separate array
class MySprite(Sprite):

  def is_clicked(self):
    return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
#6) while user input array matches the game array, restart at #1, continuing to add to the 
#store lives in a number variable, decrement each time the user selects wrong memory string

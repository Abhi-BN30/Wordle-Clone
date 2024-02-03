import pygame
import sys
import random
from words import *

pygame.init()

#Background music

pygame.mixer.music.load('Cipher2.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

# Constants

WIDTH, HEIGHT = 633, 700

SCREEN = pygame.display.set_mode((0,0))
BACKGROUND = pygame.image.load("2506307.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(0, 0))

pygame.display.set_caption("Wordle!")

GREEN = "#0000ff"
YELLOW = "#ffa500"
BLACK = "#000000"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

CORRECT_WORD = random.choice(WORDS)

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 25)
AVAILABLE_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 15)

SCREEN.fill("black")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 60
LETTER_Y_SPACING = 8
LETTER_SIZE = 55

# Global variables

guesses_count = 0

# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []

game_result = ""

class Letter:
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+27.5, self.bg_position[1]+27.5)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 4)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 4)
        pygame.display.update()

class Indicator:
    def __init__(self, x, y, letter):
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 48, 65)
        self.bg_color = OUTLINE

    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "black")
        self.text_rect = self.text_surface.get_rect(center=(self.x+24, self.y+30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

# Drawing the indicators on the screen.

indicator_x, indicator_y = 650, 200

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 80
    if i == 0:
        indicator_x = 685
    elif i == 1:
        indicator_x = 745

remcount = 5

rem_disp_font = pygame.font.Font('FreeSansBold.otf',16)
rem_disp_text = rem_disp_font.render(f' Attempts remaining : 6 ' , True , 'white' , 'black')
rem_disp_rect = rem_disp_text.get_rect(center = (650,10))
SCREEN.blit(rem_disp_text,rem_disp_rect)

def check_guess(guess_to_check):
    # Goes through each letter and checks if it should be green, yellow, or BLACK.
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result, remcount
    game_decided = False
    
    for i in range(5):
        
        rem_disp_font = pygame.font.Font('FreeSansBold.otf',16)
        rem_disp_text = rem_disp_font.render(f' Attempts remaining : {str(remcount)} ' , True , 'white' , 'black')
        rem_disp_rect = rem_disp_text.get_rect(center = (650,10))
        SCREEN.blit(rem_disp_text,rem_disp_rect)
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in CORRECT_WORD:
            if lowercase_letter == CORRECT_WORD[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
            
        else:
            guess_to_check[i].bg_color = BLACK
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = BLACK
                    indicator.draw()
            guess_to_check[i].text_color = "black"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()

    
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110
    
    count = 0
    for k in indicators:
        if k.bg_color == GREEN:
            count+=1
    
    if count == 5:
        
        win_disp_font = pygame.font.Font('FreeSansBold.otf',40)
        win_disp_text = win_disp_font.render(' Congrats u have won ' , True , 'white' , 'black')
        win_disp_rect = win_disp_text.get_rect(center = (600,350))
        SCREEN.blit(win_disp_text,win_disp_rect)

    if guesses_count == 6 and game_result == "":
        game_result = "L"
        los_disp_font = pygame.font.Font('FreeSansBold.otf',40)
        los_disp_text = los_disp_font.render(' Sorry u have lost ' , True , 'white','black')
        los_disp_rect = los_disp_text.get_rect(center = (600,350))
        SCREEN.blit(los_disp_text,los_disp_rect)
    

def play_again():
    # Puts the play again text on the screen.
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    
    play_again_font = pygame.font.Font("FreeSansBold.otf", 40)
    play_again_text = play_again_font.render(" Press ENTER to Play Again! or Press ESC to Quit! ", True, "white" , 'black')
    play_again_rect = play_again_text.get_rect(center=(600, 400))
    word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}!", True, "white",'black')
    word_was_rect = word_was_text.get_rect(center=(600, 450))
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()

remcount1 = 6

rem_disp_font = pygame.font.Font('FreeSansBold.otf',16)
rem_disp_text = rem_disp_font.render(f' Attempts remaining : {remcount1} ' , True , 'white' , 'black')
rem_disp_rect = rem_disp_text.get_rect(center = (650,10))
SCREEN.blit(rem_disp_text,rem_disp_rect)

def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result,remcount1
    SCREEN.fill("black")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()
    
    

    rem_disp_font = pygame.font.Font('FreeSansBold.otf',16)
    rem_disp_text = rem_disp_font.render(f' Attempts remaining : {remcount1} ' , True , 'white' , 'black')
    rem_disp_rect = rem_disp_text.get_rect(center = (650,10))
    SCREEN.blit(rem_disp_text,rem_disp_rect)

def create_new_letter():
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING

while True:
    if game_result != "":
        play_again()
        
    for event in pygame.event.get():
    
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
                        remcount-=1
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            elif event.key == pygame.K_ESCAPE :
                pygame.quit()
                sys.exit()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()
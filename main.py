import pygame

pygame.init()
pygame.display.set_caption("Hangman")

FPS = 60
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = (255, 255, 255)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LINE_LENGTH = 40
SEPARATION = 50

spaces = []
guessed_letters = []
incorrect_count = 0



def update(word, incorrect, window):
    for l in guessed_letters: 
    
        font = pygame.font.Font(None, 40)
        letter = font.render(l.upper(), True, BLACK)
        text_rect = letter.get_rect()
        text_rect.center = ((WIDTH * 0.12) + (word.index(l)*SEPARATION), HEIGHT * 0.83)
        window.blit(letter, text_rect)
    if incorrect >=1: 
        #head
        pygame.draw.ellipse(window, BLACK, (WIDTH*0.725, HEIGHT * 0.4, 40, 40), 1)
    if incorrect >=2: 
        #torso
        pygame.draw.line(window, BLACK, (WIDTH*0.75, HEIGHT*0.45), (WIDTH*0.75, HEIGHT*0.55))
    if incorrect >=3: 
        #left arm
        pygame.draw.line(window, BLACK, (WIDTH*0.75, HEIGHT*0.475), (WIDTH*0.7, HEIGHT*0.5))
    if incorrect>=4:
        #right arm
        pygame.draw.line(window, BLACK, (WIDTH*0.75, HEIGHT*0.475), (WIDTH*0.8, HEIGHT*0.5))
    if incorrect>=5:
        #left leg
        pygame.draw.line(window, BLACK, (WIDTH*0.75, HEIGHT*0.55), (WIDTH*0.7, HEIGHT*0.6))
    if incorrect >= 6:
        #right leg
        pygame.draw.line(window, BLACK, (WIDTH*0.75, HEIGHT*0.55), (WIDTH*0.8, HEIGHT*0.6))
def draw_hanger(window):
    pygame.draw.line(window, BLACK, (WIDTH/2, HEIGHT*0.75), (WIDTH/2, HEIGHT *0.25))
    pygame.draw.line(window, BLACK, (WIDTH/2, HEIGHT*0.25), (WIDTH*0.75, HEIGHT*0.25))
    #where the body starts
    pygame.draw.line(window, BLACK, (WIDTH*0.75, HEIGHT*0.25), (WIDTH*0.75, HEIGHT*0.4))
def draw_spaces(window, n):
    
    for i in range(n):
        start_x = (WIDTH * 0.10) + (i * SEPARATION)
        start_y = HEIGHT * 0.85
        end_x = start_x + LINE_LENGTH
        end_y = start_y
        pygame.draw.line(window, BLACK, (start_x, start_y), (end_x, end_y))

def main(window, word):
    global incorrect_count
    run = True
    clock = pygame.time.Clock()
    
    word = word
    
    count = 0

    
    
    window.fill(BACKGROUND_COLOR)
    draw_hanger(WINDOW)
    draw_spaces(WINDOW, len(word))

    g_font = pygame.font.Font(None, 30)
    prompt = g_font.render("Please Enter Your guess :)", True, BLACK)
    prompt_rect = prompt.get_rect()
    prompt_rect.center = (WIDTH/2, HEIGHT * 0.15)
    pygame.draw.rect(window, (255, 255, 255), (WIDTH*0.15, HEIGHT*0.1, WIDTH, 100))
    window.blit(prompt, prompt_rect)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                break
        
            if event.type == pygame.KEYDOWN:
                guess = pygame.key.name(event.key).lower()
                if len(guess) == 1 and guess.isalpha():
                        if guess not in guessed_letters:
                            if guess in word:
                        
                                guessed_letters.append(guess)
                                count += 1
                                prompt = g_font.render("Nice Guess! Try Another Letter :)", True, BLACK)
                                pygame.draw.rect(window, (255, 255, 255), (WIDTH*0.15, HEIGHT*0.1, WIDTH, 100))
                                window.blit(prompt, prompt_rect)
    
                        
                                if count == len(set(word)):  # Use set to account for unique letters
                                    prompt = g_font.render("You win!", True, GREEN)
                                    pygame.draw.rect(window, (255, 255, 255), (WIDTH*0.15, HEIGHT*0.1, WIDTH, 100))
                                    window.blit(prompt, prompt_rect)
                                    run = False
                                    
                            
                            else:
                    # Handle incorrect guess if needed
                                prompt = g_font.render("Incorrect!", True, BLACK)
                                pygame.draw.rect(window, (255, 255, 255), (WIDTH*0.15, HEIGHT*0.1, WIDTH, 100))
                                window.blit(prompt, prompt_rect)
                                incorrect_count+=1
                                if incorrect_count == 6:
                                    prompt = g_font.render("You lost ;(", True, RED)
                                    pygame.draw.rect(window, (255, 255, 255), (WIDTH*0.15, HEIGHT*0.1, WIDTH, 100))
                                    window.blit(prompt, prompt_rect)
                                    run = False
                            
                            
                else:
                    prompt = g_font.render("Guess must be a single letter!", True, BLACK)
                    pygame.draw.rect(window, (255, 255, 255), (WIDTH*0.15, HEIGHT*0.1, WIDTH, 100))
                    window.blit(prompt, prompt_rect)

        update(word, incorrect_count, window)
        
        pygame.display.update()
    pygame.time.wait(1000)
    pygame.quit()   

if __name__ == "__main__":
    word = input("Enter a word without duplicate letters: ")
    if word != " ": 
        main(WINDOW, word)
        
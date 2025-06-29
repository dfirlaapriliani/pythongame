import pygame, time, random, os

pygame.init()
width, height = 600, 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Pixel Retro Snake by Firla")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
snake_block = 20
snake_speed = 10
font_style = pygame.font.Font(None, 32)
score_font = pygame.font.Font(None, 28)

bg_img = pygame.image.load(os.path.join("assets", "bg.png"))
food_img = pygame.image.load(os.path.join("assets", "food.png"))
eat_sound = pygame.mixer.Sound(os.path.join("assets", "eat.wav"))
pygame.mixer.music.load(os.path.join("assets", "bg_music.mp3"))

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, (0, 255, 128), [x[0], x[1], snake_block, snake_block])

def your_score(score):
    value = score_font.render(f"Score: {score}", True, black)
    dis.blit(value, [10, 10])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 2])

def gameLoop():
    game_over = False
    game_close = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            dis.fill(white)
            message("Game Over! Tekan C main lagi, Q keluar", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.blit(bg_img, (0, 0))
        dis.blit(food_img, (foodx, foody))

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            eat_sound.play()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
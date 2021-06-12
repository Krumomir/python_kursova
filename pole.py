import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))

counter = 0


def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (144, 238, 144), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (144, 238, 144), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 150, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def button2(screen, position, text, color):
    font = pygame.font.SysFont("Arial", 24)
    if color == "blue":
        text_render = font.render(text, 1, (0, 0, 255))
    elif color == "green":
        text_render = font.render(text, 1, (0, 255, 0))
    elif color == "red":
        text_render = font.render(text, 1, (255, 0, 0))
    elif color == "pink":
        text_render = font.render(text, 1, (255, 182, 193))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def buildings_menu():
    global buy_factory, buy_cleaning, buy_windturbine, exit
    buy_factory = button2(screen, (500, 100), "          BUY FACTORY         ", "red")
    buy_cleaning = button2(screen, (500, 150), "BUY CLEANING STATION", "blue")
    buy_windturbine = button2(screen, (500, 200), "          BUY WINDMILL         ", "green")
    exit = button2(screen, (500, 300), "                    EXIT                   ", "red")


def buy_menu():
    global buy_land
    buy_land = button2(screen, (500, 250), "                    BUY                   ", "pink")


def menu():
    global buy_factory, buy_cleaning, buy_windturbine, buy_land, counter, exit
    b1 = button(screen, (100, 100), "      ")
    pygame.draw.rect(screen, (128,128,128), b1)
    b2 = button(screen, (200, 100), "      ")
    pygame.draw.rect(screen, (128,128,128), b2)
    b3 = button(screen, (300, 100), "      ")
    pygame.draw.rect(screen, (128,128,128), b3)
    b4 = button(screen, (100, 200), "      ")
    pygame.draw.rect(screen, (128,128,128), b4)
    b5 = button(screen, (200, 200), "      ")
    pygame.draw.rect(screen, (128,128,128), b5)
    b6 = button(screen, (300, 200), "      ")
    pygame.draw.rect(screen, (128,128,128), b6)
    b7 = button(screen, (100, 300), "      ")
    pygame.draw.rect(screen, (128,128,128), b7)
    b8 = button(screen, (200, 300), "      ")
    pygame.draw.rect(screen, (128,128,128), b8)
    b9 = button(screen, (300, 300), "      ")
    pygame.draw.rect(screen, (128,128,128), b9)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                    counter = 1
                elif b2.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b3.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b4.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b5.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b6.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b7.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b8.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b9.collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()

                if buy_factory.collidepoint(mx, my):
                    print("factory")
                if buy_cleaning.collidepoint(mx, my):
                    print("cleaning station")
                if buy_windturbine.collidepoint(mx, my):
                    if counter == 1:
                        pygame.draw.rect(screen, (0, 255, 0), b1)
                if buy_land.collidepoint(mx, my):
                    if counter == 1:
                        pygame.draw.rect(screen, (255, 182, 193), b1)




        pygame.display.update()


menu()

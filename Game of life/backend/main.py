from game import *
import pygame

def main():
    game = PyGame()
    game.set_up()

    board = Board(game.screen)
    board.update_screen()
    while game.is_running():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.terminate()

        board.update()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
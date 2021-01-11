import pygame


class Board:
    def __init__(self, level):
        self.level = level
        self.cell_size = 30

    def render(self, screen):
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == '#':
                    pygame.draw.rect(screen, pygame.Color('blue'),
                                     ((25 + j * 30, 25 + i * 30), (30, 30)), 0)
                elif self.level[i][j] == '-':
                    pygame.draw.rect(screen, pygame.Color('brown'),
                                     ((25 + j * 30, 25 + i * 30), (30, 10)), 0)
                elif self.level[i][j] == '.':
                    pygame.draw.circle(screen, pygame.Color('pink'),
                                       (40 + j * 30, 40 + i * 30), 3)
                elif self.level[i][j] == ',':
                    pygame.draw.circle(screen, pygame.Color('pink'),
                                       (40 + j * 30, 40 + i * 30), 7)

    def find_cell(self, pos):
        '''когда пакмен будет находиться на клетке с точкой,то сюда будут передоваться его координаты, чтобы определить положение клетки и по ней удалить её из self.level'''
        x, y = pos[0], pos[1]
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if x > 25 + j * 30 and x < 25 + (j + 1) * 30 and \
                        y > 25 + i * 30 and y < 25 + (i + 1) * 30:
                    return i, j


if __name__ == '__main__':
    pygame.init()
    menu_text = ['Pac-Man', '1 level']
    font = pygame.font.Font(None, 30)
    text_coord = 100
    width, height = 500, 500
    size = width, height
    screen_menu = pygame.display.set_mode(size)
    string_rendered = font.render(menu_text[0], 5, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    text_coord += 50
    intro_rect.top = text_coord
    intro_rect.x = 50
    text_coord += intro_rect.height
    screen_menu.blit(string_rendered, intro_rect)
    for line in menu_text[1:]:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen_menu.blit(string_rendered, intro_rect)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        pygame.display.flip()

    file_level = 1
    if file_level == 1:
        file_name = 'level1.txt'
    try:
        f = open(file_name, 'rt', encoding="utf-8")
        level = [[one for one in f.readline().replace('\n', '')] for _ in
                 range(22)]
        f.close()
        board = Board(level)
        width, height = 32 * len(level[0]), 32 * len(level)
        size = width, height
        screen_play = pygame.display.set_mode(size)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(board.find_cell(event.pos))
            board.render(screen_play)
            pygame.display.flip()
        pygame.quit()
    except FileNotFoundError:
        print('Файл с уровнем не найден')

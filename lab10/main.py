import pygame as pg
import sys, random
from pygame import Vector2
from database import get_or_create_user, save_progress

# Запрашиваем имя пользователя
username = input("Enter your username: ")

# Получаем или создаем пользователя и его данные
user_id, saved_score, saved_level = get_or_create_user(username)

# Инициализация Pygame
pg.init()  # Запускаем Pygame
clock = pg.time.Clock()  # Создаем объект для контроля времени

cell_size = 40  # Размер клетки в пикселях
cell_number = 20  # Количество клеток по горизонтали и вертикали

# Установка окна игры
screen = pg.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pg.display.set_caption("Snake Game")  # Установка заголовка окна

game_font = pg.font.Font('freesansbold.ttf', 25)  # Шрифт для отображения текста

# Определение различных типов еды с их весами и временем жизни
FOOD_TYPES = {
    "apple": {"color": (211, 25, 55), "points": 1, "lifetime": 5000},
    "banana": {"color": (255, 255, 0), "points": 2, "lifetime": 4000},
    "grape": {"color": (138, 43, 226), "points": 3, "lifetime": 3000}
}


class FRUIT:
    def __init__(self, snake):
        self.snake = snake  # Ссылка на объект змеи
        self.spawn_fruit()  # Генерация первого фрукта

    def draw_fruit(self):
        # Отрисовка фрукта на экране
        fruit_rect = pg.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pg.draw.rect(screen, self.color, fruit_rect)

    def spawn_fruit(self):
        # Генерация новой позиции фрукта
        while True:
            self.pos = Vector2(random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))
            if self.pos not in self.snake.body:  # Проверка, что фрукт не появляется на змее
                break

        self.type = random.choice(list(FOOD_TYPES.keys()))  # Случайный выбор типа фрукта
        self.color = FOOD_TYPES[self.type]["color"]  # Цвет фрукта
        self.points = FOOD_TYPES[self.type]["points"]  # Очки, которые дает фрукт
        self.lifetime = FOOD_TYPES[self.type]["lifetime"]  # Время жизни фрукта
        self.spawn_time = pg.time.get_ticks()  # Отслеживание времени появления фрукта

    def check_expiration(self):
        # Проверка, не истекло ли время жизни фрукта
        if pg.time.get_ticks() - self.spawn_time > self.lifetime:
            self.spawn_fruit()  # Генерация нового фрукта


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 10), Vector2(7, 10)]  # Начальная позиция змеи
        self.direction = Vector2(1, 0)  # Направление движения змеи
        self.new_block = False  # Флаг для добавления нового блока

    def draw_snake(self):
        # Отрисовка змеи на экране
        for block in self.body:
            body_block = pg.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pg.draw.rect(screen, (64, 109, 228), body_block)

    def move_snake(self):
        # Движение змеи
        self.body.insert(0, self.body[0] + self.direction)  # Добавление нового блока в направлении движения
        if not self.new_block:
            self.body.pop()  # Удаление последнего блока, если не добавляется новый
        self.new_block = False  # Сброс флага

    def add_block(self):
        # Добавление нового блока к змее
        self.new_block = True


class MAIN:
    def __init__(self, score=0, level=1):
        self.snake = Snake()  # Создание объекта змеи
        self.fruit = FRUIT(self.snake)  # Создание объекта фрукта
        self.score = score  # Начальный счет
        self.level = level  # Начальный уровень
        self.speed = max(50, 150 - (self.level - 1) * 20)  # Начальная скорость игры
        self.last_growth_time = pg.time.get_ticks()  # ВРЕМЯ ДЛЯ РОСТА ЗМЕИ 
        self.walls = self.create_walls(level)  # Создание стен для уровня

    def create_walls(self, level):
        walls = []
        if level == 1:
            walls = [(5, 5), (6, 5), (7, 5)]
        elif level == 2:
            walls = [(3, 3), (3, 4), (4, 4), (5, 4)]
        elif level == 3:
            walls = [(2, 2), (2, 3), (3, 3), (4, 3), (5, 3)]
        return walls

    def draw_walls(self):
        for wall in self.walls:
            pg.draw.rect(screen, (255, 0, 0), pg.Rect(wall[0] * cell_size, wall[1] * cell_size, cell_size, cell_size))

    def update(self):
        # Обновление состояния игры
        self.snake.move_snake()  # Движение змеи
        self.check_collision()  # Проверка на столкновения
        self.check_fail()  # Проверка на поражение
        self.fruit.check_expiration()  # Проверка на истечение времени жизни фрукта
        current_time = pg.time.get_ticks()
        if current_time - self.last_growth_time >= 3000:  # МОЯ ЗАДАЧА 3 секунды
            self.snake.add_block()  # Adding new block 
            self.last_growth_time = current_time  # синхрон со временем

    def draw(self):
        # Отрисовка элементов игры
        self.snake.draw_snake()  # Отрисовка змеи
        self.fruit.draw_fruit()  # Отрисовка фрукта
        self.draw_walls()  # Отрисовка стен
        self.draw_text()  # Отрисовка текста счета и уровня

    def check_collision(self):
        # Проверка на столкновение змеи с фруктом
        if self.fruit.pos == self.snake.body[0]:
            self.score += self.fruit.points  # Увеличение счета на количество очков фрукта
            self.snake.add_block()  # Добавление блока к змее
            self.fruit.spawn_fruit()  # Генерация нового фрукта
            if self.score % 5 == 0:
                self.level_up()  # Повышение уровня каждые 5 очков

    def level_up(self):
        # Повышение уровня игры
        if self.level < 5:
            self.level += 1  # Увеличение уровня
            self.speed = max(50, self.speed - 20)  # Уменьшение времени между обновлениями
            pg.time.set_timer(SCREEN_UPDATE, self.speed)  # Установка таймера обновления экрана
            self.walls = self.create_walls(self.level)  # Перегенерация стен

    def check_fail(self):
        # Проверка на поражение
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number or self.snake.body[0] in self.snake.body[1:]:
            self.game_over()  # Завершение игры
        for wall in self.walls:
            if self.snake.body[0] == Vector2(wall[0], wall[1]):
                self.game_over()  # Завершение игры

    def game_over(self):
        # Завершение игры
        save_progress(user_id, self.score, self.level)
        sys.exit(pg.quit())  # Выход из Pygame и завершение программы

    def draw_text(self):
        # Отрисовка текста счета и уровня
        score_text = f"Score: {self.score}"
        level_text = f"Level: {self.level}"
        warning_text = f"Snake grows every: 3 seconds"
        screen.blit(game_font.render(score_text, True, (255, 255, 255)), (10, 10))  # Отрисовка счета
        screen.blit(game_font.render(level_text, True, (255, 255, 255)), (10, 40))  # Отрисовка уровня
        screen.blit(game_font.render(warning_text, True, (255, 255, 255)), (10, 70))


SCREEN_UPDATE = pg.USEREVENT  # Создание события для обновления экрана
main_game = MAIN(score=saved_score, level=saved_level)  # Создание объекта MAIN
pg.time.set_timer(SCREEN_UPDATE, main_game.speed)  # Установка таймера обновления экрана
paused = False
running = True  
while running:
    for event in pg.event.get():  # Обработка событий
        if event.type == pg.QUIT:
            running = False  # Выход из игры
            pg.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            if not paused:
                main_game.update()  # Обновление состояния игры
        elif event.type == pg.KEYDOWN:  # Обработка нажатий клавиш
            if event.key == pg.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)  # Изменение направления на вверх
            if event.key == pg.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)  # Изменение направления на вниз
            if event.key == pg.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)  # Изменение направления на влево
            if event.key == pg.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)  # Изменение направления на вправо
            elif event.key == pg.K_p:
                paused = not paused
                if paused:
                    from database import save_progress
                    save_progress(user_id, main_game.score, main_game.level)

    screen.fill((170, 215, 81))  # Очистка экрана
    main_game.draw()  # Отрисовка элементов игры
    pg.display.flip()  # Обновление экрана
    clock.tick(60)  # Ограничение кадров в секунду
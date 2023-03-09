import random
from tkinter import *

# Constants
window_width = 1200
window_height = 500
space_size = 10
snake_length = 3
speed = 100
color_body = '#0f1ad2'
color_heade = '#24ffc4'
food_color = '#ff42d0'
background_color = 'black'


class Snake:
    def __init__(self):
        self.snake_length = snake_length
        self.coord = [[0, 0]] * 3
        self.square = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=color_body)
            self.square.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (window_width/space_size) - 1) * space_size  # 1200/25 = 120
        y = random.randint(0, (window_height/space_size) - 1) * space_size  # 500/25 = 50

        self.coord = [x, y]

        canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=food_color)


def move (snake, food):
    for x, y in snake.coord:
        square = canvas.create_rectangle(x, y, x +space_size, y + space_size, fill=color_body)
    x, y = snake.coord[0]

    if (direction == 'down'):
        y += space_size
    elif (direction == 'up'):
        y -= space_size
    elif (direction == 'left'):
        x -= space_size
    elif (direction == 'right'):
        x += space_size


    snake.coord.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=color_heade)
    snake.square.insert(0, square)

    if (x == food.coord[0] and y == food.coord[1]):
        global score

        score += 1

        label_score.config(text='Score: {}'.format(score))
        canvas.delete('food')

        food = Food()
    else:
         x, y = snake.coord[-1]
         square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=background_color)

         del snake.coord[-1]
         canvas.delete(snake.square[-1])
         del snake.square[-1]

    if (check_collisions(snake)):
        game_over()
    else:
        window.after(speed, move, snake, food)

def change_direction(new_dir):
    global direction

    if (new_dir == 'down'):
        if (direction !='up'):
            direction = new_dir
    elif (new_dir == 'up'):
        if (direction !='down'):
            direction = new_dir
    if (new_dir == 'left'):
        if (direction !='right'):
            direction = new_dir
    if (new_dir == 'right'):
        if (direction !='left'):
            direction = new_dir

def check_collisions(snake):
    x, y = snake.coord[0]

    if (x < 0 or x >= window_width):
        return True
    elif (y < 0 or y >= window_height):
        return True

    for snake_length in snake.coord[1:0]:
        if (x == snake_length[0] and y == snake_length[1]):
            return True

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Futura PT', 50), text='Game Over', fill='red')
    canvas.create_text(canvas.winfo_width()/3, canvas.winfo_height()/3 ,
                       font=('Futura PT', 50), text='Try again', fill='blue')

window = Tk()
window.title('Змейка')
window.resizable(False, False)

score = 0
direction = 'down'

label_score = Label(window, text='Счет: {}'.format(score), font=('Arial', 40))
label_score.pack()

canvas = Canvas(window, height=window_height, width=window_width, bg=background_color)
canvas.pack()

window.geometry('1200x500')

window.bind('<Down>', lambda  event: change_direction('down'))
window.bind('<Up>', lambda  event: change_direction('up'))
window.bind('<Left>', lambda  event: change_direction('left'))
window.bind('<Right>', lambda  event: change_direction('right'))

snake = Snake()
food = Food()

move(snake, food)

window.mainloop()
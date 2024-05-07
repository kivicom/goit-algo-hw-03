'''використовується для графічного малювання.'''
import turtle

def koch_curve(t, order, size):
    '''Функція koch_curve є рекурсивною і використовується 
        для малювання кожного сегмента Кривої Коха.'''

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    '''Ця функція встановлює графічне вікно і черепашку для малювання'''

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Початкова позиція малюнка по центру екрана
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Повторюємо малювання трьох сторін, щоб утворити повну сніжинку Коха
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)  # Поворот на 120 градусів праворуч для формування трикутника

    window.mainloop()

# Виклик функції
draw_koch_snowflake(3)

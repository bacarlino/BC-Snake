def fruit_scoring(snake, scores):
    scores[snake.id] += (len(snake.body) * 10)

def no_fruit_scoring(snake, scores):
    pass
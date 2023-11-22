from flask import Flask, render_template, request

app = Flask(__name__)

position = {
    'x': 0,
    'y': 0
}

directions = ['north', 'east', 'south', 'west']
current_direction = 'north'

@app.route('/')
def index():
    return render_template('index.html', position=position, direction=current_direction)

@app.route('/move', methods=['POST'])
def move():
    global position

    movement = request.form['movement']

    if movement == 'forward':
        if current_direction == 'north':
            position['y'] += 1
        elif current_direction == 'east':
            position['x'] += 1
        elif current_direction == 'south':
            position['y'] -= 1
        elif current_direction == 'west':
            position['x'] -= 1
    elif movement == 'backward':
        if current_direction == 'north':
            position['y'] -= 1
        elif current_direction == 'east':
            position['x'] -= 1
        elif current_direction == 'south':
            position['y'] += 1
        elif current_direction == 'west':
            position['x'] += 1

    return render_template('index.html', position=position, direction=current_direction)

@app.route('/turn', methods=['POST'])
def turn():
    global current_direction

    turn_direction = request.form['turn']

    if turn_direction == 'left':
        current_direction = directions[(directions.index(current_direction) - 1) % 4]
    elif turn_direction == 'right':
        current_direction = directions[(directions.index(current_direction) + 1) % 4]

    return render_template('index.html', position=position, direction=current_direction)

@app.route('/reset', methods=['POST'])
def reset():
    global position, current_direction

    position = {
        'x': 0,
        'y': 0
    }

    current_direction = 'north'

    return render_template('index.html', position=position, direction=current_direction)

if __name__ == '__main__':
    app.run()


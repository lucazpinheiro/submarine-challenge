
class Submarine():
    def __init__(self):
        self.x_axis = 0
        self.y_axis = 0
        self.z_axis = 0
        self.direction = 'north'

    def reset_state(self):
        self.x_axis = 0
        self.y_axis = 0
        self.z_axis = 0
        self.direction = 'north'
    
    def get_current_state(self):
        return (self.x_axis, self.y_axis, self.z_axis, self.direction)

    def log_current_state(self):
        print(f'X axis: {self.x_axis}, Y axis: {self.y_axis}, Z axis: {self.z_axis}, Direction: {self.direction}')

    def move_forward(self):
        if self.direction == 'north':
            self.y_axis += 1
        elif self.direction == 'south':
            self.y_axis -= 1
        elif self.direction == 'east':
            self.x_axis += 1
        elif self.direction == 'west':
            self.x_axis -= 1

    def move_down(self):
        self.z_axis -= 1

    def move_up(self):
        if self.z_axis == 0:
            print("can't go above ocean level")
            return
        else:
            self.z_axis += 1
        
    def turn_right(self):
        if self.direction == 'north':
            self.direction = 'east'
        elif self.direction == 'east':
            self.direction = 'south'
        elif self.direction == 'south':
            self.direction = 'west'
        elif self.direction == 'west':
            self.direction = 'north'

    def turn_left(self):
        if self.direction == 'north':
            self.direction = 'west'
        elif self.direction == 'west':
            self.direction = 'south'
        elif self.direction == 'south':
            self.direction = 'east'
        elif self.direction == 'east':
            self.direction = 'north'

    def process_commands(self, commands):
        for letter in commands:
            if letter == 'L' or letter == 'l':
                self.turn_left()
            elif letter == 'R' or letter == 'r':
                self.turn_right()
            elif letter == 'U' or letter == 'u':
                self.move_up()
            elif letter == 'D' or letter == 'd':
                self.move_down()
            elif letter == 'M' or letter == 'm':
                self.move_forward()

    def command_input(self, commands = None):
        if commands is None:
            commands = list(str(input('enter commands \n> ')))
            print(commands)
            self.process_commands(commands)
        else:
            self.process_commands(commands)



def run_tests(initial_input, expected_output):
    sb = Submarine()
    sb.command_input(initial_input)
    if (expected_output == sb.get_current_state()):
        print('SUCCESSFUL!!!')
    else:
        print('FAILED!!! :(')
    sb.log_current_state()
    print('__________________________________')



print('first test')
run_tests('LMRDDMMUU', (-1, 2, 0, 'north'))


print('second test')
run_tests('RMMLMMMDDLL', (2, 3, -2, 'south'))

print('third test')
run_tests('UUU', (0, 0, 0, 'north'))

# run_tests('RMMLMMMDDLL', (2, 3, -2, 'south'))

# sb = Submarine()

# sb.command_input()

# sb.log_current_state()
from blessings import Terminal
from time import sleep

t = Terminal()

# TText formatting
print(t.bold('This text is bold'))
print(t.underline('This text is underline'))

# text color and highlight
print(t.red('Some red text'))
print(t.red_on_yellow('Text red on yellow'))

# compund formatting
print(t.bold_red_on_bright_green('Bold text red on bright green'))

# Normal text
print('Normal Text')

# Positioning Text
def position(x, y):
    with t.location(x, y):
        print(f'Text controlled by location ({x}, {y})')

for i in range(10):
    position(10+i, t.height - i)

with t.fullscreen():
# callable formats
    print('I am', t.bold, 'bold text', t.normal, 'followed by normal')
    print(f'I am {t.bold}bold text {t.normal}followed by normal')
    sleep(2)

# Applications
# Teminal color test program

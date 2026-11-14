import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    print('''================
    TASKFLOW    
================

    [1] Add task
    [2] List all tasks
    [0] Exit
''')

    option = int(input('Select an option between those 3: '))

    clear_screen()

    if option == 1:
        print('''================
    TASKFLOW    
================
Option selected: [1] Add task
''')
        task = input('Type here what kind of task you want to add: ')
        print('Task added with successful!')
        time.sleep(3)

    elif option == 2:
        print(f'''================
    TASKFLOW    
================
Option selected: [2] List all tasks
Task: {task};
''')
        time.sleep(10)

    elif option == 0:
        print(f'''================
    TASKFLOW    
================
Option selected: [0] Exit
        
Bye! See you next time...
''')
        time.sleep(2)
        break

    else:
        print("[Error] You didn't choose a valid option! Try again")
        time.sleep(2)
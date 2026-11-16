import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

task_list = []

while True:
    clear_screen()
    print('''
================
    TASKFLOW    
================

    [1] Add task
    [2] List all tasks
    [0] Exit
''')

    try:
        option = int(input('Select an option between those 3: '))
    except ValueError:
        print('Invalid input! Try again with valid inputs (1, 2 or 0).')
        time.sleep(3)
        continue

    clear_screen()

    if option == 1:
        while True:
            clear_screen()

            print('''
================
    TASKFLOW    
================
Option selected: [1] Add task
''')
            new_task = input('Type here your new task or [f] for finish: ').strip()

            if new_task.lower() == 'f':
                print('\nFinished!')
                time.sleep(3)
                break

            if not new_task:
                print('\nError! Tasks cannot be empty.')
                time.sleep(3)
                continue

            task_list.append(new_task)
            print('\nTask added with successful!')
            time.sleep(3)

    elif option == 2:
        while True:
            clear_screen()

            print(f'''
================
    TASKFLOW    
================
Option selected: [2] List all tasks
''')
            if not task_list:
                print('Your task list is empty!')
            else:
                for index, task in enumerate(task_list, start=1):
                    print(f'Task {index} - {task}')


            go_back = input('\nType "g" to go back to the main menu: ')

            if go_back.lower() == 'g':
                print('\nGoing back to main menu...')
                time.sleep(3)
                break
            else:
                print('\nInvalid input! Please type "g" to go back.')
                time.sleep(3)

    elif option == 0:
        print(f'''
================
    TASKFLOW    
================
Option selected: [0] Exit
        
Bye! See you next time...
''')
        time.sleep(2)
        break

    else:
        print('''
================
    TASKFLOW
================

    [1] Add task
    [2] List all tasks
    [0] Exit

Select an option between those 3: 
[Error] Option does not exist! Try again...
''')
        time.sleep(2)
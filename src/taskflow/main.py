import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(option=None):
    clear_screen()

    print('''
================
    TASKFLOW    
================
''')

    if option is not None:
        print(f'Option selected: [{option}]\n')

task_list = []

while True:
    show_header()
    print('''
    [1] Add task
    [2] List all tasks
    [0] Exit
''')

    option = input('Select an option between those 3: ')

    if option not in('0', '1', '2'):
        print('\n[Error] Invalid option! Try again...')
        time.sleep(2)
        continue

    clear_screen()

    if option == '1':
        while True:
            show_header(1)

            new_task = input('Type here your new task or [finish] to finish: ').strip()

            if new_task.lower() == 'finish':
                print('\nFinished!')
                time.sleep(2)
                break

            if not new_task:
                print('\nError! Tasks cannot be empty.')
                time.sleep(2)
                continue

            task_list.append(new_task)
            print('\nTask added successfully!')
            time.sleep(2)

    elif option == '2':
        while True:
            show_header(2)

            if not task_list:
                print('Your task list is empty!')
            else:
                for index, task in enumerate(task_list, start=1):
                    print(f'Task {index} - {task}')


            go_back = input('\nType "back" to go back to the main menu: ').strip()

            if go_back.lower() == 'back':
                print('\nGoing back to main menu...')
                time.sleep(2)
                break
            else:
                print('\nInvalid input! Please type "back" to go back.')
                time.sleep(2)

    elif option == '0':
        show_header(0)
        print('Bye! See you next time...')
        time.sleep(2)
        break
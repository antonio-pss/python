import actions
import models


def menu():
    print('1 - List All.')
    print('2 - List by Country.')
    print('3 - Search by title.')
    print('4 - Search by type.')
    print('0 - Leave.')


option: int
show = models.Show()
actions.ShowActions.load_shows()

while True:
    menu()
    option = int(input('Option: '))

    match option:
        case 1:
            actions.ShowActions.list_shows()
        case 2:
            actions.ShowActions.list_country(input('Country: '))
        case 3:
            actions.ShowActions.search_title(input('Title: '))
        case 4:
            actions.ShowActions.search_type(input('Type: '))
        case 0:
            break

    if option == 0:
        break

import actions
import models


def menu():
    print('1 - Add Vehicle.')
    print('2 - List Vehicles.')
    print('3 - List Vehicles by Brand.')
    print('4 - List Vehicles by Model.')
    print('5 - Average Vehicles price by brand.')
    print('0 - Leave')


option: int
vehicle = models.Vehicle()
actions.VehicleActions.load_vehicles()

while True:
    menu()
    option = int(input('Option: '))

    match option:
        case 1:
            vehicle.brand = str(input('Brand: '))
            vehicle.color = str(input('Color: '))
            vehicle.model = str(input('Model: '))
            vehicle.plate = str(input('Plate: '))
            vehicle.price = float(input('Price: '))
            actions.VehicleActions.add_vehicle(vehicle=vehicle)
            vehicle = models.Vehicle()
        case 2:
            actions.VehicleActions.list_all()
        case 3:
            actions.VehicleActions.list_brand(str(input('Brand: ')))
        case 4:
            actions.VehicleActions.list_model(str(input('Model: ')))
        case 5:
            average = actions.VehicleActions.average_brand(str(input('Brand: ')))
            print(f'Average: {average}')
        case 0:
            break

    if option == 0:
        break

actions.VehicleActions.save_vehicles()
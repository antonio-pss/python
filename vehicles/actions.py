import models
from typing import List

vehicles = list()


class VehicleActions:
    @staticmethod
    def load_vehicles():
        file = open('vehicles.txt', 'r')
        lines = file.readlines()
        columns = list()

        for item in lines:
            columns.append(item.split(';'))

        for item in columns:
            vehicles.append(models.Vehicle(item[0], item[1], item[2], item[3], float(item[4])))

    @staticmethod
    def save_vehicles():
        file = open('vehicles.txt', 'w')
        line: str
        for item in vehicles:
            line = f'{item.brand};{item.color};{item.model};{item.plate};{item.price};\n'
            file.write(line)

    @staticmethod
    def add_vehicle(vehicle: models.Vehicle):
        vehicles.append(vehicle)

    @staticmethod
    def list_all():
        for item in vehicles:
            print(f'Brand: {item.brand} | Color: {item.color} | Model: {item.model} '
                  f'| Plate: {item.plate} | Price: {item.price}')

    @staticmethod
    def list_brand(brand: str):
        for item in vehicles:
            if item.brand == brand:
                print(f'Brand: {item.brand} | Color: {item.color} | Model: {item.model} '
                      f'| Plate: {item.plate} | Price: {item.price}')

    @staticmethod
    def list_model(model: str):
        for item in vehicles:
            if item.model == model:
                print(f'Brand: {item.brand} | Color: {item.color} | Model: {item.model} '
                      f'| Plate: {item.plate} | Price: {item.price}')

    @staticmethod
    def average_brand(brand: str):
        average = 0.0
        number = 0
        for item in vehicles:
            if item.brand == brand:
                average += item.price
                number += 1
        return average/number

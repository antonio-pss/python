import models

shows = []


class ShowActions:
    @staticmethod
    def load_shows():
        file = open('netflix.csv', 'r', encoding="utf8")
        lines = file.readlines()
        lines.pop(0)

        columns = list()
        for line in lines:
            columns.append(line.split(','))

        for item in columns:
            shows.append(models.Show(s_id=item[0], s_type=item[1], title=item[2], country=item[5]))

    @staticmethod
    def list_shows():
        for item in shows:
            print(f'Show ID: {item.id} | Type: {item.type} | Title: {item.title} | Country: {item.country}')

    @staticmethod
    def list_country(country: str):
        for item in shows:
            if item.country == country:
                print(f'Show ID: {item.id} | Type: {item.type} | Title: {item.title} | Country: {item.country}')

    @staticmethod
    def search_title(title: str):
        for item in shows:
            if item.title == title:
                print(f'Show ID: {item.id} | Type: {item.type} | Title: {item.title} | Country: {item.country}')

    @staticmethod
    def search_type(s_type: str):
        for item in shows:
            if item.type == s_type:
                print(f'Show ID: {item.id} | Type: {item.type} | Title: {item.title}')

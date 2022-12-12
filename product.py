import pyshorteners
class Product():
    def __init__(self, name: str, url: str, comission: float, rating: float, count_rating: int, temperature: int):
        self.name = name
        try:
            shortener = pyshorteners.Shortener()
            self.url = shortener.tinyurl.short(url)
        except:
            self.url = url
        self.comission = comission
        self.rating = rating
        self.count_rating = count_rating
        self.temperature = temperature

    def log(self):
        print(f'Nome: {self.name}\nUrl: {self.url}\nRating: {self.rating}\nCount Rating: {self.count_rating}\nTemperature: {self.temperature}°\n\n')

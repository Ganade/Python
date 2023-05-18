from enum import property


class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    def give_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie('avengers - infinity war', 2018, 160)
avengers.give_likes()
print(f'Name: {avengers.name} - Year: {avengers.year} - Seasons: {avengers.duration} - Likes: {avengers.likes}')

supernatural = Series('Supernatural', 2005, 16)
supernatural.give_likes()
supernatural.name = 'Superman'
print(f'Name: {supernatural.name} - Year: {supernatural.year} - Seasons: {supernatural.seasons} - '
      f'Likes: {supernatural.likes}')

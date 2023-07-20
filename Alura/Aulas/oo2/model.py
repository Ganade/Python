from enum import property


class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self._year = year
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

    @property
    def year(self):
        return self._year

    def __str__(self):
        return f'Name: {self._name} - Year: {self._year} - Likes: {self._likes}'


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Name: {self._name} - Year: {self._year} - Likes: {self._likes} - Duration: {self.duration} min'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self._name} - Year: {self._year} - Likes: {self._likes} - Seasons: {self.seasons} '


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def listing(self):
        return self._programs

    def __len__(self):
        return len(self._programs)


avengers = Movie('avengers - infinity war', 2018, 160)
supernatural = Series('Superman', 2005, 16)
avatar = Movie('Avatar 2', 2022, 170)
smallvile = Series('Smallvile', 2003, 10)
supernatural.name = 'Supernatural'
supernatural.give_likes()
avatar.give_likes()
smallvile.give_likes()
supernatural.give_likes()
avengers.give_likes()

movies_and_series = [avengers, avatar, smallvile, supernatural]
weekend_playlist = Playlist('Weekend Playlist', movies_and_series)

print(f'length of Playlist "{weekend_playlist.name}": {len(weekend_playlist.listing)} items:')

for program in weekend_playlist:
    print(f'- {program}')

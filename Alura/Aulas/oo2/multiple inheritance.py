class Employee:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def register_hours(hours):
        print(f'Hours registered {hours}.')

    def show_tasks(self):
        print('Did a lot of work...')


class Caelum(Employee):
    def show_tasks(self):
        print('Did a lot of work, Caelumer')

    @staticmethod
    def search_monthly_courses(month=None):
        print(f'Showing courses - {month}' if month else 'Showing courses for this month')


class Alura(Employee):
    # def show_tasks(self):
    # print('Did a lot of work, Alurete!')
    @staticmethod
    def search_unanswered_questions():
        print('Showing unanswered forum questions')


class Hipster:
    def __init__(self):
        self.name = None

    def __str__(self):
        return f'Hipster, {self.name}'


class Junior(Alura):
    pass


class MidLevel(Alura, Caelum, Hipster):
    pass


jose = Junior("José")
jose.search_unanswered_questions()
jose.show_tasks()

luan = MidLevel('Luan')
luan.search_unanswered_questions()
luan.search_monthly_courses()

luan.show_tasks()

print(luan)

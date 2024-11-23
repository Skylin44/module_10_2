import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power, day = 0):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.day = day

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            self.enemy -= self.power
            self.day += 1

            print(f'{self.name}, сражается {self.day} день(дня)..., осталось {self.enemy} воинов.')
            time.sleep(1)
        print(f'{self.name}, одержал победу спустя {self.day} дней(дня)!')

time.time()
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')


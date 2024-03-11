import random
import concurrent.futures
import time


class Trapecia:
    def __init__(self, fudze1, fudze2, simagle):
        self.fudze1 = fudze1
        self.fudze2 = fudze2
        self.simagle = simagle

    def __str__(self):
        return f"ტრაპეციის სიმაღლეა{self.simagle} ფუძე1: {self.fudze1} ფუძე2 {self.fudze2}"

    def area(self):
        return 0.5 * (self.fudze2 + self.fudze1) / self.simagle

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __mod__(self, other):
        return self.area() / other.area()


class Otxkutxedi(Trapecia):
    def __init__(self, sigrdze, simagle):
        super().__init__(sigrdze, sigrdze, simagle)

    def area(self):
        return self.fudze1 * self.simagle

    def __str__(self):
        return f"ოთხკუთხედის სიგრძეა {self.simagle} და სიგანეა {self.fudze1}"


class Kvadrati(Otxkutxedi):
    def __init__(self, gverdi):
        super().__init__(gverdi, gverdi)

    def area(self):
        return self.fudze1 ** 2

    def __str__(self):
        return f"კვადრატის გვერდია {self.fudze1}"


def fartobis_gamotvla(figura):
    figura.area()


def threading_(figura):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor1:
        executor1.submit(fartobis_gamotvla, figura)


def main():
    start = time.time()
    digit_list = [[random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)] for _ in range(10)]
    lst = [Trapecia(*random.choice(digit_list)) for _ in range(50)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(threading_, lst)

    end = time.time()

    print(f"time {end - start}")


if __name__ == "__main__":
    main()

    # მხოლოდ პროცესით დაჭირდა  0.9650840759277344
    # ორივეს ერთად 0.7087452411651611
    # მხოლოდ ნაკადებით 0.0010001659393310547

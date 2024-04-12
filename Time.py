from random import randint
from typing import Optional


class Time:
    def __init__(self, hour: Optional[int] = 0, minute: Optional[int] = 0, second: Optional[int] = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __add__(self, other):
        total_seconds = self.second + other.second
        carry_minutes, seconds = divmod(total_seconds, 60)

        total_minutes = self.minute + other.minute + carry_minutes
        carry_hours, minutes = divmod(total_minutes, 60)

        hours = (self.hour + other.hour + carry_hours) % 24

        return Time(hours, minutes, seconds)

    def __sub__(self, other):
        total_seconds = self.second - other.second
        if total_seconds < 0:
            total_seconds = 60
            minutes -= 1
        else:
            minutes = 0

        total_minutes = self.minute - other.minute - minutes
        if total_minutes < 0:
            total_minutes += 60
            hours -= 1
        else:
            hours = 0

        total_hours = self.hour - other.hour - hours

        return Time(total_hours, total_minutes, total_seconds)


def main(h1, m1, s1, h2, m2, s2) -> None:
    t1 = Time(h1, m1, s1)
    t2 = Time(h2, m2, s2)

    print(f"Time 1: {t1.__str__()}")
    print(f"Time 2: {t2.__str__()}")

    add_time = t1 + t2
    print(f"Add time result {add_time.__str__()}")

    subtract_time = t1 - t2
    print(f"Subtract time result {subtract_time.__str__()}")

    print()


def generate_hour():
    # bound it to 11 cause of addition
    # ideally it should be 23
    return randint(0, 12)


def generate_minute():
    return randint(0, 59)


def generate_seconds():
    return randint(0, 59)


def swap(value1, value2):
    value1, value2 = value2, value1

    return value1, value2


if __name__ == "__main__":
    for _ in range(10):
        h1 = generate_hour()
        m1 = generate_minute()
        s1 = generate_seconds()

        h2 = generate_hour()
        m2 = generate_minute()
        s2 = generate_seconds()

        if h1 < h2:
            h1, h2 = swap(h1, h2)

        if m1 < m2:
            m1, m2 = swap(m1, m2)

        if s1 < s2:
            s1, s2 = swap(s1, s2)

        main(h1, m1, s1, h2, m2, s2)

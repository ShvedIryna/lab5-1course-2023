"""
lab5.py_corrected.py
"""


class RaceHorse:
    """
    class
    """

    def __init__(self, speed, age, name, place_in_race=None):
        """
        init
        :param speed:
        :param age:
        :param name:
        :param place_in_race:
        """
        self.__speed = speed
        self.__age = age
        self.__name = name
        self.__place_in_race = place_in_race

    def get_speed(self):
        """
        get_speed
        :return:
        """
        return self.__speed

    def get_age(self):
        """
        get_age
        :return:
        """
        return self.__age

    def get_name(self):
        """
        get_name
        :return:
        """
        return self.__name

    def get_place_in_race(self):
        """
        get_place_in_race
        :return:
        """
        return self.__place_in_race

    def set_place_in_race(self, place):
        """
        set_place_in_race
        :param place:
        :return:
        """
        self.__place_in_race = place


class Race:
    """
    race
    """

    def __init__(self):
        """
        init
        """
        self.participants = []

    def add__participant(self, horse):
        """
        add__participant
        :param horse:
        :return:
        """
        if 3 <= horse.get_age() <= 7:
            self.participants.append(horse)

    def remove_participant(self, horse):
        """
        remove_participant
        :param horse:
        :return:
        """
        if horse in self.participants:
            self.participants.remove(horse)

    def sort_participants_by_speed(self):
        """
        sort_participants_by_speed
        :return:
        """
        self.participants.sort(key=lambda x: x.get_speed(), reverse=True)

    def assign_places_in_race(self):
        """
        assign_places_in_race
        :return:
        """
        self.sort_participants_by_speed()
        for i in range(min(3, len(self.participants))):
            self.participants[i].set_place_in_race(i + 1)

    def avr_age(self):
        """
        avr_age
        :return:
        """
        if not self.participants:
            return None

        average_age = sum(horse.get_age() for horse in self.participants) / len(self.participants)

        winner = max(self.participants, key=lambda x:
        x.get_speed() + abs(x.get_age() - average_age))
        return winner
        


def main():
    """
    main
    :return:
    """
    horse1 = RaceHorse(21, 4, "Andre")
    horse2 = RaceHorse(20, 6, "Inde")
    horse3 = RaceHorse(18, 4, "Fore")
    horse4 = RaceHorse(22, 7, "Mant")

    race = Race()
    race.add__participant(horse1)
    race.add__participant(horse2)
    race.add__participant(horse3)
    race.add__participant(horse4)

    race.assign_places_in_race()

    for participant in race.participants:
        print(
            f"{participant.get_name()} - Speed:"
            f" {participant.get_speed()},"
            f" Age: {participant.get_age()},"
            f"Place in Race: {participant.get_place_in_race()}"
        )

    winner = race.avr_age()
    if winner:
        print(f"The winner is {winner.get_name()} with a speed of {winner.get_speed()}")
    else:
        print("No participants in the race.")


if __name__ == '__main__':
    main()

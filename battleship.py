import random

class Battleship:
    ship_coords: list = []
    allowed_guesses: int = 20
    guesses_made: int = 0
    hot_upper_limit: int = 2
    hot_lower_limit: int = 1
    warm_upper_limit: int = 4
    warm_lower_limit: int = 3

    def __init__(self, *args, **kwargs):
        while True:
            ship_one = (random.randint(0,7), random.randint(0,7))
            ship_two = (random.randint(0, 7), random.randint(0, 7))
            if ship_one != ship_two:
                break
        self.ship_coords.append(ship_one)
        self.ship_coords.append(ship_two)

    def take_input(self):
        # TODO: add better exception handling here, make e.g. 9,9 an invalid input
        while True:
            raw_guess = input('Enter a comma-separated co-ordinate in the form "1,2" ')
            if len(raw_guess) == 3:
                break
            else:
                print("Invalid input")
        return raw_guess

    def process_input(self, raw_guess):
        guess = raw_guess.split(',')
        self.guesses_made += 1
        # resolve the offset of the list index starting at 0 but the user input starting at 1
        return (int(guess[0]) - 1, int(guess[1]) - 1)

    def determine_hit(self, guess_x, guess_y):
        if (guess_x, guess_y) in self.ship_coords:
            print("You hit a ship!")
            self.ship_coords.remove((guess_x, guess_y))
            return True
        return False

    def determine_proximity(self, guess_x, guess_y):
        shortest_distance = 999
        for ship_coord in self.ship_coords:
            proximity = abs(guess_x - ship_coord[0]) + abs(guess_y - ship_coord[1])
            if proximity < shortest_distance:
                shortest_distance = proximity
        if shortest_distance <= self.hot_upper_limit and shortest_distance >= self.hot_lower_limit:
            print("Hot")
        elif shortest_distance <= self.warm_upper_limit and shortest_distance >= self.warm_lower_limit:
            print("Warm")
        else:
            print("Cold")

    def determine_ships_destroyed(self):
        if len(self.ship_coords) != 0:
            print((str(len(self.ship_coords))) + " Ships still remain")
            return False
        else:
            print("All ships cleared")
            return True

    def determine_guesses_used(self):
        if self.guesses_made == self.allowed_guesses:
            print("All guesses used")
            return True
        else:
            print(str(self.allowed_guesses - self.guesses_made) + " guesses remain")
            return False

    def play(self):
        print('Start Battleship, grid is 8x8')
        game_ended = False
        while not game_ended:
            raw_guess = self.take_input()
            coord_x, coord_y = self.process_input(raw_guess)
            hit = self.determine_hit(coord_x, coord_y)
            if not hit:
                self.determine_proximity(coord_x, coord_y)
            game_ended = self.determine_ships_destroyed() or self.determine_guesses_used()
        exit(0)

if __name__ == "__main__":
    battleship = Battleship()
    battleship.play()




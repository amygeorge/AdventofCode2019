class Fuel:
    def __init__(self, mass):
        self.mass = mass
        self.fuel = 0

    def calc_fuel(self):
        self.fuel = int(self.mass/3-2)

    def calculate_fuel(self):
        self.calc_fuel()
        temp = self.fuel
        sum = self.fuel
        while temp > 0:

            if int(temp/3-2) > 0:
                sum += int(temp/3-2)
                temp = int(temp/3-2)
            else:
                temp = 0
        return sum

    def say_state(self):
        print("I need {} litres of gas:".format(self.fuel))

    def calc_all(self, fuel_list):
            fuel_sum = 0
            for line in fuel_list:
                curr_fuel = Fuel(float(line))
                fuel_sum += curr_fuel.calculate_fuel()
                curr_fuel.say_state()
            print("I need a total of {} litres of gas:".format(fuel_sum))
            return fuel_sum

class File:
    def __init__(self, text):
        self.text = text

    def read_file(self):
        with open(self.text) as f:
            text_list = f.readlines()
        return text_list

if __name__ == '__main__':
       module = Fuel(0)
       text = File('Mass.txt')
       module.calc_all(text.read_file())
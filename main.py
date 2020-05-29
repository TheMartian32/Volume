"""
========================================
Calculates the volume of certain objects
========================================
"""

from fractions import Fraction

class repeat_question():
    def ask_for(self, prompt, error_msg=None, _type=None):
        """ While the desired prompt is not given, it repeats the prompt. """
        while True:
            inp = input(prompt).strip()
            if not inp:
                if error_msg:
                    print(error_msg)
                continue

            if _type:
                try:
                    inp = _type(inp)
                except ValueError:
                    if error_msg:
                        print(error_msg)
                    continue
            return inp


ask = repeat_question()


class volume():
    def __init__(self, base=0, height=0, fraction=0, base_length=0, base_height=0):
        self.base = base
        self.height = height
        self.fraction = fraction
        self.base_length = base_length
        self.base_height = base_height

    def vol(self):
        print('\n----------------------------')
        # * Asks the user if they are using a fraction or not.
        using_frac = ask.ask_for(
            'Are you using a fraction? (Y/N): ', 'Not an answer.', str)

        # * Inputs to determine the area of a base.
        base_l = self.base_length = ask.ask_for(
            'What is the base length?: ', 'Not a base length', float)
        base_h = self.base_height = ask.ask_for(
            'What is the base height?: ', 'Not a base height', float)
        self.height = ask.ask_for(
                'What is the height?: ', 'Not a height', float)
        print('----------------------------')

        # * Area of a base
        base_area = base_l*base_h
        if using_frac[0] == 'y':
            frac = ask.ask_for(
                'Please input the fraction you are using: ', 'Not a decimal')
            print('----------------------------')
            f = Fraction(frac)
            volume_calculation = f*base_area*self.height
            return volume_calculation

        if using_frac[0] == 'n':
            volume_calculation = base_area*self.height
            return volume_calculation


v = volume()


class calc():
    """
    This class is responsible for the calculations of volume
    """

    def __init__(self, base_length=0, base_height=0, height=0):
        self.base_length = base_length
        self.base_height = base_height
        self.height = height

    def vol_rect_prism(self):

        volume = v.vol()

        return print(f'\nThe volume is {volume}.')
    def vol_tri_prism(self):
        volume = v.vol()
        return print(f'\nThe volume is {volume}.')

    def calc_type(self):

        while True:
            result = ask.ask_for(
                '\nWhat calculation are you making?: ', 'Not supported.', str)

            if result in ['v', 'volume', 'vol']:
                area_type = ''
                print('\n----------------------------')
                area_type = ask.ask_for(
                    'What object are you calculating the volume for?: ', 'Not supported', str)
                print('----------------------------')
                if area_type in ['r', 'rect', 'rectangular prism']:
                    c.vol_rect_prism()
                    break

            else:
                print('Not supported.')


c = calc()

if __name__ == "__main__":
    c.calc_type()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        repeat = input(
            '\nWould you like to repeat the program? (Y/N): ').lower()
        if repeat[0] == 'y'.lower():
            c.calc_type()
            continue
        if repeat[0] == 'n'.lower():
            break

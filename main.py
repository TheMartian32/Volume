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
        """This is the main method responsible for calculating the volume of the supported objects.

        Returns:
            Float/Int -- Using the parameters the user provides, it calculates the volume.
        """

        print('\n----------------------------')

        # * Asks the user if they are using a fraction or not.
        using_frac = ask.ask_for(
            'Are you using a fraction? (Y/N): ', 'Not an answer.', str)

        # * Inputs to determine the area of a base.
        base_l = self.base_length = ask.ask_for(
            'What is the base length?: ', 'Not a base length', float)

        base_h = self.base_height = ask.ask_for(
            'What is the base height?: ', 'Not a base height', float)

        # * Inputs to determine the height of the object.
        self.height = ask.ask_for(
            'What is the height?: ', 'Not a height', float)

        print('----------------------------')

        # * Asks the user if the object is or is not a triangular pyramid.
        is_tri = ask.ask_for(
            'Is the object a triangular pyramid? (Y/N): ', 'Not an answer.', str)

        # * Area of a base
        base_area = base_l*base_h

        # * Asks the user if they are using a fraction, then if they are, uses the fraction module to convert the input to a fraction.
        if using_frac[0] == 'y':
            frac = ask.ask_for(
                'Please input the fraction you are using: ', 'Not a fraction', Fraction)

            print('----------------------------')

            # * Asks if the object is a triangle or is not a triangle.

            if is_tri[0] == 'y':
                f = Fraction(frac)
                volume_calculation = f*0.5*base_area*self.height
                return volume_calculation

            # * If it is not a triangle, this code executes.
            else:
                f = Fraction(frac)
                volume_calculation = f*base_area*self.height
                return volume_calculation

        if using_frac[0] == 'n':
            volume_calculation = base_area*self.height
            return volume_calculation


v = volume()


class calc():


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

    def vol_pyramid(self):
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

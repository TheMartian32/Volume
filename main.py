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
    """Calculates the volume of a given object.

    Returns:
        Float/Int -- Based off what the user inputs into the program it outputs a floating point number or an integer.
    """

    # * Setting up parameters that almost every object will need.
    def __init__(self, base=0, height=0, fraction=0, base_length=0, base_height=0):
        """This is the basic format for just about every object that the vol method will use to calculate volume.

        Keyword Arguments:
            base {int/float} -- Length of object (default: {0})
            height {int/float} -- Height of object (default: {0})
            fraction {int/float} -- If there is a fraction, this is the parameter. (default: {0})
            base_length {int/float} -- Length of a base (default: {0})
            base_height {int/float} -- Height of a base (default: {0})
        """
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

        # * Asks the user if the object is or is not a triangular pyramid.
        is_tri = ask.ask_for(
            'Is the object a triangular pyramid? (Y/N): ', 'Not an answer.', str)

        # * Inputs to determine the area of a base.
        base_l = self.base_length = ask.ask_for(
            'What is the base length?: ', 'Not a base length', float)

        base_h = self.base_height = ask.ask_for(
            'What is the base height?: ', 'Not a base height', float)

        # * Inputs to determine the height of the object.
        self.height = ask.ask_for(
            'What is the height?: ', 'Not a height', float)

        print('----------------------------')

        # * Area of a base
        base_area = base_l*base_h

        # * Asks the user if they are using a fraction, then if they are, uses the fraction module to convert the input to a fraction.
        if using_frac[0] == 'y':
            frac = ask.ask_for(
                'Please input the fraction you are using: ', 'Not a fraction', Fraction)

            print('----------------------------')

            # * Asks if the object is a triangle or is not a triangle.

            if is_tri[0] == 'y':
                # using the fraction module, if the user is using a fraction, in which case they have too, it passes the input into a Fraction method.
                f = Fraction(frac)
                # * Formula for triangular pyramid
                volume_calculation = f*0.5*base_area*self.height

                return print(f'\nThe volume is {volume_calculation} units cubed.')

            # * If it is not a triangle, this code executes.
            else:
                f = Fraction(frac)
                # * Formula for objects that still require a fractional component.
                volume_calculation = f*base_area*self.height

                return print(f'\nThe volume is {volume_calculation} units cubed.')

        if using_frac[0] == 'n':

            # * Formula for something like a rectangular prism.
            volume_calculation = base_area*self.height

            return print(f'\nThe volume is {volume_calculation} units cubed.')


v = volume()


class ResultsInputs():

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
                    v.vol()
                    break

            else:
                print('Not supported.')


ri = ResultsInputs()

if __name__ == "__main__":
    ri.calc_type()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        repeat = input(
            '\nWould you like to repeat the program? (Y/N): ').lower()
        if repeat[0] == 'y'.lower():
            ri.calc_type()
            continue
        if repeat[0] == 'n'.lower():
            break

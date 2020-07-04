"""
========================================
Calculates the volume of certain objects
========================================
"""
from fractions import Fraction
from rich.console import Console
from rich.theme import Theme
from rich import print

#* Custom theme for rich
custom_theme = Theme({
    "good": "green",
    "bad": "bold red"
})

console = Console(theme=custom_theme)


class UI_Inputs():
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

    def colored_input(self, string1='', string2='', string3='', color1='green', color2='red', divider='', has_input=False, input_msg='', _type=None, error_msg=None):
        """
        prints out a colored and formatted print statement using the rich python library
        and can use input but it currently doesnt work.

        Args:
            string1 (str, optional): What you want the user to see, e.g the print statement. Defaults to ''.
            string2 (str, optional): the first part of the text to be colored. Defaults to ''.
            string3 (str, optional): the second part of the text to be colored. Defaults to ''.
            color1 (str, optional): first color. Defaults to 'green'.
            color2 (str, optional): second color. Defaults to 'red'.
            divider (str, optional): something to divide the colors. Defaults to ''.
            has_input (bool, optional): If you want input set to True. Defaults to False.
            input_msg (str, optional): input messsage, best left to empty string. Defaults to ''.
            _type ([type], optional): type you want to check for in input. Defaults to None.
            error_msg ([type], optional): error message if the type is not correct. Defaults to None.

        Returns:
            [type]: [description]
        """
        # * message for the user to see
        msg1 = print(f'{string1}')

        # * the colored part of the text
        msg2 = print(
            f'[{color1}]{string2}[/{color1}]{divider}[{color2}]{string3}[/{color2}]')

        # * Checks if the input is True
        if has_input == True:
            inp = ask.ask_for(f'{input_msg}')
        return msg1, msg2

    def calc_type(self):
        """
        While the user does not give v, volume, or vol,
        the prompt repeats.
        """

        while True:
            print(
                'Type [bold cyan]v[/bold cyan] [bold]or[/bold] [bold cyan]V[/bold cyan]:')
            result = ask.ask_for(
                ':', 'Not supported.', str)

            if result in ['v', 'volume', 'vol', 'V']:
                v.vol()
                break
            else:
                break


ask = UI_Inputs()


class Volume():
    """
    Calculates the volume of a given object.

    Returns:
        Float/Int -- Based off what the user inputs into the program it outputs a floating point number or an integer.
    """

    # * Setting up parameters that almost every object will need.
    def __init__(self, base=0, height=0, fraction=0, base_length=0, base_height=0):
        """
        This is the basic format for just about every object that the vol method will use to calculate volume.

        / in this case means 'or'

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
        """
        This is the main method responsible for calculating the volume of the supported objects.

        Returns:
            Float/Int -- Using the parameters the user provides, it calculates the volume.
        """

        print('\n----------------------------')

        # * Asks the user if they are using a fraction or not.
        frac_question = ask.colored_input(
            string1='\nAre you using a fraction?', string2='Y', string3='N', divider='/')
        using_frac = ask.ask_for(':', 'Not an answer', str)

        # * Asks the user if the object is or is not a triangular pyramid.
        tri_question = ask.colored_input(string1='\nIs the object a triangular pyramid?', string2='Y',
                                         string3='N', divider='/')
        is_tri = ask.ask_for(':', 'Not an answer', str)

        # * Inputs to determine the area of a base.
        base_l = self.base_length = ask.ask_for(
            '\nBase length: ', 'Not a base length', float)

        base_h = self.base_height = ask.ask_for(
            '\nBase height: ', 'Not a base height', float)

        # * Inputs to determine the height of the object.
        h = self.height = ask.ask_for(
            '\nHeight: ', 'Not a height', float)

        print('----------------------------')

        # * Area of a base
        base_area = base_l*base_h

        # * Asks the user if they are using a fraction, then if they are, uses the fraction module to convert the input to a fraction.
        if using_frac[0] == 'y':
            frac_question = ask.colored_input(
                string1='Please input the fraction you are using (Here is an example) ', string2='1', string3='3', divider='/')
            is_frac = ask.ask_for(':', 'Not an answer', str)

            print('----------------------------')

            # * Asks if the object is a triangle or is not a triangle.

            if is_tri[0] == 'y':
                # using the fraction module, if the user is using a fraction, in which case they have too, it passes the input into a Fraction method.
                f = Fraction(is_frac)
                # * Formula for triangular pyramid
                volume_calculation = f*0.5*base_area*h

                return print(f'The volume is {volume_calculation} units cubed.')

            # * If it is not a triangle, this code executes.
            else:
                f = Fraction(is_frac)
                # * Formula for objects that still require a fractional component.
                volume_calculation = f*base_area*h

                return print(f'\nThe volume is {volume_calculation} units cubed.')

        if using_frac[0] == 'n':

            # * Formula for something like a rectangular prism.
            volume_calculation = base_area*h

            return print(f"\nThe volume is {volume_calculation} units cubed.")


v = Volume()

if __name__ == "__main__":
    ask.calc_type()

    repeat = ''
    while True:

        # * Asks to repeat the script.
        print(
            '\nWould you like to [bold green]repeat[/bold green] the program?')
        print('[green]Y[/green]/[red]N[/red]:')

        repeat = ask.ask_for(':', 'not an answer', str)

        if repeat[0] == 'y'.lower():
            ask.calc_type()
            continue
        if repeat[0] == 'n'.lower():
            break

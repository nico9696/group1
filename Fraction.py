class Fraction(object):

    slash_reached = False
    temp_numerator = ""
    temp_denominator = ""
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            for i in numerator:
                if i == "-":
                    if slash_reached == False:
                        temp_numerator = "-"
                    else:
                        temp_denominator = "-"
                elif i in "1234567890":
                    if slash_reached == False:
                        temp_numerator += i
                    else:
                        temp_denominator += i
                elif i == "/":
                    slash_reached = True

        numerator = int(temp_numerator)
        denominator = int(temp_denominator)

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
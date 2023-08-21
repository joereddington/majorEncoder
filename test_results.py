#TODO 
import set_generator

def confirm(number, text):
    number=number.replace(".","")
    words=text.lower().split()
    result_number = ''.join(set_generator.convert_to_integer(word) for word in words)
    if number==result_number:
        print("match")
    else:
        print("fail")

# Speed of light 
confirm("299792", "Winged Tigon")
confirm("299792", "indigo octagon")
confirm("299792", "Candied Takedown")

# Boltzmann constant 
confirm("1.380649", "calm cheeseboard")

# Newtonican Constant of graviation
confirm("6.67430", "upbeat rock music")
confirm("6.67430", "happy thermos")
confirm("6.67430", "pubic tiramisu")
confirm("6.67430", "epic bathroom ooze")




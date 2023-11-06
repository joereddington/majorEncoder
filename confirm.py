import set_generator


#This file confirms that the existing keys we have work for the numbers we have - it's to avoid typos. 
# It also generates some of the latex code for the book


def confirm(number, text):
    number=number.replace(".","")
    words=text.lower().split()
    result_number = ''.join(set_generator.convert_to_integer(word) for word in words)
    if number==result_number:
        print("match")
    else:
        print("fail")

def to_latex(text):
    return_me="\\begin{enumerate}\n"
    return_me+="\\item Start with `{}'\n".format(text)
    replace_dict = {
        'l': '1',
        'n': '2',
        'm': '3',
        'r': '4',
        'f': '5',
        'v': '5',
        'b': '6',
        'p': '6',
        't': '7',
        'ch': '8',
        'sh': '8',
        'g': '9',
        's': '0',
        'd': '9',
        'z': '0'
    }
    for key, value in replace_dict.items():
        text = text.replace(key, value)
    return_me+="\\item Replace the Major System letters to get start with `{}'\n".format(text)
    # Remove all non-numeric characters

    result = ''.join([char for char in text if char.isdigit()])
    return_me+="\\item Remove the unused letters we get: {}\n".format(result)
    result = result[:1] + '.' + result[1:]
    return_me+="\\item Replace the decimal point to get: {}\n".format(result)
    return_me+="\\end{enumerate}\n"
    return return_me

# Speed of light 
confirm("299792", "Winged Tigon")
confirm("299792", "indigo octagon")
confirm("299792", "Candied Takedown")

# Planck Constant
confirm("6.62607015","cobweb in books with saliva")
confirm("6.62607015","happen because it's life")

# Reduced Planck Constant 
# NOT treid

# Boltzmann constant 
confirm("1.380649", "calm cheeseboard")

# Newtonican Constant of graviation
confirm("6.67430", "upbeat rock music")
confirm("6.67430", "happy thermos")
confirm("6.67430", "pubic tiramisu")
confirm("6.67430", "epic bathroom ooze")
print(to_latex("happy thermos"))

#[O[ICosmological constant
confirm("1.089","clockwise chad")
confirm("1.089","lazy eyeshadow")
confirm("1.089","Jealous cowshed")


#stefan-boltzmann constant 
confirm("5.670374419","Fab task metric world")
confirm("5.670374419","Fab tusk metric world")


# Electron mass
confirm("9.1093837015","Glazed mash comatose elf")
confirm("9.1093837015","Glazed mash comatose elf")
confirm("9.1093837015","Highly sexed amish meet sea wolf")

# Proton Mass 
confirm("1.67262192369","albeit one pencil had numbed") 
confirm("1.67262192369","Whaleboat napkin hooligan jumped") 



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

print("Speed of light")
confirm("299792", "Winged Tigon")
confirm("299792", "indigo octagon")
confirm("299792", "Candied Takedown")



print("Planck Constant")
confirm("6.62607015","cobweb in books with saliva")
confirm("6.62607015","happen because it's life")
confirm("6.62607015","bee hobnobs itself") # Brute recursive 

print("Reduced Planck Constant")
confirm("1.054571817","Elusive refutal chocolate") 
confirm("1.054571817","Exclusive roof-tool chocolate") 

# 1.25663706212  Vacuum magnetic pereability  - checked with looping recusion brute

# 376.730313668 Characteristic impedance of vacuum checked with looping recusion brute
# Boltzmann constant 
confirm("1.380649", "calm cheeseboard")

# Newtonican Constant of graviation
confirm("6.67430", "upbeat rock music")
confirm("6.67430", "happy thermos")
confirm("6.67430", "pubic tiramisu")
confirm("6.67430", "epic bathroom ooze")
print(to_latex("happy thermos"))


# Coulomb Constant 
confirm("8.9875517923", "Chad shut afflicted cinema")  
confirm("8.9875517923", "She headshot afflicted enemy")  

#Cosmological constant
confirm("1.089","clockwise chad")
confirm("1.089","lazy eyeshadow")
confirm("1.089","Jealous cowshed")


#stefan-boltzmann constant 
confirm("5.670374419","Fab task metric world")
confirm("5.670374419","Fab tusk metric world")
confirm("5.670374419","Hoofbeat smother world")

#First radiation constant 
confirm("3.741771852", "materiality 'til' shaven") 
# At a particular university you can use 'matriculate' 



#First radiation constant for spectral radiance 
confirm("1.191042972","Illegalize orangutan") 

# Second radiation constant 
confirm("1.438776877","Alarm chatty bushtit")

print("Wien wavelength displacement law constant") 
confirm("2.897771955","unwashed kitty-cat laid-off") 

# 5.878925757  wien 
print("Wien frequency displacement law constant") 

confirm("5.878925757","fish watched unfit feet")


# 3.002916077 wien 
print("Wien entropy displacement law constant") 
confirm("3.002916077","messianic goalpost cat") 

# 1.602176634 elementary charge 



print("Conductance quantum ")
confirm("7.748091729","Hot thrushes gloating") 

print("invest conductance quantum")
confirm("12906.40372","liking escapers hometown")
confirm("12906.40372","landscape horsemeat ink")
confirm("12906.40372","Landscaper cosmetician")

print("von Klizing constant") 
confirm("25812.80745","knavish lunches thive") 



print("magnetic flux quantum") 
confirm("2.067833848","inspect chummy church") 

print("inverse find-structure constant") 
confirm("137.035999084","acclimatise movie eggheads choir") 


# Electron mass
confirm("9.1093837015","Glazed mash comatose elf")
confirm("9.1093837015","Glasgow moo checkmates elf") 
confirm("9.1093837015","Highly sexed amish meet sea wolf")

# Proton Mass 
confirm("1.67262192369","albeit one pencil had numbed") 
confirm("1.67262192369","Whaleboat napkin hooligan jumped") 

# Neutron Mass 
confirm("1.67492749804", "Cleopatra decentered chaser") 
#Note - is that the amerian spelling


# Tau mass 
confirm("3.16754","Mail beautifier")

# Top quark mass 
confirm("3.0784", "Ham Switcher") 

# W-to-Z mass ratio 
confirm("0.88153","Sushi shelf mac") 

#weak mixing angle 
confirm("0.22290","scannings")


# bohn magneton
confirm("9.2740100783","headhunters closest chum")


# nuclear magneton 
confirm("5.0507837461","evasive scotch metacarpal") 


#classial electon radius 
confirm("2.8179403262","unshackle outdoorsmn pony") 


#Thomson cross section :( 


print("Bohr radius")
confirm("5.29177210903","fondle quotational sadism") 
confirm("5.29177210903","vexingly taxational sadism") 


print("Hartree energy")
confirm("4.3597447222071","Remove deterioration on newcastle")

print("Rydberg unit of energy")


print("Rydberg constant")

print("Fermi coupling constant")
confirm("1.1663787","wallop bee matchete" )
print("Avogadro constant")
confirm("6.02214076","bison concealers tape")
confirm("6.02214076","poison cancelers tuba") 



print("molar gas constant")

print("Faraday constant")
print("molar Planck constant")
confirm("   3.9903127128934314","medicaid simulant clinched my airmailer")
confirm("   3.9903127128934314","medicaid simulant clinched homeroom liar")
print("atomic mass of carbon-12")
confirm("1.99264687992","lego kidnap crapshoot guidance")
confirm("1.99264687992","'Aladdin burp!' shouted dan!")

# There are better ways of remembering modar mass but... 
print("molar mass of carbon-12")
confirm("11.9999999958","ill-judged goody-goody hogfish") 
confirm("11.9999999958","ill-judged giddy dogfish") 

print("atomic mass constant")
print("molar mass constant")
print("molar volume of silicon")
confirm("1.205883199","Aliens fish chemical dog") 
print("hyperfine transition frequency of 133Cs")
confirm("9192631770","golden bee omelettes") 

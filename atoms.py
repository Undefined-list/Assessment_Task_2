#all of this is seperated into a module so that the other code does not get too cluttered/confusing, as well as this code only being proccesses that involve the atoms.
class Atoms:
    #creates a class to make atoms
    def __init__(self, name, weight, charge, symbol):
        self.weight = weight
        self.charge = charge
        self.symbol = symbol
        self.name = name
    #holds all of the information about an atom that will be needed for future use
class NonMetals(Atoms):
    #a subclass of atoms to hold info useful to naming.
    def __init__(self, name, weight, charge, symbol, sufix_name):
        super().__init__(name, weight, charge, symbol)
        self.sufix_name = sufix_name
    def Balence(self, Positive):
        Negativecharge = self.charge * -1
    #making negative charge into an int that can be directly compared with the positive charge
        if Negativecharge == Positive.charge:
            return f"{Positive.symbol} {self.symbol}"
            #returns the equation if they have the exact same charge
        elif Negativecharge > Positive.charge:
            factor = Negativecharge%Positive.charge
            #used to tell if the positive charge fits exactly into the Negative charge
            divisor = Negativecharge/Positive.charge
            if factor == 0:
                #instantly returns the equation
                return f"{Positive.symbol} {int(divisor)} {self.symbol}"
            else:
                for x in range(1, 5):
                    for y in range(1, 5):
                        pos = Positive.charge * y
                        neg = Negativecharge * x
                        is_it_balence = neg / pos
                        #uses compounding for statements to get every combination of integers between 1 and 5,  and then uses that to multiply the charges until they are balenced
                        if is_it_balence == 1:
                            return f"{Positive.symbol} {y} {self.symbol} {x}"
        elif Positive.charge > Negativecharge:
            factor = Positive.charge%Negativecharge
            divisor = Positive.charge/Negativecharge
            if factor == 0:
                return f"{Positive.symbol} {self.symbol} {int(divisor)}"
            else:
                for x in range(1, 5):
                    for y in range(1, 5):
                        pos = Positive.charge * y
                        neg = Negativecharge * x
                        is_it_balence = pos / neg  
                        if is_it_balence == 1:
                            return f"{Positive.symbol} {y} {self.symbol} {x}"
                        #repeated code, but oposite purpose, if positive is bigger than negative
Hydrogen = Atoms("Hydrogen", 1.008, 1, "H")
Helium = Atoms ("Helium", 4.0026, 0, "He")
Lithium = Atoms("Lithium", 6.94, 1, "Li")
Beryllium = Atoms("Berylium", 9.0122, 2, "Be")
Boron = Atoms("Boron", 10.81, 3, "B")
Carbon = NonMetals("Carbon", 12.011, -4, "C", "carbide")
Nitrogen = NonMetals("Nitrogen", 14.007, -3, "N", "nitride")
Oxygen = NonMetals("Oxygen", 16, -2, "O", "oxide")
Fluorine = NonMetals("Fluorine", 18.998, -1, "F", "flouride")
Neon = Atoms("Neon", 20.18, 0, "Ne")
Sodium = Atoms("Sodium", 22.99, 1, "Na")
Magnesium = Atoms("Magnesium", 24.305, 2, "Mg")
Aluminium = Atoms("Aluminium", 26.982, 3, "Al")
Silicon = Atoms("Silicon", 28.085, 4, "Si")
Phosphorus = NonMetals("Phosphorus", 30.974, -3, "P", "phosphide")
Sulfur = NonMetals("Sulfur", 32.06, -2, "S", "sulfide")
Chlorine = NonMetals("Chlorine", 35.45, -1, "Cl", "chloride")
Argon = Atoms("Argon", 39.948, 0, "Ar")
#first 3 periods defined with all info
Full_list = (Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon, Sodium, Magnesium, Aluminium, Silicon, Phosphorus, Sulfur, Chlorine, Argon)
def naming(atomiceq):
    spliteq = atomiceq.split(" ")
    #splits the inputted atomic eq into a list
    for x in Full_list:
        if len(spliteq)== 4:
            if x.symbol == spliteq[0]:
                positive_name = x.name
            if x.symbol == spliteq[2]:
                negative_name = x.sufix_name
        #checks length of list so no index error, and then checks symbol compared to placement of it based on the lengs of the list.
        if len(spliteq)== 3:
            if x.symbol == spliteq[0]:
                positive_name = x.name
            if x.symbol == spliteq[2] or x.symbol == spliteq[1]:
                negative_name = x.sufix_name    
            
        if len(spliteq)== 2:
            if x.symbol == spliteq[0]:
                positive_name = x.name
            if x.symbol == spliteq[1]:
                negative_name = x.sufix_name
    Full_name = f"{positive_name} {negative_name}"
    return Full_name
#returns the proper name, this will need to be iterated apon in further versions.

import flet as ft
import atoms
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#allows use of subscript numbers, used when doing the formula
def main(page: ft.Page):
    page.title = "Balencing Basic Diatomic Ionic Compounds"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    class Dropdowns_maker(ft.Dropdown):
    #simplifying the creation of dropdowns, since there is more than one.
        def __init__(self, name, description, change):
            super().__init__()
            #this is the creation of a subclass, but we do not know the properties of the original.
            self.label = name
            self.hint_text = description
            self.options = []
            self.on_change= change
    def creatingdropdowns(Dropd):
    #simplifies adding a large amount of options into a dropdown
            for x in atoms.Full_list:
                if Dropd.label == "Negative Element":
                #if the dropdown is this specific dropdown, it will only add certain values into the dropdown.
                    if x.charge < 0:
                        Dropd.options.append(ft.dropdown.Option(x.name))
                if Dropd.label == "Positive Element":
                    if x.charge > 0:
                        Dropd.options.append(ft.dropdown.Option(x.name))
    def changed_results(e):
        if Negativeelement.value == neg_none:
             T.value = "Please select a negative element."
        elif Positiveelement.value == pos_none:
             T.value = "Please select a positive element."
             #all of this is just error handling.
        else: 
             for y in atoms.Full_list:
                if y.name == Negativeelement.value:
                    Negative_element = y
                if y.name == Positiveelement.value:
                    Positive_element = y
                    #all of this uses a for loop to search through the whole list of elements
             atomic_equation = Negative_element.Balence(Positive_element)
             Name_of_formula = atoms.naming(atomic_equation)
             T.value = f"The name of the diatomic equation you have made is {Name_of_formula}. It's equation is {atomic_equation.replace(" ", "").translate(SUB)}."
        page.update()
    Negativeelement = Dropdowns_maker("Negative Element", "Negative charge", changed_results)
    Positiveelement = Dropdowns_maker("Positive Element", "Positive Charge", changed_results)
    creatingdropdowns(Negativeelement)
    creatingdropdowns(Positiveelement)
    atoms_content = ft.Row(
        alignment= ft.MainAxisAlignment.CENTER,
        controls= [ 
            Positiveelement,
            ft.Icon(name= ft.icons.ADD_ROUNDED, color=ft.colors.LIGHT_BLUE_ACCENT_200),
            Negativeelement,
        ],
     spacing= 10,
     #placing everything into a neat row
    )
    neg_none = Negativeelement.value
    pos_none = Positiveelement.value
    #gets the empty values of the dropdowns, so that it can check if there has been any input
    T= ft.Text("Please select One element from each dropdown")
    page.add(
         atoms_content,
        ft.Row(
             controls= [
                  T
             ],
             alignment= ft.MainAxisAlignment.CENTER,
             spacing= 20
        )
        #puts everything on the screen
    )
ft.app(target=main)
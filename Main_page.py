import flet as ft
import atoms
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#allows use of subscript numbers, used when doing the formula
def main(page: ft.Page):
    page.title = "Balencing basic diatomic ionic compounds"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    class Dropdowns_maker(ft.Dropdown):
    #simplifying the creation of dropdowns, since there is more than one.
        def __init__(self, name, description):
            super().__init__()
            #this is the creation of a subclass, but we do not know the properties of the original.
            self.label = name
            self.hint_text = description
            self.options = []

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
    def Balence_button_pressed(e):
        if Negativeelement.value == neg_none and Positiveelement.value == pos_none:
             T.value = "Please select one of the options from the dropdowns above."
        elif Negativeelement.value == neg_none:
             T.value = "Please select a negative element."
        elif Positiveelement.value == pos_none:
             T.value = "Please select a positive value."
             #all of this is just error handling.
        else:
             T.value = ""
             #this makes the error text go away if you enter stuff correctly.
             for y in atoms.Full_list:
                if y.name == Negativeelement.value:
                    Negative_element = y
                if y.name == Positiveelement.value:
                    Positive_element = y
                    #all of this uses a for loop to search through the whole list of elements
             atomic_equation = atoms.Ballence(Positive_element, Negative_element)
             #using the ballencing function from the created module
             Opendialogue(e, atomic_equation.translate(SUB), atoms.naming(atomic_equation))
             #turns all numbers in the equation into subscript, and gets the named version
        page.update()
        #all of this happens whenever the button gets pressed
    Show_results = ft.AlertDialog(
        title= ft.Text("Balenced results")
        #basic dialogue, to be iterated on
    )
    def Opendialogue(e, atomic_equation, Name_of_formula):
        page.dialog = Show_results
        Show_results.open = True
        Show_results.content = ft.Text(f"The name of the diatomic equation you have made is {Name_of_formula}. It's equation is {atomic_equation.replace(" ", "")}")
        #this will show different things on the dialogue depending on the user input
    Balence_button =  ft.ElevatedButton(
        text= "Balence?",
        on_click= Balence_button_pressed,
        bgcolor= ft.colors.AMBER_300
        )
    Negativeelement = Dropdowns_maker("Negative Element", "Negative charge")
    Positiveelement = Dropdowns_maker("Positive Element", "Positive Charge")
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
    T= ft.Text()
    page.add(
         atoms_content,
        ft.Row(
             controls= [
                  T,
                  Balence_button
             ],
             alignment= ft.MainAxisAlignment.END,
             spacing= 20
        )
        #puts everything on the screen
    )
ft.app(target=main)
import periodictable

# # get element info using symbol
def get_element_info(symbol):
    if not periodictable.elements.symbol(symbol):
        print("Invalid element symbol!!!")
        return
    element = periodictable.elements.symbol(symbol)
    print("Element: ", element.name)
    print("Symbol: ", element.symbol)
    print("Atomic Number: ", element.number)
    print("Atomic Weight: ", element.mass)
    print("Density: ", element.density)

element_symbol = input("Enter Element symbol: ")
get_element_info(element_symbol)
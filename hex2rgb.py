"""
Simple script for converting HEX to RGB and RGB to Hex
"""


def rgb_hex():  # Function for RGB to HEX conversion
    invalid_msg = "Error, Invalid Input."
    # Input collection
    red = int(input("Enter red (R) value: "))
    if red < 0 or red > 255:
        print(invalid_msg)
        return
    green = int(input("Enter green (G) value: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return
    blue = int(input("Enter blue (B) value: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return
    val = (red << 16) + (green << 8) + blue  # Shifts bits left by pre-determined amount
    print("Hexidecimal Value: %s" % (hex(val)[2:]).upper())  # Final output


def hex_rgb():  # Function for HEX to RGB conversion
    hex_val = input("Enter a hex value: ")  # Request input
    if len(hex_val) != 6:  # Tests for valid Hexidecimal input
        print("Error, Invalid Input")
        return
    else:
        hex_val = int(hex_val, 16)  # Converts to base 16 int
    # Bit shifting and conversion
    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print("Red: %s Green: %s Blue: %s" % (red, green, blue))  # Final output


def convert():  # Menu function
    while True:
        option = input(
            "Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: "
        )
        if option == "1":
            print("RGB to Hex...")
            rgb_hex()
        elif option == "2":
            print("HEX to RGB...")
            hex_rgb()
        elif option == "X" or "x":
            break
        else:
            print("Error")


convert()
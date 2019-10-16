"""
Simple script for converting HEX to RGB and RGB to Hex
"""

import argparse


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


parser = argparse.ArgumentParser(description="Takes user selection for which operation to perform")
parser.add_argument("Conversion", metavar="conversion", type=str, help="Specify either hex2rgb or rgb2hex after the script name")
args = parser.parse_args()

try:
    if args.Conversion == "hex2rgb":
        hex_rgb()
    elif args.Conversion == "rgb2hex":
        rgb_hex()
except (ValueError, KeyboardInterrupt):
    print("\r\nYou either CTRL-C'd out or need to specify a value, pal.")

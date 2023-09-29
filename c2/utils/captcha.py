import random, os, sys
import string
import pyfiglet
from sys import stdout
from rgbprint import gradient_print, Color
from colorama import Fore, Back


def convert_to_ascii(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art


# Generate a textual CAPTCHA with random text using ASCII characters
def generate_captcha():
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
    return captcha_text


# Verify if the user-provided response matches the CAPTCHA
def verify_captcha(user_input, captcha_text):
    return user_input.lower() == captcha_text.lower()


# Main function to run the CAPTCHA verification process
def run_captcha_verification(max_attempts):
    captcha_text = generate_captcha()
    print_ascii_captcha(captcha_text)
    attempts = 0
    while attempts < max_attempts:
        print()
        print()
        stdout.write('          ' + Back.WHITE + '                                ')
        user_input = input(Back.RESET + '       \rEnter Captcha: ' + Fore.BLACK + Back.WHITE)
        if verify_captcha(user_input, captcha_text):
            print("CAPTCHA successful!")
            print(Back.RESET)
            return True
        else:
            attempts += 1
            if attempts < max_attempts:
                os.system('cls')
                print(Back.RESET + "CAPTCHA failed! Please try again.")
            else:
                print("CAPTCHA failed after", max_attempts, "attempts!")
                sys.exit()


# Display the CAPTCHA using ASCII characters
def print_ascii_captcha(captcha_text):
    ascii_text = convert_to_ascii(captcha_text)
    gradient_print(ascii_text, start_color=0x4BBEE3, end_color=Color.magenta)
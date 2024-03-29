# Assignment: wp1
# Author: Kyle Palacios
# Date Created: 01/29/2024


import sys


def read_file():
    try:
        str(sys.argv[1])[-4:] == ".txt"
        with open(sys.argv[1], "r") as original_file:
            original_file.seek(0, 2)
            num_bytes = original_file.tell()
            byte_list = []
            original_file.seek(0)
            for i in range(num_bytes):
                byte_list.append(original_file.read(1))
                original_file.seek(i+1)
            if not byte_list:
                print("\nYou provided an empty txt file.")
                print("Please enter a non-empty file to encrypt.")
                sys.exit()
            return reversed(byte_list)
    except FileNotFoundError:
        print("\nYour file could not be found.")
        print("Please enter a valid, existing txt file.")
        sys.exit()
    except AssertionError:
        print("\nYou must provide files with the extension .txt")
        sys.exit()


def encrypt_file(rev_byte_list):
    try:
        assert str(sys.argv[2])[-4:] == ".txt"
        with open(sys.argv[2], "w") as encrypted_file:
            for byte in rev_byte_list:
                encrypted_file.write(byte)
    except AssertionError:
        print("\nYour encrypted file's extension must be .txt")
        sys.exit()


if __name__ == "__main__":
    rev_byte_list = read_file()
    encrypt_file(rev_byte_list)

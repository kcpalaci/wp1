#Assignment: wp1
#Author: Kyle Palacios
#Date Created: 01/29/2024


import sys


def read_file():
    with open(sys.argv[0], "r") as original_file:
        original_file.seek(0,2)
        num_bytes = original_file.tell()
        byte_list = []
        original_file.seek(0)
        for i in range(num_bytes):
            byte_list.append(original_file.read(1))
            original_file.seek(i)
        return reversed(byte_list)
    

def encrypt_file(rev_byte_list):
    with open(sys.argv[1], "w") as encrypted_file:
        for byte in rev_byte_list:
            encrypted_file.write(byte)


if __name__ == "__main__":
    rev_byte_list = read_file()
    encrypt_file(rev_byte_list)
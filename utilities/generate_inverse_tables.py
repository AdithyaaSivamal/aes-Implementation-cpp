import numpy as np

# Initialize tables for multiplication by 2 and 3 in GF(2^8)
mul2 = np.zeros(256, dtype=np.uint8)
mul3 = np.zeros(256, dtype=np.uint8)

def initialize_tables():
    """
    Initializes the tables for multiplication by 2 and 3.
    """
    for i in range(256):
        x = i << 1  # Multiply by 2 (shift left by 1)
        mul2[i] = x ^ 0x1b if x > 255 else x  # XOR with 0x1b if overflow occurs
        mul3[i] = mul2[i] ^ i  # Multiply by 3 is equivalent to mul2 ^ original

def print_table(name, table):
    """
    Prints the given table in a formatted manner.

    Args:
        name (str): The name of the table.
        table (numpy.ndarray): The table to be printed.
    """
    print(f"uint8_t {name}[256] = {{")
    for i in range(256):
        end_char = ", " if i < 255 else ""
        print(f"0x{table[i]:02X}", end=end_char)
        if (i + 1) % 16 == 0:
            print()
    print("};\n")

def main():
    # Initialize multiplication tables for 2 and 3
    initialize_tables()

    # Define tables for multiplication by 9, 11, 13, and 14
    mul9 = np.zeros(256, dtype=np.uint8)
    mul11 = np.zeros(256, dtype=np.uint8)
    mul13 = np.zeros(256, dtype=np.uint8)
    mul14 = np.zeros(256, dtype=np.uint8)

    # Initialize tables for multiplication by 9, 11, 13, and 14
    for i in range(256):
        mul9[i] = mul2[mul2[mul2[i]]] ^ i  # Multiply by 9
        mul11[i] = mul2[mul2[mul2[i]]] ^ mul2[i] ^ i  # Multiply by 11
        mul13[i] = mul2[mul2[mul2[i]]] ^ mul2[mul2[i]] ^ i  # Multiply by 13
        mul14[i] = mul2[mul2[mul2[i]]] ^ mul2[mul2[i]] ^ mul2[i]  # Multiply by 14

    # Print the generated tables
    print_table("mul9", mul9)
    print_table("mul11", mul11)
    print_table("mul13", mul13)
    print_table("mul14", mul14)

if __name__ == "__main__":
    main()

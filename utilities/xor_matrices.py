import argparse

def xor_matrices(matrix1, matrix2):
    """
    Performs element-wise XOR operation on two 4x4 hexadecimal matrices.

    Args:
        matrix1: A list of lists representing the first 4x4 matrix (hex values).
        matrix2: A list of lists representing the second 4x4 matrix (hex values).

    Returns:
        A list of lists representing the XORed matrix (hex values).
    """

    # Check if matrices are 4x4
    if len(matrix1) != 4 or len(matrix1[0]) != 4 or len(matrix2) != 4 or len(matrix2[0]) != 4:
        raise ValueError("Matrices must be 4x4.")

    # Initialize the result matrix
    result = []

    # Perform element-wise XOR operation
    for i in range(4):
        row = []
        for j in range(4):
            # Convert hex values to integers, perform XOR, and convert back to hex
            result_hex = hex(int(matrix1[i][j], 16) ^ int(matrix2[i][j], 16))[2:].upper()
            # Ensure single-digit hex values are padded with '0'
            result_hex = result_hex.zfill(2)
            row.append(result_hex)
        result.append(row)
    
    return result

def parse_matrix(matrix_str):
    """
    Parses a string representation of a 4x4 hexadecimal matrix.

    Args:
        matrix_str: A string representing the matrix in row-major order (space separated values).

    Returns:
        A list of lists representing the 4x4 matrix (hex values).
    """

    # Ensure the string contains 16 hex values
    if len(matrix_str.split()) != 16:
        raise ValueError("Matrix string must contain 16 hexadecimal values.")

    # Initialize the matrix
    matrix = []

    # Split the string into rows and add to the matrix
    for i in range(4):
        row = matrix_str.split()[i*4:(i+1)*4]
        matrix.append(row)
    
    return matrix

if __name__ == "__main__":
    # Set up argument parser for command-line interface
    parser = argparse.ArgumentParser(description="XOR two 4x4 hexadecimal matrices")
    parser.add_argument("matrix1", type=str, help="First 4x4 hexadecimal matrix (space separated values)")
    parser.add_argument("matrix2", type=str, help="Second 4x4 hexadecimal matrix (space separated values)")
    args = parser.parse_args()

    # Try-except block for handling potential errors
    try:
        # Parse matrices from command-line arguments
        matrix1 = parse_matrix(args.matrix1)
        matrix2 = parse_matrix(args.matrix2)

        # Perform XOR operation and print result
        xor_result = xor_matrices(matrix1, matrix2)
        for row in xor_result:
            print(" ".join(row))
    except ValueError as e:
        print(f"Error: {e}")

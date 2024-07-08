Sure, here's a professional `README.txt` for your AES project:

---

# AES Encryption Demo

This project is a supplementary example for a post on my blog, [Threat Treks](https://threattreks.wordpress.com/). It demonstrates the mechanism behind AES encryption and decryption.<br>
**Note:** This code is not intended for use as a secure encryption tool. It is a personal project aimed at researching and understanding AES.

## Prerequisites

To run this project, you need to have a C++ compiler and `make` installed on your system.

### Install `make` on Windows

1. **Install Chocolatey** (if not already installed):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; \
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor [System.Net.SecurityProtocolType]::Tls12; \
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

2. **Install `make`**:

```powershell
choco install make
```

3. **Run `make`**:

```powershell
make
```

### Install `make` on Linux

1. **Install `make`** (if not already installed):

```bash
sudo apt-get update
sudo apt-get install build-essential
```

2. **Run `make`**:

```bash
make
```

## Compilation

You can compile the project using `make`:

```bash
make
```

Alternatively, you can compile using `g++`:

```bash
g++ -o test_aes .\tests\test_aes.cpp .\src\transformations.cpp .\key_expansion\key_expansion.cpp
g++ -o test_key_exp .\tests\debug_key_expansion.cpp .\src\transformations.cpp .\key_expansion\key_expansion.cpp
g++ -o aes .\src\aes.cpp .\src\transformations.cpp .\key_expansion\key_expansion.cpp
```

## Usage

Run the executable with the following syntax:

```bash
./aes
```

The program will prompt you to enter the plaintext and key.

### Example:

```bash
Enter plaintext: This is a test.
Enter key (32 hex digits): 00112233445566778899aabbccddeeff
```

## Detailed Description

### Key Expansion
The AES key expansion is responsible for generating a set of round keys from the original key. Each round key is used in one of the encryption or decryption rounds.

### Encryption
The AES encryption process involves several steps: SubBytes, ShiftRows, MixColumns, and AddRoundKey. These transformations provide confusion, diffusion, and the complexity necessary for secure encryption.

### Decryption
The AES decryption process involves the inverse transformations: InverseShiftRows, InverseSubBytes, InverseMixColumns, and AddRoundKey. These steps reverse the encryption process to recover the original plaintext.

## Notes

- Ensure your key is 32 hex digits long (128 bits).
- The plaintext will be padded to fit the block size if necessary.

## Disclaimer

This code is for educational purposes only and should never be used for real encryption tasks. It is an oversimplified demonstration of the AES algorithm.

---

This README provides a clear overview of the project, instructions for setup, compilation, and usage, and an explanation of the key processes involved.

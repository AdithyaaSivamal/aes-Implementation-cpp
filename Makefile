CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11

# Define the source directories
SRC_DIR = src
KEY_EXP_DIR = key_expansion
TESTS_DIR = tests

# source files
SRC_FILES = $(SRC_DIR)/transformations.cpp $(KEY_EXP_DIR)/key_expansion.cpp
AES_SRC = $(SRC_DIR)/aes.cpp

# target executables
TARGETS = test_aes.exe test_key_exp.exe aes.exe

# Default target
all: $(TARGETS)

# test_aes.exe
test_aes.exe: $(TESTS_DIR)/test_aes.cpp $(SRC_FILES)
	$(CXX) $(CXXFLAGS) -o $@ $^

# test_key_exp.exe
test_key_exp.exe: $(TESTS_DIR)/debug_key_expansion.cpp $(SRC_FILES)
	$(CXX) $(CXXFLAGS) -o $@ $^

# aes.exe
aes.exe: $(AES_SRC) $(SRC_FILES)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Clean up object files and executables
clean:
	rm -f $(TARGETS) *.o 

.PHONY: all clean

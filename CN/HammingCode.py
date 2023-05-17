import math

# Function to calculate the parity bits for a given message
def calculate_parity_bits(message):
    n = len(message)
    # Calculate the number of parity bits required
    r = 0
    while 2**r < n + r + 1:
        r += 1
    # Initialize the parity bits to 0
    parity_bits = [0] * r
    # Calculate the parity bits using XOR operations
    for i in range(r):
        for j in range(2**i-1, n, 2**(i+1)):
            for k in range(2**i):
                if j+k < n:
                    parity_bits[i] ^= int(message[j+k])
    return parity_bits

# Function to correct a single-bit error in a message using Hamming code
def hamming_decode(message):
    n = len(message)
    # Calculate the number of parity bits
    r = 0
    while 2**r < n + 1:
        r += 1
    # Calculate the parity bits for the received message
    parity_bits = calculate_parity_bits(message)
    # Check if any parity bit is incorrect
    error_bit = 0
    for i in range(r):
        if parity_bits[i] != int(message[2**i-1]):
            error_bit += 2**i-1
    if error_bit > 0:
        # Correct the error by flipping the incorrect bit
        message = list(message)
        message[error_bit] = str(1 - int(message[error_bit]))
        message = ''.join(message)
    # Remove the parity bits and return the original message
    return message[:n-r]

# Get the input from the user
m = int(input("Enter the number of bits in your data: "))
# Calculate the number of parity bits required
r = 0
while 2**r < m + r + 1:
    r += 1
# Calculate the total length of the message
n = m + r
# Get the input message from the user
message = input("Enter a message of length {}: ".format(m))
# Calculate the parity bits for the message
parity_bits = calculate_parity_bits(message)
# Append the parity bits to the message
for i in range(r):
    message = message[:2**i-1] + str(parity_bits[i]) + message[2**i-1:]
# Print the encoded message
print("Encoded message:", message)
# Get the input message from the user with a single-bit error
error_message = input("Enter the encoded message with a single-bit error: ")
# Correct the error in the message
corrected_message = hamming_decode(error_message)
# Print the corrected message
print("Corrected message:", corrected_message)

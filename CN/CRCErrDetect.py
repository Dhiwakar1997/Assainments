def crc(message, divisor):
    """
    Performs CRC (Cyclic Redundancy Check) on the given message using the given divisor.
    Returns the remainder of the division, which can be used to detect errors.
    """
    # Convert the message and divisor to binary strings
    message_bin = ''.join(format(ord(c), '08b') for c in message)
    divisor_bin = format(divisor, 'b')

    # Pad the message with zeros equal to the length of the divisor minus 1
    padded_message = message_bin + '0' * (len(divisor_bin) - 1)

    # Perform the division using binary XOR operations
    remainder = ''
    for i in range(len(divisor_bin)):
        remainder += padded_message[i]
    for i in range(len(divisor_bin), len(padded_message)):
        if remainder[0] == '1':
            temp = int(remainder, 2) ^ int(divisor_bin, 2)
            remainder = format(temp, 'b')
        else:
            remainder = remainder[1:]
        remainder += padded_message[i]

    # Return the remainder as a binary string
    return remainder

# Example usage
message = "Computer Networks!"
divisor = 0b1011
remainder = crc(message, divisor)
print("Message:", message)
print("Divisor:", bin(divisor))
print("Remainder:", remainder)



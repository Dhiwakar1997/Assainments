def two_dimensional_parity_check(data_bits):
    """
    Performs a two-dimensional parity check on the given data bits.
    Returns the corrected data if an error is detected, otherwise returns the original data.
    """
    # Get the number of rows and columns in the data
    num_rows = len(data_bits)
    num_cols = len(data_bits[0])

    # Calculate the row and column parity bits
    row_parity = [0] * num_rows
    col_parity = [0] * num_cols
    for i in range(num_rows):
        for j in range(num_cols):
            row_parity[i] ^= data_bits[i][j]
            col_parity[j] ^= data_bits[i][j]

    # Check the row and column parity bits for errors
    row_parity_error = False
    col_parity_error = False
    for i in range(num_rows):
        if row_parity[i] != 0:
            row_parity_error = True
            break
    for j in range(num_cols):
        if col_parity[j] != 0:
            col_parity_error = True
            break

    # If there is an error, determine the position of the error bit
    if row_parity_error or col_parity_error:
        error_row = -1
        error_col = -1
        for i in range(num_rows):
            for j in range(num_cols):
                row_parity_check = row_parity[i] ^ data_bits[i][j]
                col_parity_check = col_parity[j] ^ data_bits[i][j]
                if row_parity_check == 0 and col_parity_check == 0:
                    continue
                elif row_parity_check == 1 and col_parity_check == 1:
                    error_row = i
                    error_col = j
                elif row_parity_check == 1:
                    error_row = i
                elif col_parity_check == 1:
                    error_col = j

        # Correct the error bit
        data_bits[error_row][error_col] ^= 1

    # Return the corrected data bits, if any
    return data_bits
data_bits = [    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 1]
]
corrected_data_bits = two_dimensional_parity_check(data_bits)
for i in corrected_data_bits:
    print(i)

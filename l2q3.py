# Define the S-box 1 table
s_box_1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def s_box_lookup(s_box, input_bits):
    # Convert the input bits to row and column indices
    row = int(input_bits[0] + input_bits[5], 2)  # First and last bits form the row index
    col = int(input_bits[1:5], 2)  # Middle four bits form the column index
    # Get the output from the S-box
    return format(s_box[row][col], '04b')  # Convert the output to a 4-bit binary string

# Example usage
input_bits = '011011'  # 6-bit input
print(f"Input Bits: {input_bits}")

# Perform S-box 1 lookup
output_bits = s_box_lookup(s_box_1, input_bits)
print(f"Output Bits: {output_bits}")

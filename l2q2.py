# Define the expansion P-box table
expansion_p_box = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

def expand(block, expansion_table):
    return ''.join(block[i-1] for i in expansion_table)

# Example usage
input_block = '11110000101010101111000010101010'  # 32-bit input
print(f"Input Block: {input_block}")

# Expansion Permutation
expanded_block = expand(input_block, expansion_p_box)
print(f"Expanded Block: {expanded_block}")

# To demonstrate that it works correctly, we will show the lengths of the input and output blocks
print(f"Input Block Length: {len(input_block)} bits")
print(f"Expanded Block Length: {len(expanded_block)} bits")

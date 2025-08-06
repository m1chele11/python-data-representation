def logic_circuit(A, B, C):
    # Compute the individual terms
    term1 = A and B
    term2 = (not A) and (not B)
    term3 = A and B and C

    # Final output  OR logic
    output = term1 or term2 or term3
    return int(output)  # Convert boolean (0 or 1)









# Test

# Given test cases
test_cases = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]

# Run test cases
print("A B C | Output")
print("---------------")
for A, B, C in test_cases:
    print(A, B, C, "|", logic_circuit(A, B, C))

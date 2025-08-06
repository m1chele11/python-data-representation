





def binary_to_text(file_path):
    with open(file_path, 'r') as file:
        binary_data = file.read().replace("\n", "").strip()  # Read input
    
    # Split into 8-bit chunks
    characters = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    
    # Convert binary to ASCII
    text = ''.join([chr(int(char, 2)) for char in characters])
    
    print("Decoded Text:", text)


#test:
binary_to_text("binary.txt")
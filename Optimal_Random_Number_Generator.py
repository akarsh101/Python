# Importing the Hadamard (H) gate and Measure operation from the ProjectQ quantum library
from projectq.ops import H, Measure

# Importing the MainEngine class from the ProjectQ quantum library to create a quantum engine
from projectq import MainEngine

# Defining a function named 'rando' which takes 'number' as an argument
def rando(number):
    # Initializing the quantum engine
    quantum = MainEngine()
    # Allocating 'number' of qubits and storing them in a list
    qubits = [quantum.allocate_qubit() for _ in range(number)]
    
    # Applying the Hadamard gate to each qubit to create a superposition state
    for q in qubits:
        H | q

    # Flushing the quantum engine to ensure all operations are executed
    quantum.flush()

    # Initializing an empty list to store the measurement results
    random_bits = []
    # Measuring each qubit and storing the result in the 'random_bits' list
    for q in qubits:
        Measure | q
        quantum.flush()  # Ensure measurement is executed before reading the result
        # Converting the measurement result to an integer and appending it to 'random_bits'
        random_bits.append(int(q))

    # Converting the list of bits to a binary string
    bit_string = ''.join(map(str, random_bits))
    # Converting the binary string to an integer and returning both the integer and the string
    return int(bit_string, 2), bit_string

# Defining a function named 'generate_random_number' which takes 'min_value' as an argument
def generate_random_number(min_value):
    # Determining the number of bits needed to generate a random number
    num_bits = min_value * 3
    while True:
        # Generating a random number and its binary string representation
        random_number, bit_string = rando(num_bits)
        # Checking if the generated number is greater than or equal to 'min_value'
        if random_number >= min_value:
            break
    # Returning the valid random number and its binary string representation
    return random_number, bit_string

# Prompting the user to input a minimum value and converting it to an integer
min_value = int(input("Type your number: "))
# Generating a random number and its binary string representation that is greater than or equal to 'min_value'
random_number, bit_string = generate_random_number(min_value)

# Printing the generated random binary string
print(f"Random binary string: {bit_string}")
# Printing the generated random number
print(f"Random number: {random_number}")

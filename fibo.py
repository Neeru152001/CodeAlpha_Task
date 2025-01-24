def generate_fibonacci(n):
    if n <= 0:
        return []

    # Initialize the first two terms of the Fibonacci sequence
    sequence = [0, 1]

    # Generate the sequence up to n terms
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence[:n]  # Return only the first n terms


# Get user input and display the Fibonacci sequence
if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of terms: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = generate_fibonacci(num_terms)
            print(f"The first {num_terms} terms of the Fibonacci sequence are:")
            print(fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter an integer.")

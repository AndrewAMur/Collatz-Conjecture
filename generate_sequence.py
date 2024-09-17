def collatz_sequence(n):
    if n <= 0:
        raise ValueError("The input must be a positive integer.")

    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

def main():
    try:
        start_number = int(input("Enter a positive integer to start the Collatz sequence: "))
        if start_number <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive integer.")
        return
    
    sequence = collatz_sequence(start_number)
    print("The Collatz sequence is:")
    print(sequence)

if __name__ == "__main__":
    main()

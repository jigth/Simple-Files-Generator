import os
import sys
import random
import lorem

def generate_lorem_ipsum():
    # Generate a random number of paragraphs (1 to 5)
    num_paragraphs = random.randint(1, 5)
    paragraphs = [lorem.paragraph() for _ in range(num_paragraphs)]
    return '\n\n'.join(paragraphs)

def generate_files(num_files, directories):
    total_dirs = len(directories)
    if total_dirs == 0:
        print("No directories provided.")
        return

    if total_dirs > num_files:
        print("Warning: More directories provided than files to generate.")

    # Generate random weights for each directory
    weights = [random.random() for _ in range(total_dirs)]
    total_weight = sum(weights)

    # Calculate distribution of files based on weights
    distribution = [int(num_files * (weight / total_weight)) for weight in weights]

    # Adjust distribution to ensure the total number of files matches num_files
    total_distribution = sum(distribution)
    if total_distribution < num_files:
        difference = num_files - total_distribution
        for i in range(difference):
            distribution[i % total_dirs] += 1
    elif total_distribution > num_files:
        difference = total_distribution - num_files
        for i in range(difference):
            distribution[i % total_dirs] -= 1

    # Create directories if they don't exist
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Generate files
    file_count = 0
    for i, directory in enumerate(directories):
        num_files_in_dir = distribution[i]
        for j in range(num_files_in_dir):
            file_count += 1
            filename = os.path.join(directory, f"file_{file_count}.txt")
            lorem_text = generate_lorem_ipsum()
            with open(filename, 'w') as f:
                f.write(lorem_text)

    print(f"Generated {file_count} files across {total_dirs} directories.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 myProgram.py <num_files> <directory1> [<directory2> ...]")
        sys.exit(1)

    num_files = int(sys.argv[1])
    directories = sys.argv[2:]

    generate_files(num_files, directories)

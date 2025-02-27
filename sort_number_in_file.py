def sort_number(input_file, output_file):
    numbers = []
    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            numbers.append(int(line.strip()))

    numbers.sort()

    with open(output_file, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")
            
if __name__ == '__main__':
    sort_number("C:/WorkSpace/input.txt", "C:/WorkSpace/output.txt")
# data_analyzer.py

def analyze_data(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count

    minimum = min(numbers)
    maximum = max(numbers)

    print("Data Analysis Results:")
    print(f"Numbers: {numbers}")
    print(f"Count: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")


def main():
    data = input("Enter numbers separated by spaces: ")
    numbers = [float(num) for num in data.split()]
    
    analyze_data(numbers)


if __name__ == "__main__":
    main()

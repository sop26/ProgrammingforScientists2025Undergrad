
def main():
    numbers = [3, 1, 2]
    ordered = [0] * len(numbers)
    index_of_min = 0

    for i in range (0, len(numbers)):
        min = numbers[i]
        for j in range(i, len(numbers)):
            if numbers[j] < min:
                min = numbers[j]
                index_of_min = j
        numbers[index_of_min] = numbers[i]
        ordered[i] = min
    print(ordered)

if __name__ == "__main__":
    main()


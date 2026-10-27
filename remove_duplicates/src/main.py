def remove_duplicates(numbers: list[int]) -> list[int]:
    seen = set()
    result = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


def main():
    numbers = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    print(remove_duplicates(numbers))


if __name__ == "__main__":
    main()
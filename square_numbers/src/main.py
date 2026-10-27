def get_squares():
    return list(map(lambda num: num ** 2, range(1, 21)))


def main():
    print(get_squares())


if __name__ == "__main__":
    main()
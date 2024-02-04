from utils import filter_list


def main():
    seq = input("Enter a sequence of integers separated by space: ")
    try:
        numbers = list(map(int, seq.split()))
        print(filter_list(numbers))
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    main()

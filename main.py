from activity_menager import create_activity_sequence


def print_query(num):
    lista=create_activity_sequence(num, "spostamento", False,  3, False)

    for a in lista:
        print(f'{a.insert()}')


if __name__ == '__main__':
    print_query(1)


def is_triangle(a, b, c):
    if a + b < c:
        return "No"
    if a + c < b:
        return "No"
    if b + c < a:
        return "No"
    return "Yes"


def read_integers(num_of_input=3):
    print("enter three numbers (integer) and hit the enter key")
    raw = input("enter three numbers (integer), and hit the enter key: ")
    striped_input = raw.strip()

    if striped_input == "":
        return read_integers(num_of_input)

    entries = striped_input.split()
    if len(entries) != num_of_input:
        return read_integers(num_of_input)

    return [int(x) for x in entries]


if __name__ == "__main__":
    lengths = read_integers(3)
    print(f"{lengths} is triangle: {is_triangle(*lengths)}")

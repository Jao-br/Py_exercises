def reverse_str(str):
    reverse_str = ""
    for char in str:
        reverse_str = char + reverse_str

    return reverse_str

def get_user_input():
    return input("Digite a palavra que deseja inverter: ")

def print_results(original_str, reversed_str):
    print(f">>>>>{original_str} {reversed_str}")

def main():
    while True:
        original_str = get_user_input()
        reversed_str = reverse_str(original_str)
        print_results(original_str, reversed_str)

main()
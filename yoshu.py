import pyperclip

def xxx():
    x, y = map(int, input().split())
    Z = []
    result=""
    for c in range(x, y + 1):
        print(f"{c}-> ", end="")
        Z.append(input())

    for a, b in zip(range(x, y + 1), Z):
        result+= (f"({a}){b}")

    print(result)
    pyperclip.copy(result)
if __name__ == '__main__':
    while True:
        xxx()
        print("\n")

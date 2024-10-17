import pyperclip
import sys

def xxx():
    while True:
        try:
            x, y = map(int, input("Please enter the question numbers (lower and upper limits).\n >> ").split())
            if x > y:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n   Please enter the correct format.\n    ex) 0 2\n   0 is minimum, 2 is maximum.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                continue
            break
        except ValueError:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n   Please enter the correct format.\n    ex) 0 2\n   0 is minimum, 2 is maximum.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue
        except KeyboardInterrupt:
            print("\n   exit program.\n\n\n\n")
            sys.exit()



    Z = []
    result=""
    for c in range(x, y + 1):
        while True:
            try:
                Z.append(input(f"{c}-> "))
                break
            except ValueError:
                continue
            except KeyboardInterrupt:
                print("\n   exit program.\n\n\n\n")
                sys.exit()


    for a, b in zip(range(x, y + 1), Z):
        result+= (f"({a}){b}")

    print(result)
    print("\n   result is copied to clipboard.\n")
    pyperclip.copy(result)


if __name__ == '__main__':
    while True:
        xxx()
        while True:
            try:
                i=list(map(int,input(f"0 is exit , other is comtinue.\n >>")))
            except ValueError:
                continue
            except KeyboardInterrupt:
                print("\n   exit program.\n\n\n\n")
                sys.exit()

        if i[0]==0:
            print("\n   exit program.\n\n\n\n")
            sys.exit()
        print("\n")

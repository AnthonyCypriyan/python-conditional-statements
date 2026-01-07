n = int(input())
if n >= 0 and n <= 100:
    if n >= 90:
        print("Grade A")
    elif n >= 75:
        print("Grade B")
    elif n >= 50:
        print("Grade C")
    else:
        print("Fail")

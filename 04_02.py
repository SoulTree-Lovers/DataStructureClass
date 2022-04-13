def do_sum():
    num = []
    for i in range(5):
        inp = input("Type the number: ")
        num.append(int(inp))

    sum = 0
    for j in num:
        sum += int(j)
    
    print(sum)

if __name__ == "__main__":
    do_sum()
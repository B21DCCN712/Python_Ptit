def is_even(num):
    return num % 2 == 0

def main():
    N = int(input())
    A = list(map(int, input().split()))

    stack = []

    for num in A:
        if stack and is_even(stack[-1] + num):
            stack.pop()  # Loại bỏ cặp phần tử có tổng chẵn
        else:
            stack.append(num)

    print(len(stack))

if __name__ == "__main__":
    main()

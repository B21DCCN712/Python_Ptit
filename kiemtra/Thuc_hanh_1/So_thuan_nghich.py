def is_palindrome(num_str):
    return num_str == num_str[::-1]

def count_palindromic_numbers(a, b, M):
    def count_palindromic_numbers_single_base(n, base):
        count = 0
        while n > 0:
            digit = n % base
            count = count * base + digit
            n //= base
        return count

    def count_palindromic_numbers_range(n, base):
        count = 0
        for _ in range(2):
            palindrome = count_palindromic_numbers_single_base(n, base)
            if palindrome >= a and palindrome <= b:
                count += 1
            n -= 1
        return count

    count = 0
    for base in range(2, M + 1):
        max_num = int((base ** (len(str(b)) // 2 + 1)) ** 0.5) + 1
        for num in range(max_num):
            count += count_palindromic_numbers_range(num, base)

    return count

a, b, m = map(int, input().split())
print(count_palindromic_numbers(a, b, m))

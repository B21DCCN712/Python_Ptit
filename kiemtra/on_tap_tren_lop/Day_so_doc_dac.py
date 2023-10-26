def is_dodac(N, A):
    # Tạo một từ điển để lưu trữ vị trí xuất hiện cuối cùng của mỗi phần tử trong dãy A
    last_occurrence = {}
    unique_count = 0  # Số lượng phần tử độc nhất trong dãy con hiện tại
    result = "NO"

    left = 0  # Vị trí bên trái của dãy con
    for right in range(N):
        if A[right] in last_occurrence and last_occurrence[A[right]] >= left:
            # Nếu phần tử đã xuất hiện trước đó trong dãy con hiện tại, cập nhật left
            left = last_occurrence[A[right]] + 1

        last_occurrence[A[right]] = right  # Cập nhật vị trí xuất hiện cuối cùng
        unique_count = right - left + 1  # Số lượng phần tử độc nhất trong dãy con

        if unique_count == right - left + 1 and unique_count >= 2:
            result = "YES"

    return result


# Hàm main để đọc dữ liệu và in kết quả
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        result = is_dodac(N, A)
        print(result)

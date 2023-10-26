# Hàm tính số lượng xâu t thỏa mãn yêu cầu
def count_strings(N, M, s):
    MOD = M  # Lấy MOD để tránh tràn số
    len_s = len(s)
    
    # Tạo một mảng DP với N+1 hàng và độ dài xâu s+1 cột
    dp = [[0] * (len_s + 1) for _ in range(N + 1)]
    
    # Khởi tạo giá trị ban đầu
    dp[0][0] = 1
    
    # Duyệt qua từng độ dài của xâu t
    for i in range(1, N + 1):
        for j in range(len_s + 1):
            # Nếu j > 0 và xâu s[j-1] trùng với xâu t[i-1]
            if j > 0 and s[j - 1] == t[i - 1]:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
            # Cộng thêm dp[i][j] với dp[i-1][j] để tính số cách tạo xâu t
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
    
    # Tổng số cách tạo xâu t có độ dài N và s là xâu con của t
    result = dp[N][len_s]
    return result

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    s = input().strip()
    
    # Gọi hàm count_strings và in kết quả theo modulo M
    result = count_strings(N, M, s)
    print(result % M)

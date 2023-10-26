# Đọc dữ liệu từ file DATA.in
with open('DATA.in', 'r') as file:
    lines = file.readlines()

def is_integer(s):
    try:
        num =int(s)
        return num >= -(2**31) and num <= (2**31 - 1)
    except ValueError:
        return False

filtered_content = []
for line in lines:
    words = line.split()
    non_integer_words = [word for word in words if not is_integer(word)]
    filtered_content.extend(non_integer_words)

filtered_content.sort()

for i in filtered_content:
    print(i,end=' ')
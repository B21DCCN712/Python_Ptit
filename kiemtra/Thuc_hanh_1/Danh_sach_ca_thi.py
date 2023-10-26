# Đọc số ca thi từ file
with open('CATHI.in', 'r') as file:
    n = int(file.readline().strip)

ca_thi_list = []

for i in range(n):
    mathi = "C" + str(i + 1).zfill(3)
    ngaythi = file.readline().strip()
    giothi = file.readline().strip()
    sophong = file.readline().strip()
    time = ngaythi + " " + giothi
    ca_thi_list.append([mathi, time, sophong])

sorted_ca_thi_list = sorted(ca_thi_list, key=lambda x: (x[1], x[0]))

for ca_thi in sorted_ca_thi_list:
    print(ca_thi[0], ca_thi[1], ca_thi[2])

# with open('CATHI.in', 'r') as file:
#     n = int(file.readline())
#     ca_thi_list = []
#     for i in range(n):
#         mathi = "C" + str(i + 1).zfill(3)
#         ngaythi = file.readline().strip()  
#         giothi = file.readline().strip() 
#         sophong = file.readline().strip()
#         time = ngaythi + " " + giothi
#         ca_thi_list.append([mathi, time, sophong])
# sorted_ca_thi_list = sorted(ca_thi_list, key=lambda x: (x[1], x[0]))

# for ca_thi in sorted_ca_thi_list:
#     print(ca_thi[0], ca_thi[1], ca_thi[2])

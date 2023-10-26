with open("E:\Ki_1_nam_3\Lap_trinh_voi_python\Danh_sach\SOTAY.txt") as filein:
    lines=filein.readlines()
    for line in lines:
        print(line)

with open("E:\Ki_1_nam_3\Lap_trinh_voi_python\Danh_sach\DIENTHOAI.txt",'w') as fileout:
    for i in range(0,len(lines),3):
        fileout.write(f"{lines[0].strip()}: {lines[1].strip()} {lines[2].strip()}\n")
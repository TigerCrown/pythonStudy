#정수
print("{:d}".format(52))

#특정 칸만큼 출력
print("{:5d}".format(52))
print("{:10d}".format(52))
print("{:05d}".format(52))
print("{:010d}".format(52))

print("{:5d}".format(52))
print("{:5d}".format(-52))
print("{:=5d}".format(52))
print("{:=5d}".format(-52))

print("{:+5d}".format(52))
print("{:+5d}".format(-52))
print("{:=+5d}".format(52))
print("{:=+5d}".format(-52))
#부호
print("{:=+05d}".format(52))
print("{:=+05d}".format(-52))

#부동소수점
print("{:f}".format(52))
print("{:=+20f}".format(52))
print("{:=+20f}".format(-52))
print("{:=+20.1f}".format(52))
print("{:=+20.2f}".format(-52))

print("{:.1f}".format(52.455))
print("{:.2f}".format(52.455))
print("{:.3f}".format(52.455))
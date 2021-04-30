result = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_result = bytearray.fromhex(result)

for i in range(0x00, 0xFF):
    flag = ""
    for byte in bytes_result:
        flag = flag + chr(byte ^ i)
    if 'crypto' in flag:
        break

print("FLAG: " + flag)
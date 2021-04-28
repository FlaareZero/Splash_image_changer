import io

offset1 = 0x5000
offset2 = 0x740000
offset3 = 0xE7B000
offset4 = 0x15B6000

imgsize = 0x73AFA0

output = open("logo.img", "r+b")

input = open("locked.bmp", "rb")
output.seek(offset1)
output.write(input.read())
input.close()

input = open("fastboot.bmp", "rb")
output.seek(offset2)
output.write(input.read())
input.close()

input = open("unlocked.bmp", "rb")
output.seek(offset3)
output.write(input.read())
input.close()

input = open("error.bmp", "rb")
output.seek(offset4)
output.write(input.read())
input.close()

output.close()

from PIL import Image

img = Image.open("dark.jpg")
"""
print(img.size)
print(img.getpixel((1000,134)))"""
message = "CSC{Hi_there}"
message_2 = []
for i in message:
	message_2.extend([int(i) for i in f"{ord(i):08b}"])
	print(f"{ord(i):08b}")
print(message_2)
w,h = img.size
count = 0
for i in range(w):
	if count == len(message_2)-1:break
	for j in range(h):
		if count == len(message_2)-1:break
		rgb = list(img.getpixel((i, j)))
		for v, value in enumerate(rgb):
			rgb[v] = value if value%2==message_2[count] else value%(254+message_2[count] )
		img.putpixel((i, j), 255)
img.show()

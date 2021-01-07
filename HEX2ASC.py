def t2h(txt):
	asc = []
	for each in txt:
		asc.append(ord(each))
	Hex = []
	for each in asc:
		Hex.append(hex(each))
	return Hex

def h2t(Hex):
	Hex = Hex.spilt(",")
	txt = ""
	for each in Hex:
		txt = txt + chr(each)
	return txt

def get_input():
	actions = int(input("请选择要进行的操作：\n1、加密\n2、解密\n(输入对应的数字)"))
	if actions == 1:
		return 1
	elif actions == 2:
		return 2
	else:
		return -1

def main():
	user_in = get_input()
	if user_in == 1:
		out = t2h(input("要加密的内容？"))
		print("加密后的内容：" + str(out))
	elif user_in == 2:
		out = h2t(input("要解密的内容？"))
		print("解密后的内容：" + out)
	else:
		print("参数不合法，请重新输入！")
		while user_in == 1 or user_in == 2:
			user_in = get_input()

if __name__ =="__main__":
	print("欢迎使用文本加密工具！")
	print("本工具的加密原理是通过将文本转换成ASCII码，再将ASCII码转换成16进制，以进行加密。")
	main()
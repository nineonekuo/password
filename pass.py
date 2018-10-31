password = 'abc'
a = 3 #剩餘機會
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功')
		break #逃出
	else:
		a = a - 1
		print('密碼錯誤! 還有',a,'次機會')
		if a == 0:
			print('登入失敗')
			break

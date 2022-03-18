print('		Email Validation 	')
email = input("Enter Email : ")
if(len(email) >= 6):
	if( not " " in email):
		if('@' in email) and ('.' in email):
			if(email[0].isalpha()):
				if(email[-3] == '.')  or (email[-4]=='.'):
					if(email.islower()):
						if(email[-1:-4:-1].isalpha()):
							if(email.count('@') == 1) and (email.count(".") == 1) or (email.count('_') == 1) :
								if not ( '$' in email and "%" in email and "#" in email):
									print('Correct Email .')
								else:
									print('incorrect email ?')
							else:
								print('incorrect email ?')
						else:
							print('incorrect email ?')
					else:
						print('incorrect email ?')
				else:
					print('incorrect email ?')
			else:
				print('incorrect email ?')
		else:
			print('incorrect email ?')
	else:
		print('incorrect email ?')
else:
	print('wrong email 1')
morse_sym_dict={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..',
'j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...',
't':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----',
'2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','.':'.-.-.-',',':'--..--','?':'..--..','/':'--..-.','@':'.--.-.'}

morse_dict={
'di-dah': 'A',
'dah-di-di-dit': 'B',
'dah-di-dah-dit': 'C',
'dah-di-dit': 'D',
'dit': 'E',
'di-di-dah-dit': 'F',
'dah-dah-dit': 'G',
'di-di-di-dit':'H',
'di-dit':'I',
'di-dah-dah-dah':'J',
'dah-di-dah':'K',
'di-dah-di-dit': 'L',
'dah-dah': 'M',
'dah-dit': 'N',
'dah-dah-dah':'O',
'di-dah-dah-dit':'P',
'dah-dah-di-dah':'Q',
'di-dah-dit':'R',
'di-di-dit':'S',
'dah':'T',
'di-di-dah':'U',
'di-di-di-dah':'V',
'di-dah-dah':'W',
'dah-di-di-dah':'X',
'dah-di-dah-dah':'Y',
'dah-dah-di-dit':'Z',
'dah-dah-dah-dah-dah':'0',
'di-dah-dah-dah-dah':'1',
'di-di-dah-dah-dah':'2',
'di-di-di-dah-dah':'3',
'di-di-di-di-dah':'4',
'di-di-di-di-dit':'5',
'dah-di-di-di-dit':'6',
'dah-dah-di-di-dit':'7',
'dah-dah-dah-di-dit':'8',
'dah-dah-dah-dah-dit':'9',
'di-dah-di-di-dit':'&',
'di-dah-dah-dah-dah-dit':"'",
'di-dah-dah-di-dah-dit':'@',
'dah-di-dah-dah-di-dah':')',
'dah-di-dah-dah-dit':'(',
'dah-dah-dah-di-di-dit': ':',
'dah-dah-di-di-dah-dah': ',',
'dah-di-di-di-dah': '=',
'dah-di-dah-di-dah-dah': '!',
'di-dah-di-dah-di-dah':'.',
'dah-di-di-di-di-dah':'-',
'di-dah-di-dah-dit':'+',
'di-dah-di-di-dah-dit':'"',
'di-di-dah-dah-di-dit':'?',
'dah-di-di-dah-dit':'\\'
}


def encode_morse(data):
	result_str=""
	try:
		for i in data:
			if i in morse_sym_dict:
				result_str+=morse_sym_dict[i]+" "
			else:
				result_str+=i
	except:
		print("Invalid Data Format")
		result_str=""
	return result_str

def decode_morse(data):
	output_morse=''
	for i in data.split(" "):
		if(i==""):
			output_morse+=" "
		else:
			for key, value in morse_sym_dict.items():
				if(value==i):
					output_morse+=key
	return output_morse

def decode_morse_eng(code):
	plain=''
	try:
		code_arr=code.split(' ')
		for i in range(0, len(code_arr)):
			if(code_arr[i][-1]=='\n'):
				plain+=morse_dict[code_arr[i][:-1]]
			else:				
				plain+=morse_dict[code_arr[i]]
	except:
		for i in range(0, len(code_arr)):
			if(code_arr[i][-1]=='\n'):
				plain+=morse_dict[code_arr[i][:-1]]
			else:				
				plain+=morse_dict[code_arr[i]]				
		print("Invalid Data Format")
		plain=''	
	return plain

def encode_morse_eng(code):
	output_morse=''
	for i in code:
		for key,value in morse_dict.items():
			if(value==i):
				output_morse+=key
		
	return output_morse
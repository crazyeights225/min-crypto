
import math

def rot13n_cipher(data, n):
    data_arr=""
    for i in range(0, len(data)):
        x=ord(data[i])
        #UPPERS
        if(x>64 and x<91):
            x-=65
            y=(x+n)%26
            z=(y+65)

        #LOWERS
        elif(x>96 and x<123):
            x-=97
            y=(x+n)%26
            z=(y+97)

        else:
            z=x
        data_arr+=chr(z)
    return data_arr

def rot47n_cipher(data, n):
	data_arr=""
	for i in range(0, len(data)):
		if(data[i]!=' '):
			x=(ord(data[i])+n)
			if(x>126):
				x=x%127
				x+=33
			data_arr+=chr(x)
		else:
			data_arr+=data[i]
	return data_arr

def brute_force_rot13n_cipher(data):
	data_arr=""
	for i in range(1, 27):
		data_arr=rot13n_cipher(data, i)
		print(data_arr)

def brute_force_rot13n_kw(data, tar2):
	data_arr=""
	for i in range(1, 27):
		data_arr=rot13n_cipher(data, i)
		if(tar2 in data_arr):
			print(data_arr)

def brute_force_rot47n_cipher(data):
	data_arr=""
	for i in range(1, 128):
		data_arr=rot47n_cipher(data, i)
		print(data_arr)

def brute_force_rot47n_kw(data, tar2):
	data_arr=""
	for i in range(1, 128):
		data_arr=rot47n_cipher(data, i)
		if(tar2 in data_arr):
			print(data_arr)

def rot13_cipher(data):
	return rot13n_cipher(data, 13)

def rot47_cipher(data):
	return rot47n_cipher(data, 47)

def lower_wheel_rotate(x, n):
	if(x+n>122):
		y=((x+n)%123)+97
	elif(x+n<97):
		y=123-(97-(x+n))
	else:
		y=x+n
	return chr(y)

def upper_wheel_rotate(x, n):
	if(x+n>90):
		y=((x+n)%91)+65
	elif(x+n<65):
		y=91-(65-(x+n))
	else:
		y=x+n
	return chr(y)

def correct_key_size(data, key):
	if(len(data)!=len(key)):
		n=math.ceil(len(data)/len(key))
		new_key=key*n
		return new_key
	else:
		return key

def is_lower(x):
	lower_min=97
	lower_max=122
	return (x >= lower_min and x <=lower_max)

def is_upper(x):
	upper_min=65
	upper_max=90
	return (x >= upper_min and x <= upper_max)

def vigenere_encode(data, key):
	lower_min=97
	upper_min=65
	new_key=correct_key_size(data, key)
	data_str=""
	for i in range(len(data)):
		x=ord(data[i])
		y=ord(new_key[i])
		if(is_lower(x)):
			if(is_upper(y)):
				y=ord(new_key[i].lower())
				data_str+=lower_wheel_rotate(y, (x-lower_min))
			elif(is_lower(y)):
				data_str+=lower_wheel_rotate(y, (x-lower_min))
			else:
				return None

		elif(is_upper(x)):
			if(is_lower(y)):
				y=ord(new_key[i].upper())
				data_str+=upper_wheel_rotate(y, (x-upper_min))
			elif(is_upper(y)):
				data_str+=upper_wheel_rotate(y, (x-upper_min))
			else:
				return None
		else:
			data_str+=data[i]
	return data_str

def vigenere_decode(data, key):
	lower_min=97
	upper_min=65
	new_key=correct_key_size(data, key)
	data_str=""
	for i in range(len(data)):
		x=ord(data[i])
		y=ord(new_key[i])
		if(is_lower(x)):
			if(is_upper(y)):
				y=ord(new_key[i].lower())
				data_str+=lower_wheel_rotate(x, (-1*abs(lower_min-y)))
			elif(is_lower(y)):
				data_str+=lower_wheel_rotate(x, (-1*abs(lower_min-y)))
			else:
				return None

		elif(is_upper(x)):
			if(is_lower(y)):
				y=ord(new_key[i].upper())
				data_str+=upper_wheel_rotate(x, (-1*abs(upper_min-y)))
			elif(is_upper(y)):
				data_str+=upper_wheel_rotate(x, (-1*abs(upper_min-y)))
			else:
				return None
		else:
			data_str+=data[i]
	return data_str



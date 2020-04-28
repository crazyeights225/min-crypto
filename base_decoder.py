import base64
import base58

def encode_b64(data):
	data_bytes = data.encode("utf-8")
	data_enc=base64.b64encode(data_bytes)
	return data_enc.decode("utf-8")

def decode_b64(data):
	data_dec=base64.b64decode(data)
	return data_dec.decode("utf-8")

def encode_b32(data):
	data_bytes = data.encode("utf-8")
	data_enc=base64.b32encode(data_bytes)
	return data_enc.decode("utf-8")

def decode_b32(data):
	data_dec=base64.b32decode(data)
	return data_dec.decode("utf-8")

def encode_b16(data):
	data_bytes = data.encode("utf-8")
	data_enc=base64.b16encode(data_bytes)
	return data_enc.decode("utf-8")

def decode_b16(data):
	data_dec=base64.b16decode(data)
	return data_dec.decode("utf-8")

def encode_b58(data):
	data_bytes = data.encode("utf-8")
	data_enc=base58.b58encode(data_bytes)
	return data_enc.decode("utf-8")

def decode_b58(data):
	data_dec=base58.b58decode(data)
	return data_dec.decode("utf-8")

def encode_b2(data):
    return ' '.join(format(ord(x), 'b') for x in data)

def decode_b2(data):
    return ''.join(chr(int(x, 2)) for x in data.split(' '))
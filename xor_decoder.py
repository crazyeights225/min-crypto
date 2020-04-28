import math

from base_decoder import encode_b16, decode_b16

def clean_xor_cipher(data, key):
    n=len(data)
    data_arr=""
    for d, k in zip(data, key):
        x=ord(d)^ord(k)
        data_arr+=chr(x)
    return data_arr

def xor_test(data, key):
    data_hex=encode_b16(data)
    key_hex=encode_b16(key)
    data_dec=int(data_hex, 16)
    key_dec=int(key_hex, 16)
    data_xor=data_dec^key_dec
    hex_data_xor=hex(data_xor)[2:]
    #return decode_b16(hex_data_xor)
    return hex_data_xor

def xor_cipher(data, key):
    if(len(data)!=len(key)):
        n=math.ceil(len(data)/len(key))
        new_key=key*n
        return clean_xor_cipher(data, new_key)
    else:
        return clean_xor_cipher(data, key)


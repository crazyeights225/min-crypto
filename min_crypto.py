from tabulate import tabulate

from tar_struct import Tar
from rotn_decoder import *
from morse_decoder import *
from base_decoder import *
from dna_decoder import *
from xor_decoder import *

options_table_body=[["db64 [TARGET NO.]","Decode Base64"],
	["eb64 [TARGET NO.]", "Encode Base64"],
	["db32 [TARGET NO.]", "Decode Base32"],
	["eb32 [TARGET NO.]", "Encode Base32"],
	["db58 [TARGET NO.]", "Decode Base58"],
	["eb58 [TARGET NO.]", "Encode Base58"],
	["db62 [TARGET NO.]", "Decode Base62"],
	["eb62 [TARGET NO.]", "Encode Base62"],
	["db85 [TARGET NO.]", "Decode Base85"],
	["eb85 [TARGET NO.]", "Encode Base85"],
	["db16 [TARGET NO.]", "Decode Base16"],
	["eb16 [TARGET NO.]", "Encode Base16"],
	["db8 [TARGET NO.]", "Decode Base8"],
	["eb8 [TARGET NO.]", "Encode Base8"],
	["db2 [TARGET NO.]", "Decode Base2"],
	["eb2 [TARGET NO.]", "Encode Base2"],
	["rot13 [TARGET NO.]", "ROT13 cipher"],
	["rot13 [TARGET NO.] [AMOUNT]", "ROT13 by n cipher"],
	["rot13 [TARGET NO.] -bf", "Brute force ROT13 cipher"],
	["rot13 [TARGET NO.] -bf -k=[KEYWORD]", "Brute force ROT13 cipher with keyword"],
	["rot47 [TARGET NO.]", "ROT47 cipher"],
	["rot47 [TARGET NO.] [AMOUNT]", "ROT47 by n cipher"],
	["rot47 [TARGET NO.] -bf", "Brute force ROT47 cipher"],
	["rot47 [TARGET NO.] -bf -k=[KEYWORD]", "Brute force ROT47 cipher with keyword"],
	["evig [TARGET NO.] [KEY]", "Encode Vigenere cipher"],
	["dvig [TARGET NO.] [KEY]", "Decode Vigenere cipher"],
	["exor [TARGET NO.] [KEY]", "Encode/Decode XOR"],
	["dmorssy [TARGET NO.]", "Decode morse code (symbols)"],
	["emorssy [TARGET NO.]", "Encode morse code (symbols)"],
	["dmorsal [TARGET NO.]", "Decode morse code (words)"],
	["emorsal [TARGET NO.]", "Encode morse code (words)"],
	["ddna [TARGET NO.]", "Decode DNA cipher"],
	["edna [TARGET NO.]", "Encode DNA cipher"],
	["tar [STRING]", "Set target string"],
	["show", "Show target structure"],
	["out [FILENAME]", "Write target to file"],
	["in [FILENAME]", "Read target from file"],
	["search [SOMETHING]", "Search for encoding type"],
	["options", "Show options"],
	["quit/exit", "Quit"]]

option_table_headers=["Syntax", "Command"]

def search_ciphers(query):
	sub_table=[]
	query=query.lower()
	if(query=="all"):
		sub_table=options_table_body
	else:
		for i in options_table_body:
			if query in i[1].lower():
				sub_table.append(i)
	
	print("\n"+tabulate(sub_table, option_table_headers, tablefmt="simple")+"\n")

def show_options():
	print("\n"+tabulate([
	["[COMMAND] [TARGET NO.]","Encode/Decode Target"],
	["tar [STRING]", "Set target string"],
	["show", "Show target structure"],
	["out [FILENAME]", "Write target to file"],
	["in [FILENAME]", "Read target from file"],
	["search [SOMETHING]", "Search for encoding type"],
	["options", "Show options"],
	["quit/exit", "Quit"]
	], headers=["Syntax", "Command"],tablefmt="simple")+"\n")

def get_data(cmd, num_pos, tar):
	try:
		tar_no=int(cmd[num_pos:])
		data=tar.get_data(tar_no)
		if(data is None):
			print("invalid target")
		return data, tar_no
	except:
		print("invalid input")
		return None

def control_menu(cmd, tar):
	if(cmd[0:4]=="eb2 "):
		data=get_data(cmd,4,tar)
		if(data is not None):		
			new_data=encode_b2(data[0])
			tar.add_operation(new_data, "Encode B2", data[1])
	if(cmd[0:4]=="db2 "):
		data=get_data(cmd,4,tar)
		if(data is not None):		
			new_data=decode_b2(data[0])
			tar.add_operation(new_data, "Decode B2", data[1])
	if(cmd[0:4]=="db64"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=decode_b64(data[0])
			tar.add_operation(new_data, "Decode B64", data[1])
	if(cmd[0:4]=="eb64"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=encode_b64(data[0])
			tar.add_operation(new_data, "Encode B64", data[1])
	if(cmd[0:4]=="db16"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=decode_b16(data[0])
			tar.add_operation(new_data, "Decode B16", data[1])
	if(cmd[0:4]=="eb16"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=encode_b16(data[0])
			tar.add_operation(new_data, "Encode B16", data[1])
	if(cmd[0:4]=="db32"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=decode_b32(data[0])
			tar.add_operation(new_data, "Decode B32", data[1])
	if(cmd[0:4]=="eb32"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=encode_b32(data[0])
			tar.add_operation(new_data, "Encode B32", data[1])
	if(cmd[0:4]=="db58"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=decode_b58(data[0])
			tar.add_operation(new_data, "Decode B58", data[1])
	if(cmd[0:4]=="eb58"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=encode_b58(data[0])
			tar.add_operation(new_data, "Encode B58", data[1])
	if(cmd[0:5]=="rot13"):
		options=cmd.split(" ")
		if(len(options)==2):
			data=get_data(cmd,6,tar)
			if(data is not None):		
				new_data=rot13_cipher(data[0])
				tar.add_operation(new_data, "ROT13", data[1])
		elif(len(options)>2):
			if(len(options)==3 and options[2]=="-bf"):
				data=get_data(options[1],0,tar)
				if(data is not None):		
					brute_force_rot13n_cipher(data[0])
			elif(len(options)==4 and options[2]=="-bf" and options[3][0:3]=="-k="):
				data=get_data(options[1],0,tar)
				if(data is not None):		
					brute_force_rot13n_kw(data[0], options[3][3:])
			elif(len(options)==4 and options[3]=="-bf" and options[2][0:3]=="-k="):
				data=get_data(options[1],0,tar)
				if(data is not None):
					brute_force_rot13n_kw(data[0], options[2][3:])
			elif(len(options)==3):
				try:
					tarno=int(options[1])
					data=tar.get_data(tarno)
					tar2=int(options[2])
					if(data is not None):
						new_data=rot13n_cipher(data, tar2)
						tar.add_operation(new_data, "ROT13n "+str(tar2), tarno)
				except:
					print("Invalid data format")

		else:
			print("Invalid command")
	if(cmd[0:5]=="rot47"):
		options=cmd.split(" ")
		if(len(options)==2):
			data=get_data(cmd,6,tar)
			if(data is not None):		
				new_data=rot47_cipher(data[0])
				tar.add_operation(new_data, "ROT47", data[1])
		elif(len(options)>2):
			if(len(options)==3 and options[2]=="-bf"):
				data=get_data(options[1],0,tar)
				if(data is not None):		
					brute_force_rot47n_cipher(data[0])
			elif(len(options)==4 and options[2]=="-bf" and options[3][0:3]=="-k="):
				data=get_data(options[1],0,tar)
				if(data is not None):		
					brute_force_rot47n_kw(data[0], options[3][3:])
			elif(len(options)==4 and options[3]=="-bf" and options[2][0:3]=="-k="):
				data=get_data(options[1],0,tar)
				if(data is not None):
					brute_force_rot47n_kw(data[0], options[2][3:])
			elif(len(options)==3):
				try:
					tarno=int(options[1])
					data=tar.get_data(tarno)
					tar2=int(options[2])
					if(data is not None):
						new_data=rot47n_cipher(data, tar2)
						tar.add_operation(new_data, "ROT47n "+str(tar2), tarno)
				except:
					print("Invalid data format")

		else:
			print("Invalid command")
	

	if(cmd[0:4]=="edna"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=encode_dna(data[0])
			tar.add_operation(new_data, "Encode DNA cipher", data[1])
	if(cmd[0:4]=="ddna"):
		data=get_data(cmd,5,tar)
		if(data is not None):		
			new_data=decode_dna(data[0])
			tar.add_operation(new_data, "Decode DNA cipher", data[1])

	if(cmd[0:7]=="emorssy"):
		data=get_data(cmd,7,tar)
		if(data is not None):		
			new_data=encode_morse(data[0])
			tar.add_operation(new_data, "Encode MORSE SYM.", data[1])
	if(cmd[0:7]=="dmorssy"):
		data=get_data(cmd,7,tar)
		if(data is not None):		
			new_data=decode_morse(data[0])
			tar.add_operation(new_data, "Decode MORSE SYM.", data[1])
	if(cmd[0:7]=="emorsal"):
		data=get_data(cmd,7,tar)
		if(data is not None):		
			new_data=encode_morse_eng(data[0])
			tar.add_operation(new_data, "Encode MORSE ENG.", data[1])
	if(cmd[0:7]=="dmorsal"):
		data=get_data(cmd,7,tar)
		if(data is not None):		
			new_data=decode_morse_eng(data[0])
			tar.add_operation(new_data, "Decode MORSE ENG.", data[1])
	if(cmd[0:4]=="exor"):	
		tars=cmd.split(" ")
		try:
			tarno=int(tars[1])
			data=tar.get_data(tarno)
			tar2=tars[2]
			if(data is not None):
				new_data=xor_cipher(data, tar2)
				tar.add_operation(new_data, "XOR "+tar2, tarno)
		except:
			print("Invalid data format")
	if(cmd[0:4]=="evig"):	
		tars=cmd.split(" ")
		try:
			tarno=int(tars[1])
			data=tar.get_data(tarno)
			tar2=tars[2]
			if(data is not None):
				new_data=vigenere_encode(data, tar2)
				tar.add_operation(new_data, "Encode Vigenere "+tar2, tarno)
		except:
			print("Invalid data format")
	
	if(cmd[0:4]=="dvig"):	
		tars=cmd.split(" ")
		try:
			tarno=int(tars[1])
			data=tar.get_data(tarno)
			tar2=tars[2]
			if(data is not None):
				new_data=vigenere_decode(data, tar2)
				tar.add_operation(new_data, "Decode Vigenere "+tar2, tarno)
		except:
			print("Invalid data format")
	if(cmd[0:7]=="search "):
		query=cmd[7:]
		search_ciphers(query)

	if(cmd[0:4]=="tar "):
		data=cmd[4:]
		tar.clear_data()
		tar.add_operation(data, "Original String", "")
	if(cmd[0:4]=="out "):
		data=cmd[4:]
		tar.write_tar(data)
	if(cmd[0:3]=="in "):
		data=cmd[3:]
		tar.read_tar(data)
	if(cmd=="show"):
		tar.show_tar()
	if(cmd=="options"):
		show_options()


def main():
	cmd=""
	tar=Tar()
	while(cmd!="quit" and cmd!="exit"):
		cmd=str(input("\033[1;32;40m >> \033[0m"))
		control_menu(cmd, tar)
		
main()


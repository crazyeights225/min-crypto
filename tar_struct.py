from tabulate import tabulate

class Tar:
	def __init__(self):
		self.tar=[]
		self.operations=[]
		self.sources=[]
	
	def clear_data(self):
		self.tar.clear()
		self.operations.clear()
		self.sources.clear()
	
	def get_data(self, i):
		if(len(self.tar)<=i):
			return None
		else:
			return self.tar[i]	
	
	def format_big_text(self, txt):
		new_txt=""
		n=len(txt)
		for i in range(0, n//40):
			new_txt+=txt[i*40:(i*40)+40]+"\n"
		new_txt+=txt[-(n%40):]
		return new_txt				

	def get_tar_table(self):
		headers=["No.", "String", "Operation", "Source"]
		table=[]
		for i in range(0, len(self.tar)):
			if(len(self.tar[i])>40):
				tar_line=self.format_big_text(self.tar[i])
				table.append([i, tar_line, self.operations[i], self.sources[i]])
			else:
				table.append([i, self.tar[i], self.operations[i], self.sources[i]])
		return "\n"+tabulate(table, headers, tablefmt="psql")+"\n"
	

	def show_tar(self):
		print(self.get_tar_table())
	
	def add_operation(self, data_str, oper, source):
		self.tar.append(data_str)
		self.operations.append(oper)
		self.sources.append(source)

	def write_tar(self, filename):
		with open(filename, "w") as f:
			f.write(self.get_tar_table())

	def read_tar(self, filename):
		tar_str=""
		try:
			with open(filename, "r") as f:
				for i in f:
					tar_str+=i
			self.add_operation(tar_str, "Original String", "")
		except:
			print("Invalid File")

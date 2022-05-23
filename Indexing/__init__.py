#!/usr/bin/env python3

import json
from Lindex import lindex
from time import asctime

# Makes sure to only pass dictionaries with strings to `dtb().set()`

class dtb(lindex):
	def __init__(self, filename: str):
		super().__init__(StringIndexes = True)
		self.StringIndexes = True
		self.filename = filename
		self.FILEISBROKENSTRING = "{}"

	def QUERY(self) -> bool:
		# Attempts to read file
		try:
			with open(self.filename, "r") as file:
				json.loads(file.read())
				file.close()
		except Exception as e:
			# Tries to Write a Backup File
			try:
				with open(self.filename, "r") as file:
					data = file.read()
					file.close()
				name = "Backup--" + "-".join(asctime().split(":")) + ".dtb"
				with open(name, "w") as file:
					file.write(f"{e}\n{data}")
					file.close()
			except FileNotFoundError:
				pass
			# Resets the Original File to FILEISBROKENSTRING
			with open(self.filename, "w") as file:
				file.write(self.FILEISBROKENSTRING)
				file.close()				

	def GetInfo(self) -> dict:
		self.QUERY()
		with open(self.filename, "r") as data:
			super().__init__(dictionary = json.loads(data.read()), StringIndexes = self.StringIndexes)
			data.close()
		return self

	# Writes file to PersonInfo file
	def WriteInfo(self) -> bool:
		self.QUERY()
		with open(self.filename, "w") as data:
			data.write(json.dumps(self))
			data.close()
		return True


f = dtb("a").GetInfo()
path = [i for i in range(3)]
f.set(*path)
f.pprint()
f.WriteInfo()

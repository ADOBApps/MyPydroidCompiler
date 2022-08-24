# _*_ coding: utf-8 _*_
"""
Created on 23/08/2022
	Class to manage and compile
@author: ADOB
"""

import subprocess
import platform

class PyCompiler:

	def __init__ (self):
		print("Calling constructor")
		


	def __del__ (self):
		class_name = self.__class__.__name__
		print(class_name, "destroyed")
		##self.Starter()

	# Start and verify system
	def Starter (self):
		mysys = platform.system()
		print(("Estamos en {}").format(mysys))
		if(mysys == "Windows"):
			try:
				myproc = subprocess.run(["python", "--version"],
					stdout=subprocess.PIPE,
					check=True
				)
			except subprocess.CalledProcessError as error:
				print("Error: ", error)
			else:
				print("returncode:", myproc.returncode)
				print(("Have {} bytes in stdout:\n{}").format(
					len(myproc.stdout),
					myproc.stdout.decode('utf-8'))
				)
		else:
			print(("Estamos en {}").format(mysys))

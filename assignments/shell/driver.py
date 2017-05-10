from commands import main
from file_cmds import File
from ls import ls
import os


class Shell:

	"""
	Please follow the below syntax while execution

	1. ls  or ls path
	2. cp source destination
	3. cat/head/tail/less/wc filepath
	4. cd or cd ~ or cd path
	5. mkdir dir_name (you can pass multiple dirs separated by space)
	6. rmdir (same as mkdir)
	7. rm filename (same as mkdir)
	8. mv source destination
	9. chmod mode file
	10. cat file | grep keyword
	11. Single word commands: 'history/who/pwd'
	12. Type exit to exit the program

	"""

	def __init__(self, cmd):
		
		print(Shell.__doc__)
		self.cmd = cmd
		self.history = []

	
	def execute(self):

		self.history.append(self.cmd.split()[0])

		self.args = self.cmd.split()

		for param in ['>', '<', '>>', '|']:
			if param in self.cmd:
				# call redirect method
				pass

		
		# ls command
		if self.cmd.startswith("ls"):
			ls(self.args)
			

		# grep command
		if "grep" in self.cmd and len(self.args) == 5:
			path = self.args[1]
			keyword = self.args[-1]
			if os.path.exists(path):
				f = open(path, "r")
				for line in f.readlines():
					if keyword in line:
						print(line)
					else:
						print("")
			else:
				print("File doesn't exists..")
		

		# file commands
		if self.cmd.startswith("cp"):
			if len(self.args) < 3:
				print("Please check the syntax")
			else:
				File.cp(self.args[1], self.args[2])

		for cmd in ["cat", "head", "less", "tail", "wc"]:
			if self.cmd.startswith(cmd) and len(self.args) == 2:
				for arg in self.args.split():
					File.display(self.cmd, arg) 


		# basic commands
		for cmd in ["cd", "chmod", "mkdir", "mv", "pwd", "rmdir", "rm"]:
			if self.cmd.startswith(cmd):
				return main(self.cmd)


		if self.cmd.split()[0] == "history":
			print("\n".join(self.history))
			

		if self.cmd.split()[0] == "who":
			user = os.path.expanduser('~').split('\\')[-1]
			print("Currently Logged User: %s" %user)


def main():

	while True:
		shell_ip = input("[shell@~] ")
		shell = Shell(shell_ip)
		if  sheel_ip == "exit":
			break

if __name__ == "__main__":
	main()

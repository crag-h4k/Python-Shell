import sys, os, subprocess, shlex, time, re

result = 0
while 1:

	cmd = raw_input("PythonShell> ")
	cmd = cmd.split(" ")
	if cmd[0] != "":
		if cmd[0] == "pwd":
			print os.getcwd()
		elif cmd[0] == "help":
			print "Here are the available commands \nhelp\npwd\nls\nps\ncd\nfindFile\ndate\nopen\nkill\nfindWord\nexit"
		elif cmd[0] == "ls":
			print os.system('ls')
		elif cmd[0] == "ps":
			 print os.system('ps')
			 #pid = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]
		elif cmd[0] == "cd":
			if len(cmd) == 2:
				os.chdir(cmd[1])
			else:
				print "give me a valid directory"
			#os.chdir(path)
		elif cmd[0] == "date":
			print time.strftime("%c")
		elif cmd[0] == "kill":
			processID = input("What's the PID of the process you want to kill? ")
			processIDString = str(processID)
			os.system('pkill '+processIDString)
		elif cmd[0] == "findFile":
			fileName = input("What's the name of the file you want to find?")
			currentDirectory = os.getcwd()

			while True:
				fileList = os.listdir(currentDirectory)
				parentDirectory = os.path.dirname(currentDirectory)
				if fileName in fileList:
					print "File is here: ", currentDirectory
					break
				else:
					if currentDirectory == parentDirectory:
						print "File not found."
						break
					else:
						currentDirectory = parentDirectory
		elif cmd[0] == "open":
			programName = input("Which program do you want to start?")
			subprocess.call(['open', programName])
		elif cmd[0] == "findWord":
			fileName = input("Which file do you want to search for the word...cat...?")
			file = open(filename, "r")
			for line in file:
				if re.match("(.*)(C|c)at(.*)", line):
					print "Found a kitty!"
		elif cmd[0] == "exit":
			exit()
		else:
			continue

import subprocess

def run_command(command):

	command = command.rstrip()
	try:
		child = subprocess.check_output(command,shell=True)
	except Exception as e:
		child = "can't execute the command.."
	return child

execute = "ls /root/gitskills/net_safe/mysbprocess"
output = run_command(execute)
print(output)

#result:
# b'mysubprocess.py\nreadme_subprocess.txt\nsub001.py\n'
# [Finished in 0.1s]
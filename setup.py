import subprocess
s = subprocess.getstatusoutput(f'pip3 install requests')
b = subprocess.getstatusoutput(f'pip3 install termcolor')
print(s[1])
print(" ")
print(b[1])

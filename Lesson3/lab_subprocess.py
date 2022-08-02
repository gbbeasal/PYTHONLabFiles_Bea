#The subprocess module allows you to spawn new processes, 
#onnect to their input/output/error pipes, and obtain their return codes.


###executing shell commands:
import subprocess
proc = subprocess.run(['ls', '-l']) #outputs directory list w/o printing

print(proc, '\n\n') #if = to 0, script is a sucess

print('STDOUT:')
###capturing STDOUT:
proc = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
print(proc)
proc.stdout
proc.stderr

print(proc2.stdout)
print(proc2.stderr)
print(proc.stdout.decode()) #not for c9

###Intentionally raising errors:
proc = subprocess.run(['cat', 'somefile.txt'])

error_proc = subprocess.run(['cat', 'somefile.txt'], check=True)
import subprocess

rows, columns = subprocess.check_output(['stty', 'size']).split()
column = str(columns)
print("Your current shell width is " + column[2:-1] + ".")
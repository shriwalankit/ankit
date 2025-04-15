import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x ankit')
    os.system('./ankit')
elif bit == '32bit':
    os.system('chmod +x ankit32')
    os.system('./ankit32')
else:
    print('device not supported')

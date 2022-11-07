# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib

def md5(data):
    return hashlib.md5(str(data).encode()).hexdigest()

print(md5(1))
print(len(md5(1)))
print("p\"p")
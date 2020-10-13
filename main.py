import zipfile

PATH = 'password.zip'
DIGITS = 4

for x in range(pow(10, DIGITS)):
    password = str(x).zfill(DIGITS)
    with zipfile.ZipFile(PATH) as file:
        try:
            print(password)
            file.extractall(pwd=password.encode(), path='extracted')
            break
        except Exception as e:
            pass

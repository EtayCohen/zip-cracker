import sys
import zipfile


def crack(path, num_of_digits):
    for x in range(pow(10, num_of_digits)):
        password = str(x).zfill(num_of_digits)
        with zipfile.ZipFile(path) as file:
            try:
                print(password)
                file.extractall(pwd=password.encode(), path='extracted')
                break
            except Exception as e:
                pass


def main():
    if len(sys.argv) > 2:
        crack(sys.argv[1], int(sys.argv[2]))
    else:
        print("USAGE: python main.py path num_of_digits")


if __name__ == '__main__':
    main()

name = input('Enter a file name')
try:
    with open(name+'.txt','r') as f:
        if f.name == 'text.txt':
            raise Exception
except FileNotFoundError as e:
    print(f"file is not present {e}")
except Exception:
    print("This file cannot be read")
else:
    d = f.read()
    print(d)
finally:
    print("sorry")
    
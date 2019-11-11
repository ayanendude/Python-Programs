# Author: OMKAR PATHAK
# This program prints the entered message

def justPrint(text):
    '''This function prints the text passed as argument to this function'''
    print(text)

if __name__ == '__main__':
    justPrint('Hello')

def main():
    print ("Hello World!")

if __name__== "__main__":
    main()

print ("Guru99")

oldstring = 'I like Guru99'
newstring = oldstring.replace('like', 'love')
n1 = newstring.replace ('G','H')
print(newstring)
print (n1)

string="12345"
print(''.join(reversed(string)))
print(":".join("Python"))

word="guru99 career guru99"
print(word.split('r'))

a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")
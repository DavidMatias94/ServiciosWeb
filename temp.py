from flask import Flask
import string    
import random

app = Flask(__name__)
filePath = 'C:\\Users\\david\\.spyder-py3\\cadenas.txt'

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/generate')
def generate():
    S = random.randint(10, 20)
    ran = ''.join(random.choices(string.ascii_letters, k = S))
    #''.join(random.choices(string.ascii_letters + string.digits, k = S))
    with open(filePath, 'a') as f:
        f.write(ran + '\n')

    return "Nueva cadena generada: " + ran

@app.route('/file')
def file():
    file = open(filePath, 'r')
    lines = file.read()
    return str(lines)

@app.route('/find/<cadena>')
def find(cadena):
    # Using readlines()
    file = open(filePath, 'r')
    lines = file.readlines()
    string = []
    count = 0
    for line in lines:
        a,b = 'áéíóúÁÉÍÓÚ','aeiouAEIOU'
        trans = str.maketrans(a,b)
        #print(line.translate(trans))
        find = line.find(cadena)
        print(line)
        print(line.translate(trans))
        print(line.translate(trans).casefold())
        find = line.translate(trans).casefold().find(cadena.translate(trans).casefold())
        if (find != -1):
            start = find
            stop = start + len(cadena)
            #print (line[start:stop])
            string.append(line[start:stop])
            count += 1
        else:
            print ("Doesn't contains given substring")
    
    return 'Coincidencias de la cadena \'' + cadena + '\': ' + str(count) + ' --> '  + str(string)

if __name__ == '__main__':
    if checkFileExistance(filePath) == False:
        open(filePath, 'a').close()
    app.run(host='localhost', port=12345, debug=True)


import random


def getData(fileName):
    with open (fileName, 'r') as file:
        data = file.read().replace('\n', '')
        data = data.split(',')

    return data

def pickQuestion(data):
    question = random.choice(data)
    return question

def removeQuestion(fileName, question):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    with open(fileName, 'w') as file:
        for line in lines:
            if line.strip(',\n') != question:
                file.write(line)
        
        file.truncate()


    
if __name__ == "__main__":
    fileName = input("What is the name of your Question file?: ")
    try:
        data = getData(fileName)
        question = pickQuestion(data)
        removeQuestion(fileName,question)
        print(question)
    except IndexError:
        print("Congratulations! It looks like you have completed all the questions")
    except FileNotFoundError:
        print("I couldn't find that file, make sure it exists in the same folder as the script")


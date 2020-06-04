import random


def getData(self,fileName):
    with open (fileName, 'r') as file:
        data = file.read().replace('\n', '')

    return data

def pickQuestion(self,data):
    question = random.choice(data)
    return question

def removeQuestion(self,fileName, question):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    with open(fileName, 'w') as file:
        for line in lines:
            if line.strip('\n') != question:
                file.write(line)
        
        file.truncate()


    
if __name__ == "__main__":
    fileName = input("What is the name of your Question file?: ")
    data = getData(fileName)
    question = pickQuestion(data)
    removeQuestion(fileName,question)
    print(question)

                    

    
        
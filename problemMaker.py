A1 = 19
A2 = 19
A3 = 31
A4 = 31
A5 = 19
A6 = 19
B = 10


if __name__ == "__main__":
    with open ('stat2003_questions.txt', 'w') as file:
        for question in range(1,A1+1):
            file.write('A1 Q'+str(question)+','+'\n')
        for question in range(1,A2+1):
            file.write('A2 Q'+str(question)+',' +'\n')
        for question in range(1,A3+1):
            file.write('A3 Q'+str(question)+',' +'\n')
        for question in range(1,A4+1):
            file.write('A4 Q'+str(question)+',' +'\n')
        for question in range(1,A5+1):
            file.write('A5 Q' +str(question)+',' +'\n')
        for question in range(1,A6+1):
            file.write('A6 Q'+str(question)+',' +'\n')
        for question in range(1,B+1):
            file.write('B Q' + str(question)+',' +'\n')



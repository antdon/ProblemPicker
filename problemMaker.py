A1 = 19
A2 = 19
A3 = 31
A4 = 31
A5 = 19
A6 = 19
B = 10
Ex15 = 8
Ex16 = 9
Ex17 = 8
Ex18 = 8
Ex19 = 7


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
        for question in range(1,Ex15+1):
            file.write('2015 Exam Q' + str(question)+',' +'\n')
        for question in range(1,Ex16+1):
            file.write('2016 Exam Q' + str(question)+',' +'\n')
        for question in range(1,Ex17+1):
            file.write('2017 Exam Q' + str(question)+',' +'\n')
        for question in range(1,Ex18+1):
            file.write('2018 Exam Q' + str(question)+',' +'\n')
        for question in range(1,Ex19+1):
            file.write('2019 Exam Q' + str(question)+',' +'\n')
        
        
        
        
        
        



alphabet = ['a)','b)','c)','d)','e)','f)','g)','h)','i)','j)','k)','l)','m)','n)','o)','p)','q)','r)','s)','t)','u)','v)','w)','x)','y)','z)']
if __name__ == "__main__":
    newFileName = input("what would you like to name your question file? ")
    numOfQuestions = int(input("How many questions would you like in your file? "))
    numOfSubQuestions = int(input("How many subquestions does each question have? 1-26 "))

    
    with open (newFileName, 'w') as file:
        for question in range(1,numOfQuestions):
            for subquestion in range(1,numOfSubQuestions):
                file.write('Q' + str(question)+ alphabet[subquestion-1]+'\n')
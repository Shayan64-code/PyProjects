
# quiz = [
#     {"question": "What is the capital of France", "answer": "Paris"},
#     {"question": "What is 2+2", "answer": "4"},
#     {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"}
# ]

# money = 0
# for item in quiz:                                             #Improved one
#     print("Q:", item["question"])
#     ans = input("Your Answer ")
#     if ans.strip().lower() == item["answer"].lower():
#         money += 100
#         print("Your Answer is correct")
#         print("Add Rs: ", money)
#     else:
#         print("This is wrong")
#         money -= 100
#         print("Deduct Rs: ", money)


# #Example 2:  Using Tuples in list
# quiz = [
#     ("What is the capital of Italy", "Rome"),
#     ("What is 12 x 2", "24"),
#     ("What is the King of Fruits", "Mango")
# ]

# for question, answer in quiz:
#     print("Q:", question)
#     ans = input("Your Answer: ")
#     if ans.strip().lower() == answer.lower():
#         print("Your ans is correct")
#     else:
#         print("This is Wrong")

# #Example with only Dictionary

# quiz = {
#     "What is the color of sky?": "Blue",
#     "What is 10 / 2?": "5",
#     "What is 2 + 5 is": "7"
# }

# for question, answer in quiz.items():
#     print("Q:", question)
#     ans = input("Your Answer: ")
#     if ans.strip().lower() == answer.lower():
#         print("Your ans is correct")
#     else:
#         print("This is Wrong")


# #Practice:
# KBC = [
#     {"question":"What is Capital of France: ","answer":"Paris"},
#     {"question":"What is 2+2: ","answer":"4"},
#     {"question":"What is the King of Fruits: ","answer":"Mango"}
# ]

# money = 0
# for x in KBC:
#     print(x["question"])
#     ans = input("Give Your Answer: ")
#     if ans.strip().lower()==x["answer"].strip().lower():
#         print("Your answer is correct!!!")
#         money +=100                          #money/or every other variable cannot assign directly in print or
#         print("Money added Rs 100:", money)   #other like this money+=100.
#     else:
#         print("You are wrong")
#         money -=100
#         print("Money deducted Rs 100:", money) 
# print("Money Taken Home:",money)


questions = [
    ["What is Capital of France: ","Paris","Italy","German","France","a"],
    ["What is 2+2: ","5","11","4","12", "c"],
    ["What is the King of Fruits: ","Apple","Mango","Banana","Kiwi","b"],
    ["What is my name: ","Ahmed","Farooq","Ali","Shayan","d"]
]
levels = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000, 2560000, 5120000, 10240000, 20480000]

#Example with List in List:

# money = 0
# for i in range(0, len(questions)):
#     question = questions[i]
#     #print(questions[i])
#     print(f"Question for Rs. {levels[i]}")
#     print(f"Question is: {question[0]}")
#     print(f"a. {question[1]}        b. {question[2]}")
#     print(f"c. {question[3]}        d. {question[4]}")

#     reply = input("Your Answer: ")
#     if reply == question[-1]:
#         print(f"Your answer is correct, Added Rs:{levels[i]}")
#         money = int(levels[i])
#     else:
#         print(f"Your answer is wrong")
#         break
# print(f"Money you earned: Rs {money}")

###Same but little changes.
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    #print(questions[i])
    print(f"Question for Rs. {levels[i]}")
    print(f"Question is: {question[0]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")

    reply = input("Your Answer: ")
    if reply == question[-1]:
        print(f"Your answer is correct, Added Rs:{levels[i]}")
        if i == 0:
            money = int(levels[0])
        elif i == 3:
            money = int(levels[3])
        elif i == 7:
            money = int(levels[7])
        elif i == 11:
            money = int(levels[11])
    else:
        print(f"Your answer is wrong")
        break
print(f"Money you earned: Rs {money}")

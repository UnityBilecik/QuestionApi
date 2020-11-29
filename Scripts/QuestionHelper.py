import json

def ReadData():
    with open("Data/Questions.json","r",encoding="utf-8") as file:
        return json.load(file)


def GetQuestion(amount=5,diffuculty="",questionType=""):
    questionList = list()
    questions = ReadData()

    for item in questions:
        if(diffuculty!="" and item["diffuculty"]!=diffuculty):
            continue

        if(questionType!="" and item["questionType"]!=questionType):
            continue

        questionList.append(item)
        if(questionList.__len__() > amount-1):
            break;

    return questionList


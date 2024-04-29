import os
#import requests
#import json
import random
from datetime import datetime

VERSION = [0, 0, 1]
NUMBER_SYMBOLS = ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑪", "⑫", "⑬", "⑭", "⑮", "⑯", "⑰", "⑱", "⑲", "⑳", "㉑", "㉒", "㉓", "㉔", "㉕", "㉖", "㉗", "㉘", "㉙", "㉚", "㉛", "㉜", "㉝", "㉞", "㉟", "㊱", "㊲", "㊳", "㊴", "㊵", "㊶", "㊷", "㊸", "㊹", "㊺", "㊻", "㊼", "㊽", "㊾", "㊿"]

def writeTxt(fileName, givenName, content):
    name = "생성된 문제 파일/" + givenName + " - " + fileName + " @SleepySoong.txt"
    file = open(name, 'w')
    file.write(content)
    file.close()
    print("  [!] 파일 [ " + fileName + ".txt ] 이 저장되었습니다!")

"""
def verbVariation(cash, originalContent):
    content = originalContent
    verbList = []
    for word in content.split(' '):
        if word.encode().isalpha():
            www = word.lower()
            isVerb = False
            if www in cash:
                isVerb = cash[www]
            else:
                data = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + www).json()
                try:
                    data = data[0]["meanings"]
                except:
                    isVerb = False # Error
                    cash[www] = isVerb
                    print("{www}를 영어 사전에서 조회하는데 실패했습니다.. 동사가 아닌 단어로 등록합니다")
                    continue
                for meaning in data:
                    if meaning['partOfSpeech'] == "verb":
                        isVerb = True
                        print("{www}를 영어 사전에서 조회한 결과 동사입니다.. 캐쉬 데이터에 추가합니다")
                        continue
            cash[www] = isVerb
            if isVerb:
                verbList.append(www)
    with open('단어 사전 캐쉬/data.json','w') as f:
    json.dump(cash, f, ensure_ascii=False, indent=4)
    return ?
"""

def beVerbVariation(originalContent):
    if(originalContent == ""):
        return "본문을 입력하지 않았습니다"
    content = originalContent
    #beVerbList_simpleTense = ['is', 'am', 'are'] #am과 is의 구분은 너무 쉬워서 제외 함
    beVerbList_simpleTense = ['is', 'are']
    beVerbList_pastTense   = ['was', 'were']
    for verb in beVerbList_simpleTense:
        content = content.replace(" " + verb + " ", " ***" + beVerbList_simpleTense[random.randint(0, len(beVerbList_simpleTense) - 1)] + "*** ")
    for verb in beVerbList_pastTense:
        content = content.replace(" " + verb + " ", " ***" + beVerbList_pastTense[random.randint(0, len(beVerbList_pastTense) - 1)] + "*** ")
    return content

def orderVariation(originalContent):
    if(originalContent == ""):
        return "본문을 입력하지 않았습니다"
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
    if(len(content) < 6):
        return "7개 이상의 문장으로 구성되어 있는 지문만 순서 문제를 제작할 수 있습니다"
    firstMassCut = round(len(content) / 3)
    secondMassCut = firstMassCut * 2
    firstMassContent = ""
    for firstIndex in range(0, firstMassCut):
        firstMassContent = firstMassContent + content[firstIndex] + "."
    secondMassContent = ""
    for secondIndex in range(firstMassCut + 1, secondMassCut):
        secondMassContent = secondMassContent + content[secondIndex] + "."
    thirdMassContent = ""
    for thirdIndex in range(secondMassCut + 1, len(content)):
        thirdMassContent = thirdMassContent + content[thirdIndex] + "."
    contentList = [firstMassContent, secondMassContent, thirdMassContent]
    shuffledList = contentList.copy()
    random.shuffle(shuffledList)
    firstOrder = 0
    secondOrder = 0
    thirdOrder = 0
    for i in range(len(shuffledList)):
        if shuffledList[i] == contentList[0]:
            firstOrder = ['A', 'B', 'C'][i]
        elif shuffledList[i] == contentList[1]:
            secondOrder = ['A', 'B', 'C'][i]
        else:
            thirdOrder = ['A', 'B', 'C'][i]

    return "[A] " + shuffledList[0] + "\n\n[B] " + shuffledList[1] + "\n\n[C] " + shuffledList[2] + "\n\n\n** 정답: " + firstOrder + " --> " + secondOrder + " --> " + thirdOrder

def blankVariation(originalContent):
    if(originalContent == ""):
        return "본문을 입력하지 않았습니다"
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
    if(len(content) < 6):
        return "7개 이상의 문장으로 구성되어 있는 지문만 빈칸 문제를 제작할 수 있습니다"
    sentenceNumToRemove = random.randint(0, len(content)-1)
    removedSentence = content[sentenceNumToRemove]
    content[sentenceNumToRemove] = "________________"
    return "다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.\n\n" + ". ".join(content) + "\n\n\n** 정답: " + removedSentence

def insert_shuffle(num):
    sentenceNum = num.copy()
    random.shuffle(sentenceNum)
    first = sentenceNum.pop()
    second = sentenceNum.pop()
    third = sentenceNum.pop()
    fourth = sentenceNum.pop()
    fifth = sentenceNum.pop()
    return [first, second, third, fourth, fifth]

def insertVariation(text):
    text = text.replace(". ", ".") # 나중에 .을 기준으로 문장을 나누기 위한 작업
    text = text.replace(".\n", ".") # 나중에 .을 기준으로 문장을 나누기 위한 작업
    sentences = text.split(".") # .을 기준으로 문장을 나누어 리스트에 담음
    count = len(sentences) # 문장의 갯수
    randomIndex = random.randint(0, count-1) # 삽입 문제로 출제할 문장의 인덱스를 정함
    randomSentence = sentences[randomIndex] # 위에서 정한 인덱스에 있는 문장 (문제로 출제될 문장)
    del sentences[randomIndex]
    indexesWithOption = [randomIndex] # 앞에 선지가 달릴 문장들의 인덱스를 담아두는 리스트 (해당 문장이 제거되면 뒤에 있는 문장에는 무조건 선지가 붙어야하고 이게 정답임)
    tempIndexes = list(range(0, count-1)) # 문장 하나를 제거 했으니까 -1을 해줌
    del tempIndexes[randomIndex]
    random.shuffle(tempIndexes)
    indexesWithOption += tempIndexes[0:4] # 선지를 넣을 4개의 인덱스를 랜덤으로 정하여 추가
    indexesWithOption.sort() # 정렬을 하지 않으면 randomIndex가 무조건 1번이 됨
    answer = -1
    temp = 0
    for i in indexesWithOption:
        temp += 1
        sentences[i] = NUMBER_SYMBOLS[temp] + " " + sentences[i]
        if i == randomIndex:
            answer = temp
    return "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.\n\n[ " + randomSentence + " ]\n\n" + ". ".join(sentences) + "\n\n\n** 정답: " + NUMBER_SYMBOLS[answer]

if not os.path.exists("본문 파일"):
    os.mkdir("본문 파일")

if not os.path.exists("생성된 문제 파일"):
    os.mkdir("생성된 문제 파일")

"""
if not os.path.isfile("단어 사전 캐쉬/data.json"):
    with open('단어 사전 캐쉬/data.json','w') as f:
        json.dump({}, f, ensure_ascii=False, indent=4)

with open("단어 사전 캐쉬/data.json", "r") as json_file:
    cash = json.load(json_file)

print("\n\n  [!] 단어 사전 캐쉬를 불러옵니다...  | " + ", ".join(cash) + "\n\n")
"""

while(True):
    givenName = input("\n\n  ■ 영어 변형 문제 제작기 | @SleepySoong ■\n  [!] 문제를 생성할 파일의 이름을 확장자를 제외하고 입력해주세요 (*.txt만 지원합니다) : \n  - 주의: 변형 문제를 만들기 위해선 7개 이상의 문장으로 구성된 영어 본문이 필요합니다 \n")
    if not os.path.isfile("본문 파일/" + givenName + ".txt"):
        print("  [!] 존재하지 않는 파일 입니다. 확장자가 txt가 맞는지, 본문 파일 폴더에 파일이 있는지 확인해주세요!")
    else:
        print("  [!] 파일을 로딩중입니다: " + givenName +  ".txt")
        break

file = open("본문 파일/" + givenName + ".txt", 'rt', encoding='UTF8')
originalContent = ''.join(file.readlines()).replace("\n", "")
file.close()

print("\n\n  [!] 변형 문제 제작을 시작합니다.. 시간이 어느 정도 소요될 수 있습니다..\n\n")

# be 동사 변형 문제
writeTxt("be 동사 변형 문제", givenName, beVerbVariation(originalContent))

# 순서 배열 문제
writeTxt("순서 배열 문제", givenName, orderVariation(originalContent))

# 빈칸 문제
writeTxt("빈칸 문제", givenName, blankVariation(originalContent))

# 삽입 문제
writeTxt("삽입 문제", givenName, insertVariation(originalContent))

# 동사 변경 문제
#writeTxt("동사 변형 문제.txt", verbVariation(originalContent))

print("\n\n  [!] 변형 문제 제작이 성공적으로 완료되었습니다. 프로그램을 종료합니다.")
print("  - 원본 파일: " + givenName + ".txt")

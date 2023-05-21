import os
#import requests
#import json
import random
from datetime import datetime

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
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
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
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
    sentenceNumToRemove = random.randint(0, len(content)-1)
    removedSentence = content[sentenceNumToRemove]
    content[sentenceNumToRemove] = "________________"
    return ". ".join(content) + "\n\n\n** 빈칸에 들어갈 문장: " + removedSentence

def insert_shuffle(num):
    sentenceNum = num.copy()
    random.shuffle(sentenceNum)
    first = sentenceNum.pop()
    second = sentenceNum.pop()
    third = sentenceNum.pop()
    fourth = sentenceNum.pop()
    fifth = sentenceNum.pop()
    return [first, second, third, fourth, fifth]

def insertVariation(originalContent):
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
    if(len(content) < 6):
        return "7개 이상의 문장으로 구성되어 있는 지문만 삽입 문제를 제작할 수 있습니다"
    sentenceNum = [*range(0, len(content))]
    data = insert_shuffle(sentenceNum)
    error = 0
    while(True):
        if abs(data[0] - data[1]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[0] - data[2]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)     
        elif abs(data[0] - data[3]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[0] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[1] - data[2]) < 2:
            error = error + 1+ "번째 
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[1] - data[3]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[1] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)  
        elif abs(data[2] - data[3]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum) 
        elif abs(data[2] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum) 
        elif abs(data[3] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)  
        else:
            print("  [!] 삽입 문제 | 사용할 수 있는 경우의 수를 찾았습니다: [" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]")
            break
    first = data[0]
    second = data[1]
    third = data[2]
    fourth = data[3]
    fifth = data[4]
    removedSentence = content[first]
    content[first]  = "● ★"
    content[second] = "● " + content[second]
    content[third]  = "● " + content[third]
    content[fourth] = "● " + content[fourth]
    content[fifth]  = "● " + content[fifth]
    textedContent = ". ".join(content)
    textedContent = textedContent.replace("●", "①", 1)
    textedContent = textedContent.replace("●", "②", 1)
    textedContent = textedContent.replace("●", "③", 1)
    textedContent = textedContent.replace("●", "④", 1)
    textedContent = textedContent.replace("●", "⑤", 1)
    content = textedContent.split(".")
    if "" in content:
        content.remove("")
    return "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.\n\n[ " + removedSentence + " ]\n\n" + textedContent.replace("★.", "") + "\n\n\n** 정답: " + content[first][0:3]
    
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
    givenName = input("\n\n  ■ 영어 변형 문제 제작기 | @SleepySoong ■\n  [!] 문제를 생성할 파일의 이름을 확장자를 제외하고 입력해주세요 (*.txt만 지원합니다) : ")
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

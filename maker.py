import os
import random
from datetime import datetime
import itertools

VERSION = [0, 0, 3]

NUMBER_SYMBOLS = ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑪", "⑫", "⑬", "⑭", "⑮", "⑯", "⑰", "⑱", "⑲", "⑳", "㉑", "㉒", "㉓", "㉔", "㉕", "㉖", "㉗", "㉘", "㉙", "㉚", "㉛", "㉜", "㉝", "㉞", "㉟", "㊱", "㊲", "㊳", "㊴", "㊵", "㊶", "㊷", "㊸", "㊹", "㊺", "㊻", "㊼", "㊽", "㊾", "㊿"]
ORDER_CANDIDATES = ["A", "B", "C"]


def writeTxt(fileName, givenName, content):
    name = "생성된 문제 파일/" + givenName + " - " + fileName + " @SleepySoong.txt"
    file = open(name, 'w')
    file.write(content)
    file.close()
    print("  [!] 파일 [ " + fileName + ".txt ] 이 저장되었습니다!")


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


def orderVariation(text):
    def convertNumToStr(option: list) -> list: # 숫자로 구성된 배열 순서 정보가 담긴 리스트를 문자(A, B, C)로 변경해주는 함수
        return [ORDER_CANDIDATES[option.index(0)], ORDER_CANDIDATES[option.index(1)], ORDER_CANDIDATES[option.index(2)]]
    def convertListToStr(option: list) -> str: # 선지 정보가 담긴 리스트를 문자 (예시; (A) - (C) - (B))로 변경해주는 함수
        return f"({option[0]}) - ({option[1]}) - ({option[2]})"
    sentences = convertText(text)
    firstSentence = sentences.pop(0) # 첫 번째 문장을 저장해두고 리스트에서 제거 함
    count = len(sentences) # 문장의 갯수
    criterion = int(count/3) # 한 덩어리에 몇 문장을 넣어야 할지 정함 (한 덩어리에 criterion 문장)
    mass = [sentences[0:criterion], sentences[criterion:criterion*2], sentences[criterion*2:]] # criterion을 기준으로 문장을 3 덩어리로 나눠서 저장
    temp = list(range(3)) # 3 덩어리를 섞기 위한 작업 시작
    random.shuffle(temp) # 0, 1, 2 -> x, y, z (덩어리 섞기)
    mass[0], mass[1], mass[2] = mass[temp[0]], mass[temp[1]], mass[temp[2]] # 섞기
    optionPermutations = list(itertools.permutations(list(range(0, 3)))) # 선지를 만들기 위해 0, 1, 2로 만들 수 있는 모든 조합 찾기
    optionPermutations.remove(tuple(temp)) # 정답을 제외하고 선지에 넣을 나머지 4개를 찾을 계획
    random.shuffle(optionPermutations) # 랜덤으로 4개를 찾기 위해 섞음
    options = [temp] + list(map(list, optionPermutations[0:4])) # 정답 선지 + 랜덤 선지 4개
    options.sort() # 선지 배열
    options = list(map(convertNumToStr, map(list, options))) # 숫자를 영어로 변환
    correctOrder = convertNumToStr(temp) # 정답 선지
    print(options)
    return "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것을 고르시오.\n\n[ " + str(firstSentence) + " ]\n\n\n(A) " + ". ".join(mass[0]) + "\n\n(B) " + ". ".join(mass[1]) + "\n\n(C) " + ". ".join(mass[2]) + "\n\n\n" + NUMBER_SYMBOLS[1] + convertListToStr(options[0]) + "\n" + NUMBER_SYMBOLS[2] + convertListToStr(options[1]) + "\n" + NUMBER_SYMBOLS[3] + convertListToStr(options[2]) + "\n" + NUMBER_SYMBOLS[4] + convertListToStr(options[3]) + "\n" + NUMBER_SYMBOLS[5] + convertListToStr(options[4]) + "\n\n\n** 정답: " + NUMBER_SYMBOLS[options.index(correctOrder) + 1]


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


def insertVariation(text):
    sentences = convertText(text)
    count = len(sentences) # 문장의 갯수
    randomIndex = random.randint(0, count-1) # 삽입 문제로 출제할 문장의 인덱스를 정함
    randomSentence = sentences[randomIndex] # 위에서 정한 인덱스에 있는 문장 (문제로 출제될 문장)
    del sentences[randomIndex]
    indexesWithOption = [randomIndex] # 앞에 선지가 달릴 문장들의 인덱스를 담아두는 리스트 (해당 문장이 제거되면 뒤에 있는 문장에는 무조건 선지가 붙어야하고 이게 정답임)
    tempIndexes = list(range(0, count-1)) # 문장 하나를 제거 했으니까 -1을 해줌
    del tempIndexes[randomIndex]
    random.shuffle(tempIndexes)
    indexesWithOption += tempIndexes[0:4] # 선지를 넣을 4개의 인덱스를 랜덤으로 정하여 추가
    indexesWithOption.sort() # 정렬을 하지 않으면 randomIndex가 무조건 선지  1번이 됨
    answer = -1
    temp = 0
    for i in indexesWithOption:
        temp += 1
        sentences[i] = NUMBER_SYMBOLS[temp] + " " + sentences[i]
        if i == randomIndex:
            answer = temp
    return "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.\n\n[ " + randomSentence + " ]\n\n" + ". ".join(sentences) + "\n\n\n** 정답: " + NUMBER_SYMBOLS[answer]


def convertText(text: str) -> list:
    text = text.replace(". ", ".") # 나중에 .을 기준으로 문장을 나누기 위한 작업
    text = text.replace(".\n", ".") # 나중에 .을 기준으로 문장을 나누기 위한 작업
    return text.split(".") # .을 기준으로 문장을 나누어 리스트에 담음


if not os.path.exists("본문 파일"):
    os.mkdir("본문 파일")

if not os.path.exists("생성된 문제 파일"):
    os.mkdir("생성된 문제 파일")

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

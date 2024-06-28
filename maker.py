import os
import random
import itertools

VERSION = [0, 0, 3]

NUMBER_SYMBOLS = ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑪", "⑫", "⑬", "⑭", "⑮", "⑯", "⑰", "⑱", "⑲", "⑳", "㉑", "㉒", "㉓", "㉔", "㉕", "㉖", "㉗", "㉘", "㉙", "㉚", "㉛", "㉜", "㉝", "㉞", "㉟", "㊱", "㊲", "㊳", "㊴", "㊵", "㊶", "㊷", "㊸", "㊹", "㊺", "㊻", "㊼", "㊽", "㊾", "㊿"]
ORDER_CANDIDATES = ["A", "B", "C"]


def write_txt(file_name, name, contents):
    file = open("생성된 문제 파일/" + name + " - " + file_name + " @SleepySoong.txt", 'w')
    file.write(contents)
    file.close()
    print("  [!] 파일 [ " + file_name + ".txt ] 이 저장되었습니다!")


def be_verb_variation(text):
    if(text == ""):
        return "본문을 입력하지 않았습니다"
    BE_VERB_LIST_SIMPLE_TENSE = ['is', 'are'] # am과 is의 구분은 너무 쉬워서 제외 함
    BE_VERB_LIST_PAST_TENSE   = ['was', 'were']
    for verb in BE_VERB_LIST_SIMPLE_TENSE:
        text = text.replace(" " + verb + " ", " ***" + BE_VERB_LIST_SIMPLE_TENSE[random.randint(0, len(BE_VERB_LIST_SIMPLE_TENSE) - 1)] + "*** ")
    for verb in BE_VERB_LIST_PAST_TENSE:
        text = text.replace(" " + verb + " ", " ***" + BE_VERB_LIST_PAST_TENSE[random.randint(0, len(BE_VERB_LIST_PAST_TENSE) - 1)] + "*** ")
    return text


def order_variation(text):
    def convert_num_to_str(option: list) -> list: # 숫자로 구성된 배열 순서 정보가 담긴 리스트를 문자(A, B, C)로 변경해주는 함수
        return [ORDER_CANDIDATES[option.index(0)], ORDER_CANDIDATES[option.index(1)], ORDER_CANDIDATES[option.index(2)]]
    def convert_list_to_str(option: list) -> str: # 선지 정보가 담긴 리스트를 문자 (예시; (A) - (C) - (B))로 변경해주는 함수
        return f"({option[0]}) - ({option[1]}) - ({option[2]})"
    stcs = convert_txt(text)
    first_stc = stcs.pop(0) # 첫 번째 문장을 저장해두고 리스트에서 제거 함
    count = len(stcs) # 문장의 갯수
    criterion = int(count/3) # 한 덩어리에 몇 문장을 넣어야 할지 정함 (한 덩어리에 criterion 문장)
    mass = [stcs[0:criterion], stcs[criterion:criterion*2], stcs[criterion*2:]] # criterion을 기준으로 문장을 3 덩어리로 나눠서 저장
    temp = list(range(3)) # 3 덩어리를 섞기 위한 작업 시작
    random.shuffle(temp) # 0, 1, 2 -> x, y, z (덩어리 섞기)
    mass[0], mass[1], mass[2] = mass[temp[0]], mass[temp[1]], mass[temp[2]] # 섞기
    option_perms = list(itertools.permutations(list(range(0, 3)))) # 선지를 만들기 위해 0, 1, 2로 만들 수 있는 모든 조합 찾기
    option_perms.remove(tuple(temp)) # 정답을 제외하고 선지에 넣을 나머지 4개를 찾을 계획
    random.shuffle(option_perms) # 랜덤으로 4개를 찾기 위해 섞음
    options = [temp] + list(map(list, option_perms[0:4])) # 정답 선지 + 랜덤 선지 4개
    options.sort() # 선지 배열
    options = list(map(convert_num_to_str, map(list, options))) # 숫자를 영어로 변환
    correct_order = convert_num_to_str(temp) # 정답 선지
    print(options)
    return "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것을 고르시오.\n\n[ " + str(first_stc) + " ]\n\n\n(A) " + ". ".join(mass[0]) + "\n\n(B) " + ". ".join(mass[1]) + "\n\n(C) " + ". ".join(mass[2]) + "\n\n\n" + NUMBER_SYMBOLS[1] + convert_list_to_str(options[0]) + "\n" + NUMBER_SYMBOLS[2] + convert_list_to_str(options[1]) + "\n" + NUMBER_SYMBOLS[3] + convert_list_to_str(options[2]) + "\n" + NUMBER_SYMBOLS[4] + convert_list_to_str(options[3]) + "\n" + NUMBER_SYMBOLS[5] + convert_list_to_str(options[4]) + "\n\n\n** 정답: " + NUMBER_SYMBOLS[options.index(correct_order) + 1]


def blank_variation(text):
    if(text == ""):
        return "본문을 입력하지 않았습니다"
    text = text.split(".")
    if "" in text:
        text.remove("")
    if(len(text) < 6):
        return "7개 이상의 문장으로 구성되어 있는 지문만 빈칸 문제를 제작할 수 있습니다"
    stc_num_to_del = random.randint(0, len(text)-1)
    removed_stc = text[stc_num_to_del]
    text[stc_num_to_del] = "________________"
    return "다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.\n\n" + ". ".join(text) + "\n\n\n** 정답: " + removed_stc


def insert_variation(text):
    stcs = convert_txt(text)
    count = len(stcs) # 문장의 갯수
    rand_idx = random.randint(0, count-1) # 삽입 문제로 출제할 문장의 인덱스를 정함
    rand_stc = stcs[rand_idx] # 위에서 정한 인덱스에 있는 문장 (문제로 출제될 문장)
    del stcs[rand_idx]
    idxes_with_option = [rand_idx] # 앞에 선지가 달릴 문장들의 인덱스를 담아두는 리스트 (해당 문장이 제거되면 뒤에 있는 문장에는 무조건 선지가 붙어야하고 이게 정답임)
    temp_idxes = list(range(0, count-1)) # 문장 하나를 제거 했으니까 -1을 해줌
    del temp_idxes[rand_idx]
    random.shuffle(temp_idxes)
    idxes_with_option += temp_idxes[0:4] # 선지를 넣을 4개의 인덱스를 랜덤으로 정하여 추가
    idxes_with_option.sort() # 정렬을 하지 않으면 rand_idx가 무조건 선지  1번이 됨
    answer = -1
    temp = 0
    for i in idxes_with_option:
        temp += 1
        stcs[i] = NUMBER_SYMBOLS[temp] + " " + stcs[i]
        if i == rand_idx:
            answer = temp
    return "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.\n\n[ " + rand_stc + " ]\n\n" + ". ".join(stcs) + "\n\n\n** 정답: " + NUMBER_SYMBOLS[answer]


def convert_txt(text: str) -> list:
    text = text.replace(". ", ".") # 나중에 .을 기준으로 문장을 나누기 위한 작업
    text = text.replace(".\n", ".") # 나중에 .을 기준으로 문장을 나누기 위한 작업
    return text.split(".") # .을 기준으로 문장을 나누어 리스트에 담음


if not os.path.exists("본문 파일"):
    os.mkdir("본문 파일")

if not os.path.exists("생성된 문제 파일"):
    os.mkdir("생성된 문제 파일")

while(True):
    name = input("\n\n  ■ 영어 변형 문제 제작기 | @SleepySoong ■\n  [!] 문제를 생성할 파일의 이름을 확장자를 제외하고 입력해주세요 (*.txt만 지원합니다) : \n  - 주의: 변형 문제를 만들기 위해선 7개 이상의 문장으로 구성된 영어 본문이 필요합니다 \n")
    if not os.path.isfile("본문 파일/" + name + ".txt"):
        print("  [!] 존재하지 않는 파일 입니다. 확장자가 txt가 맞는지, 본문 파일 폴더에 파일이 있는지 확인해주세요!")
    else:
        print("  [!] 파일을 로딩중입니다: " + name +  ".txt")
        break

file = open("본문 파일/" + name + ".txt", 'rt', encoding='UTF8')
original_contents = ''.join(file.readlines()).replace("\n", "")
file.close()

print("\n\n  [!] 변형 문제 제작을 시작합니다.. 시간이 어느 정도 소요될 수 있습니다..\n\n")

# be 동사 변형 문제
write_txt("be 동사 변형 문제", name, be_verb_variation(original_contents))

# 순서 배열 문제
write_txt("순서 배열 문제", name, order_variation(original_contents))

# 빈칸 문제
write_txt("빈칸 문제", name, blank_variation(original_contents))

# 삽입 문제
write_txt("삽입 문제", name, insert_variation(original_contents))

# 동사 변경 문제
#write_txt("동사 변형 문제.txt", verbVariation(original_contents))

print("\n\n  [!] 변형 문제 제작이 성공적으로 완료되었습니다. 프로그램을 종료합니다.")
print("  - 원본 파일: " + name + ".txt")

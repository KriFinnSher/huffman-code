from collections import Counter, namedtuple
from heapq import heapify, heappop, heappush


class Node(namedtuple("Node", ["left_child", "right_child", "char"])):
    def set_codes(self, codes_map, code_):
        if self.char:
            codes_map[self.char] = code_
        if self.left_child:
            self.left_child.set_codes(codes_map, code_ + "0")
        if self.right_child:
            self.right_child.set_codes(codes_map, code_ + "1")

    def __lt__(self, other):
        return False


def encode_line(line):
    freq_list = []
    for ch, freq in Counter(line).items():
        freq_list.append((freq, Node(None, None, ch)))
    heapify(freq_list)
    while len(freq_list) > 1:
        freq1, left = heappop(freq_list)
        freq2, right = heappop(freq_list)
        heappush(freq_list, (freq1 + freq2, Node(left, right, None)))

    codes_map = {}
    if freq_list:
        freq, root = heappop(freq_list)
        root.set_codes(codes_map, "")
    return codes_map


def decode_line(encoded_line, codes_map):
    line = []
    t_code = ""
    for ch in encoded_line:
        t_code += ch
        for letter in codes_map:
            if codes_map[letter] == t_code:
                line.append(letter)
                t_code = ""
                break
    return line


def file_to_line(filename):
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            return input_file.read()
    except OSError as err:
        print("can't open", err)
        return None


test = """
    Началось нечто совсем для Мити неожиданное и удивительное. Он ни за что бы не мог  прежде,
    даже за минуту пред сим, предположить, чтобы так мог кто-нибудь обойтись с ним,  с  Митей
    Карамазовым! Главное, явилось нечто унизительное, а с их стороны «высокомерное и  к  нему
    презрительное». Еще ничего бы снять сюртук, но его попросили раздеться и далее.  И  не то
    что попросили, а, в сущности, приказали; он это отлично понял. Из гордости и презрения он
    подчинился вполне, без слов. За занавеску вошли, кроме  Николая  Парфеновича,  и прокурор,
    присутствовали и несколько мужиков, «конечно, для силы, — подумал Митя, — а может, и  еще
    для чего-нибудь».
"""
code = encode_line(test)
encoded = "".join(code[ch] for ch in test)
decoded = decode_line(encoded, code)
# print("".join(decoded))
# print(encoded)
# print(len(test) * 8, len(encoded))
# for i in sorted(code):
#     print(i + ": " + code[i])
test_file = file_to_line("test.txt")
code_1 = encode_line(test_file)
encoded_1 = "".join(code_1[ch] for ch in test_file)
decoded_1 = decode_line(encoded_1, code_1)
print("".join(decoded_1))
print(encoded_1)
print(len(test_file) * 8, len(encoded_1))
for i in sorted(code_1):
    print(i + ": " + code_1[i])

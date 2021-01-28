"""Most frequently used words in a text 4"""


# Write a __function that, given a string of text (possibly with punctuation and line-breaks), returns an array
# of the top-3 most occurring words, in descending order of the number of occurrences.
#
# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# (No need to handle fancy punctuation.) Matches should be case-insensitive, and the words in the result should be
# lowercased. Ties may be broken arbitrarily. If a text contains fewer than three unique words, then either the top-2
# or top-1 words should be returned, or an empty array if a text contains no words.
# Bonus points (not really, but just for fun):
# Avoid creating an array whose memory footprint is roughly as big as the input text.
# Avoid sorting the entire array of unique words.
#
# Напишите функцию, которая, учитывая строку текста (возможно, с пунктуацией и разрывами строк),
# возвращает массив из топ-3 наиболее часто встречающихся слов в порядке убывания числа вхождений.
# Допущения:
# Слово - это строка букв (от А до Я), необязательно содержащая один или несколько апострофов ( "" ) в ASCII.
# (Не нужно обращаться с причудливой пунктуацией.) Совпадения должны быть нечувствительны к регистру, а слова в результате
# должны быть записаны в нижнем регистре. Связи могут быть разорваны произвольно. Если текст содержит менее трех
# уникальных слов, то должны быть возвращены либо топ-2, либо топ-1 слова, либо пустой массив, если текст не содержит слов.
# Бонусные баллы (не совсем, но просто для удовольствия):
# 1. Избегайте создания массива, объем памяти которого примерно равен объему входного текста.
# 2. Избегайте сортировки всего массива уникальных слов.

# def top_3_words(text):
#     array = []
#     print(text)
#     print(set(text.lower().split()))
#     array = text.lower().split()
#     # print(array)
#     top_dict = {column: text.count(column) for column in set(text.lower().split())}
#
#     print(top_dict)
#
#     # print(len(top_dict))
#     # n = 3 if len(top_dict) > 3 else len(top_dict)
#     # for column in range(n):
#     #     print(max(top_dict.keys()))
#     # print('sdfsdf')
#     top_list = [top_dict.pop(max(top_dict.items())) for column in range(3 if len(top_dict) > 3 else len(top_dict))]
#
#     return top_list

def top_3_words(text):
    print(text)
    del_list = ['"', '//','/','.',',',':','?',';','!','-','_','"']
    text = text.lower().split()
    for i in del_list:
        for j in range(len(text)):
            text[j] = text[j].replace(i,'')
    text = ' '.join(text).split()

    print(text)
    top_list = list()
    top_dict = dict()


    for i in set(text):
        count = 0
        for j in text:
            if i == j:
                count += 1
        top_dict.setdefault(i, count)

    for i in range(3) if len(top_dict)>3 else range(len(top_dict)):
        m = [0, 0]
        for key, value in top_dict.items():
            if value > m[0]:
                m[0] = value
                m[1] = key
        print(m)
        del top_dict[m[1]]
        top_list.append(m[1])
    return top_list

# Чужой уод  ldt две библиотеки которые нужно будет изучить
from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]

# st = "//wont won't won't "  # , ["won't", 'wont]
# st = 'a a a  b  c c  d d d d  e e e e e'# ['e', 'd', 'a']
st = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""  # ["a", "of", "on"]
# st = 'dSa;?dSa_,,.!dSa-dSa:.:klbg, ;dSa,,dSa??dSa_dSa :_:!dSa.;_:dSa...dSa.?dSa,!, dSa!;dSa!dSa/?/?/dSa---:.klbg;::_dSa .,/-dSa;! dSa.!..?dSa?_klbg.dSa;?' # ['dsa', 'klbg']
# st = "leXlzYht . LFNUtH-./,_X'KcmUoC.zwGqHDWkeg?:.bAZ/;xwWzEK::AyBlVtSMZp?WGn,!xwWzEK;!:!bAZ!X'KcmUoC:bQlzBCEMt' ;;bSfs!,- AyBlVtSMZp/;_xwWzEK??,bQlzBCEMt'..;/_bSfs??;_/bSfs,./:zwGqHDWkeg;!-- WGn,X'KcmUoC-.:_,AyBlVtSMZp:_!xwWzEK/AyBlVtSMZp-zwGqHDWkeg;:/bSfs/_-._X'KcmUoC--LFNUtH;,;LFNUtH-;:?bSfs,:?AyBlVtSMZp:,;;X'KcmUoC.bQlzBCEMt'?bSfs-;bSfs:!-._zwGqHDWkeg.-./?xwWzEK ! !/zwGqHDWkeg-:!_-dOphEeWu??_.zwGqHDWkeg?_ :tInPE.?zwGqHDWkeg!_/X'KcmUoC/;. ;bSfs:zwGqHDWkeg;/_CTZCTudAXA_/!;zwGqHDWkeg-CTZCTudAXA!;,;X'KcmUoC,?.xwWzEK!?-bQlzBCEMt',WGn .dOphEeWu;!,bSfs._/!zwGqHDWkeg ?zwGqHDWkeg:-?dOphEeWu?;! LFNUtH/dOphEeWu/zwGqHDWkeg- -/_WGn?./dOphEeWu:dOphEeWu_/:,X'KcmUoC_xwWzEK: --zwGqHDWkeg!!-X'KcmUoC-,!dOphEeWu!:!AyBlVtSMZp?.zwGqHDWkeg--!_-LFNUtH/ AyBlVtSMZp-bQlzBCEMt'..__.xwWzEK.cCCQjmyNFZ_,;xwWzEK _zwGqHDWkeg_xwWzEK!,?,_dOphEeWu/bQlzBCEMt'-LFNUtH;xwWzEK-?::_dOphEeWu;.//?dOphEeWu._?:.AyBlVtSMZp,_:zwGqHDWkeg/?-/tInPE,/../X'KcmUoC?/bAZ-:!dOphEeWu:?/_xwWzEK, !/bSfs-.bQlzBCEMt' xwWzEK_/-AyBlVtSMZp-:bSfs,-?_;AyBlVtSMZp__bQlzBCEMt': AyBlVtSMZp?!;!bQlzBCEMt'!_-,;X'KcmUoC,X'KcmUoC!;dOphEeWu-- /bSfs!_ _zwGqHDWkeg;_:;:X'KcmUoC .;,bQlzBCEMt';,:_dOphEeWu-/!,X'KcmUoC,zwGqHDWkeg.bQlzBCEMt'. -AyBlVtSMZp!;.X'KcmUoC;_ -bSfs.dOphEeWu/ ;bSfs?bSfs?/:,zwGqHDWkeg/zwGqHDWkeg:, -.tInPE.; !!AyBlVtSMZp -,;:bSfs;:?zwGqHDWkeg,,-!bSfs,!/:xwWzEK_-_bAZ.-/;:bQlzBCEMt',,/,xwWzEK//,;?bQlzBCEMt'_!_/LFNUtH;zwGqHDWkeg.?..,dOphEeWu./;xwWzEK xwWzEK.-.:_zwGqHDWkeg ::dOphEeWu / __zwGqHDWkeg:/.._bQlzBCEMt'  ,?_LFNUtH xwWzEK-!;--LFNUtH!?/,bQlzBCEMt' :?LFNUtH?, ;bSfs,,.?!X'KcmUoC.leXlzYht?;; xwWzEK:X'KcmUoC//bQlzBCEMt'?LFNUtH,!??cCCQjmyNFZ.;;dOphEeWu.,__AyBlVtSMZp?/!!:xwWzEK;bAZ; -bAZ WGn_X'KcmUoC /?bSfs,_?/ bSfs.,??zwGqHDWkeg/_!/X'KcmUoC: ?LFNUtH ?:.xwWzEK;!??xwWzEK!??bSfs ?:-xwWzEK xwWzEK; tInPE.; zwGqHDWkeg !bAZ ;:  AyBlVtSMZp_; _bQlzBCEMt'!!bSfs_ -dOphEeWu..;;/AyBlVtSMZp .LFNUtH_!;,,bSfs?/?!_X'KcmUoC/,,?X'KcmUoC/:,//zwGqHDWkeg;_;CTZCTudAXA?xwWzEK ,?LFNUtH, ::;AyBlVtSMZp:dOphEeWu. :? X'KcmUoC:_leXlzYht,-xwWzEK zwGqHDWkeg,xwWzEK;?/:/leXlzYht;bAZ-LFNUtH_WGn .?:LFNUtH!- bQlzBCEMt'_!X'KcmUoC.??bSfs_tInPE;,/,xwWzEK!_!/-X'KcmUoC:. --dOphEeWu/ ;! X'KcmUoC._,/bAZ:.,LFNUtH.bSfs.. ;bSfs? -. bAZ;/,!.xwWzEK,LFNUtH;_AyBlVtSMZp__:-AyBlVtSMZp!dOphEeWu,"
# ['xwwzek', 'zwgqhdwkeg', 'bsfs']
print(Counter(st.lower().split()))

def sanitize(text):
    text_sanitized = ""
    for i in text:
        if i.isalpha() or i == "'":
            text_sanitized += i
        else:
            text_sanitized += " "
    l = text_sanitized.split()
    r = []
    for i in l:
        if len(i) != 0 and i != "'"*len(i):
            r.append(i.lower())
    return r


def top_3_words(text):
    l = sanitize(text)
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_dict[:3]]
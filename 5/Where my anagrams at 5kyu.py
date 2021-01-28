"""What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
Что такое анаграмма? Ну, два слова-это анаграммы друг друга, если они оба содержат одни и те же буквы.

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
"""
def anagrams(word, words):
  i = 0
  w = set(word)
  n = len(word)
  while i != len(words):
      if (len(words[i]) != n) or (set(words[i]) != w):
          words.pop(i)
          i -= 1
      else:
          for s in w:
              if word.count(s) != word.count(s):
                  words.pop(i)
      i += 1
      print(i, words)
  return words

# чужой код
def anagrams(word, words):
    return [item for item in words if sorted(item)==sorted(word)]
# он сделал так вернул список string - результат  обхода по списку и если отсортированные буквы в слове равны отсорированным буквам элемента списка



#print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'] )) # ['aabb', 'bbaa'])
#print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) #['carer', 'racer'])

words = ['aabb', 'abcd', 'bbaa', 'dada']
word = 'abba'
#reduce()
new_list = list(filter(lambda x: x == set(word), list(map(set, words))))

print(new_list)
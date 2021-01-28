# We need a method in the List Class that may count specific digits from a given list of integers. This marked digits will
# be given in a second list. The method .count_spec_digits()/.countSpecDigits() will accept two arguments, a list of an
# uncertain amount of integers integers_lists/integersLists (and of an uncertain amount of digits, too) and a second list,
# digits_list/digitsList that has the specific digits to count which length cannot be be longer than 10
# (It's obvious, we've got ten digits). The method will output a list of tuples, each tuple having two elements,
# the first one will be a digit to count, and second one, its corresponding total frequency in all the integers of the
# first list. This list of tuples should be ordered with the same order that the digits have in digitsList

class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        st = ''.join(map(str,integers_list))
        return [(element , st.count(str(element))) if str(element) in st else (element, 0) for element in digits_list]



l = List()
integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
# == [(1, 7), (8, 5), (4, 0)]
print(l.count_spec_digits(integers_list, digits_list))


#чужой код
class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        s = "".join(str(i) for i in integers_list)
        return [(dig, s.count(str(dig))) for dig in digits_list]
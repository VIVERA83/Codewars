

# мой  при чем           оказался почти как у лучших
def make_readable(seconds):
    return f'{str(seconds//3600).rjust(2,"0")}:{str((seconds%3600)//60).rjust(2,"0")}:{str(seconds%60).rjust(2,"0")}'

print(make_readable(86399))


# чужой код
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

def make_readable(n):
    return f'{n//3600:02d}:{(n%3600)//60:02d}:{n%60:02d}'
def make_readable(seconds):
    return ':'.join(map(str, ['%02d' % (seconds // 60 ** i % (100 if i == 2 else 60)) for i in range(3)][::-1]))

make_readable=lambda s:'%02d:%02d:%02d'%(s/3600,s/60%60,s%60)

#Test.assert_equals(make_readable(0), "00:00:00")
#Test.assert_equals(make_readable(5), "00:00:05")
#Test.assert_equals(make_readable(60), "00:01:00")
#Test.assert_equals(make_readable(86399), "23:59:59")
#Test.assert_equals(make_readable(359999), "99:59:59")
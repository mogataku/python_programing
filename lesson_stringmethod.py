# string method
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)
is_start = s.startswith(('F'))
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
# 大文字を小文字に変更
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Kaiko'))
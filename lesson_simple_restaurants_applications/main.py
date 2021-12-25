# おすすめのレストランを紹介する簡単なアプリケーションです
import csv
import os

# 初回入力者かどうか判定します
newpeople = False
# 次に紹介するレストランがあるかどうかのフラグです
nextresFlg = False
# 紹介するレストランのカウント数です
resCount = 0

# 紹介するレストランがあるかどうか判定します
if os.path.exists('restaurants.csv'):
    with open('restaurants.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            resCount += 1
            resdict = {'Name': row['Name'], 'Count': row['Count']}
else:
    # 紹介するレストランがないため、初回入力者であると判定します
    newpeople = True

print('''\
----------------------------------------------------
こんにちは！
ここはおすすめのレストランを紹介するサイトです。
あなたの名前は何ですか？
----------------------------------------------------
''')

while True:
    name = input('あなたの名前を入力してください : ')
    name = name.strip()  # 空白文字のみの入力は無視する
    if name != '':
        break

if newpeople:
    print('''\
    
    ----------------------------------------------------
    {}さん。どこのレストランが好きですか？
    ----------------------------------------------------
    '''.format(name))

    while True:
        res = input('お好きなレストランの名前を入力してください : ')
        res = res.strip()  # 空白文字のみの入力は無視する
        if res != '':
            break
else:
    print('''\

    ----------------------------------------------------
    {}さん。
    私のお勧めのレストランは、{}です。
    こちらのレストランは好きですか？
    ----------------------------------------------------
        '''.format(name, resdict['Name']))

    while True:
        res = input('[Yes/No] : ')
        res = res.strip()  # 空白文字のみの入力は無視する
        # Yes No 以外の回答を受け付けないようにする
        if res == 'Yes':
            break
        if res == 'No':
            nextresFlg = True
            break

if nextresFlg:
    print('''\

    ----------------------------------------------------
    {}さん。どこのレストランが好きですか？
    ----------------------------------------------------
    '''.format(name))

    while True:
        res = input('お好きなレストランの名前を入力してください : ')
        res = res.strip()  # 空白文字のみの入力は無視する
        if res != '':
            break

print('''\

----------------------------------------------------
{}さん。ご回答ありがとうございました。
良い一日を！さようなら
----------------------------------------------------
'''.format(name))

with open('restaurants.csv', 'w+') as csv_file:
    filednames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=filednames)
    writer.writeheader()
    if newpeople:
        writer.writerow({'Name': res, 'Count': 1})
    else:
        print(resdict)
        print(resCount)
        while resCount < 0:
            resCount -= 0
            writer.writerow({'Name': resdict['Name'], 'Count': resdict['Count']})
        writer.writerow({'Name': res, 'Count': 1})


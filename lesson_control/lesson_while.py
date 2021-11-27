# while continue break
count = 0
while count < 5:
    print(count)
    count += 1
    # ++は使えない

count2 = 0
# このままでは無限ループになる
while True:
    if count2 >= 5:
        # ここでループから抜ける
        break
    if count2 == 2:
        count2 += 1
        # このコードの下に処理が行かず、10行目に戻る
        continue
    print(count)
    count2 += 1

# while else
count3 = 0
while count3 < 5:
    print(count3)
    count3 += 1
# breakでループを抜けなかった場合、ループの終わりに呼ばれる
else:
    print('done')
#try, except, finally
print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print(e)
finally:    #例外が発生した場合もしなかった場合も常に最後に行う処理をfinally節に指定できる。
    print(2)

#例外情報の取得
import traceback, sys

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print('0では割り算できません')
    #print(traceback.format_exc())   #例外情報の取得
    sys.stderr.write(traceback.format_exc())    #標準エラー出力
finally:
    print(2)
    
#複数例外
#未定義変数
print(1)
try:
    number = 0
    answer = 100 / number
    print(answer2)
except ZeroDivisionError as e:
    print("0では割り算できません")
except NameError as e:
    print("未定義の変数を呼び出しています")
    print(e)
finally:
    print(2)

#

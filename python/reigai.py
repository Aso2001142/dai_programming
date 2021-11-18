print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print(e)
finally:    #例外が発生した場合もしなかった場合も常に最後に行う処理をfinally節に指定できる。
    print(2)


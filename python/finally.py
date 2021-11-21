# finally
# 例外が発生した場合もしなかった場合も常に最後に行う処理をfinally節に指定できる。
def test_exception(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e:
        print(5)
        raise e
    finally:
        print(6)

print(1)
try:
    answer = test_exception(0)
    print(7)
except ZeroDivisionError as e:
    print(8)
    print(e)

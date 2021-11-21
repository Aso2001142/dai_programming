# raise

print(1)
try:
    print(2)
    raise Exception("意図的な例外") //エラーメッセージ
    print(3)
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
finally:
    print(4)

# 例外は伝わる 
# 例外が発生した場合、呼び出し元へその例外が伝わる
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
    print(6)

print(1)
try:
    answer = test_exception(0)  # 呼び出し元
    print(7)
except ZeroDivisionError as e:
    print(8)
    print(e)

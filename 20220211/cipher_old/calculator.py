# -----------------------------------------------------------------------------
viewx = 0         # 전역 변수 (Global Variable)

class Calc:
    global viewx  # 클래스 안에서의 전역 변수 (Global Variable) 액세스 선언 (무효함)
    value = 0     # 클래스 Integer 변수를 선언 (Class variable)
    title = []    # 클래스 String  변수를 선언 (Class variable)

    def __init__(self, head_title): # 클래스 생성자
        self.result = 0   # 인스턴스 변수 (Instance variable)
        self.number = 0   # 인스턴스 변수 (Instance variable)
        self.title  = head_title
        Calc.value  = 0
        Calc.title  = head_title
        print("---> Head Title   :", Calc.title)
        print("---> Global viewx :", viewx) # 전역 변수 (Global Variable) 액세스

    def __del__(self):             # 클래스 소멸자
        Calc.value -= 1

    def set_value(self, numberx):
        if Calc.value == numberx:  # 넘버 비교 때 (Class Variable)
            print("---> Same Calc.value :", Calc.value)

        if self.value == numberx:  # 넘버 비교 때 (Instance variable)
            print("---> Same self.value :", self.value)

        print("---> Set number :", numberx) # 클래스 안의 함수의 인수를 표시
        print("---> Set viewx  :", viewx)   # 전역 변수 (Global Variable) 액세스
        Calc.value  = numberx
        self.number = numberx
        return Calc.value

    def set_title(self, titlex):
        if Calc.title is titlex:   # 문자 비교 때 (Class Variable)
            print("---> Same Calc.Title :", Calc.title)

        if self.title is titlex:   # 문자 비교 때 (Instance variable)
            print("---> Same self.Title :", self.title)

        Calc.title = titlex # Class Variable
        self.title = titlex # Instance variable
        return Calc.title

    def add(self, numberx):
        self.result += numberx
        return self.result

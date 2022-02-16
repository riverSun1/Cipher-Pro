# -----------------------------------------------------------------------------
from calculator import Calc # calculator.py 내의 클래스 (Class Name) 액세스
import calculator as gv     # calculator.py 내의 전역 변수 (Global Variable) 액세스

gv.viewx = 1 # 전역 변수 (Global Variable) 액세스
cal1 = Calc("PC")

gv.viewx = 2 # 전역 변수 (Global Variable) 액세스
cal2 = Calc("IoT")

print("cal1.title  :", cal1.title) # 클래스 안의 인스턴스 변수 읽기
print("cal2.title  :", cal2.title) # 클래스 안의 인스턴스 변수 읽기
print("Set Value   :", cal1.set_value(1))
print("Set Value   :", cal2.set_value(2))
print("cal1.number :", cal1.number) # 클래스 안의 인스턴스 변수 읽기
print("cal2.number :", cal2.number) # 클래스 안의 인스턴스 변수 읽기
print("Cal1.Add 1  :", cal1.add(1))
print("Cal2.Add 2  :", cal2.add(2))
print("Set Value   :", cal1.set_value(0))
print("Set Title 1 :", cal1.set_title("PC"))
print("Set Title 2 :", cal2.set_title("IoT"))
print(Calc.value) # 클래스 변수 읽기
print(Calc.title) # 클래스 변수 읽기
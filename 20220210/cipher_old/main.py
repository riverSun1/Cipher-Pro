import sys 
from cipher import MyApp
import cipher as c
from PyQt5.QtWidgets import QApplication, QWidget
import qdarkstyle

#-----------------------------------------------------------------------------------------
if __name__ == '__main__': # 모듈의 이름이 저장되는 내장 변수
#-----------------------------------------------------------------------------------------

    app = QApplication(sys.argv) #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5')) #다크테마
    
    c.views = 0
    pc = MyApp() # PC
    MyApp.title = 'PC'
    pc.change_title('PC')
    pc.move(250, 100)

    c.views = 1
    iot = MyApp() # iot
    MyApp.title = 'IoT'
    iot.change_title('IoT')
    iot.move(1300, 100)

    sys.exit(app.exec_())
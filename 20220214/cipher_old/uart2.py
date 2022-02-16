# 키 인덱스 
KEY_LEFT     = 0
KEY_UP       = 1
KEY_RIGHT    = 2
KEY_DOWN     = 3
KEY_SELECT   = 4
KEY_START    = 5
KEY_SQUARE   = 6
KEY_TRIANGLE = 7
KEY_X        = 8
KEY_CIRCLE   = 9

# 키 매핑 
Keymap = {
    b'a': [KEY_LEFT, 'KEY_LEFT'],
    b'w': [KEY_UP, 'KEY_UP'],
    b'd': [KEY_RIGHT, 'KEY_RIGHT'],
    b's': [KEY_DOWN, 'KEY_DOWN'],
    b'1': [KEY_SELECT, 'KEY_SELECT'],
    b'2': [KEY_START, 'KEY_START'],
    b'y': [KEY_SQUARE, 'KEY_SQUARE'],
    b'u': [KEY_TRIANGLE, 'KEY_TRIANGLE'],
    b'h': [KEY_X, 'KEY_X'],
    b'j': [KEY_CIRCLE, 'KEY_CIRCLE'],
    }
# 프로토콜
class rawProtocal(Protocol):
    # 연결 시작시 발생
    def connection_made(self, transport):
        self.transport = transport
        self.running = True

    # 연결 종료시 발생
    def connection_lost(self, exc):
        self.transport = None

    #데이터가 들어오면 이곳에서 처리함.
    def data_received(self, data):
        #입력된 데이터와 키맵을 비교해서 있다면
        if data in Keymap:
            # 매핑된 키의 문자열 출력
            print(Keymap[data][1])
            
            # Keymap[data][0]은 키 인덱스
            # 매칭되는 key 인덱스 가져옴
            key = Keymap[data][0]
            
            # 매핑 키가 CIRCLE 키이면 프로그램 종료        
            if key == KEY_CIRCLE:
                self.running = False
        else:
            print('Unknown data', data)

    # 데이터 보낼 때 함수
    def write(self,data):
        print(data)
        self.transport.write(data)
        
    # 종료 체크
    def isDone(self):
        return self.running


# 포트 설정
PORT = '/dev/ttyUSB0'
# 연결
ser = serial.serial_for_url(PORT, baudrate=9600, timeout=1)

# 쓰레드 시작
with ReaderThread(ser, rawProtocal) as p:
    while p.isDone():
        time.sleep(1)

# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221156763486
import cryptor
import binascii

def main():
    
    #msg = 'plain text'
    msg = '해원'
    key = 'hisecure'
    print("메시지 data:", msg)
    print("메시지 key :", key)

    enc_msg = cryptor.enc_xor(msg.encode(), key.encode()) # 암호화된 데이터를 결과로 준다.
    print("암호화된 데이터 :", enc_msg) # str(enc_msg))
    print(str(binascii.hexlify(enc_msg), "utf-8"))
    print(binascii.hexlify(enc_msg))

    dec_msg = cryptor.enc_xor(enc_msg, key.encode()) # 복호화된 데이터를 결과로 준다.
    print("복호화된 데이터 :", dec_msg.decode())
    
    #print(dec_msg)
    print(dec_msg.decode()) # utf-8로 설정한 것과 같다. # 인코딩 방식 미지정 경우, UTF-8 사용.
    #print(dec_msg.decode('utf-8'))

    if msg == dec_msg.decode():
        print("같다")
    else:
        print("다르다")

main()

# D:\uTorrent\cryptor\testn.py
# window 기본 엔코딩 방식 : cp949 
# cmd에서 확인하기 : chcp
# ubuntu linux 기본 엔코딩 방식 : utf-8
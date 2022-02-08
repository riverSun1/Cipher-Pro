def enc_xor(msg,key): # 두 값 비교해서 같으면 0, 다르면 1
    msg_size = len(msg)
    key_size = len(key)
    enc = bytearray() # 빈 바이트 배열 객체 생성
    
    for i in range(msg_size):
        
        msg_xor = msg[i]^key[i%key_size] # i%key_size를 통해 key길이가 초과하는 것을 방지하였다.
        enc.append(msg_xor)
        
    return enc

def main():
    
    #msg = 'plain text'
    msg = '해원'
    
    key = 'hisecure'

    print("메시지 data:", msg)
    print("메시지 key :", key)

    enc_msg = enc_xor(msg.encode(), key.encode()) # 암호화된 데이터를 결과로 준다.
    print("암호화된 데이터 :", enc_msg)

    dec_msg = enc_xor(enc_msg, key.encode()) # 복호화된 데이터를 결과로 준다.
    print("복호화된 데이터 :", dec_msg.decode())
    
    #print(dec_msg)
    print(dec_msg.decode()) # utf-8로 설정한 것과 같다. # 인코딩 방식 미지정 경우, UTF-8 사용.
    #print(dec_msg.decode('utf-8'))

    #if msg == dec_msg.decode():
    #    print("같다")
    #else:
    #    print("다르다")

main()

# window 기본 엔코딩 방식 : cp949 
# cmd에서 확인하기 : chcp
# ubuntu linux 기본 엔코딩 방식 : utf-8
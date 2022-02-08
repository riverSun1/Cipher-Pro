import binascii

s1="A"

print(ord(s1)) # 65 # 10진 아스키코드로 변환
# ord() 함수는 바이트 문자열의 문자를 나타내는 정수를 반환합니다.

print(s1.encode())

print(binascii.unhexlify(s1))

#print(s1.decode())

#xor 연산 특징
#if a xor b = c
#c xor b = a
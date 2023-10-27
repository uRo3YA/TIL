from pyvisa import ResourceManager

_host = '192.168.122.72'
_port = 5025

rm = ResourceManager() # visa 객체를 생성합니다.

# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다. 
psa_client = rm.open_resource(f'TCPIP{_port}::INSTR')

print (psa_client.query('*IDN?')) # 기기 정보를 출력합니다.

psa_client.write(f"MMEM:STORE:SCREEN 'C:TEMP.GIF'") # PSA screenshot
# img = psa_client.query_binary_values('HCOPy:SDUMp:DATA?') # 이진 데이터를 가져오기는 하지만, 변환 어려움
psa_client.write("MMEM:DATA? 'C:TEMP.GIF'")
img = psa_client.read_raw()

header_index = img.find(b'GIF')
if (header_index > 0): # find GIF header
    img = img[header_index:]

# 화면 캡쳐 파일 저장하기
with open('psa.gif', 'wb') as f:
    f.write(img)
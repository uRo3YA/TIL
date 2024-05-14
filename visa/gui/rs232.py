import pyvisa
import time
# PyVISA를 초기화합니다.
rm = pyvisa.ResourceManager('@py')
list=rm.list_resources()
print(list)

# VISA 주소나 시리얼 포트 이름을 여기에 입력합니다.
instrument_address = 'ASRL3::INSTR'
# instrument_address= "GPIB"
# 인스트루먼트에 연결합니다.
instrument = rm.open_resource(instrument_address)

# 시리얼 포트 설정을 구성합니다.
instrument.baud_rate = 9600  # 통신 속도
instrument.data_bits = 8    # 데이터 비트
instrument.parity = pyvisa.constants.Parity.none  # 패리티 비트 (없음)
instrument.stop_bits = pyvisa.constants.StopBits.one  # 정지 비트

# 데이터를 송신합니다.
command = "*IDN?"  # 예제 명령
response=instrument.write(command)
# print(type(response))
time.sleep(0.1)

# 데이터를 수신합니다.
response = instrument.read("\n")
print("인스트루먼트 응답:", response)

# 연결을 닫습니다.
instrument.close()

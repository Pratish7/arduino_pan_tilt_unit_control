import time
import serial
import sys

serial_port = "/dev/ttyACM0"
baud_rate=115200

try:
    port=serial.Serial(
            port=serial_port,
            baudrate=baud_rate,
            timeout=1
        )
except serial.serialutil.SerialException as e:
        print(e)
        sys.exit()
        
def tilt_up():
    MR_Bit = '0'
    LE_Bit = '0'
    TCE_Bit = '0'  
    ZCE_Bit = '0'
    PE_Bit = '0'
    ZE_Bit = '0'
    FE_Bit = '0'
    PLR_Bit = '0'  
    ZIO_Bit = '0'   
    FIO_Bit = '0'   
    TE_Bit = '1'
    TUD_Bit = '1'
    
    data = FIO_Bit+ZIO_Bit+TUD_Bit+PLR_Bit+FE_Bit +ZE_Bit+TE_Bit+PE_Bit+ZCE_Bit+TCE_Bit+LE_Bit+MR_Bit
    
    try:
        ser_data = port.readline()
        if(ser_data):
            #decData = int(data, 2)
            to_send = (str(data).encode())
            port.write(to_send)
            
            
            
            time.sleep(1)
        
            exit_data = '000000000000'
        
        ser_data = port.readline()
        if(ser_data):
            decData = int(exit_data, 2)
            to_send = (str(exit_data).encode())
            port.write(to_send)
            port.close()
            sys.exit()
            
    except Exception as e:
        print(e)
        sys.exit()
            
tilt_up()
 

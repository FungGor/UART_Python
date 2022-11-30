# CRC Check Sum. STM32MCP_calChecksum checks the incoming data's integrity from UART
def STM32MCP_calChecksum(msg, size):
    total = 0
    n = 0
    while n != size:
        total = total + msg[n]
        n = n+1
    return (total & 0xFF) + ((total>>8) & 0xFF)
# motor_control.py processes the incoming messages from the ECU
import STM32MCP_Lib
import ECU_Data

def motorcontrol_processGetRegisterFrameMsg(txPayload: bytearray, txPayloadLength, rxPayload: bytearray, rxPayloadLength):
    regID = txPayload[0]
    match regID:
        case STM32MCP_Lib.STM32MCP_REG_ID.STM32MCP_BUS_VOLTAGE_REG_ID:
            pass
        case STM32MCP_Lib.STM32MCP_REG_ID.STM32MCP_TORQUE_MEASURED_REG_ID:
            pass
        case STM32MCP_Lib.STM32MCP_REG_ID.STM32MCP_HEATSINK_TEMPERATURE_REG_ID:
            pass
        case STM32MCP_Lib.STM32MCP_REG_ID.STM32MCP_SPEED_MEASURED_REG_ID:
            pass

def motorcontrol_processGetMotorBehaviorFrameMsg(txPayload: bytearray,txPayloadLength, rxPayload: bytearray, rxPayloadLength):
    regID = txPayload[0]
    if (regID == STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_ERROR_REPORT):
        fault = rxPayload[0]
        match fault:
            case STM32MCP_Lib.ECU_ERROR_CODE.SYS_NORMAL_CODE:
                pass
            case STM32MCP_Lib.ECU_ERROR_CODE.HALL_SENSOR_ERROR_CODE:
                pass
            case STM32MCP_Lib.ECU_ERROR_CODE.PHASE_I_ERROR_CODE:
                pass
            case STM32MCP_Lib.ECU_ERROR_CODE.MOSFET_ERROR_CODE:
                pass
            case STM32MCP_Lib.ECU_ERROR_CODE.GATE_DRIVER_ERROR_CODE:
                pass
            case STM32MCP_Lib.ECU_ERROR_CODE.BMS_COMM_ERROR_CODE:
                pass
            case STM32MCP_Lib.ECU_ERROR_CODE.MOTOR_TEMP_ERROR_CODE:
                pass
            case STM32MCP_Lib.ECU_ERROR_CODE.BATTERY_TEMP_ERROR_CODE:
                pass
    elif (regID == STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_CURRENT):
        pass
    elif (regID == STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_MOTOR_TEMPERATURE):
        pass
    elif (regID == STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_MOTOR_DRIVER_TEMP):
        pass
    elif (regID == STM32MCP_Lib.ESCOOTER_BEHAVIOURS.ESCOOTER_BATTERY_VOLTAGE):
        pass

def motorcontrol_exceptionHandler():
    print("Data Package is corrupted")

def motorcontrol_errorHandler(errorCode):
    match errorCode:
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_BAD_FRAME_ID:
            print("STM32MCP Error: Bad Frame ID received.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_WRITE_ON_READ_ONLY:
            print("STM32MCP Error: Write on Read-Only Register.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_READ_NOT_ALLOWED:
            print("STM32MCP Error: Read Not Allowed on this Register.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_BAD_TARGET_DRIVE:
            print("STM32MCP Error: Bad Target Drive.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_OUT_OF_RANGE:
            print("STM32MCP Error: Value Out of Range.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_BAD_COMMAND_ID:
            print("STM32MCP Error: Bad Command ID.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_OVERRUN_ERROR:
            print("STM32MCP Error: Overrun Error.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_TIMEOUT_ERROR:
            print("STM32MCP Error: Timeout Error.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_BAD_CRC:
            print("STM32MCP Error: Bad CRC.")
        case STM32MCP_Lib.STM32MCP_ERROR_CODE.STM32MCP_BAD_TARGET_DRIVE:
            print("STM32MCP Error: Bad Target Drive.")
    
def motorcontrol_showReceivedMessage(rxMsg: bytearray, frameID, rxPayloadLength, rxPayload, txPayloadLength, txPayload):
    print(f"Received Message with Frame ID: {frameID}")
    #for i in range(len(rxPayload)):
    print(f"RxPayload is: {' '.join(f'{hex(b)}' for b in rxPayload)}")
        #print("\n")
    print(f"Rx Payload Length: {rxPayloadLength}")
    #for i in range(len(txPayload)):
    print(f"TxPayload is: {' '.join(f'{hex(b)}' for b in txPayload)}")
    print(f"Tx Payload Length: {txPayloadLength}")
    print("\n")
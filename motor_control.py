# motor_control.py processes the incoming messages from the ECU
import STM32MCP_CTL
import STM32MCP_Lib

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

#Message Receive Handler --> Handles the incoming message from ECU
def motorcontrol_rxMsgCB(rxMsg: bytearray, STM32MCP_txMsgNode):
    frameID = STM32MCP_txMsgNode.txMsg[0] & 0x1F

    rxPayloadLength = rxMsg[1]
    rxPayload = rxMsg[2:2+rxPayloadLength]

    txPayloadLength = STM32MCP_txMsgNode.size
    txPayload = STM32MCP_txMsgNode.txMsg[2:2+txPayloadLength]

    match frameID:
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_SET_REGISTER_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_GET_REGISTER_FRAME_ID:
            motorcontrol_processGetRegisterFrameMsg(txPayload,txPayloadLength,rxPayload,rxPayloadLength)           
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_EXECUTE_COMMAND_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_GET_BOARD_INFO_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_EXECUTE_RAMP_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_GET_REVUP_DATA_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_SET_REVUP_DATA_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_STARTING_FRAME_CODES.STM32MCP_SET_CURRENT_REFERENCES_FRAME_ID:
            pass
        case STM32MCP_Lib.ESCOOTER_BEHAVIOR_ID:
            motorcontrol_processGetMotorBehaviorFrameMsg(txPayload,txPayloadLength,rxPayload,rxPayloadLength)
            pass
        case STM32MCP_Lib.STM32MCP_SET_DRIVE_MODE_CONFIG_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_SET_DYNAMIC_TORQUE_FRAME_ID:
            pass
    del rxPayload
    del txPayload

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
    
def motorcontrol_showReceivedMessage(rxMsg: bytearray):
    for i in range(len(rxMsg)):
        print(f"Byte {i}: {hex(rxMsg[i])}")
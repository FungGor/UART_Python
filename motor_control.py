# motor_control.py processes the incoming messages from the ECU
import STM32MCP_CTL
import STM32MCP_Lib

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
            pass
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
            pass
        case STM32MCP_Lib.STM32MCP_SET_DRIVE_MODE_CONFIG_FRAME_ID:
            pass
        case STM32MCP_Lib.STM32MCP_SET_DYNAMIC_TORQUE_FRAME_ID:
            pass
    del rxPayload
    del txPayload







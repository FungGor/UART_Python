#This library implements the functions for controllling the STM32 Motor Driver (Applicable for F1xxx and F4xxx Series) 
import STM32MCP_Lib
import timer_thread_control


#Object referencing to the first motor controller register attribute
regAttribute = STM32MCP_Lib.STM32MCP_regAttribute_t()

STM32MCP_CBs = STM32MCP_Lib.STM32MCP_CBs_t()

#define UART Configuration Parameters 
#Create UART Objects (Register UART)
UART_PORT  = "COM3"
BAUD_RATE  = 9600
PARITY     = 'NONE'
STOPBITS   = 1
BYTE_SIZE  = 8
TIMEOUT    = None
uart_Event = None
uart = STM32MCP_Lib.STM32MCP_uartManager_t(UART_PORT,BAUD_RATE,PARITY,STOPBITS,BYTE_SIZE,TIMEOUT,uart_Event)

# define the timer for STM32MCP Protocol
# @ Objects : timerManager:     Normal timer counting for data transmission
#           : heartbeatManager: Check the connection's stability
timerManager = STM32MCP_Lib.STM32MCP_timerManager_t()
heartbeatManager = STM32MCP_Lib.STM32MCP_timerManager_t()

rxObj = STM32MCP_Lib.STM32MCP_rxMsgObj_t()

#STM32MCP Queue Linked List Pointer
STM32MCP_headPtr = STM32MCP_Lib.STM32MCP_txNode_t(None,0,None)
STM32MCP_tailPtr = STM32MCP_Lib.STM32MCP_txNode_t(None,0,None)
STM32MCP_queueSize = 0

retransmissionCount = 0x00
communicationState = STM32MCP_Lib.STM32MCP_COMMUNICATION_DEACTIVE

#Register value
#Developers should modify the following data structures if they wish to use more or less registers
STM32MCP_regTargetMotorVal = 0
STM32MCP_refFlagsVal = [0,0,0,0]
STM32MCP_regStatusVal = 0
STM32MCP_regControlModeVal = 0
STM32MCP_regTorqueReferenceVal = [0,0]
STM32MCP_regFluxReferenceVal = [0,0]
STM32MCP_regBusVoltageVal = [0,0]
STM32MCP_regHeatSinkTemperatureVal = [0,0]
STM32MCP_regMotorPowerVal = [0,0]
STM32MCP_regSpeedMeasuredVal = [0,0,0,0]
STM32MCP_regSpeedKP = [0,0]
STM32MCP_regTorqueMeasuredVal = [0,0]

#Array of Objects from STM32MCP_regAttribute_t
FluxPayload = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_FLUX_REFERENCE_REG_ID, STM32MCP_Lib.STM32MCP_FLUX_REFERENCE_PAYLOAD_LENGTH,
STM32MCP_regFluxReferenceVal, STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ | STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_WRITE)

TorquePayload = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_TORQUE_REFERENCE_REG_ID, STM32MCP_Lib.STM32MCP_TORQUE_REFERENCE_PAYLOAD_LENGTH,
STM32MCP_regTorqueReferenceVal,STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ | STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_WRITE )

TargetMotor = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_TARGET_MOTOR_REG_ID, STM32MCP_Lib.STM32MCP_TARGET_MOTOR_PAYLOAD_LENGTH,
STM32MCP_regTargetMotorVal, STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ | STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_WRITE)

STM32_FLAG = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_STATUS_REG_ID, STM32MCP_Lib.STM32MCP_STATUS_PAYLOAD_LENGTH,
STM32MCP_regStatusVal,STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ)

STM32_STATUS = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_CONTROL_MODE_REG_ID, STM32MCP_Lib.STM32MCP_CONTROL_MODE_PAYLOAD_LENGTH,
STM32MCP_regControlModeVal, STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ | STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_WRITE)

MOTOR_VOLTAGE = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_BUS_VOLTAGE_REG_ID, STM32MCP_Lib.STM32MCP_BUS_VOLTAGE_PAYLOAD_LENGTH,
STM32MCP_regBusVoltageVal,STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ)

MOTOR_TEMPERATURE = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_HEATSINK_TEMPERATURE_REG_ID, STM32MCP_Lib.STM32MCP_HEATSINK_TEMPERATURE_PAYLOAD_LENGTH,
STM32MCP_regHeatSinkTemperatureVal,STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ)

MOTOR_POWER = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_MOTOR_POWER_REG_ID, STM32MCP_Lib.STM32MCP_MOTOR_POWER_PAYLOAD_LENGTH,
STM32MCP_regMotorPowerVal,STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ)

MOTOR_SPEED = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_SPEED_MEASURED_REG_ID, STM32MCP_Lib.STM32MCP_SPEED_MEASURED_PAYLOAD_LENGTH,
STM32MCP_regSpeedMeasuredVal,STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ)

STM32_Iq = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_TORQUE_MEASURED_REG_ID, STM32MCP_Lib.STM32MCP_TORQUE_MEASURED_PAYLOAD_LENGTH, 
STM32MCP_regTorqueMeasuredVal,STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ)

MOTOR_KP = STM32MCP_Lib.STM32MCP_regAttribute_t(STM32MCP_Lib.STM32MCP_SPEED_KP_REG_ID, STM32MCP_Lib.STM32MCP_SPEED_KP_PAYLOAD_LENGTH,
STM32MCP_regSpeedKP, STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_READ | STM32MCP_Lib.STM32MCP_REGISTER_PERMIT_WRITE)

STM32MCP_REG_ATTRIBUTE = []
STM32MCP_REG_ATTRIBUTE.append(TargetMotor)
STM32MCP_REG_ATTRIBUTE.append(MOTOR_VOLTAGE)
STM32MCP_REG_ATTRIBUTE.append(MOTOR_SPEED)
STM32MCP_REG_ATTRIBUTE.append(MOTOR_TEMPERATURE)
STM32MCP_REG_ATTRIBUTE.append(STM32_Iq)
STM32MCP_REG_ATTRIBUTE.append(STM32_STATUS)


# @fn       STM32MCP_initQueue
#
# @brief    To get set the head and tailPtr
#
# @param    None
def STM32MCP_initQueue():
    STM32MCP_headPtr = None
    STM32MCP_tailPtr = None
    STM32MCP_queueSize = 0


# @fn         STM32MCP_getQueueSize
#
# @brief      To get the current size of the queue
#
# @param      None
# 
# @return     The size of the queue
def STM32MCP_getQueueSize():
    return STM32MCP_queueSize


# @fn      STM32MCP_queueIsEmpty
# 
# @brief   To check if he txMsg queue is empty
#
# @param   None
#
# @return  None
def STM32MCP_queueIsEmpty():
    if (STM32MCP_headPtr == None & STM32MCP_tailPtr == None):
        return 0x01
    else:
        return 0x00


# @fn      STM32MCP_enqueueMsg
#
# @param   txMsg  The memory address of the fist byte of uart tx message
#          size   The size of the uart tx message in number of bytes
#  
# @return  None
def STM32MCP_enqueueMsg(txMsg, sizeMsg):
    #linear linked list with first in first out structure 
    if (STM32MCP_getQueueSize() <= STM32MCP_Lib.STM32MCP_MAXIMUM_NUMBER_OF_NODE):
        tempPtr = STM32MCP_Lib.STM32MCP_txNode_t()
        tempPtr.txMsg = txMsg
        tempPtr.size  = sizeMsg
        tempPtr.next  = None
        if(STM32MCP_tailPtr == None):
            STM32MCP_headPtr = tempPtr
            STM32MCP_tailPtr = tempPtr
        else:
            STM32MCP_tailPtr.next = tempPtr
            STM32MCP_tailPtr = tempPtr
        STM32MCP_queueSize = STM32MCP_queueSize + 1
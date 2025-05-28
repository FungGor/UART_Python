#This library implements the functions for controllling the STM32 Motor Driver (Applicable for F1xxx and F4xxx Series) 
import STM32MCP_Lib
import numpy as np


#Object referencing to the first motor controller register attribute
regAttribute = STM32MCP_Lib.STM32MCP_regAttribute_t()
STM32MCP_CBs = STM32MCP_Lib.STM32MCP_CBs_t()

#define UART Configuration Parameters 
#Create UART Objects (Register UART)
UART_PARAM = {
    "PORT": "COM3",
    "BAUD_RATE": 115200,
    "PARITY": 'NONE',
    "STOPBITS": 1,
    "BYTE_SIZE": 8,
    "TIMEOUT": None,
    "uart_Event": None
}
uart = STM32MCP_Lib.STM32MCP_uartManager_t(
    port=UART_PARAM["PORT"],
    baudrate=UART_PARAM["BAUD_RATE"],
    parity=UART_PARAM["PARITY"],
    stopbits=UART_PARAM["STOPBITS"],
    bytesize=UART_PARAM["BYTE_SIZE"],
    timeout=UART_PARAM["TIMEOUT"],
    uart_Event=UART_PARAM["uart_Event"]
)

# define the timer for STM32MCP Protocol
# @ Objects : timerManager:     Normal timer counting for data transmission
#           : heartbeatManager: Check the connection's stability
timerManager = STM32MCP_Lib.STM32MCP_timerManager_t()
heartbeatManager = STM32MCP_Lib.STM32MCP_timerManager_t()

rxObj = STM32MCP_Lib.STM32MCP_rxMsgObj_t()

#STM32MCP Queue Linked List Pointer as global variable
#STM32MCP_headPtr = STM32MCP_Lib.STM32MCP_txNode_t()
#STM32MCP_tailPtr = STM32MCP_Lib.STM32MCP_txNode_t()
#STM32MCP_queueSize = 0


retransmissionCount = 0x00
communicationState = STM32MCP_Lib.STM32MCP_COMMUNICATION_DEACTIVE

class STM32MCP_CommunicationProtocol:
        # @fn       STM32MCP_startCommunication
        # @brief    It is used to start the communication
        # @param    None
        # @return   None
        def STM32MCP_startCommunication():
            if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_DEACTIVE:
                communicationState = STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE

        # @fn       STM32MCP_closeCommunication
        # @brief    It is used to stop the communication
        # @param    None
        # @return   None
        def STM32MCP_closeCommunication():
            if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE:
                communicationState = STM32MCP_Lib.STM32MCP_COMMUNICATION_DEACTIVE
                #STM32MCP_emptyQueue()


class STM32MCP_FIFO_Queue:
        # @fn      STM32MCP Queue Initialization
        def __init__(self):
            # @brief    It is used to initialize the queue
            # @param    None
            self.STM32MCP_headPtr = None
            self.STM32MCP_tailPtr = None
            self.STM32MCP_queueSize = 0

        # @fn       STM32MCP_initQueue
        # @brief    To get set the head and tailPtr
        # @param    None
        def STM32MCP_initQueue(self):
            self.STM32MCP_headPtr = None
            self.STM32MCP_tailPtr = None
            self.STM32MCP_queueSize = 0

        # @fn         STM32MCP_getQueueSize
        # @brief      To get the current size of the queue
        # @param      None
        # @return     The size of the queue
        def STM32MCP_getQueueSize(self):
            return self.STM32MCP_queueSize

        # @fn      STM32MCP_queueIsEmpty 
        # @brief   To check if he txMsg queue is empty
        # @param   None
        # @return  None
        def STM32MCP_queueIsEmpty(self):
            if (self.STM32MCP_headPtr == None & self.STM32MCP_tailPtr == None):
                return 0x01
            else:
                return 0x00
            
        # @fn      STM32MCP_enqueueMsg
        # @param   txMsg  The memory address of the fist byte of uart tx message
        #          size   The size of the uart tx message in number of bytes 
        # @return  None
        def STM32MCP_enqueueMsg(self,txMsg, sizeMsg):
            if (self.STM32MCP_getQueueSize() <= STM32MCP_Lib.STM32MCP_MAXIMUM_NUMBER_OF_NODE):
                tempPtr = STM32MCP_Lib.STM32MCP_txNode_t() #Create the new node
                # @brief   To set the txMsg and sizeMsg in the new node
                # @param   txMsg  The memory address of the first byte of uart tx message
                #          size   The size of the uart tx message in number of bytes
                # @return  None
                # @note    The txMsg is a pointer to the first byte of the message
                #          The sizeMsg is the size of the message in number of bytes
                tempPtr.txMsg = txMsg
                tempPtr.size  = sizeMsg
                tempPtr.next  = None
                if(self.STM32MCP_tailPtr == None):
                    self.STM32MCP_headPtr = tempPtr
                    self.STM32MCP_tailPtr = tempPtr
                else:
                    self.STM32MCP_tailPtr.next = tempPtr
                    self.STM32MCP_tailPtr = tempPtr
                self.STM32MCP_queueSize = self.STM32MCP_queueSize + 1
            else:
                print("STM32MCP_enqueueMsg: Queue is full, cannot enqueue message")
                txMsg = None
                return None

        # @fn      STM32MCP_dequeueMsg
        # @brief   To dequeue the first message in the queue (FIFO)
        # @param   None
        # @return  The memory address of the first byte of the dequeued message
        def STM32MCP_dequeueMsg(self):
            if(self.STM32MCP_headPtr == None):
                return None
            else:
                tempPtr = self.STM32MCP_headPtr 
                self.STM32MCP_headPtr = self.STM32MCP_headPtr.next
                if(self.STM32MCP_headPtr == None):
                    self.STM32MCP_tailPtr = None
                self.STM32MCP_queueSize = self.STM32MCP_queueSize - 1
                #Remove the reference to the dequeued node to help with garbage collection
                tempPtr.next = None

        #@fn     STM32MCP_emptyQueue
        #@brief  To empty all the messages in the queue
        #@param  None
        #@return None
        def STM32MCP_emptyQueue(self):
            while(self.STM32MCP_queueIsEmpty() == 0x00):
                self.STM32MCP_dequeueMsg() 


class PayLoadHandler: 
    def checkSum(msg: bytes, size: int) -> int:
       total = 0
       n = 0
       while n!= size:
           total += msg[n]
           n += 1
       return (total & 0xFF) + ((total >> 8) & 0xFF)
    

class STM32MCP_FlowControlManager: 
    def __init__(self):
        self.rxObj = STM32MCP_Lib.STM32MCP_rxMsgObj_t()
    
    def STM32MCP_resetFlowControlHandler(self):
        self.rxObj.currIndex = 0x00
        self.rxObj.payloadlength = 0xFF
    
    def STM32MCP_flowControlHandler(self, receivedByte: int):
        if self.rxObj.currIndex < STM32MCP_Lib.STM32MCP_RX_MSG_BUFF_LENGTH-1:
            return None
        

# @fn      STM32MCP_controlEscooterBehavior
# @brief   To control the escooter behavior
# @param   behaviorID  The ID of the behavior to be controlled
# @return  None
def STM32MCP_controlEscooterBehavior(behaviorID : int):
    if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE:
        length = STM32MCP_Lib.ESCOOTER_BEHAVIOUR_PAYLOAD_LENGTH+3
        txFrame = bytearray(length)
        txFrame[0] = (STM32MCP_Lib.STM32MCP_MOTOR_ID.STM32MCP_MOTOR_1_ID) | (STM32MCP_Lib.ESCOOTER_BEHAVIOR_ID)
        txFrame[1] = STM32MCP_Lib.ESCOOTER_BEHAVIOUR_PAYLOAD_LENGTH
        txFrame[2] = behaviorID
        txFrame[3] = PayLoadHandler.checkSum(txFrame, length-1)

        #Enqueue the message to the txMsg queue
        if STM32MCP_FIFO_Queue.STM32MCP_queueIsEmpty() == 0x01:
            #timerManager.STM32MCP_startTimer()
            STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame, length)
            #uartManager.STM32MCP_uartSendMsg(txFrame, length)
        else:
            STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame, length)


# @fn      STM32MCP_setDynamicCurrent
# @brief   It is used for changing the IQ instantly in order to change the Motor's speed
# @param   throttlePercent:  Throttle percentage (0-100)
#          IQValue:          instant Current (s16A)
# @return  None
def STM32MCP_setDynamicCurrent(throttlePercent: int, IQValue: int):
    if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE:
        length = STM32MCP_Lib.STM32MCP_SET_DYNAMIC_TORQUE_FRAME_PAYLOAD_LENGTH + 3
        txFrame = bytearray(length)
        txFrame[0] = (STM32MCP_Lib.STM32MCP_MOTOR_ID.STM32MCP_MOTOR_1_ID) | (STM32MCP_Lib.STM32MCO_SET_DYNAMIC_TORQUE_FRAME_ID)
        txFrame[1] = STM32MCP_Lib.STM32MCP_SET_DYNAMIC_TORQUE_FRAME_PAYLOAD_LENGTH
        txFrame[2] = throttlePercent  & 0xFF
        txFrame[3] = (throttlePercent >> 8) & 0xFF
        txFrame[4] = (throttlePercent >> 16) & 0xFF
        txFrame[5] = (throttlePercent >> 24) & 0xFF
        txFrame[6] = IQValue & 0xFF
        txFrame[7] = (IQValue >> 8) & 0xFF
        txFrame[8] = (IQValue >> 16) & 0xFF
        txFrame[9] = (IQValue >> 24) & 0xFF
        txFrame[10] = PayLoadHandler.checkSum(txFrame, length-1)
        #Enqueue the message to the txMsg queue
        if STM32MCP_FIFO_Queue.STM32MCP_queueIsEmpty() == 0x01:
            #timerManager.STM32MCP_startTimer()
            STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame, length)
            #uartManager.STM32MCP_uartSendMsg(txFrame, length)
        else:
            STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame, length)


# @fn      ON_BOARD_DIAGNOSIS_BEHAVIOUR
# @brief   To control the on-board diagnosis behavior
# @param   behaviorID  The ID of the behavior to be controlled
# @return  None
def ON_BOARD_DIAGNOSIS_BEHAVIOUR(behaviorID : int):
    if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE:
        length = STM32MCP_Lib.ON_BOARD_DIAGNOSIS_PAYLOAD_LENGTH + 3
        txFrame = bytearray(length)
        txFrame[0] = (STM32MCP_Lib.STM32MCP_MOTOR_ID.STM32MCP_MOTOR_1_ID) | (STM32MCP_Lib.ON_BOARD_DIAGNOSIS_MODE_FRAME_ID)
        txFrame[1] = STM32MCP_Lib.ON_BOARD_DIAGNOSIS_PAYLOAD_LENGTH
        txFrame[2] = behaviorID
        txFrame[3] = PayLoadHandler.checkSum(txFrame, length-1)
        #Enqueue the message to the txMsg queue
        if STM32MCP_FIFO_Queue.STM32MCP_queueIsEmpty() == 0x01:
            #timerManager.STM32MCP_startTimer()
            STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame, length)
            #uartManager.STM32MCP_uartSendMsg(txFrame, length)
        else:
            STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame, length)
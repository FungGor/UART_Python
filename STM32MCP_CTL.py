#This library implements the functions for controllling the STM32 Motor Driver (Applicable for F1xxx and F4xxx Series) 
import STM32MCP_Lib
import numpy as np
import timer_thread_control
from STM32MCP_Lib import STM32MCP_MAXIMUM_NUMBER_OF_NODE


#Object referencing to the first motor controller register attribute
regAttribute = STM32MCP_Lib.STM32MCP_regAttribute_t()

STM32MCP_CBs = STM32MCP_Lib.STM32MCP_CBs_t()

#define UART Configuration Parameters 
#Create UART Objects (Register UART)
UART_PORT  = "COM3"
BAUD_RATE  = 115200
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
            if self.STM32MCP_getQueueSize() <= STM32MCP_MAXIMUM_NUMBER_OF_NODE:
                STM32MCP_tempPtr = STM32MCP_Lib.STM32MCP_txNode_t(txMsg, sizeMsg, None)
                if self.STM32MCP_tailPtr is None:
                    self.STM32MCP_headPtr = STM32MCP_tempPtr
                    self.STM32MCP_tailPtr = STM32MCP_tempPtr
                else:
                    self.STM32MCP_tailPtr.next = STM32MCP_tempPtr
                    self.STM32MCP_tailPtr = STM32MCP_tempPtr
                self.STM32MCP_queueSize = self.STM32MCP_queueSize + 1
            else:
                #Throw Exception Handler 
                #STM32MCP_CBs->exMsgCb(STM32MCP_QUEUE_OVERLOAD);
                #free(txMsg); 
                print("Queue is full, cannot enqueue message")

        # @fn      STM32_dequeueMsg
        # @brief   It is used for dequeuing the txMsg Queue 
        # @return  None
        def STM32MCP_dequeueMsg(self):
            if self.STM32MCP_headPtr is None:
                return None
            self.STM32MCP_headPtr = self.STM32MCP_headPtr.next
            if self.STM32MCP_headPtr is None:
                self.STM32MCP_tailPtr = None
            self.STM32MCP_queueSize = self.STM32MCP_queueSize - 1

        # @fn      STM32MCP_emptyQueue
        # @brief   It is used for emptying the txMsg queue
        # @return  None
        def STM32MCP_emptyQueue(self):
            while self.STM32MCP_queueIsEmpty() == 0x00:
                self.STM32MCP_dequeueMsg()

        def STM32MCP_showMsgQueue(self):
            STM32MCP_currPtr = self.STM32MCP_headPtr
            while STM32MCP_currPtr is not None:
                STM32MCP_currPtr = STM32MCP_currPtr.next


class Packet:
        # @fn     STM32MCP_calCheckSum
        # @brief  It is used to calculate th checksum
        # @param  msg : the encoded txMsg used tocalculate the checksum
        #         size: the size of the uart txMsg in number of bytes
        def calCheckSum(msg, size):
            total = 0
            n = 0
            while (n != size):
                total = total + msg[n]
                n = n + 1
            return (total & 0xFF) + ((total >> 8) & 0xFF)


class Packet_Send:
        # @fn      STM32MCP_getRegisterFrame
        # @brief   It is used to read a value from a relevant motor control
        #          variable. See Get register frame. 
        # @param   motorID:   The motor that will be selected
        #          regID:     The register that you want to read
        def STM32MCP_getRegisterFrame(motorID, regID):
            if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE:
                txFrame = np.zeros((STM32MCP_Lib.STM32MCP_GET_REGISTER_FRAME_PAYLOAD_LENGTH+3),dtype=np.uint8)
                txFrame[0] = motorID | STM32MCP_Lib.STM32MCP_GET_REGISTER_FRAME_ID
                txFrame[1] = STM32MCP_Lib.STM32MCP_GET_REGISTER_FRAME_PAYLOAD_LENGTH
                txFrame[2] = regID
                txFrame[3] = Packet.STM32MCP_calCheckSum(txFrame,3)
                #Insert it into the queue
                if STM32MCP_FIFO_Queue.STM32MCP_queueIsEmpty():
                    STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame,4)
                else:
                    STM32MCP_FIFO_Queue.STM32MCP_enqueueMsg(txFrame,4)

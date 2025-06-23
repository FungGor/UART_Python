#This library implements the functions for controllling the STM32 Motor Driver (Applicable for F1xxx and F4xxx Series) 
import STM32MCP_Lib
import retransmissionHandler
import motor_control

retransmissionCount = 0x00
communicationState = STM32MCP_Lib.STM32MCP_COMMUNICATION_DEACTIVE
queue = None # Global variable to hold the queue instance
uartPtr = None
flowControl = None

#Assign the UART pointer to the global variable uartPtr for accessing the uart perpherals defined in class UART_Protocol() in uart_protocol.py
def STM32MCP_ptrUART_register(ptrUART):
    global uartPtr
    uartPtr = ptrUART

#Assign the Flow Control pointer from uart_protocol.py to the flowControl global variable for accessing the memeber functions in STM32MCP_FlowControlHandler class
def ECU_OBD_Protocol_Register(ptrFlowControl):
    global flowControl
    #Initialize the Queue
    flowControl = ptrFlowControl

class STM32MCP_CommunicationProtocol:
        # @fn       STM32MCP_startCommunication
        # @brief    It is used to start the communication
        # @param    None
        # @return   None
        def STM32MCP_startCommunication():
            global communicationState
            if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_DEACTIVE:
                communicationState = STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE

        # @fn       STM32MCP_closeCommunication
        # @brief    It is used to stop the communication
        # @param    None
        # @return   None
        def STM32MCP_closeCommunication():
            global communicationState
            if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE:
                communicationState = STM32MCP_Lib.STM32MCP_COMMUNICATION_DEACTIVE
                queue.STM32MCP_emptyQueue()
                retransmissionHandler.stop_retransmission_thread()

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
            if ( (self.STM32MCP_headPtr == None) and (self.STM32MCP_tailPtr == None) ):
                return 0x01
            else:
                return 0x00
            
        # @fn      STM32MCP_enqueueMsg
        # @param   txMsg  The memory address of the fist byte of uart tx message
        #          size   The size of the uart tx message in number of bytes 
        # @return  None
        def STM32MCP_enqueueMsg(self,txMsg, sizeMsg):
            if (self.STM32MCP_getQueueSize() <= STM32MCP_Lib.STM32MCP_MAXIMUM_NUMBER_OF_NODE):
                tempPtr = STM32MCP_Lib.STM32MCP_txNode_t(txMsg, sizeMsg) #Create the new node
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
                print("\n")
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
                print("Size of the Queue after dequeue: ", self.STM32MCP_queueSize)
                #Remove the reference to the dequeued node to help with garbage collection
                tempPtr.next = None

        # @fn      STM32MCP_showQueue
        # @brief   To show the contents of the queue (Just for debugging purpose)
        # @param   None
        def STM32MCP_showQueue(self):
            currentPtr = self.STM32MCP_headPtr
            if currentPtr is None:
                print("Queue is empty")
                return
            while currentPtr is not None:
                print(f"Message: { [hex(b) for b in currentPtr.txMsg] }, Size: {currentPtr.size}")
                currentPtr = currentPtr.next

        #@fn     STM32MCP_emptyQueue
        #@brief  To empty all the messages in the queue
        #@param  None
        #@return None
        def STM32MCP_emptyQueue(self):
            while(self.STM32MCP_queueIsEmpty() == 0x00):
                self.STM32MCP_dequeueMsg() 

def MsgQueueInit():
    # Initialize the message queue
    global queue
    queue = STM32MCP_FIFO_Queue()
    queue.STM32MCP_initQueue()
    print("STM32MCP FIFO Queue Initialized")
    print("Queue Size: ", queue.STM32MCP_getQueueSize())
    print("Queue is Empty: ", queue.STM32MCP_queueIsEmpty())

# Test functions to demonstrate the queue functionality
def showQueueStatus():
    global queue
    print("Queue Size after queuing: ", queue.STM32MCP_getQueueSize())
    print("Queue is Empty: ", queue.STM32MCP_queueIsEmpty())

#Test functions to demonstrate the queue functionality
def showAllQueueMessages():
    global queue
    queue.STM32MCP_showQueue()

# Test functions to demonstrate the queue functionality
def clearMsg():
    global queue
    queue.STM32MCP_emptyQueue()

class PayLoadHandler: 
    def checkSum(msg: bytes, size: int) -> int:
       total = 0
       n = 0
       while n!= size:
           total += msg[n]
           n += 1
       return (total & 0xFF) + ((total >> 8) & 0xFF)      
    
def STM32_SERIAL_PORT_INIT():
    print("isInitialized ? :", uartPtr.uartInit())
    print("isOpened ? ", uartPtr.uartOpen())
    print("Status ? ",uartPtr.connectionStatus())

class STM32MCP_FlowControlHandler(): 
    def __init__(self):
        self.rxbuffer = bytearray()
        self.rxObj = STM32MCP_Lib.STM32MCP_rxMsgObj_t(bytearray(STM32MCP_Lib.STM32MCP_RX_MSG_BUFF_LENGTH), 0x00, 0xFF)
        self.rxObj.rxMsgBuf.clear()
    
    # @fn     STM32MCP_resetFlowControlHandler
    # @brief  It is used for resetting the current Index and payloadLength
    # @param  receivedByte: The byte received from uart receiver
    #         rxObj:        An object representing the received message and assosciate variables
    def STM32MCP_resetFlowControlHandler(self):
        self.rxObj.currIndex = 0x00
        self.rxObj.payloadlength = 0xFF

    def flowControlHandler(self, receivedByte):
        global retransmissionCount
        if(self.rxObj.currIndex < STM32MCP_Lib.STM32MCP_RX_MSG_BUFF_LENGTH - 1):
            #Start Receiving Incoming Frame Now !!!
            if(self.rxObj.currIndex == 0x00):
                if queue.STM32MCP_headPtr is not None:
                    #Reset the timer counter
                    #retransmissionHandler.stop_retransmission_counting()
                    #retransmissionHandler.resume_retransmission_counting()
                    #Check if the received byte is a valid starting byte
                    if ((receivedByte == 0xFF) or (receivedByte == 0xF0)):
                        self.rxObj.rxMsgBuf.append(receivedByte)
                        self.rxObj.currIndex += 1
            #What's the length of Payload?
            elif(self.rxObj.currIndex == 0x01):
                #retransmissionHandler.stop_retransmission_counting()
                #retransmissionHandler.resume_retransmission_counting()
                self.rxObj.rxMsgBuf.append(receivedByte)
                self.rxObj.payloadlength = self.rxObj.rxMsgBuf[self.rxObj.currIndex]
                self.rxObj.currIndex += 1
            #Data Frame Processing
            elif(self.rxObj.currIndex < self.rxObj.payloadlength + 0x03):
                #retransmissionHandler.stop_retransmission_counting()
                #retransmissionHandler.resume_retransmission_counting()
                self.rxObj.rxMsgBuf.append(receivedByte)
                self.rxObj.currIndex += 1

            if(self.rxObj.currIndex == self.rxObj.payloadlength + 0x03):
                if(PayLoadHandler.checkSum(self.rxObj.rxMsgBuf, self.rxObj.payloadlength + 2) == receivedByte):
                    if self.rxObj.rxMsgBuf[0] == 0xF0:
                        #retransmissionHandler.stop_retransmission_thread()
                        motor_control.motorcontrol_showReceivedMessage(self.rxObj.rxMsgBuf)
                        #Come to the next transmission
                        # As long as the server receives Acknowledgement from the client with valid message, the queuing message is dequeued 
                        # and the next message is sent
                        queue.STM32MCP_dequeueMsg()
                        if queue.STM32MCP_queueIsEmpty() == 0x00:                           
                            if(queue.STM32MCP_headPtr is not None):
                                uartPtr.uartWrite(queue.STM32MCP_headPtr.txMsg)
                            retransmissionCount = 0x00  # Reset retransmission count after successful transmission
                    elif self.rxObj.rxMsgBuf[0] == 0xFF:
                        motor_control.motorcontrol_exceptionHandler()
                        # ERROR HANDLING --> EXCEPTION HANDLING
                        queue.STM32MCP_dequeueMsg()
                        if queue.STM32MCP_queueIsEmpty() == 0x00:
                            #retransmissionHandler.start_retransmission_thread()
                            if(queue.STM32MCP_headPtr is not None):
                                uartPtr.uartWrite(queue.STM32MCP_headPtr.txMsg)
                            retransmissionCount = 0x00
                    self.rxObj.rxMsgBuf.clear()  # Clear the buffer after processing
                    self.STM32MCP_resetFlowControlHandler()
                else:
                    print("Warning: CRC Error")
                    self.rxObj.rxMsgBuf.clear()
                    self.STM32MCP_resetFlowControlHandler()
        else:
            self.STM32MCP_resetFlowControlHandler()

    def receiveBufferProcessing(self,rx):
        self.rxbuffer.extend(rx)  # Append the received byte to the buffer
        while len(self.rxbuffer) > 1:  # Assuming you want to process after receiving 4 bytes
            for i in range(len(self.rxbuffer)):
                self.flowControlHandler(self.rxbuffer[i])
            self.rxbuffer.clear()
            if len(self.rxbuffer) == 0:
                break

def ECU_Protocol_Retransmission():
    global queue
    global retransmissionCount
    if (queue.STM32MCP_headPtr is not None):
        #retransmissionHandler.start_retransmission_thread()
        uartPtr.uartWrite(queue.STM32MCP_headPtr.txMsg)
        flowControl.STM32MCP_resetFlowControlHandler()
        retransmissionCount += 1
        print("\n")
        print("Retransmission Count: ", retransmissionCount)
        if(retransmissionCount > STM32MCP_Lib.STM32MCP_MAXIMUM_RETRANSMISSION_ALLOWANCE):
            STM32MCP_CommunicationProtocol.STM32MCP_closeCommunication()

def ECU_RetransmitHandling():
    global  retransmissionCount
    retransmissionCount += 1
    print("\n")
    print("Retransmission Count: ", retransmissionCount)
    if(retransmissionCount > STM32MCP_Lib.STM32MCP_MAXIMUM_RETRANSMISSION_ALLOWANCE):
        STM32MCP_CommunicationProtocol.STM32MCP_closeCommunication()

def resetRetransmissionCount():
    global retransmissionCount
    retransmissionCount = 0x00

# @fn      STM32MCP_controlEscooterBehavior
# @brief   To control the escooter behavior
# @param   behaviorID  The ID of the behavior to be controlled
# @return  None
def STM32MCP_controlEscooterBehavior(behaviorID : int):
    global queue
    if communicationState == STM32MCP_Lib.STM32MCP_COMMUNICATION_ACTIVE:
            length = STM32MCP_Lib.ESCOOTER_BEHAVIOUR_PAYLOAD_LENGTH+3
            txFrame = bytearray(length)
            txFrame[0] = (STM32MCP_Lib.STM32MCP_MOTOR_ID.STM32MCP_MOTOR_1_ID) | (STM32MCP_Lib.ESCOOTER_BEHAVIOR_ID)
            txFrame[1] = STM32MCP_Lib.ESCOOTER_BEHAVIOUR_PAYLOAD_LENGTH
            txFrame[2] = behaviorID
            txFrame[3] = PayLoadHandler.checkSum(txFrame, length-1)
            #Enqueue the message to the txMsg queue
            if queue.STM32MCP_queueIsEmpty() == 0x01:
                queue.STM32MCP_enqueueMsg(txFrame, length)
                uartPtr.uartWrite(txFrame)
                #uartManager.STM32MCP_uartSendMsg(txFrame, length)
            else:
                queue.STM32MCP_enqueueMsg(txFrame, length)


# @fn      STM32MCP_setDynamicCurrent
# @brief   It is used for changing the IQ instantly in order to change the Motor's speed
# @param   throttlePercent:  Throttle percentage (0-100)
#          IQValue:          instant Current (s16A)
# @return  None
def STM32MCP_setDynamicCurrent(throttlePercent: int, IQValue: int):
    global queue
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
        if queue.STM32MCP_queueIsEmpty() == 0x01:
            #timerManager.STM32MCP_startTimer()
            queue.STM32MCP_enqueueMsg(txFrame, length)
            uartPtr.uartWrite(txFrame)
            #uartManager.STM32MCP_uartSendMsg(txFrame, length)
        else:
            queue.STM32MCP_enqueueMsg(txFrame, length)

# @fn      ON_BOARD_DIAGNOSIS_BEHAVIOUR
# @brief   To control the on-board diagnosis behavior
# @param   behaviorID  The ID of the behavior to be controlled
# @return  None
def ON_BOARD_DIAGNOSIS_BEHAVIOUR(behaviorID : int):
    global queue
    if communicationState == queue.STM32MCP_COMMUNICATION_ACTIVE:
        length = STM32MCP_Lib.ON_BOARD_DIAGNOSIS_PAYLOAD_LENGTH + 3
        txFrame = bytearray(length)
        txFrame[0] = (STM32MCP_Lib.STM32MCP_MOTOR_ID.STM32MCP_MOTOR_1_ID) | (STM32MCP_Lib.ON_BOARD_DIAGNOSIS_MODE_FRAME_ID)
        txFrame[1] = STM32MCP_Lib.ON_BOARD_DIAGNOSIS_PAYLOAD_LENGTH
        txFrame[2] = behaviorID
        txFrame[3] = PayLoadHandler.checkSum(txFrame, length-1)
        #Enqueue the message to the txMsg queue
        if queue.STM32MCP_queueIsEmpty() == 0x01:
            #timerManager.STM32MCP_startTimer()
            queue.STM32MCP_enqueueMsg(txFrame, length)
            uartPtr.uartWrite(txFrame)
            #uartManager.STM32MCP_uartSendMsg(txFrame, length)
        else:
            queue.STM32MCP_enqueueMsg(txFrame, length)

def Test_Datagram(behaviorID: int) -> bytearray:
    global queue # Make sure to declare it as global if you want to modify or use it
    length = STM32MCP_Lib.STM32MCP_TEST_DATAGRAM_PAYLOAD_LENGTH + 3
    txFrame = bytearray(length)
    txFrame[0] = (STM32MCP_Lib.STM32MCP_MOTOR_ID.STM32MCP_MOTOR_1_ID) | (STM32MCP_Lib.STM32MCP_TEST_DATAGRAM_FRAME_ID)
    txFrame[1] = STM32MCP_Lib.STM32MCP_TEST_DATAGRAM_PAYLOAD_LENGTH
    txFrame[2] = behaviorID
    txFrame[3] = PayLoadHandler.checkSum(txFrame, length-1)
    #Enqueue the message to the txMsg queue
    queue.STM32MCP_enqueueMsg(txFrame, length)
    uartPtr.uartWrite(txFrame)
    #print("Test Datagram: ", [hex(b) for b in txFrame])
    #print("\n")
    return txFrame

def TEST_DATA(byteID: int) -> bytearray:
    txFrame = bytearray(1)
    txFrame[0] = byteID
    length = len(txFrame)
    queue.STM32MCP_enqueueMsg(txFrame, length)
    uartPtr.uartWrite(txFrame)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
#
#
# Before you start using this library, you must read UM1052(Pg161-178).
#
#
#
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!

STM32_NUMBER_OF_REGISTERS  = 0x0A
STM32MCP_NUMBER_OF_MOTORS  = 0x01

#The maximum number of node that the buffer can hold
STM32MCP_MAXIMUM_NUMBER_OF_NODE  = 0x1E
#The maximum number of retransmission is allowed
STM32MCP_MAXIMUM_RETRANSMISSION_ALLOWANCE = 0x0A
#Maximum rx buffer length
STM32MCP_RX_MSG_BUFF_LENGTH = 0x0A
#Haert Beat Period (in ms)
STM32MCP_HEARTBEAT_PERIOD  = 1000
#Retransmission Timout Setting and Configuration i.e. 500 ms 
STM32MCP_TIMEOUT_PERIOD   =   500

#Communication State
STM32MCP_COMMUNICATION_ACTIVE   = 0x00
STM32MCP_COMMUNICATION_DEACTIVE = 0x01

#Register read and write permission
STM32MCP_REGISTER_PERMIT_READ  = 0x01
STM32MCP_REGISTER_PERMIT_WRITE = 0x02

ESCOOTER_BEHAVIOUR_PAYLOAD_LENGTH = 0x01
ESCOOTER_BEHAVIOR_ID       = 0x1B

STM32MCP_SET_DRIVE_MODE_CONFIG_FRAME_ID          = 0x13

STM32MCP_SET_DYNAMIC_TORQUE_FRAME_PAYLOAD_LENGTH = 0x08
STM32MCP_SET_DYNAMIC_TORQUE_FRAME_ID             = 0x14

ON_BOARD_DIAGNOSIS_PAYLOAD_LENGTH      = 0x01
ON_BOARD_DIAGNOSIS_MODE_FRAME_ID       = 0x15

#Just for testing purpose
STM32MCP_TEST_DATAGRAM_PAYLOAD_LENGTH = 0x01
STM32MCP_TEST_DATAGRAM_FRAME_ID       = 0x16
TEST_CASE_1                           = 0x01
TEST_CASE_2                           = 0x02
TEST_CASE_3                           = 0x03

#Select Suitable Motor ID
# @brief     It defines the motor ID of the STM32 motor control protocol
class STM32MCP_MOTOR_ID:
    STM32MCP_MOTOR_LAST_ID   =  0X00
    STM32MCP_MOTOR_1_ID      =  0x20
    STM32MCP_MOTOR_2_ID      =  0x40

#Frame ID to control the motor
# @brief     It defines the frame ID of the STM32 motor control protocol
#            Please see UM1052 (Pg 161 - 178) for more details
class STM32MCP_STARTING_FRAME_CODES:
    #Send necessary commands to the motor controller
    STM32MCP_SET_REGISTER_FRAME_ID            = 0x01
    STM32MCP_GET_REGISTER_FRAME_ID            = 0x02
    STM32MCP_EXECUTE_COMMAND_FRAME_ID         = 0x03
    STM32MCP_GET_BOARD_INFO_FRAME_ID          = 0x06
    STM32MCP_EXECUTE_RAMP_FRAME_ID            = 0x07
    STM32MCP_GET_REVUP_DATA_FRAME_ID          = 0x08
    STM32MCP_SET_REVUP_DATA_FRAME_ID          = 0x09
    STM32MCP_SET_CURRENT_REFERENCES_FRAME_ID  = 0x0A

#Payload Length for frame ID
# @brief     It defines the payload length of the frame ID
class STM32MCP_PAYLOAD_LENGTH:
    #Payload for frame id (except for set_register_frame ID)
    STM32MCP_SET_REGISTER_FRAME_PAYLOAD_LENGTH                                          = 0x03
    #Payload for frame id (except for set_register_frame ID)
    STM32MCP_GET_REGISTER_FRAME_PAYLOAD_LENGTH                                          = 0x01
    STM32MCP_EXECUTE_COMMAND_FRAME_PAYLOAD_LENGTH                                       = 0x01
    STM32MCP_EXECUTE_RAMP_FRAME_PAYLOAD_LENGTH                                          = 0x06
    STM32MCP_GET_BOARD_INFO_FRAME_PAYLOAD_LENGTH                                        = 0x00
    STM32MCP_SET_CURRENT_REFERENCES_FRAME_PAYLOAD_LENGTH                                = 0x04
    STM32MCP_SET_REVUP_DATA_FRAME_PAYLOAD_LENGTH                                        = 0x09
    STM32MCP_GET_REVUP_DATA_FRAME_PAYLOAD_LENGTH                                        = 0x01
    STM32MCP_SET_SYSTEM_CONTROL_CONFIG_PAYLOAD_LENGTH                                   = 0x01
    STM32MCP_ESCOOTER_CONTROL_DEBUG_PAYLOAD_LENGTH                                      = 0x01
    STM32MCP_SET_DRIVING_MODE_CONFIG_PAYLOAD_LENGTH                                     = 0x0A
    STM32MCP_SET_DYNAMIC_TORQUE_FRAME_PAYLOAD_LENGTH                                    = 0x08
    STM32MCP_TARGET_MOTOR_PAYLOAD_LENGTH                                                = 0x02
    STM32MCP_FLAGS_PAYLOAD_LENGTH                                                       = 0x05
    STM32MCP_STATUS_PAYLOAD_LENGTH                                                      = 0x02
    STM32MCP_CONTROL_MODE_PAYLOAD_LENGTH                                                = 0x02
    STM32MCP_SPEED_REFERENCE_PAYLOAD_LENGTH                                             = 0x05
    STM32MCP_SPEED_KP_PAYLOAD_LENGTH                                                    = 0x03
    STM32MCP_SPEED_KI_PAYLOAD_LENGTH                                                    = 0x03
    STM32MCP_SPEED_KD_PAYLOAD_LENGTH                                                    = 0x03
    STM32MCP_TORQUE_REFERENCE_PAYLOAD_LENGTH                                            = 0x03
    STM32MCP_TORQUE_KP_PAYLOAD_LENGTH                                                   = 0x03
    STM32MCP_TORQUE_KI_PAYLOAD_LENGTH                                                   = 0x03
    STM32MCP_TORQUE_KD_PAYLOAD_LENGTH                                                   = 0x03
    STM32MCP_FLUX_REFERENCE_PAYLOAD_LENGTH                                              = 0x03
    STM32MCP_FLUX_KP_PAYLOAD_LENGTH                                                     = 0x03
    STM32MCP_FLUX_KI_PAYLOAD_LENGTH                                                     = 0x03
    STM32MCP_FLUX_KD_PAYLOAD_LENGTH                                                     = 0x03
    STM32MCP_OBSERVER_C1_PAYLOAD_LENGTH                                                 = 0x03
    STM32MCP_OBSERVER_C2_PAYLOAD_LENGTH                                                 = 0x03
    STM32MCP_CORDIC_OBSERVER_C1_PAYLOAD_LENGTH                                          = 0x03
    STM32MCP_CORDIC_OBSERVER_C2_PAYLOAD_LENGTH                                          = 0x03
    STM32MCP_PPL_KI_PAYLOAD_LENGTH                                                      = 0x03
    STM32MCP_PPL_KP_PAYLOAD_LENGTH                                                      = 0x03
    STM32MCP_FLUX_WEAKENING_KP_PAYLOAD_LENGTH                                           = 0x03
    STM32MCP_FLUX_WEAKENING_KI_PAYLOAD_LENGTH                                           = 0x03
    STM32MCP_FLUX_WEAKENING_BUS_VOLTAGE_ALLOWED_PERCENTAGE_REFERENCE_PAYLOAD_LENGTH     = 0x03
    STM32MCP_BUS_VOLTAGE_PAYLOAD_LENGTH                                                 = 0x03
    STM32MCP_HEATSINK_TEMPERATURE_PAYLOAD_LENGTH                                        = 0x03
    STM32MCP_MOTOR_POWER_PAYLOAD_LENGTH                                                 = 0x03
    STM32MCP_DAC_OUT_1_PAYLOAD_LENGTH                                                   = 0x02
    STM32MCP_DAC_OUT_2_PAYLOAD_LENGTH                                                   = 0x02
    STM32MCP_SPEED_MEASURED_PAYLOAD_LENGTH                                              = 0x05
    STM32MCP_TORQUE_MEASURED_PAYLOAD_LENGTH                                             = 0x03
    STM32MCP_FLUX_MEASURED_PAYLOAD_LENGTH                                               = 0x03
    STM32MCP_FLUX_WEAKENING_BUS_VOLTAGE_ALLOWED_PERCENTAGE_MEASURED_PAYLOAD_LENGTH      = 0x03
    STM32MCP_REVUP_STAGE_NUMBERS_PAYLOAD_LENGTH                                         = 0x02
    STM32MCP_MAXIMUM_APPLICATION_SPEED_PAYLOAD_LENGTH                                   = 0x05
    STM32MCP_MINIMUM_APPLICATION_SPEED_PAYLOAD_LENGTH                                   = 0x05
    STM32MCP_IQ_REFERENCE_IN_SPEED_MODE_PAYLOAD_LENGTH                                  = 0x03
    STM32MCP_EXPECTED_BEMF_LEVEL_PLL_PAYLOAD_LENGTH                                     = 0x03
    STM32MCP_OBSERVED_BEMF_LEVEL_PLL_PAYLOAD_LENGTH                                     = 0x03
    STM32MCP_EXPECTED_BEMF_LEVEL_CORDIC_PAYLOAD_LENGTH                                  = 0x03
    STM32MCP_OBSERVED_BEMF_LEVEL_CORDIC_PAYLOAD_LENGTH                                  = 0x03
    STM32MCP_Feedforward_1Q_PAYLOAD_LENGTH                                              = 0x05
    STM32MCP_Feedforward_1D_PAYLOAD_LENGTH                                              = 0x05
    STM32MCP_Feedforward_2_PAYLOAD_LENGTH                                               = 0x05
    STM32MCP_Feedforward_VQ_PAYLOAD_LENGTH                                              = 0x03
    STM32MCP_Feedforward_VD_PAYLOAD_LENGTH                                              = 0x03
    STM32MCP_Feedforward_VQ_PI_OUT_PAYLOAD_LENGTH                                       = 0x03
    STM32MCP_Feedforward_VD_PI_OUT_PAYLOAD_LENGTH                                       = 0x03
    STM32MCP_RAMP_FINAL_SPEED_PAYLOAD_LENGTH                                            = 0x05
    STM32MCP_RAMP_DURATION_PAYLOAD_LENGTH                                               = 0x03


# Error Codes 
# @brief     It defines the error code of the STM32 motor control protocol
#            Please see UM1052 (Pg 161 - 178) for more details
class STM32MCP_ERROR_CODE:
    #Error Code
    STM32MCP_BAD_FRAME_ID       = 0x01
    STM32MCP_WRITE_ON_READ_ONLY = 0x02
    STM32MCP_READ_NOT_ALLOWED   = 0x03
    STM32MCP_BAD_TARGET_DRIVE   = 0x04
    STM32MCP_OUT_OF_RANGE       = 0x05
    STM32MCP_BAD_COMMAND_ID     = 0x07
    STM32MCP_OVERRUN_ERROR      = 0x08
    STM32MCP_TIMEOUT_ERROR      = 0x09
    STM32MCP_BAD_CRC            = 0x0A
    STM32MCP_BAD_TARGET_DRIVE   = 0x0B

#Exception Code
STM32MCP_QUEUE_OVERLOAD                             = 0x01
STM32MCP_EXCEED_MAXIMUM_RETRANSMISSION_ALLOWANCE    = 0x02

#STM32 MOTOR CONTROL PROTOCOL REGISTERS
# @brief     It defines the register ID of the STM32 motor control protocol
class STM32MCP_REG_ID:
    STM32MCP_TARGET_MOTOR_REG_ID                                                  = 0x00
    STM32MCP_FLAGS_REG_ID                                                         = 0x01
    STM32MCP_STATUS_REG_ID                                                        = 0x02
    STM32MCP_CONTROL_MODE_REG_ID                                                  = 0x03
    STM32MCP_SPEED_REFERENCE_REG_ID                                               = 0x04
    STM32MCP_SPEED_KP_REG_ID                                                      = 0x05
    STM32MCP_SPEED_KI_REG_ID                                                      = 0x06
    STM32MCP_SPEED_KD_REG_ID                                                      = 0x07
    STM32MCP_TORQUE_REFERENCE_REG_ID                                              = 0x08
    STM32MCP_TORQUE_KP_REG_ID                                                     = 0x09
    STM32MCP_TORQUE_KI_REG_ID                                                     = 0x0A
    STM32MCP_TORQUE_KD_REG_ID                                                     = 0x0B
    STM32MCP_FLUX_REFERENCE_REG_ID                                                = 0x0C
    STM32MCP_FLUX_KP_REG_ID                                                       = 0x0D
    STM32MCP_FLUX_KI_REG_ID                                                       = 0x0E
    STM32MCP_FLUX_KD_REG_ID                                                       = 0x0F
    STM32MCP_OBSERVER_C1_REG_ID                                                   = 0x10
    STM32MCP_OBSERVER_C2_REG_ID                                                   = 0x11
    STM32MCP_CORDIC_OBSERVER_C1_REG_ID                                            = 0x12
    STM32MCP_CORDIC_OBSERVER_C2_REG_ID                                            = 0x13
    STM32MCP_PPL_KI_REG_ID                                                        = 0x14
    STM32MCP_PPL_KP_REG_ID                                                        = 0x15
    STM32MCP_FLUX_WEAKENING_KP_REG_ID                                             = 0x16
    STM32MCP_FLUX_WEAKENING_KI_REG_ID                                             = 0x17
    STM32MCP_FLUX_WEAKENING_BUS_VOLTAGE_ALLOWED_PERCENTAGE_REFERENCE_REG_ID       = 0x18
    STM32MCP_BUS_VOLTAGE_REG_ID                                                   = 0x19
    STM32MCP_HEATSINK_TEMPERATURE_REG_ID                                          = 0x1A
    STM32MCP_MOTOR_POWER_REG_ID                                                   = 0x1B
    STM32MCP_DAC_OUT_1_REG_ID                                                     = 0x1C
    STM32MCP_DAC_OUT_2_REG_ID                                                     = 0x1D
    STM32MCP_SPEED_MEASURED_REG_ID                                                = 0x1E
    STM32MCP_TORQUE_MEASURED_REG_ID                                               = 0x1F
    STM32MCP_FLUX_MEASURED_REG_ID                                                 = 0x20
    STM32MCP_FLUX_WEAKENING_BUS_VOLTAGE_ALLOWED_PERCENTAGE_MEASURED_REG_ID        = 0x21
    STM32MCP_REVUP_STAGE_NUMBERS_REG_ID                                           = 0x22
    STM32MCP_MAXIMUM_APPLICATION_SPEED_REG_ID                                     = 0x3F
    STM32MCP_MINIMUM_APPLICATION_SPEED_REG_ID                                     = 0x40
    STM32MCP_IQ_REFERENCE_IN_SPEED_MODE_REG_ID                                    = 0x41
    STM32MCP_EXPECTED_BEMF_LEVEL_PLL_REG_ID                                       = 0x42
    STM32MCP_OBSERVED_BEMF_LEVEL_PLL_REG_ID                                       = 0x43
    STM32MCP_EXPECTED_BEMF_LEVEL_CORDIC_REG_ID                                    = 0x44
    STM32MCP_OBSERVED_BEMF_LEVEL_CORDIC_REG_ID                                    = 0x45
    STM32MCP_Feedforward_1Q_REG_ID                                                = 0x46
    STM32MCP_Feedforward_1D_REG_ID                                                = 0x47
    STM32MCP_Feedforward_2_REG_ID                                                 = 0x48
    STM32MCP_Feedforward_VQ_REG_ID                                                = 0x49
    STM32MCP_Feedforward_VD_REG_ID                                                = 0x4A
    STM32MCP_Feedforward_VQ_PI_OUT_REG_ID                                         = 0x4B
    STM32MCP_Feedforward_VD_PI_OUT_REG_ID                                         = 0x4C
    STM32MCP_RAMP_FINAL_SPEED_REG_ID                                              = 0x5B
    STM32MCP_RAMP_DURATION_REG_ID                                                 = 0x5C

# @brief     It defines the command ID of the STM32 motor control protocol
#            Please see UM1052 (Pg 161 - 178) for more details
#Command list
class STM32MCP_EXECUTE_COMMAND_FRAME_ID:
        STM32MCP_START_MOTOR_COMMAND_ID   = 0x01
        STM32MCP_STOP_MOTOR_COMMAND_ID    = 0x02
        STM32MCP_STOP_RAMP_COMMAND_ID     = 0x03
        STM32MCP_START_STOP_COMMAND_ID    = 0x06
        STM32MCP_FAULT_ACK_COMMAND_ID     = 0x07
        STM32MCP_ENCODER_ALIGN_COMMAND_ID = 0x08

class MOTOR_DRIVER_VOLTAGE_RANGE:
        STM32MCP_SYSTEM_MAXIMUM_VOLTAGE = 48000
        STM32MCP_SYSTEM_MINIMUM_VOLTAGE = 28000

# @brief     It defines the ID to control the behaniour of the escooter
class ESCOOTER_BEHAVIOURS:
        ESCOOTER_BOOT_ACK          =  0x00
        ESCOOTER_ERROR_REPORT      =  0x01
        ESCOOTER_THROTTLE_TRIGGER  =  0x02
        ESCOOTER_BRAKE_TRIGGER     =  0x03
        ESCOOTER_BRAKE_RELEASE     =  0x04
        ESCOOTER_TOGGLE_TAIL_LIGHT =  0x05
        ESCOOTER_TAIL_LIGHT_OFF    =  0x06
        ESCOOTER_POWER_OFF         =  0X07
        ESCOOTER_TAIL_LIGHT_ON     =  0x08
        ESCOOTER_TIMEOUT_CHECKING  =  0x09
        ESCOOTER_MOTOR_DRIVER_TEMP =  0x0A
        ESCOOTER_MOTOR_TEMPERATURE =  0x0B
        ESCOOTER_BATTERY_CURRENT   =  0x0C
        ESCOOTER_BATTERY_VOLTAGE   =  0x0D
        ESCOOTER_OBD_MODE          =  0x0E

class ECU_ERROR_CODE:
    SYS_NORMAL_CODE               = 0xFF
    BATTERY_VOLTAGE_ERROR_CODE    = 0x1A
    BATTERY_TEMP_ERROR_CODE       = 0x1A
    BMS_COMM_ERROR_CODE           = 0x1C
    BATTERY_VOLTAGE_CRIT_LOW_CODE = 0x1E
    GATE_DRIVER_ERROR_CODE        = 0x2C
    MOSFET_ERROR_CODE             = 0x2E
    PHASE_I_ERROR_CODE            = 0x2A
    CONTROLLER_TEMP_ERROR_CODE    = 0x2F
    HALL_SENSOR_ERROR_CODE        = 0x3A
    MOTOR_TEMP_ERROR_CODE         = 0x3C
    DASH_COMM_ERROR_CODE          = 0x0A
    THROTTLE_ERROR_CODE           = 0x0C
    BRAKE_ERROR_CODE              = 0x0E
    SOFTWARE_ERROR_CODE           = 0x4A
    SYS_FATAL_ERROR_CODE          = 0x0F

# Structure STM32MCP_rxMsg
# @brief     When the motor controller sends the received message back, it stores the message here
# @data      rxMsg - The memory message to the received message, the size of the message is the second index rxMsg[1]
#            motorID - The motor ID described in STM32MCP
#            frameID - The frame ID described in STM32MCP
class STM32MCP_rxMsg_t:
   def __init__ (self, frameID, rxPayloadLength, txPayloadLength, rxPayload, txPayload):
     self.framID = frameID
     self.rxPayloadLength = rxPayloadLength
     self.txPayloadLength = txPayloadLength
     self.rxPayload = rxPayload
     self.txPayload = txPayload


# @Structure STM32MCP_exMsg
# @brief     When the motor controller sends the exception, it stores the message here
# @data      exceptionCode - The exception code described in STM32MCP
class STM32MCP_exMsg_t:
    def __init__(self, exceptionCode):
     self.exceptionCode = exceptionCode


# @Structure STM32MCP_erMsg_t
# @brief     When the motor controller sends the error back, it stores the message here
# @data      exceptionCode - The error code described in STM32MCP
class STM32MCP_erMsg_t:
    def __init__(self, errorCode):
        self.errorCode = errorCode


# @Structure STM32MCP_regAttribute_t
# @brief     It is used to define a stm32 motor control register
#            Please see UM1052 (Pg 161 - 178) for more details
#
# @data      regID:            The register ID
#            payloadLength:    The length of the payload
#            payload:          The pointer of the payload
#            permission:       Read/Write permission
class STM32MCP_regAttribute_t:
    def __init__(self, regID, payloadLength, payload, permission):
        self.regID = regID
        self.payloadLength = payloadLength
        self.payload = payload
        self.permission = permission


# @Structure STM32MCP_txMsgNode   (Singly Linked List)
# @brief     It defines a message Node to be transmit.
#            Multiple node will be linked together
#            to form a FIFO transmit buffer
# 
# @data      txMsg:   The pointer to an array of bytes
#            size:    The size of the array
#            next:    The pointer of the next tx message node
class STM32MCP_txNode_t:
    def __init__(self, txMsg, size):
        self.txMsg = txMsg
        self.size = size
        self.next = None


# @Structure STM32MCP_rxMsgObj_t
# @brief     It stores the array of received bytes, payload length
#            and the current index of the received byte. When all
#            bytes are received, it will go through CRC checking
#            and pass the message to upper layer.
# 
# @data      rxMsgBuf:      An array of received bytes
#            currIndex:     The current index of the received byte
#            payloadLength: The expected payload length of the data
class STM32MCP_rxMsgObj_t:
    def __init__(self, rxMsgBuf, currIndex, payloadLength):
        self.rxMsgBuf = rxMsgBuf   #Should be a bytes or bytearray object
        self.currIndex = currIndex #Integer
        self.payloadlength = payloadLength #Integer


# @Structure STM32MCP_CBs_t
# @brief     It defines a set of function pointer that the server
#            wants to point to the application functions
#
# @data      rxHandler:  Called when received data passed CRC checking, it will be passed to rxMsgCb
#            exHandler:  Called when there are exception
#            erHandler:  Called when there are error
def STM32MCP_CBs_t():
    def rxHandler():
        return 0
    
    def exHanler():
        return 0
    
    def erHandler():
        return 0

            

# @Structure Inheritance Stucture -- STM32MCP_timerManager_t
# @brief     It defines a set of function pointer that the server
#            wants to point to the application functions
# @data      timerStart: Called when the server wants to start the retransmission timer
#            timerResetCounter: Reset the counter to zero
#            timerStop:  Called when the server wants to stop the retransmission timer
class STM32MCP_timerManager_t:
    def STM32MCP_timerStart():
        return 0

    def STM32MCP_timerResetCounter():
        return 0

    def STM32_timerStop():
        return 0
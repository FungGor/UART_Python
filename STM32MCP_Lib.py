#THE FOLLOWING PARAMETERS COME FROM THE STM32 FOC COMMAND LIST. FOR MORE DETAILS, PLEASE READ THE SDK
STM32_NUMBER_OF_REGISTERS  = 0x0A
STM32MCP_NUMBER_OF_MOTORS  = 0x01

#The maximum number of node that the buffer can hold
STM32MCP_MAXIMUM_NUMBER_OF_NODE  = 0x28

#The maximum number of retransmission is allowed
STM32MCP_MAXIMUM_RETRANSMISSION_ALLOWANCE = 0x0A

#Maximum rx buffer length
STM32MCP_RX_MSG_BUFF_LENGTH = 0xFF

#Register read and write permission
STM32MCP_REGISTER_PERMIT_READ  = 0x01
STM32MCP_REGISTER_PERMIT_WRITE = 0x02

#Frame ID
STM32MCP_MOTOR_LAST_ID   =  0X00
STM32MCP_MOTOR_1_ID      =  0x20
STM32MCP_MOTOR_2_ID      =  0x40

STM32MCP_SET_REGISTER_FRAME_ID           = 0x01
STM32MCP_GET_REGISTER_FRAME_ID           = 0x02
STM32MCP_EXECUTE_COMMAND_FRAME_ID        = 0x03
STM32MCP_GET_BOARD_INFO_FRAME_ID         = 0x06
STM32MCP__EXECUTE_RAMP_FRAME_ID          = 0x07
STM32_GET_REVUP_DATAFRAME_ID             = 0x08
STM32MCP_SET_CURRENT_REFERENCES_FRAME_ID = 0x0A

#Payload for frame id (except for set_register_frame ID)
STM32MCP_GET_REGISTER_FRAME_PAYLOAD_LENGTH           = 0x01
STM32MCP_EXECUTE_COMMAND_FRAME_PAYLOAD_LENGTH        = 0x01
STM32MCP_EXECUTE_RAMP_FRAME_PAYLOAD_LENGTH           = 0x06
STM32MCP_GET_BOARD_INFO_FRAME_PAYLOAD_LENGTH         = 0x00
STM32MCP_SET_CURRENT_REFERENCES_FRAME_PAYLOAD_LENGTH = 0x04
STM32MCP_SET_REVUP_DATA_FRAME_PAYLOAD_LENGTH         = 0x09
STM32MCP_GET_REVUP_DATA_FRAME_PAYLOAD_LENGTH         = 0x01

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

#Register ID
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

#Payload length for regID
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

#Command list
STM32MCP_START_MOTOR_COMMAND_ID                                                     = 0x01
STM32MCP_STOP_MOTOR_COMMAND_ID                                                      = 0x02
STM32MCP_STOP_RAMP_COMMAND_ID                                                       = 0x03
STM32MCP_START_STOP_COMMAND_ID                                                      = 0x06
STM32MCP_ENCODER_ALIGN_COMMAND_ID                                                   = 0x08
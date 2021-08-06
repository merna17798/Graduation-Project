/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2021 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "mlx90614.h"
#include "max30100.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
I2C_HandleTypeDef hi2c1;
I2C_HandleTypeDef hi2c2;

UART_HandleTypeDef huart1;
UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART1_UART_Init(void);
static void MX_I2C1_Init(void);
static void MX_I2C2_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
float temp_obj1=0 ;
float temp_amb=0 ;
uint16_t t_amb =0;
uint16_t t_amb_sum =0;
uint16_t t_amb_sum1 =0;
uint16_t t_d_sum1 =0;
uint8_t data_spo2_ir=0;
uint8_t data_spo2=0;
uint8_t data_ir=0;
uint8_t data_temp=0;
uint8_t data_temp_amb=0;
//uint16_t t_d[30]={0};
uint16_t t_d=0;
uint16_t t_d_sum =0;
uint16_t ir=0;
uint16_t spo2=0;
uint16_t t=0;
uint8_t counter=1+'0';
uint8_t MAX30100_Start_Flag=1+'0';
uint8_t SPO2_Flag=2+'0';
uint8_t HR_Flag=3+'0';
uint8_t TempTip_StartFlag=4+'0';
uint8_t TempTip_BodyFlag=5+'0';
uint8_t TempTip_AmpFlag=6+'0';
uint8_t TempRest_StartFlag=7+'0';
uint8_t TempRest_BodyFlag=8+'0';
uint8_t TempRest_AmbFlag=9+'0';
HAL_StatusTypeDef r_data_spo2_ir;
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  MX_I2C1_Init();
  MX_I2C2_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_TOMIN, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_TOMAX, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_PWMCTRL, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_TARANGE, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_EMISSIVITY, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_CFG1, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_SA, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_ID1, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_ID2, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_ID3, MLX90614_DBG_ON);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_ID4, MLX90614_DBG_ON);
  MLX90614_WriteReg(MLX90614_DEFAULT_SA, MLX90614_CFG1, 0xB7C0);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_CFG1, MLX90614_DBG_ON);
  MLX90614_WriteReg(MLX90614_DEFAULT_SA, MLX90614_PWMCTRL, 0x1405);
  MLX90614_ReadReg(MLX90614_DEFAULT_SA, MLX90614_PWMCTRL, MLX90614_DBG_ON);
  /* USER CODE END 2 */
  MAX30100_Init(&hi2c2);
  MAX30100_SetSpO2SampleRate(MAX30100_SPO2SR_DEFAULT);
  MAX30100_SetLEDPulseWidth(MAX30100_LEDPW_DEFAULT);
  MAX30100_SetLEDCurrent(MAX30100_LEDCURRENT_DEFAULT, MAX30100_LEDCURRENT_DEFAULT);
  MAX30100_SetMode(MAX30100_SPO2_MODE);
  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
while(1){
//
//	HAL_UART_Transmit(&huart2, &MAX30100_Start_Flag, sizeof(MAX30100_Start_Flag),1000);
//	counter++;
//	HAL_Delay(1000);
//	r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
//	HAL_Delay(1000);
	//	counter ++;
//
//	 if(data_spo2_ir==50){
//		 HAL_UART_Transmit(&huart2, &MAX30100_Start_Flag, sizeof(MAX30100_Start_Flag),1000);
//		 counter++;
//		 HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13);
//		 HAL_Delay(1000);
//	 }

//	for (int i=0;i<20;i++)
//	{
//	  temp_obj1 = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TOBJ1);
//	  HAL_Delay(5);
//
//	  temp_amb = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TAMB);
//	  HAL_Delay(5);
//	  t_d[i]=temp_obj1 ;
//
//	  t_amb=temp_amb ;
//	  HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
//	  HAL_Delay(100);
//	  t_d_sum+=t_d[i];
//	}
//	t=t_d_sum/20;
    /* USER CODE BEGIN 3 */
	r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
	if(r_data_spo2_ir==HAL_OK){
		if(data_spo2_ir==49){
			MAX30100_ReadFIFO();
			if(_max30100_mode == MAX30100_SPO2_MODE)
			{
				MAX30100_PlotBothToUART(_max30100_red_sample, _max30100_ir_sample, 16);
			}

			for(int i=0;i<16;i++){
				spo2+=_max30100_red_sample[i];
				ir+=_max30100_ir_sample[i];
			}
			spo2=(spo2/16)+'0';
			ir=(ir/16)+'0';
//			flag='1';
			//data_spo2_ir=0;
			HAL_UART_Transmit(&huart2, &MAX30100_Start_Flag, sizeof(MAX30100_Start_Flag),1000);
			r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
			if(data_spo2_ir==50){
				HAL_UART_Transmit(&huart2, &SPO2_Flag, sizeof(SPO2_Flag),1000);
				HAL_Delay(1000);
				HAL_UART_Transmit(&huart2, &ir, sizeof(ir),1000);
						//data_spo2_ir=0;
						//			HAL_Delay(100);
				r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
				if(data_spo2_ir==51){
					HAL_UART_Transmit(&huart2, &HR_Flag, sizeof(HR_Flag),1000);
					HAL_Delay(1000);
					HAL_UART_Transmit(&huart2, &spo2, sizeof(spo2),1000);
					//data_spo2_ir=0;

																}
								}


		}



		if(data_spo2_ir==52){

			temp_amb = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TAMB);
			temp_obj1 = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TOBJ1);
			t_d=temp_obj1 ;
			t_amb=temp_amb ;
			//data_spo2_ir=0;
			HAL_UART_Transmit(&huart2, &TempTip_StartFlag, sizeof(TempTip_StartFlag),1000);

			r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
			HAL_Delay(2000);
			if(data_spo2_ir==53){
				HAL_UART_Transmit(&huart2, &TempTip_BodyFlag, sizeof(TempTip_BodyFlag),1000);
				HAL_Delay(1000);
				HAL_UART_Transmit(&huart2, &t_d, sizeof(t_d),1000);
				data_spo2_ir=0;
				r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
				if(data_spo2_ir==54){
					HAL_UART_Transmit(&huart2, &TempTip_AmpFlag, sizeof(TempTip_AmpFlag),1000);
					HAL_Delay(1000);
					HAL_UART_Transmit(&huart2, &t_amb, sizeof(t_amb),1000);
					data_spo2_ir=0;
							}

			}

		}


		if(data_spo2_ir==55){

			temp_amb = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TAMB);
			temp_obj1 = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TOBJ1);
			t_d=temp_obj1 ;
			t_amb=temp_amb ;
			//data_spo2_ir=0;
			HAL_UART_Transmit(&huart2, &TempRest_StartFlag, sizeof(TempRest_StartFlag),1000);
			r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
			if(data_spo2_ir==56){
				HAL_UART_Transmit(&huart2, &TempRest_BodyFlag, sizeof(TempRest_BodyFlag),1000);
				HAL_Delay(1000);
				HAL_UART_Transmit(&huart2, &t_d, sizeof(t_d),1000);
				//data_spo2_ir=0;
				r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
				if(data_spo2_ir==57){
					HAL_UART_Transmit(&huart2, &TempRest_AmbFlag, sizeof(TempRest_AmbFlag),1000);
					HAL_Delay(1000);
					HAL_UART_Transmit(&huart2, &t_amb, sizeof(t_amb),1000);
					data_spo2_ir=0;

				}

			}
		}



	}
	while(r_data_spo2_ir==HAL_TIMEOUT){
		r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
		if(r_data_spo2_ir==HAL_OK){
			if(data_spo2_ir==49){
					MAX30100_ReadFIFO();
					if(_max30100_mode == MAX30100_SPO2_MODE)
					{
						MAX30100_PlotBothToUART(_max30100_red_sample, _max30100_ir_sample, 16);
					}

					for(int i=0;i<16;i++){
						spo2+=_max30100_red_sample[i];
						ir+=_max30100_ir_sample[i];
					}
					spo2=(spo2/16)+'0';
					ir=(ir/16)+'0';
		//			flag='1';
					//data_spo2_ir=0;
					HAL_UART_Transmit(&huart2, &MAX30100_Start_Flag, sizeof(MAX30100_Start_Flag),1000);
					r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
					if(data_spo2_ir==50){
						HAL_UART_Transmit(&huart2, &SPO2_Flag, sizeof(SPO2_Flag),1000);
						HAL_Delay(1000);
						HAL_UART_Transmit(&huart2, &ir, sizeof(ir),1000);
						//data_spo2_ir=0;
						//			HAL_Delay(100);
						r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
						if(data_spo2_ir==51){
							HAL_UART_Transmit(&huart2, &HR_Flag, sizeof(HR_Flag),1000);
							HAL_Delay(1000);
							HAL_UART_Transmit(&huart2, &spo2, sizeof(spo2),1000);
							//data_spo2_ir=0;

																		}
										}





			}


			if(data_spo2_ir==52){

				temp_amb = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TAMB);
				temp_obj1 = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TOBJ1);
				t_d=temp_obj1 ;
				t_amb=temp_amb ;
				//data_spo2_ir=0;
				HAL_UART_Transmit(&huart2, &TempTip_StartFlag, sizeof(TempTip_StartFlag),1000);
				r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
				if(data_spo2_ir==53){
					HAL_UART_Transmit(&huart2, &TempTip_BodyFlag, sizeof(TempTip_BodyFlag),1000);
					HAL_Delay(1000);
					HAL_UART_Transmit(&huart2, &t_d, sizeof(t_d),1000);
					//data_spo2_ir=0;
					r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
					if(data_spo2_ir==54){
						HAL_UART_Transmit(&huart2, &TempTip_AmpFlag, sizeof(TempTip_AmpFlag),1000);
						HAL_Delay(1000);
						HAL_UART_Transmit(&huart2, &t_amb, sizeof(t_amb),1000);
						data_spo2_ir=0;
								}

				}

			}


			if(data_spo2_ir==55){

				temp_amb = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TAMB);
				temp_obj1 = MLX90614_ReadTemp(MLX90614_DEFAULT_SA, MLX90614_TOBJ1);
				t_d=temp_obj1 ;
				t_amb=temp_amb ;
				//data_spo2_ir=0;
				HAL_UART_Transmit(&huart2, &TempRest_StartFlag, sizeof(TempRest_StartFlag),1000);
				r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
				if(data_spo2_ir==56){
					HAL_UART_Transmit(&huart2, &TempRest_BodyFlag, sizeof(TempRest_BodyFlag),1000);
					HAL_Delay(1000);
					HAL_UART_Transmit(&huart2, &t_d, sizeof(t_d),1000);
					//data_spo2_ir=0;
					r_data_spo2_ir=HAL_UART_Receive(&huart2, &data_spo2_ir, sizeof(data_spo2_ir),1000);
					if(data_spo2_ir==57){
						HAL_UART_Transmit(&huart2, &TempRest_AmbFlag, sizeof(TempRest_AmbFlag),1000);
						HAL_Delay(1000);
						HAL_UART_Transmit(&huart2, &t_amb, sizeof(t_amb),1000);
						data_spo2_ir=0;

					}

				}
			}



		}

	}
  }//while
  /* USER CODE END 3 */
}//main

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief I2C1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_I2C1_Init(void)
{

  /* USER CODE BEGIN I2C1_Init 0 */

  /* USER CODE END I2C1_Init 0 */

  /* USER CODE BEGIN I2C1_Init 1 */

  /* USER CODE END I2C1_Init 1 */
  hi2c1.Instance = I2C1;
  hi2c1.Init.ClockSpeed = 100000;
  hi2c1.Init.DutyCycle = I2C_DUTYCYCLE_2;
  hi2c1.Init.OwnAddress1 = 0;
  hi2c1.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
  hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
  hi2c1.Init.OwnAddress2 = 0;
  hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
  hi2c1.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;
  if (HAL_I2C_Init(&hi2c1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN I2C1_Init 2 */

  /* USER CODE END I2C1_Init 2 */

}

/**
  * @brief I2C2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_I2C2_Init(void)
{

  /* USER CODE BEGIN I2C2_Init 0 */

  /* USER CODE END I2C2_Init 0 */

  /* USER CODE BEGIN I2C2_Init 1 */

  /* USER CODE END I2C2_Init 1 */
  hi2c2.Instance = I2C2;
  hi2c2.Init.ClockSpeed = 100000;
  hi2c2.Init.DutyCycle = I2C_DUTYCYCLE_2;
  hi2c2.Init.OwnAddress1 = 0;
  hi2c2.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
  hi2c2.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
  hi2c2.Init.OwnAddress2 = 0;
  hi2c2.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
  hi2c2.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;
  if (HAL_I2C_Init(&hi2c2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN I2C2_Init 2 */

  /* USER CODE END I2C2_Init 2 */

}

/**
  * @brief USART1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART1_UART_Init(void)
{

  /* USER CODE BEGIN USART1_Init 0 */

  /* USER CODE END USART1_Init 0 */

  /* USER CODE BEGIN USART1_Init 1 */

  /* USER CODE END USART1_Init 1 */
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 115200;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART1_Init 2 */

  /* USER CODE END USART1_Init 2 */

}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 9600;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_SET);

  /*Configure GPIO pin : PC13 */
  GPIO_InitStruct.Pin = GPIO_PIN_13;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/

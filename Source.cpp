#define TRUE 1 #define FALSE 0 

#define F_CPU 4000000UL  // 4 MHz XTAL 

#define CMD_RESET   0x1E // ADC reset command 
#define CMD_ADC_READ 0x00 // ADC read command 
#define CMD_ADC_CONV 0x40 // ADC conversion command 
#define CMD_ADC_D1   0x00 // ADC D1 conversion 
#define CMD_ADC_D2   0x10 // ADC D2 conversion 
#define CMD_ADC_256  0x00 // ADC OSR=256
#define CMD_ADC_512  0x02 // ADC OSR=512 
#define CMD_ADC_1024 0x04 // ADC OSR=1024 
#define CMD_ADC_2048 0x06  // ADC OSR=2056 
#define CMD_ADC_4096 0x08 // ADC OSR=4096 
#define CMD_PROM_RD  0xA0 // Prom read command 

#define csb_hi() (_SFR_BYTE(PORTA) &= ~_BV(3))  // setting CSB low 
#define csb_lo() (_SFR_BYTE(PORTA) |=  _BV(3))  // setting CSB high 

//_____ I N C L U D E S  

#include <stdio.h> 
#include <util/delay.h> 
#include <avr/io.h> 
#include <math.h> 

//_____ D E F I N I T I O N S  

void spi_send(char cmd); 
void cmd_reset(void); 
unsigned long cmd_adc(char cmd); 
unsigned int cmd_prom(char coef_num); 
unsigned char crc4(unsigned int n_prom[]);

//******************************************************** //! @brief send 8 bit using SPI hardware interface //! //! @return 0  //******************************************************** void spi_send(char cmd) {   SPDR= cmd; // put the byte in the SPI hardware buffer and start sending   while (bit_is_clear(SPSR, 7));      // wait that the data is sent } 

//******************************************************** //! @brief send reset sequence //! //! @return 0  //******************************************************** 

void cmd_reset(void) {
	csb_lo();   // pull CSB low to start the command  
	spi_send(CMD_RESET); // send reset sequence  
	_delay_ms(3);   // wait for the reset sequence tim ing  
	csb_hi();   // pull CSB high to finish the command
}

//******************************************************** //! @brief preform adc conversion //! //! @return 24bit result //******************************************************** 
unsigned long cmd_adc(char cmd) {
	unsigned int ret;
	unsigned long temp = 0;
	csb_lo();      // pull CSB low  
	spi_send(CMD_ADC_CONV + cmd);   // send conversion c ommand  
	switch (cmd & 0x0f)     // wait necessary conversi on time  
	{
	case CMD_ADC_256:_delay_us(900); break;
	case CMD_ADC_512: _delay_ms(3);   break;
	case CMD_ADC_1024: _delay_ms(4);   break;
	case CMD_ADC_2048: _delay_ms(6);   break;
	case CMD_ADC_4096: _delay_ms(10);  break;
	}

	csb_hi();     // pull CSB high to finish the conve rsion  
	csb_lo();     // pull CSB low to start new command
	spi_send(CMD_ADC_READ);   // send ADC read command
	spi_send(0x00);    // send 0 to read 1st byte (MSB )  
	ret = SPDR;
	temp = 65536 * ret;
	spi_send(0x00);    // send 0 to read 2nd byte  
	ret = SPDR;
	temp = temp + 256 * ret;
	spi_send(0x00);    // send 0 to read 3rd byte (LSB )  
	ret = SPDR;
	temp = temp + ret;
	csb_hi();     // pull CSB high to finish the read command  
	return temp;
}

				   //******************************************************** //! @brief Read calibration coefficients //! //! @return coefficient //******************************************************** 

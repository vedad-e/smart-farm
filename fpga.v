module servo_motor(
    input clk,
	 input btn1,
	 input btn2,
	 input rain,
	 input dht11;
	 output servo3,
	 output pumpa1,
	 output pumpa2);

reg [19:0] counter; //
reg servo_reg1;
reg servo_reg2;
reg pumpa1_reg = 0;
reg pumpa2_reg = 0;
reg pumpaAdo = 0;
reg servo_reg3 =0;
reg rain_reg = 0;
reg [19:0] ugao;
reg [19:0] ugao2;
reg [19:0] ugao3;
reg mojBtn1  = 1;

reg [15:0] control = 0;
reg         toggle = 1;

always@(posedge clk)
begin
    //if( btn1) ugao = 75000; else ugao = 20000;
	 if ( btn1 ) ugao = 30000; else ugao = 85000;
	 if ( btn2 ) ugao2 = 30000; else ugao2 = 85000;
	 if ( dht11 ) ugao3 = 30000; else ugao3 = 85000;
	 
	 if ( btn1 )
		pumpa1_reg = 0;
	 else 
		pumpa1_reg = 1;
		
	if( rain) 
		pumpa2_reg = 0;
	else 
		pumpa2_reg = 1;
		
	if (btn2)
		pumpaAdo = 0;
	else 
		pumpaAdo = 1;
	
	if( dht11 ) 
		servo_reg3 <= 1;
	else 
		servo_reg3 <= 0;
    
	 counter <= counter + 1;
    if(counter == 'd999999) //proslo 20ms (trebamo poslat impuls
	 begin 
			counter <= 0;
	 end

    
    //if (counter < 'd75000) //dakle sve dok je counter manji od 50k gurat cemo motor
	if ( counter < ugao ) 
		begin 
			servo_reg1 <= 1;  //setujemp PWM da je pozitivan
		end
    else 
		begin
        servo_reg1 <= 0;
		  end
		if (counter <ugao2)
			servo_reg2 <=1;
		else 
			servo_reg2 <=0;
		if (counter < ugao3 )
			servo_reg3 <=1;
			else
			servo_reg3 <=0;
	 
end

assign servo1 = servo_reg1;

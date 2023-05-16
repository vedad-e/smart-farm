# Smart Farm
The goal of this project is to research and implement a Smart Farm based on IoT, FPGA and Raspberry Pi systems in order to increase the quality and quantity of the product.

The idea of this project is a system that would facilitate the work of farmers. The smart farm project would monitor certain parameters and situations on the farm and thereby make decisions in certain situations to make the work of the farmer easier.

SMART FARM is a project designed to work on the following principle:  
• Existence of a greenhouse inside which temperature and soil moisture sensors will be positioned. Depending on the value read from the sensor, certain actuators start working  
• A large field that will have a rain sensor through which we will know if it is necessary to irrigate the land  
• A hangar that will have a robotic arm whose main goal is to check whether there is a sufficient amount of water in the troughs, and to top it up if necessary.  

### Components
• Cyclone IV EP4CE6  
• Raspberry Pi  
• Arduino UNO  
• Humidity Soil Sensor  
• Rain Sensor  
• DHT11 sensor  
• Ultrasonic sensor  
• Stepper motors  
• Servo motors  
• Water pumps  

### Work Algorithm
• FPGA
  1. If the temperature sensor reads that the temperature inside the greenhouse is higher than 30 degrees, the motor that opens the window is activated. The window is open until the temperature is below 30 degrees
  2. When the rain sensor located in the field detects that it is raining, the water pump will not be activated, and the field will not be irrigated. Otherwise, the pump is activated and irrigation is carried out
  3. In case the soil moisture sensor reads that the crops need to be watered, a signal is sent to the pump to activate. When the soil is wet, the pump stops.
  4. If the pH sensor reads that the soil is acidic and needs a solution, a signal is sent to the pump, which releases that solution into the field.

It is worth noting that the rain sensor and soil moisture sensor in the greenhouse are connected to the same pump. In the event that both the field and the greenhouse need water at the same time, the pump is able to water them. Also in the case when water is needed only for the field or only for the greenhouse, the pump works on such a principle that it can supply only one part.

  The second greenhouse houses the pH sensor and has its own separate pump that activates when needed.

• RASPBERRY
  1. The robot moves along the x and y axes, and checks the 4 troughs in which there should be water. If the ultrasonic sensor detects that water is needed in the trough, a signal is sent to the pump, which is activated and the trough is replenished. In the case when the trough is filled with water, the pump is not activated and the robot goes to check the next trough.

### Photos of the project
<img src="https://i.imgur.com/Yavpgh1.jpg" width="250" height="350">
<img src="https://i.imgur.com/D8obSJ1.jpg" width="450" height="350">
<img src="https://i.imgur.com/RFYtH0r.jpg" width="450" height="350">
<img src="https://i.imgur.com/dPvGxdh.jpg" width="450" height="350">
<img src="https://i.imgur.com/rHkruvp.jpg" width="250" height="350">

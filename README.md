
# AQI-BOLT-IOT
REAL TIME AQI ALERTS
 

Pollution enters the earth's atmosphere in different ways, but the current burning issue is regarding air pollution as the world is getting developed with its new technology and inventions there are lot of harmful emissions which causes our atmosphere polluted.
 
People going out in polluted areas without precautions can also cause them prone to many respiratory diseases. To avoid this problem i have come up with an idea of message alert while going out and checking the air quality index in that area using BOLT IOT.

 
Some can argue that they can go through different apps for checking air quality index for that day ,but in such busy lives it is very difficult for people to remember it everyday. This project uses air pollution api and coordinates of your current place and sends you an alert message. This will ease the process and is technologically innovative too.
THINGS USED IN THIS PROJECT:
1.	HARDWARE COMPONENTS:
•	Bolt WIFI module
•	Buzzer
•	Male female wires (Everything is included in the BOLT IOT kit)
2. SOFTWARE COMPONENTS:
•	Bolt IOT Cloud.
•	Digital ocean droplet
•	Twilio account
•	Libraries:
1.	Bolt IOT python Library.
2.	Requests Library.
3.	Twilio Library.
4.	Openweathermap Library.
5.	Apscheduler Library.
HARDWARE SETUP
1. Hardware connections –
a) Take your bolt wifi module and make a connection from small pin of buzzer to GND of bolt module with the use of male female connecting wire.
b) Take another wire and connect longer pin of buzzer to A0 of bolt module
c) Give power supply with the help of USB cable.
2. Schematics –
 
Software Configuration And Programming:
Bolt IOT Cloud Configuration:
1.	The process starts by first getting registered at Bolt Cloud.
2. Now go to Products tab in sidebar and click on add product to create a product.
 
3. As soon as you will click the add product button, build product window will pop up. Enter product name and upload icon image as per your choice. Beside that select other options as shown in the image below.
 
4. After product build is completed your product will be available in products tab. Select it and then select configure product as shown in the image below.
 
5. Here you just need to specify the design because the coding part will be carried out using bolt python library which will be later taken care of. So as you can see in the below image, you need to select a digital pin which we have selected as pin 0 for one end of buzzer and the another end is connected to the ground. As soon as the pin is selected it needs to be assigned a variable name of your choice. Beside this you can also select the data collection rate ranging from 5 minutes to 24 hours. As soon as you are done with configurations you can save it by selecting save option from top right.
 
6. Now our product is ready to be linked with the bolt device.
 
7. As soon as you click the button showed in the above pic an alert will be displayed which will prompt you to select a device.
 
With clicking done your product is ready being linked to a device. Now we will head towards coding part. 
You can note your api keys from open weather and twilio accounts.
Programming:
You will have two files as config.py and air.py. I have used python for programming this device.
https://github.com/rtejasri02/AQI-BOLT-IOT/tree/main
Conclusion:
Here this project can also be extended by getting alert messages using "OK GOOGLE "voice controls.

For detailed doccumentation  you can go through the below file.
[STOP POLLUTION BY MITIGATION.docx](https://github.com/rtejasri02/AQI-BOLT-IOT/files/10832985/STOP.POLLUTION.BY.MITIGATION.docx)

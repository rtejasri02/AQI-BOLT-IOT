import config, requests, time 
from boltiot import Sms, Bolt  

mybolt = Bolt(config.api_key, config.device_id)
response = mybolt.isOnline()
print (response)
sms = Sms(config.SID, config.AUTH_TOKEN, config.TO_NUMBER, config.FROM_NUMBER) 

lat = "YOUR LATITUDE"
lat = str(lat)

long = "YOUR LONGITUDE"
long = str(long)
complete_url = config.weather_base_url + "lat=" + lat + "&lon=" + long + "&appid=" + config.weather_api_key
response = requests.get(complete_url)
x = response.json()
print(x["list"])
list = x["list"]

main = list[0]["main"]
aqi = main["aqi"]
if aqi == 5 or aqi == 4 :
    print("Avoid going out and try using HEPA filter at home")
    response = mybolt.digitalWrite('0', 'HIGH')
    print("Making request to Twilio to send a SMS")
    res = sms.send_sms("It's a code red day for ozone!Avoid going out and try using HEPA filter at home")
    print("Response from twilio is" + str(res))
    print("status of sms at twilio is :" + str(res.status))
     
    time.sleep(3)
    response = mybolt.digitalWrite('0', 'LOW')
if aqi == 3 or aqi == 2 :
     print("Orange alert!Air quality is moderate.")
     response = mybolt.digitalWrite('0', 'HIGH')
     print("Making request to Twilio to send a SMS")
     res = sms.send_sms("Advised to put on a mask,air quality is  poor")
     print("Response from twilio is" + str(res))
     print("status of sms at twilio is :" + str(res.status))
    
     time.sleep(3)
     response = mybolt.digitalWrite('0', 'LOW')
else:
     print(main)
     response = mybolt.digitalWrite('0', 'LOW')

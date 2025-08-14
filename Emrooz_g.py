

#date time and day of today

import requests

url="https://api.keybit.ir/time/"

response=requests.get(url)

data=response.json()


i1=data["date"]["full"]["official"]["iso"]["fa"]

print(i1)

i4=data["date"]["weekday"]["name"]

print(i4)

i5=data["date"]["other"]["gregorian"]["iso"]["en"]

print(i5)

i6=data["date"]["day"]["events"]["holy"]

 
if i6==True:

  i2=data["date"]["day"]["events"]["holy"]["text"]

  
  i3=data["date"]["day"]["events"]["holy"]["holiday"]         

  	
  print(i2)
  print(".تعطیل.")

  

else:
	print("تعطیل نیست")	
	
#now to add weather API

#w is for weather


wkey="Weather_API_key"

wurl=f"https://api.waqi.info/feed/Tabriz/?token={wkey}"

wresponse=requests.get(wurl)

wjson=wresponse.json()

aqi=wjson['data']['aqi']


if 0<= aqi <=50:
	air_quality="خوب"
	
elif 50< aqi <=100:
	air_quality="  متوسط "

elif 100< aqi <= 150:
	air_quality="  نا سالم برای گروه های حساس "

elif 150< aqi <= 200:
	air_quality="  ناسالم "
	
elif 200< aqi <= 300:
	air_quality=" خیلی ناسالم "

elif aqi > 300:
	air_quality=" مضر "

else:
	air_quality="invalid value"
	
wfinal=f" کیفیت هوا {air_quality} است "
print(wfinal)

#air temperature and humidity


latitude,longitude=38.076355,46.281210

aurl=f"https://api.api-ninjas.com/v1/weather?lat={latitude}&lon={longitude}"

akey="Ninja_API_key"

headers={
'X-Api-Key': f'{akey}'
}

aresponse=requests.get(aurl,headers=headers)

jaresponse=aresponse.json()


temp=jaresponse["temp"]

feels_like1=jaresponse["feels_like"]

humid=jaresponse["humidity"]

atf=f"  هوا {temp} درجه است "

wt=f"رطوبت هوا {humid} درصد میباشد"

rf=f" هوا {feels_like1}  درجه احساس میشود"

print(atf)
print(rf)
print(wt)
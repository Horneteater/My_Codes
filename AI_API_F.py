
#API calls to AI

import requests


model_id="deepseek-ai/DeepSeek-R1"

API_URL =f"https://api-inference.huggingface.com/models/{model_id}"

API_KEY="YOUR_API_KEY"

headers = {
"Authorization" : f"Bearer {API_KEY}" ,
"Content-Type": "application/json",
"Accept": "application/json" ,
"x-use-cache": "true"
}


prompt=str(input("Hi I'm DeepSeek, Let's chat:    "))

payload = {
    "inputs": f"{prompt}",
    "parameters": {
      "temperature" : 0.7 ,
       #higherer temp for creatity lower for accuracy
      "do_sample" : True #for applying the temperature
     }
    
}

#higherer temp for creatity lower for accuracy


  
response = requests.post(API_URL, headers=headers, json=payload , timeout=30)



if response.status_code==200:
  response2=response.content

  print(response2)
  
else:
	print("can't connect")
	print(response.status_code)
	print(response.content)

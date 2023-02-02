#python -m pip install requests
import requests
import json
import time
"""
curl -v -X POST -d @telemetry-data-with-ts.json 
https://demo.thingsboard.io/api/v1/ABC123/telemetry 
--header "Content-Type:application/json"
"""
try:
    access_token = "MqiyeOp4o0nzlQFyz6MT"
    host_url = f"https://demo.thingsboard.io/api/v1/{access_token}/telemetry" 
    print(host_url)

    #r = requests.post('https://httpbin.org/post', data={'key': 'value'})

    payload = {
        "temp" : 25,
        "humi" : 87,
        "location" : "Pune"
    }
    header = {
        "Content-Type" : "application/json"
    }

    for i in range (10):
        ret_response = requests.post(url=host_url, data=json.dumps(payload),headers=header,verify=False)
        payload["temp"] = payload["temp"] + i
        payload["humi"] = payload["humi"] + i
        time.sleep(5)
        if ret_response.status_code == 200:
            print(f"Data is sent to tb {i+1} times")
            print(ret_response.status_code)
            print(ret_response.text)  #Nothing
        else:
            print("failed to send data")
            print(ret_response.status_code)
except Exception as e:
    print(e)








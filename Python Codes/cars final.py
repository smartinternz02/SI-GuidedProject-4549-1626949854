import random
import wiotp.sdk.device
import time
myConfig = { 
    "identity": {
        "orgId": "qqjb5y",
        "typeId": "Device_2",
        "deviceId":"1224"
    },
    "auth": {
        "token": "12090909" #12090909
    }
}
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])

try:
    client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
    client.connect()
    
    while True:
        n = int(input())
        slots = dict()
        myData = dict()
        for i in range(1,n+1):
            slots[i]=random.randint(0,1)
        myData['Entry'] = random.randint(0,1000)
        #myData['Entry'] = 530
        myData['Exit'] = random.randint(0,1000)
        #myData['Exit'] = 345
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()

import random
import wiotp.sdk.device
import time
myConfig = { 
    "identity": {
        "orgId": "qqjb5y",
        "typeId": "Device_1",
        "deviceId":"1223"
    },
    "auth": {
        "token": "12090009"
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
        myData['parking'] = slots
        myData['totalslots'] = n
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()

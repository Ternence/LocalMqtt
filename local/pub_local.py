import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

if __name__ == '__main__':
    idx = 0
    while True:
        print("send success")
        publish.single("192.168.2.1",
                       payload="this is message:%s" % idx,
                       hostname="192.168.2.1",
                       client_id="lora1",
                       # qos = 0,
                       # tls=tls,
                       port=1883,
                       protocol=mqtt.MQTTv311)
        idx += 1

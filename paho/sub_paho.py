import paho.mqtt.client as mqtt

if __name__ == '__main__':
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))


    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        # 在这里处理业务逻辑
        print(msg.topic + " " + str(msg.payload))


    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("iot.eclipse.org", 1883, 60)
    client.subscribe("paho/temperature")

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.lop_forever()
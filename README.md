# Simple-Mqtt-Compose
Simple mqtt enviroment to demonstrate how to set up an MQTT broker using docker compose

In order to better understand docker-compose files as well as MQTT, this is a simple set up consisting of two "dummy" mqtt clients, and a single mqtt broker.

## Setup
If you'd like to try it yourself simply clone the repository and run `docker-compose up` in the top level directory. This will pull my custom image `johnwid92/mqtt-dummy-client` which is a simulated mqtt client that subscribes to a single topic and publishes a message to a single topic on a 1 second interval.

The compose file is configured to copy the local version of the mosquitto.conf file to configure the mqtt broker. Then, two instances of the dummy clients are started, both configured to subscribe to the message sent by the other. When run, the output will indicate that both clients are recieving messages from the other.

That's about it! Feel free to play around with the compose file, add more clients, etc.

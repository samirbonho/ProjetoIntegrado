/* 
 * MQTT-WebClient example for Web-IO 4.0
*/
var hostname = "maqiatto.com";//"m21.cloudmqtt.com";
var port = 8883;
var clientId = "dsakjdhskajdhsakjdSamir";
clientId += new Date().getUTCMilliseconds();;
var username = "samir.bonho@ifsc.edu.br";
var password = "ProjetoIFSC822";
var subscription1 = "samir.bonho@ifsc.edu.br/temperatura";
var subscription2 = "samir.bonho@ifsc.edu.br/umidade";
var subscription3 = "samir.bonho@ifsc.edu.br/altura";
var subscription4 = "samir.bonho@ifsc.edu.br/luminosidade";

mqttClient = new Paho.MQTT.Client(hostname, port, clientId);
mqttClient.onMessageArrived =  MessageArrived;
mqttClient.onConnectionLost = ConnectionLost;
Connect();

/*Initiates a connection to the MQTT broker*/
function Connect(){
	mqttClient.connect({
		onSuccess: Connected,
		onFailure: ConnectionFailed,
		keepAliveInterval: 10,
		userName: username,
		//useSSL: true,
		password: password	
	});
}

/*Callback for successful MQTT connection */
function Connected() {
  console.log("Connected");
  mqttClient.subscribe(subscription1);
  mqttClient.subscribe(subscription2);
  mqttClient.subscribe(subscription3);
  mqttClient.subscribe(subscription4);

}

/*Callback for failed connection*/
function ConnectionFailed(res) {
	console.log("Connect failed:" + res.errorMessage);
}

/*Callback for lost connection*/
function ConnectionLost(res) {
  if (res.errorCode != 0) {
	console.log("Connection lost:" + res.errorMessage);
	Connect();
  }
}

/*Callback for incoming message processing */
function MessageArrived(message) {
	console.log(message.destinationName +" : " + message.payloadString);
    var topic = message.destinationName.split("/");
    //console.log("Serah: " + topic[1]);
    document.getElementById(topic[1]).innerHTML = message.payloadString;

}




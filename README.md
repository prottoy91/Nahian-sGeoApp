# Nahian-sGeoApp
This is a geolocation based app that tracks position of a mobile ble device locally. The app is built in Django environment. the lacalization algorithm is done on matlab. the two communicate over websocket. 
For websocket comms, use the server and client libraries for connection and Rx and Tx.
To set up webscoket, put the jar file in any desirable location and add the location's path to matlab's list of static file paths

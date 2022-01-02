# smartsheet-webhook-functions

Google cloud functions that create webhook.<br>
1 respond to smartsheet challenge and send back the challenge secret to enable webhook<br>
2 respond to normarl webhook by publising the smartsheet id that issued a webhook<br>
3 other google cloud functions will subscribe the sheetid message from the pubsub and perform some required actions.<br>

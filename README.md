# discord-message (only for educational purposes)
Send discord message with python (only for educational purposes)

# Getting the token
- Open browser devtools (f12 key) or see your browser manuals to do this
- Open your the channel that you will send a message
- Search on devtools network tab you will find a request named *messages*
- Click to open the request details and search for *request headers*
- On request headers you will find a header called *authorization* and another called *path*
- Copy authorization content and put on dict with the authorization header on script
- In the path content copy the number between channels/ and /messages this will be the channel id that you will send a message
- Put your channel id in url between channels/ and /messages on script
- execute the script and your message will be sended

## Sorry for the bad english
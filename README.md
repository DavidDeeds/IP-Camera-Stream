# IP-Camera-Stream
IP-Camera-Stream

Simply set the username, password and IP address of your camera in the code for the RTSP stream and run.
You will need to press the letter q on your keyboard to quit the window.

Notes:
1. Tested working on Raspian Buster.
2. Requires imutils and opencv-python installed. You might need numpy also.
3. I have my python defaults in Buster OS set to be python3.
4. This is heavy on Raspberry Pi 4 CPU usage, the code is not yet optimised to reduce frames and bitrate to resolve this.

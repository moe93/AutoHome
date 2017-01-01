# AutoHome
  The central hub (RPi) is connected through BTooth to the Arduino stations deplyed for special tasks (Turn on TV, turn off lights, etc...)
  
  The controlling script is planned to be written in python sending specific bytes through voice commands. For instance, if the Arduino located in the bedroom is commanded to "Shut off the lights!" a byte "OFF" is sent to that specifc Arduino disconnecting power from the lights.
  
  The GUI is planned to be built with Pygame/Tkinter. Said GUI would display the current dtatus of devices "Alarm ARMED/DISARMED, Lights ON/OFF, etc...)
  
  The disaply would consist of a 36" TV screen with HDMI input. The screen is to be placed behind a two way mirror.

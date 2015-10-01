# zooplankton

### General

This project takes files from the `./data/gifs/` directory and parses them so that specific pixel RGB values are read on each frame and then written out into json files. Those json files are read and then output to serial as animations. Which pixels are read depends on the coordinates in `./config/nodes.json` with the assumption that the project "canvas" is 400 x 400 pixels.

The setup was an early raspberry pi model b with 256 MB ram, writing serial to the zooplankton transceiver (link to come?) via usb. A later raspberry pi could be used by changing the serial out device path. Test run first without starting/enabling the systemd service.


#### Proccess gif RGB values

`python ./gif_parsers/read_rgb.py`

This will output fresh json file data.


#### Visualize Node Positions

You should probably include this file!

### Running the service

In debian jessy create the following file as `sudo /lib/systemd/system/zooplankton.service`

```
[Unit]
Description=Zooplankton Animations
After=syslog.target

[Service]
Type=simple
Restart=always
User=pi
Group=pi
WorkingDirectory=/home/pi/rpi
ExecStart=/home/pi/rpi/run.py
StandardOutput=syslog
StandardError=syslog
RestartSec=1s
StartLimitInterval=0

[Install]
WantedBy=multi-user.target
```

Install via: `sudo systemctl enable zooplankton`

Start via: `sudo systemctl start zooplankton`


### TODO

1. Alter read_rgb.py to use other file formats
1. More control and feedback about
1. Thermal camera support!


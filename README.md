This may seem overkill, but it works for me:

install completely fresh latest raspbian to an sd card
sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade
sudo reboot
sudo echo "deb https://packages.cloud.google.com/apt coral-cloud-stable main" | sudo tee /etc/apt/sources.list.d/coral-cloud.list
sudo curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt install python3-coral-enviro
sudo reboot now

time to prove to yourself the hat works
sudo python3 enviro_demo.py

I now had a board working with all four readings, but without being part of the IOT platform, so I edited /usr/lib/python3/dist-packages/coral/envirocloud_config.ini to match my account details but leaving the encryption empty as suggested in the file. At this stage I was unable to get enviro_demo.py to run - it crashed out with the error @bryoneason was seeing at the top of this thread where the onboard crypto call in core.py was complaining about a file not found.

To get around that, I did the following:

cd /usr/lib/python3/dist-packages/coral/enviro
sudo wget https://pki.goog/roots.pem
sudo openssl genrsa -out rsa_private.pem 2048
sudo openssl rsa -in rsa_private.pem -pubout -out rsa_public.pem
sudo vi cloud_config.ini 
sudo vi cloud_config.ini <set all other variables to match all the rest of your gcloud settings, region etc>

time to prove to yourself everything works
sudo python3 enviro_demo.py

For me, I now have a pi, connected to the internet over my local wifi, connected to my gcp account, using the encryption keys I created, which has been running for days, all the way through pubsub and dataflow to bigquery. It has inserted tens of thousands of rows successfully.

*NB, if you want to do the same thing as a semi-tutorial (accepting i'm hardly a good tutor of anything) you'll need to:

enable apis for pubsub, dataflow, bigquery and storage first, then:

go to the IOT dashboard, create a new registry (remember the region), create a new device and make sure to add the public key you created above.

go to the pubsub dashboard, create a new topic, then create a new subscription (delivery type set to pull) for that topic

go back to the topic screen, select your topic, and from the dropdown select 'export to bigquery'

now over in the dataflow dashboard, give the flow a name, change the Cloud Dataflow Template from 'topic to bigquery' to 'subscription to bigquery', make sure you set the region to match everything else you are doing, and enter the topic you made above

in another tab, go into the bigquery dashboard and create a dataset and a table within that with the following structure:

field name | Type | Mode |

humidity | FLOAT | NULLABLE
pressure | FLOAT | NULLABLE
temperature | FLOAT | NULLABLE
ambient_light | FLOAT | NULLABLE

In another tab go into the Storage Browser, create a bucket and remember its name

Now go back to your half complete dataflow, and fill in the output table name with the details you created above and also enter the name of the storage bucket you created and put it in the Temporary Location field and finally set the flow running

go back to the bigquery dashboard, and in the query editor, you can use this to start to see your data:
SELECT * FROM <project id>:<dataset>.<table> LIMIT 1000

Alone, without the help of these tutorials:

https://cloud.google.com/community/tutorials/cloud-iot-rtdp
https://cloud.google.com/community/tutorials/cloud-iot-gateways-rpi

and the fantastic support of coral-support@google.com plus quite a lot of hours of me assuming I was wrong and hacking at things, this does all work very well indeed.

PS - I've probably missed out some steps or oversimplified others, but hopefully all this is of some assistance to someone.





<h1 class="normal-size print-break section-headline mk-heading">Environmental Sensor Board datasheet</h1>
    
  </div>
</div>

<p class="body-copy mk-paragraph" ><img src="https://coral.withgoogle.com/static/docs/images/enviro-board/enviro-profile-dims.jpg"
   class="attempt-right print-hide" style="max-width:430px" />

<h2 class="normal-size print-break section-headline mk-heading">Features</h2>

<div class="dense-list">
<ul class="mk-list">
<li class="mk-list-item body-copy">128x32 OLED display</li>
<li class="mk-list-item body-copy">Ambient light sensor (OPT3002)</li>
<li class="mk-list-item body-copy">Barometric pressure sensor (BMP280)</li>
<li class="mk-list-item body-copy">Humidity / temperature sensor (HDC2010)</li>
<li class="mk-list-item body-copy">Cryptoprocessor (ATECC608A) with Google keys</li>
<li class="mk-list-item body-copy">40-pin GPIO female connector</li>
<li class="mk-list-item body-copy">Four Grove connectors:
  <ul class="mk-list">
  <li class="mk-list-item body-copy">1x UART</li>
  <li class="mk-list-item body-copy">1x I2C</li>
  <li class="mk-list-item body-copy">1x PWM</li>
  <li class="mk-list-item body-copy">1x 3.3/5V analog</li>
  </ul>
</li>
<li class="mk-list-item body-copy">General purpose button</li>
<li class="mk-list-item body-copy">General purpose LED</li>
</ul>
</div>

<h2 class="section-headline mk-heading" id="overview">Overview</h2>

<p class="body-copy mk-paragraph" >The Environmental Sensor Board is an add-on board (also known as a pHAT or bonnet) that adds sensing
capabilities to your Coral Dev Board or Raspberry Pi projects. (It includes an EEPROM for
compatibility with Raspberry Pi boards.)</p>

<p class="body-copy mk-paragraph" >The board provides atmospheric data such as light level, barometric pressure, temperature, and
humidity. You can also attach additional sensors with the Grove connectors.</p>

<p class="body-copy mk-paragraph" >The board also includes a secure cryptoprocessor with Google keys to enable connectivity with
<a class="mk-link" target="_blank" rel="noopener noreferrer" href="https://cloud.google.com/iot-core/">Google Cloud IoT Core</a> services, allowing you to securely
connect to the device and then collect, process, and analyze the sensor data.</p>

<div class="print-hide link-arrow">
<p class="body-copy mk-paragraph" ><a class="mk-link" href="https://www.mouser.com/ProductDetail/Coral/G650-04023-01?qs=vLWxofP3U2zZXdMO1sMwsg%3D%3D">Purchase info from Mouser</a>
</div>

<div class="print-break"></div>

<h2 class="section-headline mk-heading" id="table-of-contents">Table of contents</h2>

<div class="dense-list">
<ul class="mk-list">
  <li class="mk-list-item body-copy"><a class="mk-link" href="#dimensions">Dimensions</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#requirements">Requirements</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#sensors">Sensors</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#grove-connectors">Grove connectors</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#oled-display">OLED display</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#secure-cryptoprocessor">Secure cryptoprocessor</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#header-pinout">Header pinout</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#i2c-address-reference">I2C address reference</a></li>
  <li class="mk-list-item body-copy"><a class="mk-link" href="#certifications">Certifications</a></li>
</ul>
</div>

<div class="print-break"></div>

<h2 class="section-headline mk-heading" id="dimensions">Dimensions</h2>

<table>
<thead>
<tr>
<th><strong>Measurement</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Board size</td>
<td>Board w/ components: 65 x 30 x 18.46 mm<br>
40-pin header height: 8.5 mm</td>
</tr>
<tr>
<td>Hole size/spacing</td>
<td>Diameter: 2.4 mm<br>
Horizontal spacing: 58 mm<br>
Vertical spacing: 23 mm</td>
</tr>
<tr>
<td>Weight</td>
<td>14 g</td>
</tr>
</tbody>
</table>

<figure>
   <img src="https://coral.withgoogle.com/static/docs/images/enviro-board/enviro-dims.png" />
   <figcaption><b>Figure 1.</b> Board and mounting hole dimensions (in millimeters)</figcaption>
</figure>

<h2 class="section-headline mk-heading" id="requirements">Requirements</h2>

<p class="body-copy mk-paragraph" >The board must be connected to a host with I2C, SPI, and 3.3V power. The 40-pin GPIO header and
provided software are designed to work with the Coral Dev Board or Raspberry Pi (running Mendel
Linux or Raspbian, respectively).</p>

<div class="print-break"></div>

<h2 class="section-headline mk-heading" id="sensors">Sensors</h2>

<p class="body-copy mk-paragraph" >All sensors are connected to the I2C lines from header pins 3 and 5 (see the
<a class="mk-link" href="#header-pinout">header pinout</a>).</p>

<table>
<thead>
<tr>
<th><strong>Sensor</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Humidity and temperature sensor </td>
<td>Texas Instruments HDC2010:<br>
<ul class="mk-list">
<li class="mk-list-item body-copy">Humidity range/accuracy: 0 - 100% ± 2% (typical)</li>
<li class="mk-list-item body-copy">Temperature range/accuracy: -40 - 125°C (functional) ±0.2°C (typical)</li>
</ul>
<br>
I2C address: 0x40</td>
</tr>
<tr>
<td>Ambient light sensor</td>
<td>Texas Instruments OPT3002:<br>
<ul class="mk-list">
<li class="mk-list-item body-copy">Optical spectrum: 300 - 1000 nm</li>
<li class="mk-list-item body-copy">Measurement range: 1.2 - 10 mW/cm2</li>
</ul>
<br>
I2C address:  0x45</td>
</tr>
<tr>
<td>Barometric pressure sensor</td>
<td>Bosch Sensortec BMP280:<br>
<ul class="mk-list">
<li class="mk-list-item body-copy">Operation range: 300 - 1100 hPa</li>
<li class="mk-list-item body-copy">Absolute accuracy (@ 0 - 65°C): ~ ±1 hPa</li>
<li class="mk-list-item body-copy">Relative accuracy (@ 700-900 hPa; 25 - 40°C): ± 0.12 hPa (typical)</li>
</ul>
<br>
I2C address: 0x76</td>
</tr>
</tbody>
</table>

<div class="print-break"></div>

<h2 class="section-headline mk-heading" id="grove-connectors">Grove connectors</h2>

<p class="body-copy mk-paragraph" >The Grove connectors provide easy access to the PWM, UART, and I2C pins from the baseboard, plus an
on-board analog-to-digital converter (ADC), as illustrated in figure 2.</p>

<p class="body-copy mk-paragraph" >To interact with the AIN0 analog source, use address 0x49 on the I2C lines from header pins 3
and 5 (see the <a class="mk-link" href="#header-pinout">header pinout</a>).</p>

<div class="note"><b>Note:</b>
The VDD_A pin on the analog Grove connector can be powered by either the 5V or 3.3V power
rail by the jumper pins indicated in figure 2 as the ANALOG VDD JUMPER.</div>

<figure>
   <img src="https://coral.withgoogle.com/static/docs/images/enviro-board/enviro-grove-callouts.png" style="max-width:600px" />
   <figcaption><b>Figure 2.</b> Pin functions for each Grove connector</figcaption>
</figure>

<div class="print-break"></div>

<h2 class="section-headline mk-heading" id="oled-display">OLED display</h2>

<p class="body-copy mk-paragraph" >The 128x32 OLED display is driven by the SSD1306 control chip, connected with the SPI interface.</p>

<table>
<thead>
<tr>
<th><strong>SPI function</strong></th>
<th><strong>Pin</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>MOSI  </td>
<td>19</td>
</tr>
<tr>
<td>MISO</td>
<td>21</td>
</tr>
<tr>
<td>SCLK</td>
<td>23</td>
</tr>
<tr>
<td>CL</td>
<td>24</td>
</tr>
<tr>
<td>RESET</td>
<td>22</td>
</tr>
<tr>
<td>DC</td>
<td>18</td>
</tr>
</tbody>
</table>

<h2 class="section-headline mk-heading" id="secure-cryptoprocessor">Secure cryptoprocessor</h2>

<p class="body-copy mk-paragraph" >The board includes a secure cryptoprocessor (ATECC608A) with an EEPROM that can
store up to 16 keys (256-bit), certificates, or other data. Although this chip provides a range of
cryptographic features, it is primarily included to provide secure key generation and management so
you can securely authenticate with the device when deployed into the field.</p>

<p class="body-copy mk-paragraph" >The factory setting for the Environmental Sensor Board includes one Google key (private key, public
key, and certificate) to enable communication with <a class="mk-link" target="_blank" rel="noopener noreferrer" href="https://cloud.google.com/iot-core/">Google Cloud IoT
Core</a> right out of the box. This key slot is reusable, just like
the rest of the memory, so you don't have to keep it.</p>

<div class="print-break"></div>

<h2 class="section-headline mk-heading" id="header-pinout">Header pinout</h2>

<p class="body-copy mk-paragraph" >Figure 3 shows which pins from the baseboard are used by the Environmental Sensor Board. Pins
highlighted in dark green are used by the board and not available to you (except through software
for the corresponding functions), while the pins in light green are used by the board but are still
available to you through the Grove connectors.</p>

<figure>
   <img src="https://coral.withgoogle.com/static/docs/images/enviro-board/enviro-pinout.png" style="max-width:600px" />
   <figcaption><b>Figure 3.</b> Pins used by the board</figcaption>
</figure>

<h2 class="section-headline mk-heading" id="i2c-address-reference">I2C address reference</h2>

<table>
<thead>
<tr>
<th><strong>Device</strong></th>
<th><strong>Address</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Humidity/temp sensor  </td>
<td>0x40</td>
</tr>
<tr>
<td>Ambient light sensor</td>
<td>0x45</td>
</tr>
<tr>
<td>Barometric pressure sensor</td>
<td>0x76</td>
</tr>
<tr>
<td>Analog Grove connector</td>
<td>0x49</td>
</tr>
<tr>
<td>Cryptoprocessor</td>
<td>0x30</td>
</tr>
</tbody>
</table>


# What is this?

This is the Linux kernel IIO drivers for the sensors used in the Coral
Environment Sensor board.

Note: These files are mostly identical to the drivers in mainline linux (iio/).
There are trivial changes for ease of use for DKMS.


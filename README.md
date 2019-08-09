
    <img src="/static/docs/images/enviro-board/enviro-profile-dims.jpg" />
  </div>
</div>

<p class="body-copy mk-paragraph" ><img src="/static/docs/images/enviro-board/enviro-profile-dims.jpg"
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
<p class="body-copy mk-paragraph" ><a class="mk-link" href="/products/environmental/">Purchase info</a>
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
   <img src="/static/docs/images/enviro-board/enviro-dims.png" />
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
   <img src="/static/docs/images/enviro-board/enviro-grove-callouts.png" style="max-width:600px" />
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
   <img src="/static/docs/images/enviro-board/enviro-pinout.png" style="max-width:600px" />
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

<h2 class="section-headline mk-heading" id="certifications">Certifications</h2>

<table>
<thead>
<tr>
<th><strong>Market</strong></th>
<th><strong>Certifications</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>USA</strong></td>
<td>FCC</td>
</tr>
<tr>
<td><strong>European Union</strong></td>
<td>CE</td>
</tr>
</tbody>
</table>
        </div>
      </div>
    </div>
  </div>
</section>        </div>
      </div>
    </div>

<section class="feedback-component">
	<div class="grid-container">
		<div class="row center">
			<div class="col-mobile-14 col-tablet-30 col-small-desktop-28 col-desktop-28">
				<hr class="separater" data-module-type="separator" />
			</div>
		</div>

		<div class="row feedback-row">
			<div class="feedback-container col-mobile-14 col-tablet-13 col-small-desktop-12 col-desktop-28">
				<p class="cta-primary-body">Is this content helpful?</p>

				<div>
					<button class="thumb thumb-up"><svg width="100%" height="100%" viewBox="0 0 34 41" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <path d="M21.1334,40.0344336 L21.1323966,40.0344256 C15.9572291,39.9899108 13.9114176,39.7127631 10.9459171,38.2588016 C6.72320136,36.1884374 4.7682668,35.8231657 3.40837849,36.2047375 C3.3592638,36.2185186 3.32142401,36.22968 3.29222438,36.2357757 C3.21112527,36.2675855 3.1137127,36.2973032 3.03213342,36.3150799 L2.60662684,36.407801 L2.31517319,36.0842152 C1.4810202,35.1580983 1.02520694,30.2921887 1.36301421,25.7438928 C1.56576937,23.0033161 2.00198174,21.3215689 2.52738106,20.7643136 L2.7932753,20.4822977 L3.17712605,20.5360689 L3.31550715,20.5555326 C4.22302116,20.6960422 4.54235861,20.658501 5.66200204,20.1859414 C6.5663511,19.8023815 7.79240412,18.4291469 8.95089124,16.7251562 C9.5666636,15.8212177 10.2306443,15.1968385 11.3099221,14.4079817 C11.4552871,14.3017328 11.5663219,14.2220193 11.8405981,14.0262142 C12.688555,13.4148223 12.8664102,13.2835078 13.2671584,12.9600922 L13.5007269,12.7714778 C15.4657648,11.1902985 16.0827196,10.4054647 17.1382738,7.68797605 C17.5118043,6.72427343 17.7210115,6.01030898 18.1049713,4.51823794 C18.7266049,2.0862657 19.0123165,1.46707924 20.0749358,1.27515138 C21.050799,1.09208918 21.768429,1.78121656 22.5681548,3.28971194 C23.4604529,4.98013679 22.9051993,8.43980821 21.1030393,11.8083372 C20.2663728,13.37784 20.1271175,14.5863676 20.5975156,15.4503829 C21.1213524,16.4073498 22.3777752,17.0092997 24.532372,17.2287067 C24.9786193,17.2757197 25.4144698,17.3003462 26.3188976,17.337046 C30.9738159,17.5363428 32.7501953,18.0872299 32.7501953,20.3711573 C32.7501953,21.3589925 32.505512,21.8606696 31.8522751,22.6217703 C31.7519773,22.7402952 31.720547,22.7778629 31.6732469,22.8367101 C31.3586512,23.2281062 31.2201411,23.5343213 31.213425,23.9621715 C31.204863,24.4197401 31.3193941,24.6884414 31.5735992,24.9697175 C31.6233789,25.0247983 31.6600117,25.0621453 31.7638214,25.1653583 C31.8300849,25.230289 31.8635804,25.2636366 31.9031634,25.3049728 C32.3423297,25.7635905 32.4979229,26.253213 32.4185523,27.0726945 C32.2945049,28.3826525 31.8931434,28.9248253 30.969158,29.4651272 C30.5440667,29.7131193 30.4091307,29.8458502 30.3686172,30.0825477 C30.2959679,30.5120756 30.3737038,30.764873 30.6034408,31.0739645 C30.6374548,31.1197274 30.6635911,31.1529683 30.7324887,31.2390634 C31.1921894,31.8084637 31.3367827,32.1980669 31.2499621,32.9961785 C31.1659622,33.7484823 30.9479332,34.0833432 30.401973,34.5100382 C30.2779199,34.6088744 30.2247836,34.6530384 30.1632489,34.7104864 C29.9083851,34.9484236 29.7739192,35.2067547 29.7378845,35.6657031 C29.7135533,35.9430622 29.7252962,36.1349773 29.7755358,36.5229335 C29.8705039,37.2535999 29.8399059,37.6813976 29.5570156,38.4867458 C29.0795402,39.8460502 27.629086,40.1553699 23.0433977,40.0611286 C22.3795339,40.0477524 21.7444886,40.0388723 21.1334,40.0344336 Z" stroke="#000000" stroke-width="1.5" fill="#FFFFFF" fill-rule="nonzero"></path>
    </g>
</svg></button>
					<button class="thumb thumb-down"><svg width="100%" height="100%" viewBox="0 0 34 41" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <path d="M21.1334,40.0344336 L21.1323966,40.0344256 C15.9572291,39.9899108 13.9114176,39.7127631 10.9459171,38.2588016 C6.72320136,36.1884374 4.7682668,35.8231657 3.40837849,36.2047375 C3.3592638,36.2185186 3.32142401,36.22968 3.29222438,36.2357757 C3.21112527,36.2675855 3.1137127,36.2973032 3.03213342,36.3150799 L2.60662684,36.407801 L2.31517319,36.0842152 C1.4810202,35.1580983 1.02520694,30.2921887 1.36301421,25.7438928 C1.56576937,23.0033161 2.00198174,21.3215689 2.52738106,20.7643136 L2.7932753,20.4822977 L3.17712605,20.5360689 L3.31550715,20.5555326 C4.22302116,20.6960422 4.54235861,20.658501 5.66200204,20.1859414 C6.5663511,19.8023815 7.79240412,18.4291469 8.95089124,16.7251562 C9.5666636,15.8212177 10.2306443,15.1968385 11.3099221,14.4079817 C11.4552871,14.3017328 11.5663219,14.2220193 11.8405981,14.0262142 C12.688555,13.4148223 12.8664102,13.2835078 13.2671584,12.9600922 L13.5007269,12.7714778 C15.4657648,11.1902985 16.0827196,10.4054647 17.1382738,7.68797605 C17.5118043,6.72427343 17.7210115,6.01030898 18.1049713,4.51823794 C18.7266049,2.0862657 19.0123165,1.46707924 20.0749358,1.27515138 C21.050799,1.09208918 21.768429,1.78121656 22.5681548,3.28971194 C23.4604529,4.98013679 22.9051993,8.43980821 21.1030393,11.8083372 C20.2663728,13.37784 20.1271175,14.5863676 20.5975156,15.4503829 C21.1213524,16.4073498 22.3777752,17.0092997 24.532372,17.2287067 C24.9786193,17.2757197 25.4144698,17.3003462 26.3188976,17.337046 C30.9738159,17.5363428 32.7501953,18.0872299 32.7501953,20.3711573 C32.7501953,21.3589925 32.505512,21.8606696 31.8522751,22.6217703 C31.7519773,22.7402952 31.720547,22.7778629 31.6732469,22.8367101 C31.3586512,23.2281062 31.2201411,23.5343213 31.213425,23.9621715 C31.204863,24.4197401 31.3193941,24.6884414 31.5735992,24.9697175 C31.6233789,25.0247983 31.6600117,25.0621453 31.7638214,25.1653583 C31.8300849,25.230289 31.8635804,25.2636366 31.9031634,25.3049728 C32.3423297,25.7635905 32.4979229,26.253213 32.4185523,27.0726945 C32.2945049,28.3826525 31.8931434,28.9248253 30.969158,29.4651272 C30.5440667,29.7131193 30.4091307,29.8458502 30.3686172,30.0825477 C30.2959679,30.5120756 30.3737038,30.764873 30.6034408,31.0739645 C30.6374548,31.1197274 30.6635911,31.1529683 30.7324887,31.2390634 C31.1921894,31.8084637 31.3367827,32.1980669 31.2499621,32.9961785 C31.1659622,33.7484823 30.9479332,34.0833432 30.401973,34.5100382 C30.2779199,34.6088744 30.2247836,34.6530384 30.1632489,34.7104864 C29.9083851,34.9484236 29.7739192,35.2067547 29.7378845,35.6657031 C29.7135533,35.9430622 29.7252962,36.1349773 29.7755358,36.5229335 C29.8705039,37.2535999 29.8399059,37.6813976 29.5570156,38.4867458 C29.0795402,39.8460502 27.629086,40.1553699 23.0433977,40.0611286 C22.3795339,40.0477524 21.7444886,40.0388723 21.1334,40.0344336 Z" stroke="#000000" stroke-width="1.5" fill="#FFFFFF" fill-rule="nonzero"></path>
    </g>
</svg></button>
				</div>
			</div>
		</div>
	</div>
</section>
  </section>
    </main>


<footer id="footer" data-turbolinks-permanent>
  <div class="grid-container">
    <div class="row">
      <div class="col-mobile-14 col-mobile-offset-1 col-tablet-17 col-tablet-offset-1 col-small-desktop-16 col-small-desktop-offset-2 col-desktop-16 col-desktop-offset-2 links-and-copyright">
        <ul role="menu" class="footer-items">
          <li class="item" role="none">
            <a href="/about/" data-label="About Coral"
 class="cta-primary-body color--white item-link" role="menuitem">About Coral</a>
          </li>
          <li class="item" role="none">
            <a href="/news/" data-label="News"
 class="cta-primary-body color--white item-link" role="menuitem">News</a>
          </li>
          <li class="item" role="none">
            <a href="https://www.blog.google/technology/ai/ai-principles/" data-label="Google AI principles"
               target="_blank" rel="noopener"
 class="cta-primary-body color--white item-link" role="menuitem">Google AI principles</a>
          </li>
          <li class="item" role="none">
            <a href="https://policies.google.com/terms?hl=en" data-label="Terms of service"
               target="_blank" rel="noopener"
 class="cta-primary-body color--white item-link" role="menuitem">Terms of service</a>
          </li>
          <li class="item" role="none">
            <a href="https://policies.google.com/privacy?hl=en" data-label="Privacy policy"
               target="_blank" rel="noopener"
 class="cta-primary-body color--white item-link" role="menuitem">Privacy policy</a>
          </li>
          <li class="item" role="none">
            <a href="/docs/" data-label="Documentation"
 class="cta-primary-body color--white item-link" role="menuitem">Documentation</a>
          </li>
          <li class="item" role="none">
            <a href="/projects/" data-label="Projects"
 class="cta-primary-body color--white item-link" role="menuitem">Projects</a>
          </li>
          <li class="item" role="none">
            <a href="/support/" data-label="Support"
 class="cta-primary-body color--white item-link" role="menuitem">Support</a>
          </li>
          <li class="item" role="none">
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSf0t-I4y0AS4Ymph9SRY3Gr9ppZsgE_LZ2A8_vMa7K_Do4ZQA/viewform" data-label="Contact sales"
               target="_blank" rel="noopener"
 class="cta-primary-body color--white item-link" role="menuitem">Contact sales</a>
          </li>
          <li class="item" role="none">
            <a href="/legal/" data-label="Legal"
 class="cta-primary-body color--white item-link" role="menuitem">Legal</a>
          </li>
        </ul>
        <div class="copyright-container row">
          <div class="col-mobile-16 col-tablet-28">
            <div class="logo">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 88" width="260" height="88">
    <path d="M33 40.24v-8.75h30.48c.32 1.6.48 3.55.48 5.63 0 6.72-1.84 15.04-7.76 20.96-5.76 6-13.12 9.2-22.88 9.2C15.24 67.28.04 52.56.04 34.48s15.2-32.8 33.28-32.8c10 0 17.12 3.92 22.48 9.04l-6.32 6.32c-3.84-3.6-9.04-6.4-16.16-6.4-13.2 0-23.52 10.64-23.52 23.84s10.32 23.84 23.52 23.84c8.56 0 13.44-3.44 16.56-6.56 2.56-2.56 4.28-6.48 4.92-11.52H33zm76.7 5.92c0 12.16-9.52 21.12-21.2 21.12s-21.2-8.96-21.2-21.12c0-12.24 9.52-21.12 21.2-21.12s21.2 8.88 21.2 21.12zm-9.28 0c0-7.6-5.52-12.8-11.92-12.8s-11.92 5.2-11.92 12.8c0 7.52 5.52 12.8 11.92 12.8s11.92-5.28 11.92-12.8zm55.28 0c0 12.16-9.52 21.12-21.2 21.12s-21.2-8.96-21.2-21.12c0-12.24 9.52-21.12 21.2-21.12s21.2 8.88 21.2 21.12zm-9.28 0c0-7.6-5.52-12.8-11.92-12.8s-11.92 5.2-11.92 12.8c0 7.52 5.52 12.8 11.92 12.8s11.92-5.28 11.92-12.8zm53.39-19.84v37.92c0 15.6-9.2 22-20.08 22-10.24 0-16.4-6.88-18.72-12.48l8.08-3.36c1.44 3.44 4.96 7.52 10.64 7.52 6.96 0 11.28-4.32 11.28-12.4v-3.04h-.32c-2.08 2.56-6.08 4.8-11.12 4.8-10.56 0-20.24-9.2-20.24-21.04 0-11.92 9.68-21.2 20.24-21.2 5.04 0 9.04 2.24 11.12 4.72h.32v-3.44h8.8zm-8.16 19.92c0-7.44-4.96-12.88-11.28-12.88-6.4 0-11.76 5.44-11.76 12.88 0 7.36 5.36 12.72 11.76 12.72 6.32 0 11.28-5.36 11.28-12.72zM215.29 4v62h-9.28V4h9.28zm35.9 49.12l7.2 4.8c-2.32 3.44-7.92 9.36-17.6 9.36-12 0-20.96-9.28-20.96-21.12 0-12.56 9.04-21.12 19.92-21.12 10.96 0 16.32 8.72 18.08 13.44l.96 2.4-28.24 11.68c2.16 4.24 5.52 6.4 10.24 6.4 4.72 0 8-2.32 10.4-5.84zm-22.16-7.6l18.88-7.84c-1.04-2.64-4.16-4.48-7.84-4.48-4.72 0-11.28 4.16-11.04 12.32z"/>
</svg>            </div>
            <p class="color--white copyright">Copyright 2019 Google LLC. All rights reserved.</p>
          </div>
        </div>
      </div>
      <div class="col-mobile-14 col-mobile-offset-1 col-tablet-10 col-tablet-offset-3 col-small-desktop-9 col-small-desktop-offset-3 col-desktop-7 col-desktop-offset-5 newsletter-form">
        <form>
          <h2>Stay up-to-date</h2>
          <p>Sign up to receive our newsletter</p>
          <input type="text" placeholder="Name" name="name" />
          <div class="error-message name">
<svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M9 13h2v2H9v-2zm0-8h2v6H9V5zm.99-5C4.47 0 0 4.48 0 10s4.47 10 9.99 10C15.52 20 20 15.52 20 10S15.52 0 9.99 0zM10 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" id="path-1"/></defs><g id="Symbols" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="ic/error_outline" transform="translate(-2 -2)"><g id="ic_error_outline_24px" transform="translate(2 2)"><mask id="mask-15" fill="#fff"><use xlink:href="#path-1"/></mask><g id="🎨-Color" mask="url(#mask-15)" fill="#FFA700"><path d="M9 13h2v2H9v-2zm0-8h2v6H9V5zm.99-5C4.47 0 0 4.48 0 10s4.47 10 9.99 10C15.52 20 20 15.52 20 10S15.52 0 9.99 0zM10 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" id="path-1"/></g></g></g></g></svg><span></span>
          </div>
          <input type="text" placeholder="Company (optional)" name="company" />
          <input type="text" placeholder="Email" name="email" />
          <div class="error-message email">
<svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M9 13h2v2H9v-2zm0-8h2v6H9V5zm.99-5C4.47 0 0 4.48 0 10s4.47 10 9.99 10C15.52 20 20 15.52 20 10S15.52 0 9.99 0zM10 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" id="path-1"/></defs><g id="Symbols" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="ic/error_outline" transform="translate(-2 -2)"><g id="ic_error_outline_24px" transform="translate(2 2)"><mask id="mask-15" fill="#fff"><use xlink:href="#path-1"/></mask><g id="🎨-Color" mask="url(#mask-15)" fill="#FFA700"><path d="M9 13h2v2H9v-2zm0-8h2v6H9V5zm.99-5C4.47 0 0 4.48 0 10s4.47 10 9.99 10C15.52 20 20 15.52 20 10S15.52 0 9.99 0zM10 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" id="path-1"/></g></g></g></g></svg><span></span>
          </div>
          <div class="terms-checkbox">
            <input type="checkbox" name="terms" id="terms" />
            <label for="terms">I accept Google's <a href="//www.google.com/intl/en/policies/terms/" target="_blank">Terms and Conditions</a> and acknowledge that my information will be used in accordance with Google's <a href="//www.google.com/intl/en/policies/privacy/" target="_blank">Privacy Policy</a>.</label>
          </div>




    <a href="#/" data-turbolinks="false"       class="cta 
 
 
                   form-send-cta bg-color--ice " target="_blank" rel="noopener">

	<span>Subscribe</span>

    </a>
          <div class="return-message">
            <div class="success"><svg viewBox="0 0 55 55" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><path d="M-5-5h64v64H-5V-5zm0 0h64v64H-5V-5z"/><path d="M39.725 15.698L22.152 33.272l-9.574-9.547-3.76 3.76 13.334 13.333 21.333-21.333-3.76-3.787zM27.485.818C12.765.818.818 12.765.818 27.485c0 14.72 11.947 26.667 26.667 26.667 14.72 0 26.667-11.947 26.667-26.667 0-14.72-11.947-26.667-26.667-26.667zm0 48c-11.787 0-21.333-9.546-21.333-21.333 0-11.787 9.546-21.333 21.333-21.333 11.787 0 21.333 9.546 21.333 21.333 0 11.787-9.546 21.333-21.333 21.333z" fill="#25B6BB" fill-rule="nonzero"/></g></svg></div>
            <div class="error"><svg viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M9 13h2v2H9v-2zm0-8h2v6H9V5zm.99-5C4.47 0 0 4.48 0 10s4.47 10 9.99 10C15.52 20 20 15.52 20 10S15.52 0 9.99 0zM10 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" id="path-1"/></defs><g id="Symbols" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="ic/error_outline" transform="translate(-2 -2)"><g id="ic_error_outline_24px" transform="translate(2 2)"><mask id="mask-15" fill="#fff"><use xlink:href="#path-1"/></mask><g id="🎨-Color" mask="url(#mask-15)" fill="#FFA700"><path d="M9 13h2v2H9v-2zm0-8h2v6H9V5zm.99-5C4.47 0 0 4.48 0 10s4.47 10 9.99 10C15.52 20 20 15.52 20 10S15.52 0 9.99 0zM10 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" id="path-1"/></g></g></g></g></svg></div>
            <span>You are subscribed! Thanks!</span>
          </div>
        </form>
      </div>
    </div>
  </div>
</footer>
<section class="image-expanded-component">

  <div class="modal">
    <img class="image-expanded" />
    <a href="#" class="close-modal image-expanded-close">
<?xml version="1.0" encoding="UTF-8"?>
<svg width="19px" height="19px" viewBox="0 0 19 19" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <!-- Generator: Sketch 53.2 (72643) - https://sketchapp.com -->
    <title>Close Icon</title>
    <desc>Created with Sketch.</desc>
    <g id="08---Product-Distributors" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="Coral-Product-Distributors-Modal---1440px_@2x" transform="translate(-838.000000, -387.000000)" fill="#4a4a4a">
            <g id="Modal" transform="translate(548.000000, 348.000000)">
                <polygon id="Close-Icon" points="309 40.9127517 301.412752 48.5 309 56.0872483 307.087248 58 299.5 50.4127517 291.912752 58 290 56.0872483 297.587248 48.5 290 40.9127517 291.912752 39 299.5 46.5872483 307.087248 39"></polygon>
            </g>
        </g>
    </g>
</svg>    </a>
  </div>

</section>
      <script defer src="/static/output/main.min.js?cache=90caf05"></script>


  </body>
</html>

# What is this?

This is the Linux kernel IIO drivers for the sensors used in the Coral
Environment Sensor board.

Note: These files are mostly identical to the drivers in mainline linux (iio/).
There are trivial changes for ease of use for DKMS.


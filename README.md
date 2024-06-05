# Bioinstrumentation EECS 289
Project repository for *2024 Spring EECS 289 Group 10*, UC Irvine
Last Modified: 4:45 Jun 1st,2024
## Eye Blink Detection
#### Following steps are sufficient for setting up eye blinking detection application using Cyton board from OpenBCI.
1. [GUI Download](https://openbci.com/downloads)
2. [GUI Guide](https://docs.openbci.com/Software/OpenBCISoftware/GUIDocs/#installing-the-openbci-gui-as-a-standalone-application)
3. [Cyton Guide](https://docs.openbci.com/GettingStarted/Boards/CytonGS/)
4. [EEG Setup Guide](https://docs.openbci.com/GettingStarted/Biosensing-Setups/EEGSetup/)
5. [Related Work](https://openbci.com/community/eog-eye-movement-blink-detection-with-the-openbci-cyton/)

Detailed steps ( ~~Too Lazy Reading~~ ):
1. Plug in the OpenBCI USB Dongle (make sure your USB Dongle is switched to **GPIO 6** and **not** ~~RESET~~. )
2. Switch your Cyton board to PC (not OFF or BLE) (And Plug the power ofc)
3. In GUI, select top left 
*System Control Panel* >> *LIVE* >> *Serial* >> *Auto-Connect* >> *Start Data Stream*|| After you connected, there should be signal responding when you use your finger touching the channel pins.
4. For the Color that we have:

| Pin | Connection & Body Part|
| ----------- | ----------- |
| white | bottom SRB pin \ Earlobe|
| black | bottom BIAS pin \ Earlobe|
| purple| bottom N2P pin \ 1 inch above eyebrow|
| brown | bottom N7P pin \ 1 inch above eyebrow|

5. Now when you start data stream again, you should see the signals respond to your eye blinking instantly. 


### References
- https://gnan.ece.gatech.edu/archive/agarwal-blink.pdf
- https://www.researchgate.net/publication/339935089_EEG_Signal_Processing_Model_for_Eye_Blink_Detection
- https://github.com/meagmohit/BLINK
- https://github.com/AleksandarHaber/Low-Cost-Brain-Computer-Interface-by-Using-OpenBCI-Cython-Board-MATLAB-and-Arduino
- https://www.youtube.com/watch?v=BOithxp_fEc
- https://www.youtube.com/watch?v=h5Lu9OcZ8x0

## Lab Report
### Lab 1 Data
pH Sensitivity: -2.7073220
Neurotransmitter Sensitivity: 13.458985
LOD: 5.083898586
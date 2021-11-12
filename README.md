# **APT-automation-software**

Master PC software for display automation for APT Electronics Pvt Ltd.

## **Installation guidelines**

<!-- OL -->
1. Download the zip file of the repo on your local machine
2. Extract the folder
3. cd into the folder
4. Activate the virtual environment
   * **Windows Users**: Ensure that you are using Git Bash or a similar command line environment
   
   <!-- Code Block -->
```bash
  source venv/bin/activate
```
5. Install the dependencies mentioned in requirments.txt file
   * **On Windows:**  
   ```bash
   pip install -r requirements.txt
   ```
   * **On Linux:**  
   ```bash
   pip3 install -r requirements.txt
   ```
6. Run the software

    * **On Windows:** ```python main.py```
    * **On Linux:** ```python3 main.py```

## **About the software**

<img src = "https://user-images.githubusercontent.com/55655727/141419362-6f3023ff-bd64-440b-a1aa-4b197ea9b676.png"></img>

Select the directory of images required for the specific production line and Click on send.
The software would communicate with the Raspberry Pis of the specified IP address and would automatically send documents relevant to them via the TCP/IP protocol.

Individual monitors on Individual lines could also be configured by clicking the Line button above

<img src = "https://user-images.githubusercontent.com/55655727/141419382-c737e7fc-4140-4347-a3ed-25ed76715fbe.png"></img>

## **Raspi Zero W configuration guidelines**

<p>The idea of the setup is to have servers run in Raspi's background that will listen to incoming requests from the Master PC. The communication is established using python sockets and the communication protocol is TCP to maintain reliable data transfer.</p>

<p>Assuming we are working with a fresh out-of-the box Raspberry Pi Zero W, here are some instructions to configure it</p>

<!-- OL -->
0. (Optional) For setting up Raspberry Pi Zero W on VGA displays, <a href = "https://www.youtube.com/watch?v=7WbMGzet7fg">this</a> video might be helpful.
1. Disable the firewall permanently
<!-- UL -->
  - Temporarily stop firewall
  <!-- Code Block -->
  ```bash
    sudo systemctl stop firewalld
  ```
  - Disable the firewall service at boot time
  <!-- Code Block -->
  ```bash
    sudo systemctl disable firewalld
    sudo systemctl mask --now firewalld
  ```
  - Check status of your firewall (recommended to reboot the system)
  <!-- Code Block -->
  ```bash
    sudo firewall-cmd --state
  ```

2. Disable iptables rules
<!-- Code Block -->
  ```bash
    iptables -F
  ```

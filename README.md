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
<!-- Code Block -->
```bash
  pip install -r requirements.txt
```
6. Run the software

    * **On Windows:** ```python main.py```
    * **On Linux:** ```python3 main.py```

## **About the software**

<img src = "https://user-images.githubusercontent.com/55655727/130039222-0b93eb43-2c79-47ad-9ae7-8be54d4349f2.png"></img>

Select the directory of images required for the specific production line and Click on send.
The software would communicate with the Raspberry Pis of the specified IP address and would automatically send documents relevant to them via the TCP/IP protocol.

## **Raspi Zero W configuration guidelines**

<p>The idea of the setup is to have servers run in Raspi's background that will listen to incoming requests from the Master PC. The communication is established using python sockets and the communication protocol is TCP to maintain reliable data transfer.</p>

<p>Assuming we are working with a fresh out-of-the box raspberry pi, here are some instructions to configure it</p>

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
  - Temporarily stop firewall
  <!-- Code Block -->
  ```bash
    sudo systemctl stop firewalld
  ```
2. Disable iptables rules
<!-- Code Block -->
  ```bash
    iptables -F
  ```
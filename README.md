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

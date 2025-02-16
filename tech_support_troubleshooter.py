#Enter your Python code here

def askQuestion(question):
    # Function to display a question and capture user input
    print(question)
    return input("Your response: ").lower()  # Convert the response to lowercase for easier comparison

def troubleshootInternet():
    # Troubleshooting steps for internet connectivity issues
    response = askQuestion("Is your device connected to Wi-Fi?")

    if "yes" in response:  # If the device is connected to Wi-Fi
        print("Checking Wi-Fi connection...")
        response = askQuestion("Is your Wi-Fi connected to the internet?")
        if "no" in response:
            print("Try restarting your router and modem.")  # Suggest restarting the router and modem
        else:
            print("Try restarting your device.")  # Suggest restarting the device to fix the issue
    else:
        response = askQuestion("Is your Wi-Fi turned on?")
        if "no" in response:
            print("Turn on Wi-Fi and try connecting again.")  # Suggest turning on Wi-Fi
        else:
            print("Try reconnecting to the Wi-Fi network.")  # Suggest reconnecting to the Wi-Fi network

def troubleshootPrinter():
    # Troubleshooting steps for a printer not printing
    response = askQuestion("Is the printer powered on?")
    if "no" in response:  # If the printer is off
        print("Turn on the printer.")  # Suggest turning the printer on
    else:
        response = askQuestion("Is the printer connected to the computer?")
        if "no" in response:  # If the printer is not connected
            print("Check the cable connection or try reconnecting via Bluetooth/Wi-Fi.")  # Suggest checking connections
        else:
            response = askQuestion("Is there paper and ink in the printer?")
            if "no" in response:  # If the printer is missing paper or ink
                print("Make sure there’s paper and ink/toner in the printer.")  # Suggest adding paper and ink
            else:
                print("Try restarting the printer and your computer.")  # Suggest restarting both devices

def troubleshootSlowComputer():
    # Troubleshooting steps for a slow or lagging computer
    response = askQuestion("Do you have many programs open?")
    if "yes" in response:  # If too many programs are open
        print("Close unused programs to free up memory.")  # Suggest closing unnecessary programs
    else:
        response = askQuestion("Is your hard drive nearly full?")
        if "yes" in response:  # If the hard drive is nearly full
            print("Delete unnecessary files or move them to an external storage device.")  # Suggest freeing up space
        else:
            response = askQuestion("Have you tried restarting the computer?")
            if "no" in response:  # If the computer hasn't been restarted
                print("Restart the computer to improve performance.")  # Suggest restarting the computer
            else:
                print("Check for software updates or scan for malware.")  # Suggest updates or malware scan

def troubleshootSoftwareInstallation():
    # Troubleshooting steps for failed software installation
    response = askQuestion("Do you have enough storage space?")
    if "no" in response:  # If there's not enough storage
        print("Free up some space by deleting unused files.")  # Suggest freeing up space
    else:
        response = askQuestion("Is the installer file corrupted?")
        if "yes" in response:  # If the installer file is corrupted
            print("Download a fresh copy of the installer.")  # Suggest downloading a fresh installer
        else:
            response = askQuestion("Are you using an administrator account?")
            if "no" in response:  # If not running as administrator
                print("Try running the installer as an administrator.")  # Suggest running as administrator
            else:
                print("Check for software compatibility issues.")  # Suggest checking compatibility

def troubleshootWifiDrops():
    # Troubleshooting steps for frequent Wi-Fi drops
    response = askQuestion("Are other devices having the same issue?")
    if "yes" in response:  # If other devices are also affected
        print("Restart your router.")  # Suggest restarting the router
    else:
        response = askQuestion("Is your device close to the router?")
        if "no" in response:  # If the device is too far from the router
            print("Move closer to the router.")  # Suggest moving closer to the router
        else:
            print("Update your Wi-Fi drivers or reset network settings.")  # Suggest updating drivers or resetting settings

def troubleshootBsod():
    # Troubleshooting steps for a Blue Screen of Death (BSOD)
    response = askQuestion("Did you recently install any new hardware or software?")
    if "yes" in response:  # If new hardware/software was installed
        print("Uninstall recent software or disconnect new hardware.")  # Suggest uninstalling or disconnecting
    else:
        response = askQuestion("Is your computer overheating?")
        if "yes" in response:  # If the computer is overheating
            print("Ensure the cooling system is working or clean any dust from vents.")  # Suggest cooling system check
        else:
            print("Try booting into safe mode to troubleshoot.")  # Suggest booting into safe mode for further diagnosis

def troubleshootAudio():
    # Troubleshooting steps for audio issues
    response = askQuestion("Is the volume turned up?")
    if "no" in response:  # If the volume is turned down
        print("Turn up the volume and check if the audio works.")  # Suggest turning up the volume
    else:
        response = askQuestion("Is the correct output device selected?")
        if "no" in response:  # If the wrong output device is selected
            print("Select the correct output device from the sound settings.")  # Suggest changing the output device
        else:
            print("Check the sound drivers or restart the computer.")  # Suggest checking drivers or restarting

def troubleshootUpdate():
    # Troubleshooting steps for update failures
    response = askQuestion("Do you have a stable internet connection?")
    if "no" in response:  # If there is no stable internet connection
        print("Ensure you’re connected to a stable network.")  # Suggest ensuring a stable network connection
    else:
        response = askQuestion("Is there enough storage space for the update?")
        if "no" in response:  # If there's not enough space for the update
            print("Free up some space by deleting unnecessary files.")  # Suggest freeing up space
        else:
            print("Try restarting your computer and update again.")  # Suggest restarting the computer and updating

def main():
    # Main function to handle user input and trigger troubleshooting
    print("Welcome to the Tech Support Troubleshooter!")
    print("Please describe your issue from the following options:")
    print("1. Internet Connectivity Issues")
    print("2. Printer Not Printing")
    print("3. Computer Running Slowly")
    print("4. Software Installation Issues")
    print("5. Wi-Fi Connection Drops")
    print("6. Blue Screen of Death (BSOD)")
    print("7. Audio Issues")
    print("8. Operating System Update Failure")
    
    # Ask the user to choose an issue
    choice = input("Enter the number corresponding to your issue: ")

    # Call the appropriate troubleshooting function based on the user's choice
    if choice == "1":
        troubleshootInternet()
    elif choice == "2":
        troubleshootPrinter()
    elif choice == "3":
        troubleshootSlowComputer()
    elif choice == "4":
        troubleshootSoftwareInstallation()
    elif choice == "5":
        troubleshootWifiDrops()
    elif choice == "6":
        troubleshootBsod()
    elif choice == "7":
        troubleshootAudio()
    elif choice == "8":
        troubleshootUpdate()
    else:
        print("Invalid choice. Please try again.")  # Error handling for invalid input

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
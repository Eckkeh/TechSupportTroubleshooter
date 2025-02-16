# Rule-based AI Project Ideas

## Medical Symptom Checker
- **What it does**: Provides possible diagnoses based on symptoms entered by the user.
- **How it works**: Uses a rule-based decision tree where certain symptoms correspond to predefined conditions. For example, if a user reports "fever + cough," the system might suggest "possible flu or cold."

## Tech Support Troubleshooter
- **What it does**: Guides users through common tech problems (e.g., internet not working, printer issues).
- **How it works**: Uses a rule-based flowchart where each issue leads to a series of predefined troubleshooting steps. If the Wi-Fi isn't working, the system might ask, "Is the router on?" and guide the user based on responses.

## Personality Quiz Bot
- **What it does**: Asks users questions and categorizes them into personality types based on answers.
- **How it works**: Uses predefined rules to assign points to different personality types. If a user picks "I enjoy social gatherings" → +1 to extrovert, "I prefer quiet time" → +1 to introvert, etc.

---

## Chosen Project: Tech Support Troubleshooter
I chose this project because it is relatable and can be turned into an actual program to help people who may not be able to access the internet right away.

---

## Part 3 – Rules and Logic

### 1. Internet Connectivity Issues
- **Rule**:
    - **IF** user says "internet is not working" OR "no internet connection"
    - **THEN** ask "Is your device connected to Wi-Fi?"
      - **IF** "yes"  
        **THEN** check if Wi-Fi is enabled and connected
        - **IF** not connected  
          **THEN** suggest "Try reconnecting to the Wi-Fi network"
        - **IF** connected but still no internet  
          **THEN** suggest "Restart your router and modem"
      - **IF** "no"
        **THEN** ask "Is the Wi-Fi turned on?"
        - **IF** "yes"  
          **THEN** suggest "Try reconnecting to the Wi-Fi network"
        - **IF** "no"  
          **THEN** suggest "Turn on Wi-Fi and try connecting again"

### 2. Printer Not Printing
- **Rule**:
    - **IF** user says "printer not printing" OR "printer is offline"
    - **THEN** ask "Is the printer powered on?"
      - **IF** "no"  
        **THEN** suggest "Turn on the printer"
      - **IF** "yes"  
        **THEN** ask "Is the printer connected to the computer?"
        - **IF** "no"  
          **THEN** suggest "Check the cable connection or try reconnecting via Bluetooth/Wi-Fi"
        - **IF** "yes"  
          **THEN** ask "Is there paper and ink in the printer?"
            - **IF** "no"  
              **THEN** suggest "Make sure there’s paper and ink/toner in the printer"
            - **IF** "yes"  
              **THEN** suggest "Try restarting the printer and computer"

### 3. Computer Running Slowly
- **Rule**:
    - **IF** user says "computer is slow" OR "lagging" OR "freezing"
    - **THEN** ask "Do you have many programs open?"
      - **IF** "yes"  
        **THEN** suggest "Close unused programs to free up memory"
      - **IF** "no"  
        **THEN** ask "Is your hard drive nearly full?"
          - **IF** "yes"  
            **THEN** suggest "Delete unnecessary files or move them to an external storage device"
          - **IF** "no"  
            **THEN** ask "Have you tried restarting the computer?"
              - **IF** "no"  
                **THEN** suggest "Restart the computer to improve performance"
              - **IF** "yes"  
                **THEN** suggest "Check for software updates or scan for malware"

### 4. Software Installation Issues
- **Rule**:
    - **IF** user says "can't install software" OR "installation failed"
    - **THEN** ask "Do you have enough storage space?"
      - **IF** "no"  
        **THEN** suggest "Free up some space by deleting unused files"
      - **IF** "yes"  
        **THEN** ask "Is the installer file corrupted?"
          - **IF** "yes"  
            **THEN** suggest "Download a fresh copy of the installer"
          - **IF** "no"  
            **THEN** ask "Are you using an administrator account?"
              - **IF** "no"  
                **THEN** suggest "Try running the installer as an administrator"
              - **IF** "yes"  
                **THEN** suggest "Check for software compatibility issues"

### 5. Wi-Fi Connection Drops
- **Rule**:
    - **IF** user says "Wi-Fi keeps disconnecting" OR "Wi-Fi drops frequently"
    - **THEN** ask "Are other devices having the same issue?"
      - **IF** "yes"  
        **THEN** suggest "Restart your router"
      - **IF** "no"  
        **THEN** ask "Is your device close to the router?"
          - **IF** "no"  
            **THEN** suggest "Move closer to the router"
          - **IF** "yes"  
            **THEN** suggest "Update your Wi-Fi drivers or reset network settings"

### 6. Blue Screen of Death (BSOD)
- **Rule**:
    - **IF** user says "blue screen" OR "BSOD" OR "system crash"
    - **THEN** ask "Did you recently install any new hardware or software?"
      - **IF** "yes"  
        **THEN** suggest "Uninstall recent software or disconnect new hardware"
      - **IF** "no"  
        **THEN** ask "Is your computer overheating?"
          - **IF** "yes"  
            **THEN** suggest "Ensure the cooling system is working or clean any dust from vents"
          - **IF** "no"  
            **THEN** suggest "Try booting into safe mode to troubleshoot"

### 7. Audio Issues
- **Rule**:
    - **IF** user says "no sound" OR "audio not working"
    - **THEN** ask "Is the volume turned up?"
      - **IF** "no"  
        **THEN** suggest "Turn up the volume and check if the audio works"
      - **IF** "yes"  
        **THEN** ask "Is the correct output device selected?"
          - **IF** "no"  
            **THEN** suggest "Select the correct output device from the sound settings"
          - **IF** "yes"  
            **THEN** suggest "Check the sound drivers or restart the computer"

### 8. Operating System Update Failure
- **Rule**:
    - **IF** user says "can't update" OR "update failed"
    - **THEN** ask "Do you have a stable internet connection?"
      - **IF** "no"  
        **THEN** suggest "Ensure you’re connected to a stable network"
      - **IF** "yes"  
        **THEN** ask "Is there enough storage space for the update?"
          - **IF** "no"  
            **THEN** suggest "Free up some space by deleting unnecessary files"
          - **IF** "yes"  
            **THEN** suggest "Try restarting your computer and update again"

---

## Input and Output

### Example 1:
- **Enter the number corresponding to your issue**: 1
- **Is your device connected to Wi-Fi?**
    - Your response: Yes
- **Is your Wi-Fi connected to the internet?**
    - Your response: No
- **Solution**: Try restarting your router and modem.

### Example 2:
- **Enter the number corresponding to your issue**: 2
- **Is the printer powered on?**
    - Your response: Yes
- **Is the printer connected to the computer?**
    - Your response: Yes
- **Is there paper and ink in the printer?**
    - Your response: Yes
- **Solution**: Try restarting the printer and your computer.

### Example 3:
- **Enter the number corresponding to your issue**: 3
- **Do you have many programs open?**
    - Your response: No
- **Is your hard drive nearly full?**
    - Your response: No
- **Have you tried restarting the computer?**
    - Your response: No
- **Solution**: Restart the computer to improve performance.

---

## Reflection

My rule-based system functions as an interactive troubleshooting assistant for common technical issues. It uses a structured series of if-elif-else statements to guide users through diagnostic steps based on their responses. The system begins by presenting a menu of issues, such as internet connectivity problems, printer malfunctions, or slow computer performance. Once the user selects a category, the program asks relevant yes/no questions and provides step-by-step solutions based on predefined rules. The decision-making process follows a hierarchical approach, where each response determines the next question or recommendation. By systematically narrowing down potential causes, the system helps users resolve issues efficiently without requiring advanced technical knowledge.

One of the biggest challenges I faced while prompting the AI to assist with the design and coding was ensuring that the logic remained both comprehensive and easy to follow. Initially, I had trouble structuring the troubleshooting paths to account for multiple possible causes while avoiding unnecessary complexity. I had to refine my prompts to clarify that I wanted simple, rule-based logic rather than an overly sophisticated approach. Another challenge was making sure the system handled different user inputs correctly. The AI helped by suggesting ways to standardize responses, such as converting input to lowercase for consistency. Additionally, I had to ensure that the troubleshooting steps were logically ordered so users wouldn’t be asked redundant or irrelevant questions.

Overall, the process of working with AI to develop the rule-based system was insightful. It helped me understand how early AI systems operated before the rise of machine learning, relying purely on logical rules rather than data-driven models. This project reinforced the importance of clear decision trees and structured reasoning when designing AI-powered support systems.
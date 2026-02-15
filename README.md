# NetDiscover Pro v3 🔍

Advanced WiFi Network Scanner  
Created by Ankush Kumar  
Diploma CSE Student | Cybersecurity Learner

NetDiscover Pro v3 is a local network scanner that discovers connected devices on your WiFi network, performs port scanning, detects possible IP cameras, guesses operating systems, calculates risk scores, and generates a JSON report.

------------------------------------------------------------

👨‍💻 DEVELOPER INFORMATION

Name: Ankush Kumar  
Course: Diploma in Computer Science & Engineering (CSE)  
Interest Areas: Cybersecurity, Ethical Hacking, Linux System Security  
Focus: Building practical security tools for learning and real-world understanding  

This project is part of my hands-on cybersecurity learning journey.

------------------------------------------------------------

🚀 FEATURES

- ARP Network Discovery (Find all connected devices)
- Full TCP Port Scan (1–1024)
- Camera Detection (RTSP / Web-based)
- OS Guess (TTL-based detection)
- Device Type Identification
- Risk Score Calculation
- Multithreaded Fast Scanning
- JSON Report Export

------------------------------------------------------------

⚙ REQUIREMENTS

- Python 3.x
- Same WiFi network access
- Root (sudo) recommended for Kali/Linux
- Internet connection (for installing dependencies)

------------------------------------------------------------

📦 INSTALLATION (Kali Linux / Ubuntu)

Step 1: Update System (Recommended)

     sudo apt update

Step 2: Install Git and Python (If not installed)

     sudo apt install git python3 python3-pip -y

Step 3: Clone Repository

    git clone https://github.com/ahiraankush771/NetDiscover-Pro.git

Step 4: Enter Project Folder

    cd NetDiscover-Pro

Step 5: Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------

▶ RUN (Kali / Ubuntu)

    sudo python3 netdiscover_pro_v3.py

Running with sudo is recommended for proper network scanning.

------------------------------------------------------------

📱 INSTALLATION (Termux)

Step 1: Update Termux

     pkg update

Step 2: Install Required Packages

    pkg install git python -y

Step 3: Clone Repository

    git clone https://github.com/ahiraankush771/NetDiscover-Pro.git

Step 4: Enter Folder

    cd NetDiscover-Pro

Step 5: Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------

▶ RUN (Termux)

python3 netdiscover_pro_v3.py

Note: Termux may show limited results compared to Kali Linux.

------------------------------------------------------------

📊 OUTPUT EXPLANATION

The scanner will display:

- IP Address of each device
- Number of open ports
- Device Type (Windows, Linux, Camera, etc.)
- OS Guess
- Risk Score
- Camera Detection status

A file named:

scan_report.json

will be generated in the same directory containing full scan results.

------------------------------------------------------------

⚠ IMPORTANT NOTICE

- Use only on networks you own or have permission to test.
- Unauthorized network scanning may be illegal.
- OS detection is heuristic-based and may not be 100% accurate.
- This tool is for educational and defensive security purposes only.

------------------------------------------------------------

📌 FUTURE IMPROVEMENTS

- Custom IP range input
- Service version detection
- Faster optimized scanning
- CLI arguments support
- Web dashboard interface

------------------------------------------------------------

⭐ If you find this project useful, consider giving it a star.

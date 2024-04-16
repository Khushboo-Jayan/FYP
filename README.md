# FYP
 
Extensive testing is done to verify the functionality of key functions like connectnetwork and network-scan, guaranteeing smooth connectivity and precise network scanning abilities. Expert modules such as vendorlookup, arpspoofing, and drone-motion-control are thoroughly tested to determine how well they work at executing certain tasks like drone manipulation, spoofing attacks, and vendor identification. 

The performance of the framework is also evaluated throughout the testing process under numerous circumstances, such as varied network topologies, traffic loads, and security setups. In order to improve the framework's general robustness and dependability, this evaluation aids in locating any potential problems, bottlenecks, or vulnerabilities. ​(Hacking a Wi-Fi based  drone Rubbestad)​ 

<img width="601" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/f4df7bc4-6b80-49ab-8e8f-f0c973f3e675">
 
Fig 5.2.1 SentinelGuard Commands  

5.2.1 Commands 
 

MonitorMode.py: The network adapter is successfully switched to monitor mode as expected by the MonitorMode.py script. It has good security protections, sufficient error handling, and strong functionality. 

  <img width="543" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/a00e2401-7c11-4c74-9063-87cc6cb8e4aa">

Fig 5.2.1.1 Wi-Fi adapter switch  
 

HostDiscovery.py: The device_discovery() method efficiently finds hosts within the given IP range and returns information on the hostnames, MAC addresses, and statuses of connected devices. It has precise functionality, respectable performance, and engaging user interface. Nevertheless, additional testing in various network contexts and configurations could be required to guarantee thorough coverage and dependability. 

<img width="599" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/6ab34534-3b16-480b-9c3e-67771326e160">

Fig 5.2.1.2 Tello Network Scan results  

 

 <img width="103" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/7d2a7f72-8257-4a44-9bd7-a6699a5949fe">


Fig 5.2.1.3 Issues printing Mac address 

However, further testing across diverse network configurations and environments may be necessary to ensure comprehensive coverage and reliability. 

 

ConnectCrackedNetwork.py: WPA handshake breaking passwords can be used to connect to Wi-Fi networks with the help of the connect_to_cracked_network() function. It exhibits dependable operation, suitable error management, and adequate security precautions. The script's ability to join successfully using passwords obtained through WPA handshake cracking has been tested across a variety of Wi-Fi networks. The following has been tested on three different networks.  
 

<img width="598" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/9fc7ca70-28c0-4a39-96d2-cf2a81cb1fb6">

Fig 5.2.1.4 Connection established for network 1  


<img width="594" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/230f89ab-db2e-483b-9394-17351045455a">

Fig 5.2.1.5 Connection failed for network 2 invalid BSSID 


<img width="590" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/50f3eb9a-d110-419a-bd43-2fda001fb4e0">

Fig 5.2.1.5 Connection established for network 3  

 

 

RestartNetwork.py: The restart_network_services() function effectively restarts network services to switch the Wi-Fi adapter mode from monitor to managed, facilitating normal network operation. It demonstrates reliable functionality, adequate error handling, and minimal system impact. 

<img width="599" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/91b368cc-7e12-4ca0-b440-9faeef5be4b8">

Fig 5.2.1.6 wlan0mon switched to managed mode 

5.2.2 Modules 
 

The ‘Mac Vendor Lookup’: It is an extra module in the system which helps the user identify detailed information about a device using the MAC address. The framework uses the mac-vendor-lookup python3 library which contains a copy of IEE’s OUI prefix. For instance, mac prefix C0:E4:34 belongs to AzureWave Technology Inc. cross checking with Wireshark OUI gives the same output. 


 <img width="488" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/723f6d19-40c0-4030-98de-186397b96749">

Fig 5.2.2.1. Mac Vendor Lookup module by SentinelGuard Framework 
 

<img width="290" alt="image" src="https://github.com/Khushboo-Jayan/FYP/assets/79542266/c970f2ab-0705-4c6d-a05a-1d4d933e6904">
 
Fig 5.2.2.2 Mac Vendor Lookup by OUI Wireshark Web Services  
 

WPA Handshake: The process of capturing WPA handshake packets for password cracking is automated by the wpa_capture_password_cracking() function. It offers two ways to get around this: either use a pre-existing capture file or capture the WPA handshake and use that to crack the network password. If the user selects option one the path for sniffed capture file (.cap) needs to be entered and the password cracking will be performed offline. Below the key found for testing performed on saved oneplus hotspot network is.  
Aircrack-ng 1.7 
59/10303727 keys tested (094.28 k/s) 
Tine left: hours, 7 minutes, 22 seconds 
Master Key 
Transient Key 
KEY FOUND! [ 123450789 1 
: 7F 0B A9 13 9E 96 8B 77 ES 95 25 BE 
03 AS 00 FF 26 9A 51 E2 09 F7 A3 9B 
E3 4E 38 AB 
: 43 98 56 09 09 2C 88 ID 78 9E 
10 50 58 
20 83 10 88 4A AD BE BE 80 
ED 9E ca OF 16 48 9E A9 C2 AD 58 ec 99 9C 
44 02 AF A2 5b 08 07 10 AO AF 14 5B 
F5 99 14 BE  
Fig 5.2.2.3. Saved .cap file password extraction 
 
But if there is a change in password, the capture file is too old or there has been zero sniffing and is a new network, option two is very helpful. The script starts a sequence of events when the user chooses the second option. First, it makes use of airodump-ng to track wireless traffic and determine the BSSID and channel of the target network. After that, it makes a directory to hold the data it has collected and runs airodump-ng once more to gather the handshake packets. It then gives the user instructions on how to use aireplay-ng in a different terminal to force de-authentication and start the handshake. Following the capture, the user copies the generated.cap file, which the script uses to try to crack passwords using aircrack-ng and a given wordlist. 

 

Fig 5.2.2.4. Details of intended network 

Below it can be noted that directory will be created, and user can name it accordingly and also save the capture files will include the WPA handshake. For instance, all the generated data will be stored in a specific folder named SniffedData for further study. 

 

 
 
Fig 5.2.2.5. Capture file Creation, four way handshake 

After receiving 10 de-authentication packets the client disconnects from the network it tries to reconnect by sending a WPA handshake, this is then captured and saved for later use. 

 
Fig 5.2.2.6. Deauth signals   

 
 
Fig 5.2.2.7. Wireshark analysis for EAPOL protocol 

 

Using the captured four-way handshake and the extracted rockyou.txt file we mentioned in the ‘requirement gathering’ section of this paper password can be cracked for networks. However, the solution for avoiding easy password cracking as seen below which was obtained within 0.13% of comparing with rockyou.txt a complex combination of alphanumeric values along with special characters is suggested.  

  
Fig 5.2.2.7. Password Cracked 

 

ARP 
Introduce the ARP spoofing experiment and its objectives, highlighting the significance of understanding network security vulnerabilities and potential risks associated with ARP spoofing attacks. 

ARP Spoofing Process 
Network Discovery: Utilize a custom framework with the Python host discovery function to obtain a list of IP addresses within the network range. 
ARP Spoofing Execution: Enable packet forwarding using the command below to allow packets to be forwarded through the attacker's machine. Execute ARP spoofing using arpspoof command on the attacker's machine to poison the ARP cache of the target devices, redirecting traffic through the attacker's machine. 
>>sysctl -w net.ipv4.ip_forward=1 
 
Wireshark Traffic Analysis: During the ARP spoofing experiment, Wireshark was used to capture and analyze network traffic. The captured packets revealed the following: 
ARP Requests and Responses: ARP spoofing involves sending falsified ARP messages to network devices. These messages typically consist of ARP requests asking for the MAC address corresponding to a particular IP address and ARP responses providing the requested MAC address. In the captured traffic, ARP requests were observed targeting specific IP addresses, and corresponding ARP responses were sent by the attacker's machine, providing the MAC address of the attacker instead of the legitimate device. 
Packet Redirection: After successful ARP spoofing, network traffic intended for the target device was redirected through the attacker's machine. This redirection was evident from the packet flow observed in Wireshark, where packets originally destined for the target device were instead sent to the attacker's MAC address. 
Other Relevant Packet Details: In addition to ARP packets, various other types of network traffic were observed, including TCP, UDP, and ICMP packets. These packets may contain sensitive information or commands exchanged between networked devices. 
Results:  
Glitches and Impact Assessment: The ARP spoofing attack resulted in several glitches and disruptions within the network: 
Camera Output Disruptions: Users of the controller device experienced interruptions in the live camera output from the drone. These disruptions could manifest as freezing, lagging, or pixelation of the video feed. 
Issues with Image Capture Functionality: Attempts to capture images using the controller device failed due to the network interference caused by ARP spoofing. 
Impact on Network Performance: The ARP spoofing attack imposed additional overhead on the network, leading to decreased performance and increased latency. This impact was particularly noticeable during data-intensive tasks such as streaming video or transmitting large files. 
 
 
Fig 5.2.2.8.  Wireshark capture when arp spoof commands run in background. 
 
Drone control and Live Stream: In this study, it has been identified that by exploiting an ARP spoofing attack, it is feasible to position oneself between the drone and its controller, thereby intercepting the transmitted traffic. To decode the real-time video stream, an initial establishment of a standard network connection is required, followed by the execution of the "streamon" command from the Tello SDK and the "FFplay" command from the FFmpeg utility. Subsequently, the information routed to port 11111 undergoes decoding and is displayed within a window on the computer screen, enabling visualization of the video feed. 
 
 
Fig 5.2.2.9. Wrireshark UDP packet capture after streamon command 

 

Moreover, the TelloControl.py script, beyond its network management functionalities, orchestrates a sequence of actions aimed at controlling a DJI Tello drone. Within the realm of software development, the code is structured and delineated as follows: 

Importing Modules: 
By importing functions from separate modules, it adheres to the principle of separation of concerns, making the codebase more maintainable and understandable.  
Time, OS, and functions from custom modules like ConnectCrackedNetwork, MonitorMode, WPA_Handshake, and RestartNetwork are imported by the script together with other relevant modules. By encapsulating particular functions, these modules encourage code organization and modularity. 
 
Function Execution:  
A sequence of activities is defined for the take_flight_control function to be carried out. It begins by carrying out network-related operations such entering monitor mode, obtaining the WPA handshake to crack passwords, resuming network services, and establishing a connection to a compromised network. 
It then creates an instance of the Tello class from the djitellopy library to begin communication with the Tello drone. 
 
Controlling Drone: 
Once the connection has been established, it gets battery information, sends a stream-on instruction from the drone's camera to the Tello SDK to stream video, and then launches the drone into the air. 
Then, it uses the send_rc_control method given by the Tello class to send remote control (RC) commands to control the drone's movement, including commands for landing, hovering, ascending, and forward motion. 
Meanwhile, the script uses the os.system function to run stream video feed (ffplay udp://@:11111 &) as a backgroyund process which terminats by with the drone landing.​(8 Top Methods to Run Linux Commands in Background, no date)​ 
To ensure that flight manoeuvres are executed correctly, the script introduces time delays throughout the flight sequence by using the time.sleep() function. 
 
Fig 5.2.2.10. Successful motion control alongside live stream as background process 

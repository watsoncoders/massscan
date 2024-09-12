Types of Ports: TCP and UDP
The two primary transport protocols with associated port numbers are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). Software applications and services are built to utilize either TCP or UDP and are assigned specific port numbers for communication.

TCP is a connection-based protocol that includes mechanisms for re-transmission and error correction. It is considered to be more reliable due to these built-in features.
UDP is a connectionless protocol, meaning it does not correct or recover from errors in message transmission. Often referred to as a "best-effort" protocol, UDP is faster but less reliable than TCP.
Port States
TCP and UDP ports can exist in one of three possible states depending on the system's configuration and purpose:

Open – The port is actively responding to connection attempts.
Closed – The port is not in use, and no services are running on it.
Filtered – A firewall or security mechanism is regulating traffic, blocking connection attempts to certain ports.
Security Threats Related to Open Ports
Cyber attackers often target open ports to exploit vulnerabilities. Below are some common attacks and methods hackers use to exploit open ports, followed by two notable real-world examples of attacks based on open-port weaknesses.

Common Exploits and Attacks
RDP connection abuse: Hackers may use an open Remote Desktop Protocol (RDP) port to attempt credential stuffing, gaining unauthorized access to a system, or deploying ransomware.
Denial of Service (DoS) attacks: By sending excessive connection requests to a target service, attackers aim to overwhelm it, typically by targeting web ports, resulting in legitimate users being unable to access the service.
Web-based attacks: Ports used by web services can be exploited for attacks like SQL injection and cross-site request forgery (CSRF), which take advantage of vulnerabilities within web applications.
Man-in-the-middle (MITM) attacks: Attackers can intercept unencrypted data flowing through well-known ports, capturing sensitive information such as login credentials or financial data.
Case Studies: WannaCry and RDP Pipe Plumbing
WannaCry Ransomware Attack (2017): A global attack affecting over 300,000 computers in 150 countries, WannaCry exploited a vulnerability in the SMB protocol (Port 445). Once inside a system, the ransomware encrypted critical files, demanding payment in exchange for decryption.
RDP Pipe Plumbing Vulnerability: This vulnerability affects the Remote Desktop Protocol by exploiting Windows-named pipes. Attackers target Port 3389 (RDP), creating fake named pipes to intercept communication between RDP clients and servers. This allows unauthorized access to sensitive data and system interactions.
Vulnerable Ports and Their Associated Risks
Port 21 (FTP)
File Transfer Protocol (FTP) runs on port 21, allowing file exchanges between users and servers. However, as FTP transmits data in plain text, it poses a significant security risk. Common vulnerabilities include:
Brute-force password attacks
Anonymous login access
Cross-site scripting (XSS) attacks
Directory traversal exploits
Man-in-the-middle attacks
Port 22 (SSH)
Secure Shell (SSH), commonly using port 22, offers encrypted remote access, making it more secure than Telnet. However, vulnerabilities arise from:
Unsecured SSH keys, allowing unauthorized access without passwords.
Brute-force attacks on open SSH ports to guess login credentials.
Port 23 (Telnet)
Telnet operates on port 23 and is often used for remote management of network devices. However, due to its lack of encryption, it is highly insecure. Common threats include:
Credential brute-forcing
Spoofing and credential sniffing, allowing attackers to intercept sensitive data during transmission.
Port 25 (SMTP)
Simple Mail Transfer Protocol (SMTP) uses port 25 for email exchange but lacks modern security measures. This makes it vulnerable to:
Email spoofing, where attackers forge email headers.
Spam distribution, where attackers exploit unsecured SMTP servers to send massive volumes of unsolicited emails.
Man-in-the-middle attacks, especially if emails are transmitted in plain text.
Port 53 (DNS)
Domain Name System (DNS) uses port 53 for translating domain names into IP addresses. Although critical for internet functionality, it is vulnerable to:
Distributed Denial of Service (DDoS) attacks that flood DNS servers with traffic, disrupting service.
DNS amplification attacks, which are a form of DDoS that leverage vulnerable DNS servers to magnify attack traffic.
Ports 137, 139 (NetBIOS over TCP) and 445 (SMB)
NetBIOS over TCP (ports 137, 139) and SMB (port 445) are widely used for file sharing in Windows environments. However, they are frequently targeted by attackers exploiting:
EternalBlue, a notorious vulnerability in SMBv1 that was exploited by the WannaCry ransomware attack.
NTLM hash capturing, allowing attackers to steal credentials.
Brute-force attacks on SMB login credentials.
Ports 80, 443, 8080, 8443 (HTTP/HTTPS)
These ports are used for web traffic and are commonly attacked through:
Cross-site scripting (XSS), where malicious scripts are injected into web applications.
SQL injection, where attackers manipulate databases by inserting malicious SQL code into input fields.
Cross-site request forgery (CSRF), tricking users into unknowingly submitting unauthorized requests.
Ports 1433, 1434, 3306 (SQL Server and MySQL)
SQL Server (ports 1433, 1434) and MySQL (port 3306) are commonly used database services that can be exploited for:
Distributing malware
Launching DDoS attacks
Exploiting weak database configurations
Port 3389 (RDP)
Remote Desktop Protocol (RDP) runs on port 3389 and is prone to brute-force and MITM attacks. One significant vulnerability is BlueKeep (CVE-2019-0708), which allows attackers to remotely execute code on older versions of Windows without user interaction.
Conclusion
Open ports, especially those associated with widely used services like HTTP, DNS, and SMB, are frequent targets for cyberattacks. Ensuring ports are properly secured, monitored, and closed when not in use can mitigate many of the associated risks. Implementing proper security measures like encryption, strong authentication, and firewalls is essential in defending against these vulnerabilities.

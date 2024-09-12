import xml.etree.ElementTree as ET
import csv

# Parse the Nmap XML output file
tree = ET.parse('output.xml')
root = tree.getroot()

# Open a CSV file for writing
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IP', 'Hostname', 'Port', 'Protocol', 'Service'])

    # Iterate over each host in the XML
    for host in root.findall('host'):
        ip = host.find("address[@addrtype='ipv4']").attrib['addr']
        hostname = host.find("hostnames/hostname")
        hostname = hostname.attrib['name'] if hostname is not None else ''
        
        # Iterate over each port
        for port in host.findall('ports/port'):
            portid = port.attrib['portid']
            protocol = port.attrib['protocol']
            service = port.find('service').attrib['name']
            writer.writerow([ip, hostname, portid, protocol, service])

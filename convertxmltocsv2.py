import xml.etree.ElementTree as ET
import csv

# Parse the Masscan XML output file
tree = ET.parse('output.xml')
root = tree.getroot()

# Define the path where the CSV file will be saved
csv_file_path = '/path/to/your/directory/output.csv'  # Change this to the path you want

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IP', 'Port', 'Protocol', 'Service'])

    # Iterate over each host in the XML
    for host in root.findall('host'):
        ip = host.find("address[@addrtype='ipv4']").attrib['addr']
        
        # Iterate over each port
        for port in host.findall('ports/port'):
            portid = port.attrib['portid']
            protocol = port.attrib['protocol']
            
            # Check if the service element exists
            service_element = port.find('service')
            if service_element is not None and 'name' in service_element.attrib:
                service = service_element.attrib['name']
            else:
                service = 'Unknown'  # Default if service is not present
            
            # Write data to the CSV
            writer.writerow([ip, portid, protocol, service])

print(f"Conversion completed, results saved to '{csv_file_path}'")

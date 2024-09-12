import json
import csv

# Define the input and output file names
json_file = 'output.json'
csv_file = 'masscan_results.csv'

# Open the JSON file and load it into a Python object
with open(json_file, 'r') as infile:
    data = json.load(infile)

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    # Write the header row
    writer.writerow(['IP Address', 'Port', 'Protocol', 'Status'])

    # Iterate through the Masscan JSON data and write to CSV
    for result in data:
        ip = result.get('ip', 'N/A')
        for port_info in result.get('ports', []):
            port = port_info.get('port', 'N/A')
            protocol = port_info.get('proto', 'N/A')
            status = port_info.get('status', 'N/A')
            writer.writerow([ip, port, protocol, status])

print(f"Results successfully written to {csv_file}")

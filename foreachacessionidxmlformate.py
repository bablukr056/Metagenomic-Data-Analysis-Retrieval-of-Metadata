#Retrieving ENA Accession Metadata and Saving in XML Format with Accession Number as File Name

import requests
import xml.etree.ElementTree as ET

with open("/home/bablu/Desktop/PhD/mgnify/mgnifyies.txt", "r") as file:
    ena_accessions = file.read().splitlines()

for ena_accession in ena_accessions:
    url = f"https://www.ebi.ac.uk/ena/data/view/{ena_accession}&display=xml"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        # Use the XML data as needed
        root = ET.fromstring(data)
        tree = ET.ElementTree(root)
        with open(f"{ena_accession}.xml", "w") as output_file:
            tree.write(output_file, encoding='unicode')
    else:
        print(f"Failed to retrieve data for ENA accession {ena_accession}")

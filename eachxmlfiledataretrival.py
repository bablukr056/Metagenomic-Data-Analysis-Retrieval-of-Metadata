# Code to Extract Information from XML Files

import os
import re
import requests
from lxml import etree

# Function to parse information from XML file
def parse_run_accession_xml(xml_file):
    # Parse the XML file
    tree = etree.parse(xml_file)
    # Initialize lists to store information
    sample_accessions, run_accessions, run_list = [], [], []
    title, description, primary_id = None, None, None

    # Loop through all PROJECT elements in the XML file
    for e in tree.findall("//PROJECT"):
        # Extract the PRIMARY_ID
        primary_id_element = e.find("./IDENTIFIERS/PRIMARY_ID")
        if primary_id_element is not None:
            primary_id = primary_id_element.text.strip()
        # Extract the title
        for t in e.findall("./TITLE"):
            title = t.text.strip()
        # Extract the description
        for d in e.findall("./DESCRIPTION"):
            description = d.text.rstrip() if d.text is not None else None
        # Extract the sample and run accessions
        for x in e.findall("./PROJECT_LINKS/PROJECT_LINK/XREF_LINK"):
            if x.getchildren()[0].text.strip() == "ENA-SAMPLE":
                sample_accessions = x.getchildren()[1].text.strip().split(",")
            elif x.getchildren()[0].text.strip() == "ENA-RUN":
                run_accessions = x.getchildren()[1].text.strip().split(",")
                run_list = ",".join([f"RUN:{r}" for r in run_accessions])

    # Return the extracted information in tab-separated format
    return (f"{primary_id}\t{title}\t{description}\t{sample_accessions}\t{run_accessions}\t{run_list}")

# Path to the folder containing XML files
folder_path = '/path/to/xml_files/folder/'

# Get all XML files in the folder
xml_files = [f for f in os.listdir(folder_path) if f.endswith('.xml')]

# Header for the output file
header = "PRIMARY_ID\tTitle\tDescription\tSample accessions\tRun accessions\tRun list"

# Write the extracted information to an output file
with open("output.txt", "w") as out_file:
    out_file.write(header + "\n")
    for xml_file in xml_files:
        extracted_data = parse_run_accession_xml(os.path.join(folder_path, xml_file))
        out_file.write(extracted_data + "\n")



    """This code is used to extract information from a set of XML files and write the information to an output text file. 
    The code uses the lxml library to parse the XML files and extract specific information from each file. 
    The information extracted from each XML file includes the primary ID, title, description, sample accessions
    """
# Extract Information from ENA Project XML File
#
# This code is a Python script that extracts information from a European Nucleotide Archive (ENA) project XML file, and returns the project title, description, sample accessions, run accessions, and run list.
#
# The code starts by importing the requests and lxml libraries. The requests library is used to send HTTP requests, while the lxml library is used to parse XML files.
#
# The parse_run_accession_xml function takes as input an ENA project XML file and returns the project information. The function first parses the XML file using the etree.parse function from the lxml library and stores the result in a variable called tree.
#
# Next, the function initializes four variables: sample_accessions, run_accessions, run_list, title, and description. These variables are used to store the information that is extracted from the XML file.
#
# The function then uses the findall function from the lxml library to extract information from the XML file. For each of the TITLE and DESCRIPTION elements in the PROJECT element, the function extracts the text content of the element and stores it in the title and description variables, respectively.
#
# For each of the XREF_LINK elements in the PROJECT_LINKS element, the function checks if the text content of the first child element (the DB element) is equal to "ENA-SAMPLE" or "ENA-RUN". If the text content is equal to "ENA-SAMPLE", the function extracts the text content of the second child element (the ID element) and stores it in the sample_accessions variable as a list of comma-separated accessions. If the text content is equal to "ENA-RUN", the function extracts the text content of the second child element and stores it in the run_accessions variable as a list of comma-separated accessions. The function also creates a run_list variable that consists of the run accessions prefixed with "RUN:".
#
# Finally, the function returns the title, description, sample_accessions, run_accessions, and run_list variables.
#
# The code ends by reading an XML file located at "/content/PRJDB2036_run_data.xml", calling the parse_run_accession_xml function, and storing the result in a variable called extracted_data. The function then prints the contents of the extracted_data variable.

# The rest of the data is written using writer.writerows with the extracted_data list as input. 
#
# This will write each tuple in extracted_data as a separate row in the file.

import requests
from lxml import etree
import csv

def parse_run_accession_xml(xml_file):
    tree = etree.parse(xml_file)
    sample_accessions, run_accessions, run_list = [], [], []
    title, description, primary_id = None, None, None
    
    results = []
    for e in tree.findall("//PROJECT"):
        primary_id_element = e.find("./IDENTIFIERS/PRIMARY_ID")
        if primary_id_element is not None:
            primary_id = primary_id_element.text.strip()
        for t in e.findall("./TITLE"):
            title = t.text.strip()
        for d in e.findall("./DESCRIPTION"):
            description = d.text.rstrip()if d.text is not None else None
        for x in e.findall("./PROJECT_LINKS/PROJECT_LINK/XREF_LINK"):
            if x.getchildren()[0].text.strip() == "ENA-SAMPLE":
                sample_accessions = x.getchildren()[1].text.strip().split(",")
            elif x.getchildren()[0].text.strip() == "ENA-RUN":
                run_accessions = x.getchildren()[1].text.strip().split(",")
                run_list = ",".join([f"RUN:{r}" for r in run_accessions])
                
        results.append((primary_id, title, description, sample_accessions, run_accessions, run_list))
        
    return results

xml_file = "/content/MGnify_AcessionIDes.xml"                        #change the file name accorindly.
extracted_data = parse_run_accession_xml(xml_file)

with open("MGnify_output.csv", "w") as f:                           #save in the different file name.
    writer = csv.writer(f)
    writer.writerow(["PRIMARY_ID", "Title", "Description", "Sample accessions", "Run accessions", "Run list"])
    writer.writerows(extracted_data)
#Retrieve Metadata for ENA Accessions
"""
This code is used to retrieve metadata for European Nucleotide Archive (ENA) accessions and store the data in a file. The code first opens a file named "/content/enaID" and reads its contents, which are expected to be a list of ENA accessions separated by newline characters.

The code then opens a file named "ena_metadata.txt" for writing and loops over the list of ENA accessions. For each accession, it creates a URL to retrieve the metadata for that accession from the ENA website using the requests library. The metadata is returned in XML format.

The code uses the requests.get function to send a GET request to the URL and retrieve the metadata. If the request is successful (status code 200), the code writes the XML data to the output file using output_file.write. If the request is unsuccessful, the code prints an error message indicating that the data retrieval failed for the current ENA accession.

After looping over all the accessions, the code closes both the input and output files.
"""

import requests

with open("/content/enaID", "r") as file:
    ena_accessions = file.read().splitlines()

with open("ena_metadata.txt", "w") as output_file:
    for ena_accession in ena_accessions:
        url = f"https://www.ebi.ac.uk/ena/data/view/{ena_accession}&display=xml"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.text
            # Use the XML data as needed
            output_file.write(data + "\n")
        else:
            print(f"Failed to retrieve data for ENA accession {ena_accession}")

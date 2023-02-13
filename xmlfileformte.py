#Retrieve Metadata for ENA Accessions


"""The code is used to retrieve metadata for European Nucleotide Archive (ENA) accessions and store the data in a file. Here's a detailed explanation of the code:

Import the requests library: This library is used to send HTTP requests to retrieve data from websites.

Reading the input file: The code uses the with statement to open the input file named "/content/enaID". The file.read() method is used to read the contents of the file into a string variable. The splitlines() method is then used to split the contents of the file into a list of ENA accessions, separated by newline characters.

Writing the output file: The csode uses the with statement to open the output file named "ena_metadata.xml" for writing.

Loop over the ENA accessions: The code uses a for loop to loop over the list of ENA accessions.

Create a URL: For each accession, the code creates a URL to retrieve the metadata for that accession from the ENA website. The URL is created using the f-string syntax and includes the ENA accession in the URL.

Send a GET request: The code uses the requests.get function to send a GET request to the URL and retrieve the metadata.

Check the status code: The code checks the status code of the response to determine if the request was successful. If the status code is 200, the code continues to process the data. If the status code is anything other than 200, the code prints an error message indicating that the data retrieval failed for the current ENA accession.

Convert the XML data: If the request was successful, the code converts the XML data to an ElementTree object using the xml.etree.ElementTree library.

Write the XML data to the output file: The code uses the write method of the ElementTree object to write the XML data to the output file. The write method takes the output file and the encoding as its arguments. In this case, the encoding is set to unicode.

Close the files: After looping over all the accessions, the code closes both the input and output files using the with statement.
    """


import requests
import xml.etree.ElementTree as ET

with open("/home/bablu/Desktop/PhD/mgnify/mgnifyies.txt", "r") as file:
    ena_accessions = file.readline().split()

with open("ena_metadata.xml", "w") as output_file:
    for ena_accession in ena_accessions:
        url = f"https://www.ebi.ac.uk/ena/data/view/{ena_accession}&display=xml"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.text
            # Use the XML data as neededls
            root = ET.fromstring(data)
            tree = ET.ElementTree(root)
            tree.write(output_file, encoding='unicode')

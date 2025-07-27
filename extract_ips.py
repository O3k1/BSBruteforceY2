import re  # import regular expressions library

# Open the logs.txt file for reading
with open("logs.txt", "r") as logs_file:
    # Read the content of the file and assign it to the variable named content
    content = logs_file.read()

    # Using regular expression to find valid IP addresses
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')  # raw string to interpretate the string literally, word boundary to ensure it is matching just the IP address as a separate entity as there are spaces (word boundaries) around it to ensure it is not a part of something else. ? quantifier to allow octets with no leading zeroes by matching optional single digits. The digit search is repeated 3 times (as given by the exact number quantifier of 3) to find the first 3 octets. The pattern matches 3 groups of 1 to 3 digits , this is after the character set which states that the digits can be between 0 to 9. Which is then followed by a period with a backslash in front of it to ensure it escapes it and searches for the correct period match,  the first 1-3 is the first segment/octet of the IP address, repeated 2 more times for the last 2 segments with a dot added after each iteration. The part after the  exact number quantifier of 3 ( I am referring to the "{3}") is effectively the same thing but just for the last segment/octet of the IP address. Unfortunately for me this still accepts some erroneous IP addresses as it does not limit the maximum number an octet can be to 255.
    ip_addresses = re.findall(ip_pattern, content)  # find all instances in the content variable that contains the content of logs.txt file that match the ipv4 pattern named ip_pattern. If it matches it is a valid IP address. Sadly this did not eliminate duplicate values as it does not look for distinct instances.

    if ip_addresses:  # if a matching/valid IP address is found then
        with open("ips.txt", "w") as ips_file:  # Open the ips.txt file for writing
            ips_file.write("\n".join(ip_addresses))  # Write each IP address to a new line in ips.txt using the join after each to 'add' a new line \n after each IP address, ensuring that one line only has one IP address
ips_file.close()  # close the file

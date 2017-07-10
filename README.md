# releaf_coding_challenge

The coding challenge in itself consists of scraping google search results for relevant links related to the companies
listed in Scrape_Assignment_DataSet.csv.

Having never created a webscraper before, I turned to our good old friend Google and his little cousin Youtube to see
if I could find anything of use. I chose Python because I do not have much experience as a software engineer, and the 
language is very english like. That aspect usually makes things easier for me. 

My source code is based off this <a href="https://www.youtube.com/watch?v=EELySnTPeyw">tutorial</a> on Youtube. 

During the process I ran into 2 roadbloacks:

1. Command line returned a syntax error when a company's name was attributed to company_name. My guess is it probably has something to do with the attribute being a string of words instead of a single word; just as it is demonstrated in the tutorial

2. When I tried to run my script with a single word, the command line returned an error saying the module selenium could 
not be found. This most likely has to do with the fact that selenium wasn't installed properly, or maybe its path wasn't
set up properly for some reason. I have not been able to fix this yet. There's a good chance however that resolving this
issue will automatically get rid of issue #1.

To Do Lists:

1. Retrieve relevant links related to any given company in Scrape_Assignment_Dataset.csv.

2. Pour output of links in Scrape_Assignment_Dataset.csv.

3. Update source code to prompt user to enter the name of the company they would like to get relevant links about.

import re

sentiment_analysis = [
  "AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company",
  "ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"
]

# Write a regex to match text file name
regex = r"^[aAeEiIoOuU]{2,3}.*txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))
    
	# Replace all matches with empty string
	print(re.sub(regex, "", text))
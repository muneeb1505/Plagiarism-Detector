from difflib import SequenceMatcher

with open("demo1.txt") as first_file, open("demo2.txt") as sec_file:
 info_one = first_file.read()
 info_two = sec_file.read()

 matches = SequenceMatcher(None, info_one, info_two).ratio()

 print(f"The plagiarized content is: {matches * 100} %")
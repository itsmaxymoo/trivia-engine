import os
import glob
import csv
import json


IN_DIR = "./questions"
BUILD_DIR = "./static/questions"


# Ensure we are in the proper directory
try:
	with open("./LICENSE") as fd:
		assert fd.read().index("Max Loiacono")
		fd.close()
except:
	print("Make sure you are running this script from within the project root!")
	exit(1)

try:
	if os.path.exists(BUILD_DIR):
		os.rmdir(BUILD_DIR)
	os.mkdir(BUILD_DIR)
except:
	print("Error creating output directory: " + BUILD_DIR)
	exit(1)

found_csv = glob.glob(IN_DIR + "/*.csv")



# --- Generate topic list

topic_list = list(map(lambda question_bank: question_bank.lstrip(IN_DIR + "/").rstrip(".csv"), found_csv))

with open(BUILD_DIR + "/_topics.json", "w") as fd:
	fd.write(json.dumps(topic_list))
	fd.close()



# --- Generate question banks

# TODO: this
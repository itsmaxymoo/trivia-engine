import os
import glob
import csv
import json


IN_DIR = "./questions"
BUILD_DIR = "./static/questions"
COL_DIFFICULTY = 0
COL_QUESTION_TEXT = 1
COL_RESP_START = 2
RESP_CORRECT_INDICATOR = "[x]"


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
		for file in glob.glob(BUILD_DIR + "/*"):
			os.remove(file)
	else:
		os.mkdir(BUILD_DIR)
except:
	print("Error creating output directory: " + BUILD_DIR)
	exit(1)

found_csv = glob.glob(IN_DIR + "/*.csv")



# --- For topics list file

topic_list = {}



# --- Generate question banks

class Question:
	question: str
	correct_answers: list
	false_answers: list

	def __init__(self, question: str, correct_answers: list, wrong_answers: list):
		self.false_answers = wrong_answers
		self.correct_answers = correct_answers
		if not question:
			raise ValueError("question length must be >0")
		
		self.question = question

		if len(wrong_answers) < 1 or len(correct_answers) < 1:
			raise ValueError("# responses error")
		
		for a in zip(self.correct_answers, self.false_answers):
			if len(a) < 1:
				raise ValueError("response length must be >0")
	
	def to_dict(self):
		return {
			"question": self.question,
			"correct_answers": self.correct_answers,
			"false_answers": self.false_answers
		}


# Iterate through found csv files
for csv_path in found_csv:
	stripped_name = csv_path.lstrip(IN_DIR + "/").rstrip(".csv")
	# Append to topics list
	topic_list[stripped_name] = 0

	# Create question bank
	bank = []

	with open(csv_path, newline='') as csv_file:
		csv_reader = csv.reader(csv_file, dialect="excel")
		next(csv_reader, None)

		for row in csv_reader:
			wrong_answers = []
			correct_answers = []

			for i in range(COL_RESP_START, len(row)):
				if row[i].startswith(RESP_CORRECT_INDICATOR):
					correct_answers.append(row[i].lstrip(RESP_CORRECT_INDICATOR))
				elif row[i]:
					wrong_answers.append(row[i])

			question: Question = Question(row[COL_QUESTION_TEXT], correct_answers, wrong_answers)

			bank.append(question.to_dict())
			topic_list[stripped_name] += 1

		csv_file.close()
	
	# Write bank
	with open(BUILD_DIR + "/" + stripped_name + ".json", "w") as out:
		out.write(json.dumps(bank))


# Create topics file
with open(BUILD_DIR + "/_topics.json", "w") as out:
	out.write(json.dumps(topic_list))

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
	answer: str
	false_answers = []

	def __init__(self, question: str, answer: str, wrong_answers: list):
		self.false_answers = []
		if len(question) * len(answer) < 1:
			raise ValueError("question and answer length must be >0")
		
		self.question = question
		self.answer = answer

		if len(wrong_answers) < 1 or len(wrong_answers) > 3:
			raise ValueError("# of wrong answers must be 1<n<3")
		
		for wa in wrong_answers:
			if len(wa) < 1:
				raise ValueError("wrong answer length must be >0")
			
			self.false_answers.append(wa)
	
	def to_dict(self):
		return {
			"question": self.question,
			"answer": self.answer,
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
		csv_reader = csv.DictReader(csv_file, dialect="excel")

		for row in csv_reader:
			wrong_answers = list(filter(lambda x: x, [row["FalseAnswer" + str(key_index)] for key_index in range(1, 4)]))
			question: Question = Question(row["Question"], row["Answer"], wrong_answers)

			bank.append(question.to_dict())
			topic_list[stripped_name] += 1

		csv_file.close()
	
	# Write bank
	with open(BUILD_DIR + "/" + stripped_name + ".json", "w") as out:
		out.write(json.dumps(bank))


# Create topics file
with open(BUILD_DIR + "/_topics.json", "w") as out:
	out.write(json.dumps(topic_list))

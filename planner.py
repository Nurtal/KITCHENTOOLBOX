"""
Planner
"""

import random

def select_random_receipe():
	"""
	-> Select a random receipe from index file
	"""

	# Count thenumber of lines
	index_data = open("receipe/index.txt", "r")
	number_of_lines = 0
	for line in index_data:
		number_of_lines +=1
	index_data.close()

	# make a choice
	receipe = "undef"
	choice = random.randint(0,number_of_lines)

	# Find the line corresponding to choice
	cmpt = 0
	index_data = open("receipe/index.txt", "r")
	for line in index_data:
		if(cmpt == choice):
			receipe = line.replace("\n", "")
		cmpt += 1
	index_data.close()

	return receipe


def generate_suggestion():
	"""
	-> Generate a suggestion for the week,
	   write the plannification in a csv file
	-> return a dict with the suggestions
	"""

	# Variables instanciation
	dinner_list = ["Lundi_midi", "Lundi_soir",
				   "Mardi_midi", "Mardi_soir",
				   "Mercredi_midi", "Mercredi_soir",
				   "Jeudi_midi", "Jeudi_soir",
				   "Vendredi_midi", "Vendredi_soir",
				   "Samedi_midi", "Samedi_soir",
				   "Dimanche_midi", "Dimanche_soir"]
	problem_to_solution = {}

	# Create the Suggestion
	for problem in dinner_list:
		solution = "undef"
		solution_not_found = True
		while(solution_not_found):
			solution = select_random_receipe()
			if(solution not in problem_to_solution.values() and solution != "undef"):
				problem_to_solution[problem] = solution
				solution_not_found = False

	# Write the suggestion in a csv file
	result_file = open("suggestion.csv", "w")
	for occasion in problem_to_solution:
		result_file.write(str(occasion)+";"+str(problem_to_solution[occasion])+"\n")
	result_file.close()

	# return the dict
	return problem_to_solution

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
			receipe = receipe.split(",")
			receipe = receipe[0]
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


def write_list_of_ingredients():
	##
	## Prepare a list of ingredients
	## from the suggestion file
	##

	## init result file
	output = open("listeDesCourses.txt", "w")
	output.close()

	## init data structure
	ingredients_to_quantity = {}

	## open suggestion file
	suggestion_file = open("suggestion.csv", "r")
	for line in suggestion_file:
		line = line.replace("\n", "")

		suggestion_line_in_array = line.split(";")

		receipe_name = suggestion_line_in_array[1]
		receipe_file = "undef"

		## get receipe file name from index file
		index_file = open("receipe/index.txt", "r")
		for index_line in index_file:
			index_line = index_line.replace("\n", "")
			line_in_array = index_line.split(",")
			index_receipe_name = line_in_array[0]
			if(str(index_receipe_name) == str(receipe_name)):
				receipe_file = line_in_array[1]
		index_file.close()

		## get ingredients for the receipe 
		receipe_data = open("receipe/"+str(receipe_file), "r")
		for receipe_line in receipe_data:
			receipe_line = receipe_line.replace("\n", "")
			receipe_line_in_array = receipe_line.split(",")

			ingredients = receipe_line_in_array[0]
			quantity = receipe_line_in_array[1]

			if(ingredients in ingredients_to_quantity.keys()):
				ingredients_to_quantity[ingredients] += int(quantity)
			else:
				ingredients_to_quantity[ingredients] = int(quantity)

		receipe_data.close()
	suggestion_file.close()

	## Write liste des courses
	output = open("listeDesCourses.txt", "w")
	for key in ingredients_to_quantity.keys():
		output.write(str(key)+"\t"+str(ingredients_to_quantity[key])+"\n")
	output.close()
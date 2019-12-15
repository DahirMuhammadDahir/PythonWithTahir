
def my_sum(list_of_numbers):
	result = 0
	for number in list_of_numbers:
		result += number

	return result

def my_average(list_of_numbers):
	total = my_sum(list_of_numbers)
	count = len(list_of_numbers)

	average = total / count
	return average

scores = [10, 9, 8, 20, 30]
final_average = my_average(scores)
print(final_average)
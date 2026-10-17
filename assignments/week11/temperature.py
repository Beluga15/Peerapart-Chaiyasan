"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():

 temps_list = [24,25,26,26,29,30,22]

 return temps_list

def analyze_temps(temps_list):

 min_temp = min(temps_list)

 max_temp = max(temps_list)

 average_temp = sum(temps_list) / len(temps_list)

 tuple_temp = (average_temp,max_temp,min_temp)

 return tuple_temp

def display_analysis(avg, high, low):

 print("Temperature Analysis for the Week:")

 print("Average: %.1f C" % avg)

 print(f"Highest: {high:.1f} C")

 print("Lowest: {} C".format(low))

input = get_temperatures()

result = analyze_temps(input)

display_analysis(result[0],result[1],result[2])
 
    
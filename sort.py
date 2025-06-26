#Dictionaries to be sorted

students = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"},
    {"name": "David", "age": 25, "city": "Berlin"},
]

#Manual Implementation using Lambda functions
def sort_dictionaries_manual(list_of_dicts, key_to_sort_by):
   
    return sorted(list_of_dicts, key=lambda x: x[key_to_sort_by])

# Example in use:
sorted_students_manual = sort_dictionaries_manual(students, "age")
print("Manual Sort (with lambda):", sorted_students_manual)

# Secondary sorting in case of ties (e.g., by name if ages are the same)
def sort_dictionaries_manual_multi_key(list_of_dicts, primary_key, secondary_key):
    
    return sorted(list_of_dicts, key=lambda x: (x[primary_key], x[secondary_key]))

sorted_students_manual_multi = sort_dictionaries_manual_multi_key(students, "age", "name")
print("Manual Multi-key Sort (with lambda):", sorted_students_manual_multi)


#AI Recommended Code 
import operator

def sort_dictionaries_ai(list_of_dicts, key_to_sort_by):
    
    return sorted(list_of_dicts, key=operator.itemgetter(key_to_sort_by))

# Example usage:
sorted_students_ai = sort_dictionaries_ai(students, "age")
print("AI Suggestion Sort (with itemgetter):", sorted_students_ai)

# AI suggestion for multiple keys:
def sort_dictionaries_ai_multi_key(list_of_dicts, primary_key, secondary_key):
    
    return sorted(list_of_dicts, key=operator.itemgetter(primary_key, secondary_key))

sorted_students_ai_multi = sort_dictionaries_ai_multi_key(students, "age", "name")
print("AI Multi-key Sort (with itemgetter):", sorted_students_ai_multi)
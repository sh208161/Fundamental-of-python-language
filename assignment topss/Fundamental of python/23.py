original_string = input("Enter the original string: ")
insert_string = input("Enter the string to insert: ")

middle_index = len(original_string) // 2

new_string = original_string[:middle_index] + insert_string + original_string[middle_index:]

print("Modified string:", new_string)
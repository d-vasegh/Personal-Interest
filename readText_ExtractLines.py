def extract_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                if "interested text" in line or "something else" in line:
                    f_out.write(line)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Replace 'input_file.txt' and 'output_file.txt' with your desired file paths.
input_file_path = r'C:\\Users\\username\\Projects\\lmgrd9.log'
output_file_path = r'C:\\Users\\username\\Projects\\output_file.txt'
extract_lines(input_file_path, output_file_path)
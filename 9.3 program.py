file_path="output.txt"
with open(file_path,"a") as file:
    file.write("\n this is an additional line.")
    print("context x appended to",file_path)

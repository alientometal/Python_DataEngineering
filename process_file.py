
def process_file(source_path, target_path):
    
    # open the file
    with open(source_path, "r") as file_handler:

        processed_rows = []
        header = file_handler.readline()
        header = header.upper()
        header = header.strip().split(",")
        header.append('"MEDIAN_AGE_HOUSE_VALUE_RATIO"')
        header = ",".join(header) + "\n"

        processed_rows.append(header)

        for row in file_handler.readlines():
            row = row.strip().split(",")
            row[2] = str(int(float(row[2])))
            row.append(str(float(row[2]) / float(row[8]) * 100))
            row = ",".join(row) + "\n"
            processed_rows.append(row)

    with open(target_path, "w") as target_file_handler:
        # Write to the file
        target_file_handler.writelines(processed_rows)


def main():

    source_path = "sample_data\california_housing_test.csv"
    target_path = "sample_data\california_housing_test_cp.csv"
    print("Processing file " + source_path)
    process_file(source_path, target_path)
    print("File processing finished")
    
    
if __name__ == "__main__":
    main()

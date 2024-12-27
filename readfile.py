def get_header(file_path, reading_mode="r"):
    
    # Open the file in read mode
    with open(file_path, reading_mode) as file_handler:
        breakpoint()
        # Read the contents of the file
        print(file_handler.readline())
        header = file_handler.read()
        return header.split("\n")[0]
        #print(type(header))



def main():
    
    file_path = "sample_data\california_housing_test.csv"
     
    # Do something to get the file_path
    get_header(file_path)
    
    
if __name__ == "__main__":
    main()
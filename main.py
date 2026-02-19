import pandas as pd


if __name__ == "__main__":

    # Checking the csv file using DataFarme
    products_df = pd.read_csv("lab1_data.csv", sep=";")
    print(products_df)
    
    

    print("=========================")
    # DATA PREPARATION 
    ## data cleansing
    # missing id x2 | names x2 | price missing, not available, negative, int .astype() | SEK x3 | dates format, missing, impossible 13th month
    # id
    missing_id = products_df["id"].isna()
    print(f"The number of Nan is: {missing_id.sum()}")
    print(f"To be found at: {products_df[products_df['id'].isna()].index}")
    print(missing_id)
    print("222========================")



    print("==========================")

    # name, spaces, missig names + capital letters ***ask Kristoffer if this data is normally used for product pages as well and
    # then would need capitalized letters at the beginning?
    print(f"Printing with removed spaces:")
    products_df['name'] = products_df['name'].str.strip()
    print(products_df)
    print("========================")

    missing_name = products_df["name"].isna()
    print(f"The number of Nan-missing name is: {missing_name.sum()}")
    print(f"To be found at: {products_df[products_df['name'].isna()].index}")
    print(missing_name)
    print("=========================")

    


    


    
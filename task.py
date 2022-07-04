"""
Given the database connection, complete the following:

1. Read the duplicate_items table to a DataFrame
2. Remove duplicate rows
3. Sort DataFrame by column2 ascending
4. Write the cleansed DataFrame to a new table unique_sorted_items
5. Read the item_attributes table to a DataFrame
6. Calculate which color dominates in the given items and print that color in the console
7. Calculate the total size of items (Sum of the items' size) and update the item_attributes table with the calculated column
8. Calculate the execution time of this program and print it in the console
9. Write a *single* query, which creates the items_count_by_size table with the items count by size

Notes:
    * All the functions can be modified and new ones can be created;
    * Good code readability will be considered as an advantage (reusable functions, clear variable names, simplistic code);
    * Result of this task is a private Github repository that contains 3 files: task.py, task.sqlite, task9.sql.;
    * Add @nerilau as a collaborator to Github repository;
    * If there are any questions regarding the task, contact nerijus.lauzadis@hostinger.com
"""

from pandas import DataFrame


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    import sqlite3
    conn = sqlite3.connect(db_file)

    return conn


def read_table_from_sqlite(table_name):
    """
    Function that reads the table to DataFrame

    :param str table_name: Database table name which is read
    :return DataFrame with the given table records
    """

    import pandas as pd 
    
    conn = create_connection("C:/Users/gabij/Downloads/de_task/de_task/task.sqlite")
    with conn:
        DataFrame = pd.read_sql_query("SELECT * from " + table_name, conn)
        #print(DataFrame)
        return DataFrame

    pass


def remove_duplicate_rows(df):
    """
    Function that removes duplicate from DataFrame

    :return: DataFrame with unique records
    """

    import pandas as pd 

    df1 = df.drop_duplicates()
    print(df1)

    return(df1)


    pass


def sort_rows(df, column_name, ASC):
    """
    Function that sorts DataFrame by column2 ascending

    :return: DataFrame with sorted rows
    """

    df1 = df.sort_values(by=column_name, ascending=ASC)
    return df1


    pass

def count_items_in_column(df, column_name):
    """
    Function that counts how many same items are in chosen column

    :return: item that is the most popular
    """
    df[column_name] = df[column_name].str.lower()
    #sum = df.pivot_table(columns=[column_name], aggfunc='size')
    
    print("Color(s) that is/are repeated the most: ", df[column_name].mode().values)
    
    return 


    pass


def calculate_total_and_add(df1, df2, new_column_name, group_column, calculate_column1, calculate_column2):
    """
    Function that calculates items with same item_id and adds a new column of the results

    :return: updated table with new calculated column
    """

    num = df1.groupby(group_column).count()
    df2[new_column_name] = df2[calculate_column2].reset_index(drop = True) * num[calculate_column1].reset_index(drop = True)
    
    return print(df2)

    pass


def elapsed_time(start, end):
    """
    Function that calculates elapsed time from marked start till marked finish

    :return: elapsed time
    """
    elapsed_time = end - start   

    return print('Execution time:', elapsed_time, 'seconds')  

    #pass


def main():
    """
    Main function which is executed during the runtime
    """
    import pandas as pd 
    import sqlite3
    import time

    start = time.time()

    #1. Read the duplicate_items table to a DataFrame
    duplicate_items1 = read_table_from_sqlite("duplicate_items")

    #2. Remove duplicate rows

    duplicate_items2 = remove_duplicate_rows(duplicate_items1)

    #3. Sort DataFrame by column2 ascending

    duplicate_items3 = sort_rows(duplicate_items2, "column2", 1)

    #4. Write the cleansed DataFrame to a new table unique_sorted_items

    unique_sorted_items = duplicate_items3

    #5. Read the item_attributes table to a DataFrame

    item_atributes = read_table_from_sqlite("item_attributes")

    #6. Calculate which color dominates in the given items and print that color in the console

    count_items_in_column(item_atributes, "color")

    #7. Calculate the total size of items (Sum of the items' size) and update the item_attributes table with the calculated column

    calculate_total_and_add(unique_sorted_items, item_atributes, "Sum of the items size", "id", "column2", "size")

    #8. Calculate the execution time of this program and print it in the console

    end = time.time()
    elapsed_time(start, end)

    pass


main()

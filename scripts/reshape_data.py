import pandas as pd

def main():
    # Path of the Excel file
    file_path = "data/03 processed/02readyToTransform.xlsx"

    # Step 1: Read the Excel file
    df = pd.read_excel(file_path)

    # Step 2: Reshape the data from wide to long format
    id_vars = df.columns[:10]  # Columns to keep as identifier variables
    value_vars = df.columns[10:]  # Columns to melt
    df_long = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name='Question', value_name='Answer')

    # Step 3: Save the reshaped data to a new Excel file
    output_file_path = "data/03 processed/03reshapedData.xlsx"
    df_long.to_excel(output_file_path, index=False)

    print("Reshaped data saved to:", output_file_path)

if __name__ == "__main__":
    main()
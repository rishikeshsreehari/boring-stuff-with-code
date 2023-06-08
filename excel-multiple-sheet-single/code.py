import pandas as pd

def load_sector_data(file_path, sheet_names):
    dataframes = []
    for i, sheet_name in enumerate(sheet_names):
        df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=3, header=2, usecols="B:ZZ", index_col=0)
        if i == 1:  # For sheet_names[3]
            df = df.iloc[:-2]  # Dropping last 2 rows for cleaning for sheet 2. Use as per the source data
        dataframes.append(df)
    return pd.concat(dataframes, axis=1)



def create_state_dataframe(state, sectors_data):
    state_data = {}
    for sector, data in sectors_data.items():
        sector_data = data.loc[state]
        state_data[sector] = sector_data.values
    state_df = pd.DataFrame(state_data, index=ind_df.columns)
    return state_df


ind_file = r"path\ind.xlsx"
agr_file = r"path\agr.xlsx"
ban_file = r"path\ban.xlsx"
ser_file = r"path\ser.xlsx"
man_file = r"path\man.xlsx"
con_file = r"path\cons.xlsx"

ind = pd.ExcelFile(ind_file)
agr = pd.ExcelFile(agr_file)
ban = pd.ExcelFile(ban_file)
ser = pd.ExcelFile(ser_file)
man = pd.ExcelFile(man_file)
con = pd.ExcelFile(con_file)

#Choosing sheets to process. Ignore if not required

ind_sheet_names = ind.sheet_names[2:4]  
agr_sheet_names = agr.sheet_names[2:4]
ban_sheet_names = ban.sheet_names[2:4]
ser_sheet_names = ser.sheet_names[2:4]
man_sheet_names = man.sheet_names[2:4]
con_sheet_names = con.sheet_names[2:4]


# Load sector data
ind_df = load_sector_data(ind_file, ind_sheet_names)
agr_df = load_sector_data(agr_file, agr_sheet_names)
ban_df = load_sector_data(ban_file, ban_sheet_names)
ser_df = load_sector_data(ser_file, ser_sheet_names)
man_df = load_sector_data(man_file, man_sheet_names)
con_df = load_sector_data(con_file, con_sheet_names)


output_path = r"path\output.xlsx"

excel_file = pd.ExcelWriter(output_path, engine='xlsxwriter')

# Iterate over each state
for state in agr_df.index:
    # Create a new sheet for the state
    sheet_name = state

    # Create a dictionary to hold sector data for the state
    sectors_data = {
        'Industry': ind_df,
        'Agriculture': agr_df,
        'Services': ser_df,
        'Banking': ban_df,
        'Manufacturing': man_df,
        'Construction': con_df
    }

    # Create a new DataFrame for the state sheet
    state_df = create_state_dataframe(state, sectors_data)
    state_df = state_df.transpose() #Remove this if you don't want to tranpose

    # Write the state DataFrame to the Excel file
    state_df.to_excel(excel_file, sheet_name=sheet_name)

# Save and close the Excel file
excel_file.save()
excel_file.close()

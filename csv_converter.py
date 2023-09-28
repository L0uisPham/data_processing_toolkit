import pandas as pd

read_file = pd.read_excel (".xlsx")
  
read_file.to_csv (".csv", 
                  index = None,
                  header=True)

df = pd.DataFrame(pd.read_csv(".csv"))
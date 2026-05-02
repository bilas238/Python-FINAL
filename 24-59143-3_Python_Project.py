import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  Data Loading 
#  load csv data
url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp_csv.csv"

def run_project():
    try:
        df = pd.read_csv(url)

        # Data Cleaning (Pandas)
        # keep colum and remove missing data
        
        df = df[['Country Name', 'Year', 'Value']].dropna()
        
        # filter 2026 data 
        
        df_2016 = df[df['Year'] == 2016].head(10)

        # Mathematical Operations (NumPy)
        # GDP Value in NumPy array
        
        gdp_values = np.array(df_2016['Value'])
        
        
        #to used numpy for average gdp
        
        avg_gdp = np.mean(gdp_values)
        
        print("--- Project Summary ---")
        print(f"Total Countries Analyzed: {len(df_2016)}")
        print(f"Average GDP (2016): {avg_gdp:.2f}\n")

        # Visualization (Matplotlib)
        
        plt.figure(figsize=(10, 6))
        
        # create a bar chart
        
        plt.bar(df_2016['Country Name'], df_2016['Value'], color='teal', alpha=0.7)
        
        # Graph label and title 
        
        plt.title('Top 10 Countries by GDP (2016)', fontsize=14)
        plt.xlabel('Country Name', fontsize=12)
        plt.ylabel('GDP Value', fontsize=12)
        plt.xticks(rotation=45) # Country-r naam gulo ektu baka kore deya jate pora jay
        
        plt.tight_layout()
        
        # save graph in image file
        
        plt.savefig('gdp_analysis_output.png')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_project()
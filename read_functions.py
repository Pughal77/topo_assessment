'''
Read functions for diff types. For visualisation of data we are to use matplot lib
'''
import pandas as pd
import tabula
from pptx import Presentation
'''
    This class represents the unified data structure I am to return
    Upon looking at the datasets, dataset 1 is about 2 sport and fitness companies
    dataset 3 is about quarterly revenue n stuff
    datset 4 represents the summary of performance
    for data visualisation, I think we could go about verifying the summaries for fitpro
    The unified data structure although it has 
'''
class Unified_data_structure:
    def __init__(self):
        self.data = {
            "dataset_1": None,
            "dataset_2": None,
            "dataset_3": None,
            "dataset_4": None
        }
        self.read_json("datasets/dataset1.json")
        self.read_csv("datasets/dataset2.csv")
        self.read_pdf("datasets/dataset3.pdf")
        self.read_pptx("datasets/dataset4.pptx")

    def read_json(self, filename) -> None:
        # data might be nested
        json_data = pd.read_json(filename)
        self.data['dataset_1'] = json_data

    def read_csv(self, filename) -> None:
        csv_data = pd.read_csv(filename)
        self.data['dataset_2'] = csv_data
    
    def read_pdf(self, filename) -> None:
        # use tabula
        # read and injest data from pdf
        dfs = tabula.read_pdf(filename, pages='all')
        # from checking what dfs returns, I see that it is a list with a single element
        # where dfs[0] is a pandas dataframe
        self.data['dataset_3'] = dfs[0]
        return None
    def read_pptx(self, filename) -> None:
        # convert to pdf then read pdf
        # will convert all the pptx files to pdf in specified dir
        # in this dataset we have a table in slide 2
        pptx = Presentation(filename)
        # after exploring the pptx object in python shell i found where table in slide 2 is stored
        table = pptx.slides[1].shapes[1].table
        # convert this table to a pandas dataframe
        data = []
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells]
            data.append(row_data)
        
        # Convert to Pandas DataFrame
        headers = data[0]  # Assume first row contains headers
        rows = data[1:]  # Remaining rows are data
        df = pd.DataFrame(rows, columns=headers)
        
        # as for the information in slide 1 and 3, I think its best if we manually keyed in the information
        self.data['dataset_4'] = df
        
    def unify(self, data):
        # take existing data and unify it with current
        return None
    
x = Unified_data_structure()
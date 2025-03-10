'''
Read functions for diff types. For visualisation of data we are to use matplot lib
'''
import pandas as pd

'''
    This class represents the unified data structure I am to return
    Upon looking at the datasets, dataset 1 is about 2 sport and fitness companies
    dataset 3 is about quarterly revenue n stuff
    datset 4 is
'''
class Unified_data_structure:
    def __init__(self):
        self.data = pd.DataFrame.empty()

    def read_json(filename) -> None:
        # data might be nested
        json_data = pd.read_json(filename)


    def read_csv(filename) -> None:
        result = pd.read_csv(filename)
    
    def read_pdf(filename) -> None:
        # use tabula
        return None
    def read_pptx(filename) -> None:
        # convert to pdf then read pdf
        # will convert all the pptx files to pdf in specified dir
    
    def unify(data):
        # take existing data and unify it with current
        return None
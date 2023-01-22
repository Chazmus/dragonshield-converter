import pandas
from pandas import DataFrame

"""
Dragon shield headers: Folder Name,Quantity,Trade Quantity,Card Name,Set Code,Set Name,Card Number,Condition,Printing,Language,Price Bought,Date Bought,LOW,MID,MARKET
Moxfield Headers: "Count","Tradelist Count","Name","Edition","Condition","Language","Foil","Tags","Last Modified","Collector Number","Alter","Proxy","Purchase Price"
"""


class MoxfieldConverter:

    def convert(self, dragonshield_data: DataFrame):
        return pandas.DataFrame(dragonshield_data.apply(self.map_function, axis=1).tolist())

    def map_function(self, row):
        return {
            "Name": row["Card Name"],
            "Count": row["Quantity"],
            "Edition": row["Set Code"],
            "Collector Number": row["Card Number"],
        }

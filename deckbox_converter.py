import pandas
from pandas import DataFrame

"""
Dragon shield headers: Folder Name,Quantity,Trade Quantity,Card Name,Set Code,Set Name,Card Number,Condition,Printing,Language,Price Bought,Date Bought,LOW,MID,MARKET
Deckbox headers: Count,Tradelist Count,Name,Edition,Card Number,Condition,Language,Foil,Signed,Artist Proof,Altered Art,Misprint,Promo,Textless,My Price

"""


class DeckboxConverter:

    def convert(self, dragonshield_data: DataFrame):
        return pandas.DataFrame(dragonshield_data.apply(self.map_function, axis=1).tolist())

    def map_function(self, row):
        return {
            "Name": row["Card Name"],
            "Count": row["Quantity"],
            "Card Number": row["Card Number"],
        }

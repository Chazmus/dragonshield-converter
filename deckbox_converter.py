import pandas
from pandas import DataFrame


class DeckboxConverter:

    def __init__(self):
        self.output_df = DataFrame({"Name": [], "Count": []})
        self.output_df["Count"] = self.output_df["Count"].astype(int)

    def convert(self, data: DataFrame):
        for index, row in data.iterrows():
            self.update_or_add(row["Card Name"], row["Quantity"])

        return self.output_df

    def update_or_add(self, card_name, quantity):
        if card_name in self.output_df["Name"]:
            # Card already exists, update count
            self.output_df.loc[self.output_df['Name'] == card_name, 'Count'] += quantity
        else:
            new_row = DataFrame({"Name": [card_name], "Count": [int(quantity)]})
            self.output_df = pandas.concat([self.output_df, new_row], ignore_index=True)
            # self.output_df = self.output_df.append({"Name": card_name, "Count": quantity}, ignore_index=True)

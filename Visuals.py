import pandas as pd
import os
import plotly.express as px


#ToDo: y-axis = 100% of mentions in all/the respective newspaper

class Visuals:
    def __init__(self):
        self.path = os.getcwd() + "/Data/"
        self.searchterms = pd.read_csv(self.path + "Base_Data/searchterms")["searchterms"].to_list()
        self.freq_table = pd.read_csv(self.path + "/Data_Visuals/mentions_absolute")
        self.parties = ["CDU/CSU","SPD","GRÜNE","FDP","LINKE","AFD"]

    def by_newspapers(self, searchterm:str):
        if searchterm not in self.searchterms + self.parties:
            print("Searchterm is not valid. Please check spelling.")
            return
        fig = px.line(self.freq_table, x='date', y=searchterm, color="newspaper")
        fig.update_xaxes(rangeslider_visible=True,)
        fig.show()

    def by_names(self, searchterms:list):
        for searchterm in searchterms:
            if searchterm not in self.searchterms + self.parties:
                print("Searchterm is not valid. Please check spelling.")
                return
        self.total_table = self.freq_table.groupby("date", as_index=False).sum()
        fig = px.line(self.total_table, x='date', y=searchterms)
        fig.update_xaxes(rangeslider_visible=True,)
        fig.show()


if __name__ == "__main__":
    vis = Visuals()
    vis.by_names(["CDU/CSU","SPD","GRÜNE","FDP","LINKE","AFD", "Laschet", "Scholz", "Merkel"])
    vis.by_newspapers("Baerbock")

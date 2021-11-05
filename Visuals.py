import pandas as pd
import os
import plotly.express as px

class Visuals:
    def __init__(self):
        self.path = os.getcwd() + "/Data/"
        self.searchterms = pd.read_csv(self.path + "Base_Data/searchterms")["searchterms"].to_list()
        self.absolute_count = pd.read_csv(self.path + "/Data_Visuals/mentions_absolute")
        self.relative_count = pd.read_csv(self.path + "/Data_Visuals/mentions_relative")
        self.parties = ["CDU/CSU","SPD","GRÜNE","FDP","LINKE","AFD"]

    def individual_count(self, searchterm:str, relative = True):
        if searchterm not in self.searchterms + self.parties:
            print("Searchterm is not valid. Please check spelling.")
            return
        if relative:
            freq_table = self.relative_count
        else:
            freq_table = self.absolute_count
        m = "Relative" if relative else "Absolute"
        t = m + " mentions of " + searchterm + " over time."
        y = "Percent" if relative else "Count"
        fig = px.line(freq_table, x='date', y=searchterm, color="newspaper")
        fig.update_layout(
            title=t,
            xaxis_title="Date",
            yaxis_title=y,
            legend_title="Newspaper",
            font=dict(
                size=16,
                color="Black"
            )
        )
        fig.update_xaxes(rangeslider_visible=True,)
        fig.show()

    def multiple_count(self, searchterms:list, relative=True):
        for searchterm in searchterms:
            if searchterm not in self.searchterms + self.parties:
                print("Searchterm is not valid. Please check spelling.")
                return
        if relative:
            freq_table = self.relative_count.groupby("date", as_index=False).mean()
        else:
            freq_table = self.absolute_count.groupby("date", as_index=False).sum()
        m = "Relative" if relative else "Absolute"
        t = m + " mentions of " + ", ".join(searchterms) + " over time."
        y = "Percent" if relative else "Count"
        fig = px.line(freq_table, x='date', y=searchterms)
        fig.update_layout(
            title=t,
            xaxis_title="Date",
            yaxis_title=y,
            legend_title="Politicians",
            font=dict(
                size=16,
                color="Black"
            )
        )
        fig.update_xaxes(rangeslider_visible=True,)
        fig.show()

    def party_count(self, relative = True):
        if relative:
            freq_table = self.relative_count.groupby("date", as_index=False).mean()
        else:
            freq_table = self.absolute_count.groupby("date", as_index=False).sum()
        m = "Relative" if relative else "Absolute"
        t = m + " mentions of German Parties over time."
        y = "Percent" if relative else "Count"
        fig = px.line(freq_table, x='date', y=self.parties)
        fig.update_layout(
            title=t,
            xaxis_title="Date",
            yaxis_title=y,
            legend_title="Parties",
            font=dict(
                size=16,
                color="Black"
            )
        )
        fig.update_xaxes(rangeslider_visible=True,)
        fig.show()


if __name__ == "__main__":
    vis = Visuals()
    vis.individual_count("Merkel")
    vis.multiple_count(["Scholz", "Laschet", "Baerbock"])
    vis.multiple_count(["Scholz", "Laschet", "Baerbock"],False)
    vis.party_count()

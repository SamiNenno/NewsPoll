import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Visuals:
    def __init__(self):
        self.path = os.getcwd() + "/Data/"
        self.searchterms = pd.read_csv(self.path + "Base_Data/searchterms")["searchterms"].to_list()
        self.absolute_count = pd.read_csv(self.path + "/Data_Visuals/mentions_absolute")
        self.relative_count = pd.read_csv(self.path + "/Data_Visuals/mentions_relative")
        self.poll = pd.read_csv(self.path + "/Data_Visuals/polls")
        self.parties = ["CDU/CSU", "SPD", "GRÜNE", "LINKE", "FDP", "AFD"]

    def individual_count(self, searchterm: str, relative: bool = True):
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

    def multiple_count(self, searchterms:list, relative:bool = True):
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

    def party_count(self, relative:bool = True):
        if relative:
            freq_table = self.relative_count.groupby("date", as_index=False).mean()
        else:
            freq_table = self.absolute_count.groupby("date", as_index=False).sum()
        m = "Relative" if relative else "Absolute"
        t = m + " mentions of German Parties over time."
        y = "Percent" if relative else "Count"
        fig = px.line(freq_table, x='date', y=self.parties,
                      color_discrete_sequence=["black", "red", "green", "pink", "yellow", "blue"])
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

    def plot_poll(self):
        vis_pol = self.poll.groupby("published", as_index=False).mean()
        fig = px.line(vis_pol, x='published', y=["CDU/CSU","SPD","GRÜNE","LINKE","FDP","AFD","SONSTIGE"],
                      color_discrete_sequence=["black", "red", "green", "pink", "yellow", "blue", "grey"])
        fig.update_layout(
            title="Poll results",
            xaxis_title="Date",
            yaxis_title="Percent",
            legend_title="Parties",
            font=dict(
                size=16,
                color="Black"
            )
        )
        fig.update_xaxes(rangeslider_visible=True, )
        fig.show()

    def compare_party_count(self):
        news_count = self.relative_count.groupby("date", as_index=False).mean()
        poll_count = self.poll.groupby("published", as_index=False).mean()
        colors = ["black", "red", "green", "pink", "yellow", "blue"]
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        for idx, party in enumerate(self.parties):
            trace1 = go.Scatter(
                x=news_count["date"],
                y=news_count[party],
                name=party,
                marker_color = colors[idx]
            )
            trace2 = go.Scatter(
                x=poll_count["published"],
                y=poll_count[party],
                name=party,
                marker_color = colors[idx],
                line={"dash" : "dot"},
                yaxis='y2'
            )

            fig.add_trace(trace1, secondary_y=False)
            fig.add_trace(trace2, secondary_y=False)
        fig.update_xaxes(rangeslider_visible=True, )
        fig.update_layout(
            title="Comparison of newspaper mentions and poll results for German parties",
            xaxis_title="Date",
            yaxis_title="Percent",
            legend_title="— Newspaper / -- Poll",
            font=dict(
                size=16,
                color="Black"
            )
        )
        fig.show()

    def compare_individual_count(self, politician:str, party:str):
        news_count = self.relative_count.groupby("date", as_index=False).mean()
        poll_count = self.poll.groupby("published", as_index=False).mean()
        colors = {"CDU/CSU":"black", "SPD":"red", "GRÜNE":"green", "LINKE":"pink", "FDP":"yellow", "AFD":"blue"}
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        trace1 = go.Scatter(
            x=news_count["date"],
            y=news_count[politician],
            name=politician,
            marker_color="grey"
        )
        trace2 = go.Scatter(
            x=poll_count["published"],
            y=poll_count[party],
            name=party,
            marker_color=colors[party],
            line={"dash": "dot"}
        )

        fig.add_trace(trace1, secondary_y=False)
        fig.add_trace(trace2, secondary_y=True)
        fig.update_xaxes(rangeslider_visible=True, )
        fig.show()

if __name__ == "__main__":
    vis = Visuals()
    #vis.individual_count("Merkel")
    #vis.multiple_count(["Scholz", "Laschet", "Baerbock"])
    #vis.multiple_count(["Scholz", "Laschet", "Baerbock"],False)
    #vis.party_count()
    #vis.plot_poll()
    vis.compare_party_count()
    #vis.compare_individual_count("Baerbock", "GRÜNE")
    #vis.compare_individual_count("Scholz", "SPD")
    #vis.compare_individual_count("Laschet", "CDU/CSU")
    #vis.test()
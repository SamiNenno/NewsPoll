import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Visuals:
    '''
    Class for visualising the mentions of politicians/parties
    in the newspapers and poll results
    '''
    def __init__(self):
        self.path = os.getcwd() + "/Data/"
        self.searchterms = pd.read_csv(self.path + "Base_Data/searchterms")["searchterms"].to_list()
        self.absolute_count = pd.read_csv(self.path + "/Data_Visuals/mentions_absolute")
        self.relative_count = pd.read_csv(self.path + "/Data_Visuals/mentions_relative")
        self.relative_count.iloc[:, 2:] = self.relative_count.iloc[:,2:]*100
        self.poll = pd.read_csv(self.path + "/Data_Visuals/polls")
        self.parties = ["CDU/CSU", "SPD", "GRÜNE", "LINKE", "FDP", "AFD"]

    def individual_count(self, searchterm: str, relative: bool = True):
        '''
        Plots a single politician against their poll results

        :param searchterm: What politician mention/poll result is to be plotted
        :param relative: Mentions in absolute or relative format
        :return: Plot of the aforementioned parameters
        '''
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
        '''
        Plots multiple politicians against their poll results

        :param searchterms: What politicians mention/poll result is to be plotted
        :param relative: Mentions in absolute or relative format
        :return: Plot of the aforementioned parameters
        '''
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
        '''
        Plots party mentions (= sum of mentions of all politicians belonging to the same party).

        :param relative: Mentions in absolute or relative format
        '''
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
        '''
        Plots poll results of parties
        '''
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
        '''
        Plots party newspaper mentions against poll results
        '''
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
        '''
        Plots single politician's newspaper mentions against party poll results

        :param politician: Individual politician
        :param party: Individual party
        '''
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
        t = politician + " newspaper mentions vs. " + party + " poll results"
        fig.update_layout(
            title=t,
            xaxis_title="Date",
            yaxis_title="Percent",
            legend_title="— Newspaper / -- Poll",
            font=dict(
                size=16,
                color="Black"
            )
        )
        fig.show()

if __name__ == "__main__":
    vis = Visuals()
    #vis.individual_count("Merkel")
    vis.multiple_count(["Laschet", "Scholz", "Baerbock"])
    #vis.party_count()
    #vis.plot_poll()
    #vis.compare_party_count()
    #vis.compare_individual_count("Baerbock", "GRÜNE")
    #vis.compare_individual_count("Scholz", "SPD")
    #vis.compare_individual_count("Laschet", "CDU/CSU")
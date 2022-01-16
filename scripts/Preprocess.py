import sys
import pandas as pd
import os
import pendulum
import json
import requests
import numpy as np
from flashtext import KeywordProcessor

class Poll():
    '''
    Scrapes or loads poll data and saves it.

    :param
    refresh (bool): If true, new poll data is scraped, otherwise existing data is loaded.
    path (str): path to current directory
    '''
    ## Poll Data is retrieved from https://dawum.de/
    def __init__(self, refresh = True, path="None"):
        print("Load poll data...\n")
        self.refresh = refresh
        self.url = "https://api.dawum.de/"
        self.path = os.getcwd()+"/Data/" if path=="None" else path

        if self.refresh is True:
            self.poll_data = requests.get(self.url).json()
            with open(self.path+"Base_Data/poll_data.json", "w+") as f:
                json.dump(self.poll_data, f)
        else:
            with open(self.path+"Base_Data/poll_data.json") as f:
                self.poll_data = json.load(f)
        self.poll_dict = {
            "published": [],
            "start": [],
            "end": [],
            "persons": [],
            "parliament": [],
            "institute": [],
            "SPD": [],
            "CDU/CSU": [],
            "CDU": [],
            "CSU": [],
            "GRÜNE": [],
            "FDP": [],
            "LINKE": [],
            "AFD": [],
            "SONSTIGE": [],
        }
        ## Each Parliament (Bundestag, Berlin, Thüringen) has a ID from 0 to 16.
        ## E.g. self.parliaments["0"] = {'Shortcut': 'Bundestag', 'Name': 'Bundestag', 'Election': 'Bundestagswahl'}
        self.parliaments = self.poll_data["Parliaments"]

        ## Institute which conducted the survey.
        ## E.g. self.poll_data["Institutes"]["1"] = {'Name': 'Infratest dimap'}
        self.institutes = self.poll_data["Institutes"]

        ## Parties
        ## E.g. self.parties["4"] = {'Shortcut': 'Grüne', 'Name': 'Bündnis 90/Die Grünen'}
        self.parties = self.poll_data["Parties"]

        ## Results and information about the surveys
        ## E.g self.surveys["2192"] = {
        # 'Date': '2021-10-06',
        # 'Survey_Period': {'Date_Start': '2021-09-29', 'Date_End': '2021-10-06'},
        # 'Surveyed_Persons': '10009',
        # 'Parliament_ID': '0',
        # 'Institute_ID': '16',
        # 'Tasker_ID': '14',
        # 'Results': {'2': 28, '1': 19, '4': 15, '3': 14, '7': 11, '0': 7, '5': 6}
        # }
        self.surveys = self.poll_data["Surveys"]

    def parse_poll(self):
        '''
        Parses poll data and returns it as dataframe

        :return: poll_frame (pd.DataFrame): dataframe containing poll results
        '''
        party_to_number = {}
        number_to_parliament = {}
        number_to_institute = {}
        for key, value in self.parties.items():
            party_to_number[value["Shortcut"]] = key
        for key, value in self.parliaments.items():
            number_to_parliament[key] = value["Shortcut"]
        for key, value in self.institutes.items():
            number_to_institute[key] = value["Name"]

        for key, value in self.surveys.items():
            self.poll_dict["published"].append(value["Date"])
            period = value["Survey_Period"]
            self.poll_dict["start"].append(period["Date_Start"])
            self.poll_dict["end"].append(period["Date_End"])
            self.poll_dict["persons"].append(value["Surveyed_Persons"])
            self.poll_dict["parliament"].append(number_to_parliament[value["Parliament_ID"]])
            self.poll_dict["institute"].append(number_to_institute[value["Institute_ID"]])
            results = value["Results"]
            try:
                self.poll_dict["SPD"].append(results[party_to_number["SPD"]])
            except KeyError:
                self.poll_dict["SPD"].append("No.Result")
            try:
                self.poll_dict["SONSTIGE"].append(results[party_to_number["Sonstige"]])
            except KeyError:
                self.poll_dict["SONSTIGE"].append("No.Result")
            try:
                self.poll_dict["FDP"].append(results[party_to_number["FDP"]])
            except KeyError:
                self.poll_dict["FDP"].append("No.Result")
            try:
                self.poll_dict["LINKE"].append(results[party_to_number["Linke"]])
            except KeyError:
                self.poll_dict["LINKE"].append("No.Result")
            try:
                self.poll_dict["CSU"].append(results[party_to_number["CSU"]])
            except KeyError:
                self.poll_dict["CSU"].append("No.Result")
            try:
                self.poll_dict["CDU"].append(results[party_to_number["CDU"]])
            except KeyError:
                self.poll_dict["CDU"].append("No.Result")
            try:
                self.poll_dict["GRÜNE"].append(results[party_to_number["Grüne"]])
            except KeyError:
                self.poll_dict["GRÜNE"].append("No.Result")
            try:
                self.poll_dict["CDU/CSU"].append(results[party_to_number["CDU/CSU"]])
            except KeyError:
                self.poll_dict["CDU/CSU"].append("No.Result")
            try:
                self.poll_dict["AFD"].append(results[party_to_number["AfD"]])
            except KeyError:
                self.poll_dict["AFD"].append("No.Result")

        self.poll_frame = pd.DataFrame.from_dict(self.poll_dict)

    def select_relevant_polls(self):
        '''
        Excludes poll data from before June 2021

        :return: reduced_poll_frame (pd.DataFrame): dataframe with poll data starting from June 2021
        '''
        earliest_date = pendulum.parse("06.01.2021", strict=False).format("YYYY-MM-DD")
        self.poll_frame["published"] = self.poll_frame.apply(lambda row: pendulum.parse(row["published"], strict=False).format("YYYY-MM-DD"), axis=1)
        self.reduced_poll_frame = self.poll_frame[(self.poll_frame["published"] > earliest_date) & (self.poll_frame["parliament"] == "Bundestag")]
        self.reduced_poll_frame = self.reduced_poll_frame.drop(columns=['CDU', 'CSU'])

    def fit(self):
        '''
        Clusters all functions and calls them in right order.

        :return: Final poll data as .csv file
        '''
        self.parse_poll()
        self.select_relevant_polls()
        self.poll_frame.to_csv(self.path+"Base_Data/poll_table", index=False)
        self.reduced_poll_frame.to_csv(self.path + "Data_Visuals/polls", index=False)

class Keywords():
    '''
    Creates list of keywords of politicians and parties

    :param: path (str): path to current directory
    '''
    def __init__(self, path="None"):
        print("Create searchterms...\n")
        self.path = os.getcwd()+"/Data/" if path=="None" else path
        self.abgeordnete = pd.read_csv(self.path + "Base_Data/abgeordnete_total")
        self.manual = pd.read_csv(self.path + "Base_Data/manual_keywords")
        self.search_terms = []
        self.party_dict = {"CDU/CSU":[], "SPD":[], "GRÜNE":[], "FDP":[], "LINKE":[], "AFD":[]}

    def create_searchterms(self):
        '''
        Assigns searchterm to their respective political party.

        :return: party_dict (dict): key is party name, value is list of respective searchterms.
        '''
        manual_list = self.manual["Keyword"].to_list()
        abgeordnete_list = self.abgeordnete["Name"].to_list()
        party_list = self.abgeordnete["Fraktion"].to_list()
        self.party_dict["CDU/CSU"] += manual_list[:8]
        self.party_dict["SPD"] += manual_list[8:11]
        self.party_dict["GRÜNE"] += manual_list[11:15]
        self.party_dict["LINKE"] += manual_list[15:18]
        self.party_dict["AFD"] += manual_list[18:21]
        self.party_dict["FDP"] += manual_list[21:24]
        self.search_terms += manual_list[:24]
        for idx, abgeordnet in enumerate(abgeordnete_list):
            name = ""
            for manuell in manual_list[24:]:
                if manuell in abgeordnet.split() and abgeordnet != "Tobias Lindner":
                    name = manuell
                    break
                else:
                    name = abgeordnet
            self.search_terms.append(name)
            if party_list[idx] == "AfD" or party_list[idx] == "fraktionslos (AfD)":
                self.party_dict["AFD"].append(name)
            if party_list[idx] == "CDU/CSU (CDU)" or party_list[idx] == "CDU" or party_list[idx] == "CSU":
                self.party_dict["CDU/CSU"].append(name)
            if party_list[idx] == "FDP":
                self.party_dict["FDP"].append(name)
            if party_list[idx] == "Grüne":
                self.party_dict["GRÜNE"].append(name)
            if party_list[idx] == "Linke":
                self.party_dict["LINKE"].append(name)
            if party_list[idx] == "SPD":
                self.party_dict["SPD"].append(name)


    def save_searchterms(self):
        '''
        Saves searchterms as .csv file.
        :return:
        searchterms (csv): csv file of individual searchterms
        party_searchterms (csv): csv file of searchterms for parties
        '''
        pd.DataFrame({"searchterms": self.search_terms}).to_csv(
            self.path+"Base_Data/searchterms", index=False)
        pd.DataFrame(dict([(k, pd.Series(v)) for k, v in self.party_dict.items()])).to_csv(
            self.path+"Base_Data/party_searchterms", index=False)

    def fit(self):
        '''
        Clusters all functions and calls them in right order.

        :return: Final poll data as .csv file
        '''
        self.create_searchterms()
        self.save_searchterms()


class Relevance:
    '''
    Searches newscorpus for articles that contain searchwords.

    :param: path (str): path to current directory
    '''
    def __init__(self, path="None"):
        self.path = os.getcwd()+"/Data/" if path=="None" else path
        ## Note that the newscollection is not uploaded to Github
        ## Right now (10.01.2022) it contains 92.087 aricles
        self.newscollection = pd.read_csv(self.path + "Newscollection/NewsCollection.csv")
        self.newscollection["Contains.Keyword"] = np.nan
        self.searchterms = pd.read_csv(self.path+"Base_Data/searchterms")["searchterms"].to_list()
        self.searchterm_dict = {}
        self.create_search_dict()
        self.keyword_processor = KeywordProcessor()
        self.keyword_processor.add_keywords_from_dict(self.searchterm_dict)

    def create_search_dict(self):
        '''
        Adds genitiv "s" to searchterms.
        :return: searchterm_dict (dict): dictionary of searchterms and searchterms with genitiv "s".
        '''
        for searchterm in self.searchterms:
            self.searchterm_dict[searchterm] = [searchterm, searchterm+"s"]

    def search(self):
        '''
        Searches newscorpus for articles containg at least one searchterm.

        :return: newscollection (pd.DataFrame): dataframe containing all articles and marker if they contain a searchterm.
        '''
        print("Select articles that contain searchterm...")
        for idx, article in enumerate(self.newscollection.itertuples(index=False, name=None)):
            if type(article[3]) is str:
                keywords = self.keyword_processor.extract_keywords(article[3])
                if keywords:
                    print(f"Match in: {article[0]} from {article[6]}")
                    self.newscollection.loc[idx,"Contains.Keyword"] = True
                else:
                    self.newscollection.loc[idx,"Contains.Keyword"] = False
            else:
                continue

    def save_checked_newcollection(self):
        '''
        Saves articles that contain at least one searchterm.

        :return: articles (csv): csv file containing all articles that contain at least one searchterm.
        '''
        self.newscollection[self.newscollection["Contains.Keyword"] == True].to_csv(
            self.path + "Newscollection/articles.csv", index=False)

    def fit(self):
        '''
        Clusters all functions and calls them in right order.

        :return: Final poll data as .csv file
        '''
        self.search()
        self.save_checked_newcollection()

class Frequency_Table():
    '''
    Saves a csv file with proper shape for searchterm frequencies.

    :param: path (str): path to current directory
    '''
    def __init__(self, path="None"):
        print("Create empty frame for mentions count...\n")
        self.path = os.getcwd() + "/Data/" if path == "None" else path
        self.newscollection = pd.read_csv(self.path+"Newscollection/articles.csv")
        self.searchterms = pd.read_csv(self.path+"Base_Data/searchterms")
        self.date = np.array([date if type(date) is str else "No.Date" for date in pd.unique(self.newscollection["date"])])
        self.newspaper = pd.unique(self.newscollection["newspaper"])

    def compute_table_shape(self):
        '''
        Computes shape of csv file for searchterm frequency.

        :return: frequency_table (pd.DataFrame): empty dataframe with right shape for saving searchterm frequency.
        '''
        date_col = np.repeat(self.date, self.newspaper.shape[0])
        newspapers_col = np.tile(self.newspaper, self.date.shape[0])
        count_col = np.zeros(newspapers_col.shape[0])
        table = {
            "date": date_col,
            "newspaper": newspapers_col
        }
        for searchterm in self.searchterms["searchterms"].to_list():
            table[searchterm] = count_col
        self.frequency_table = pd.DataFrame.from_dict(table)

    def save_table(self):
        '''
        Saves empty dataframe for searchterm frequencies.

        :return: searchterm_mentions_count (csv): empty dataframe for searchterm frequencies
        '''
        self.frequency_table.to_csv(self.path+"Base_Data/searchterm_mentions_count", index=False)

    def fit(self):
        '''
        Clusters all functions and calls them in right order.

        :return: Final poll data as .csv file
        '''
        self.compute_table_shape()
        self.save_table()


if __name__ == "__main__":
    poll = Poll()
    poll.fit()
    keywords = Keywords()
    keywords.fit()
    rel = Relevance()
    rel.fit()
    freq = Frequency_Table()
    freq.fit()





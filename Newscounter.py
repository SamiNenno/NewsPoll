import pandas as pd
import os
from collections import Counter
from flashtext import KeywordProcessor
import pendulum


class Newscounter:
    def __init__(self):
        print("Initiate Newscounter...\n")
        self.path = os.getcwd() + "/Data/"
        self.newscollection = \
            pd.read_csv(self.path+"Newscollection/articles.csv")
        self.searchterms = \
            pd.read_csv(self.path+"Base_Data/searchterms")["searchterms"].to_list()
        self.party_searchterms = \
            pd.read_csv(self.path+"Base_Data/party_searchterms")
        self.freq_table = \
            pd.read_csv(self.path+"Base_Data/searchterm_mentions_count")
        self.newspaper = 0
        self.content = 3
        self.date = 6
        self.searchterm_dict = {}
        self.create_search_dict()
        self.keyword_processor = KeywordProcessor()
        self.keyword_processor.add_keywords_from_dict(self.searchterm_dict)

    def create_search_dict(self):
        for searchterm in self.searchterms:
            self.searchterm_dict[searchterm] = [searchterm, searchterm + "s"]

    def count(self):
        print("Start counting...\n")
        for idx, article in enumerate(self.newscollection.itertuples(index=False, name=None)):
            date = article[self.date] if type(article[self.date]) is str else "No.Date"
            newspaper = article[self.newspaper]
            keywords = self.keyword_processor.extract_keywords(article[self.content])
            count_dict = Counter(keywords)
            print("Article:", idx+1, "Date:", date, "Newspaper:", newspaper)
            for name, count in count_dict.most_common():
                print(name, count)
                try:
                    self.freq_table.loc[
                        (self.freq_table["date"] == date) & (self.freq_table["newspaper"] == newspaper), name
                        ] += count
                except KeyError:
                    try:
                        self.freq_table.loc[
                            (self.freq_table["date"] == date) & (self.freq_table["newspaper"] == newspaper), name[:-1]] += count
                    except KeyError:
                        print("Name was not found.")
                        continue
        print("Finished counting!")


    def save_freq_count(self):
        self.freq_table.to_csv(self.path + "Base_Data/searchterm_mentions_count", index=False)

    def party_count(self):
        self.party_dict = {k: v[v.notna()].to_dict() for k, v in self.party_searchterms.items()}
        for party, searchterms in self.party_dict.items():
            self.party_dict[party] = self.freq_table.loc[:,searchterms.values()].sum(axis=1)
        self.party_frame = pd.concat([self.freq_table.loc[:,["date", "newspaper"]], pd.DataFrame.from_dict(self.party_dict)], axis=1)
        self.party_frame.to_csv(self.path + "Base_Data/party_mentions_count", index=False)

    def absolute_count(self):
        first_part = self.party_frame
        second_part = self.freq_table.drop(self.freq_table.columns[list(range(26))], axis=1)
        self.absolute_table = pd.concat([first_part, second_part], axis=1)
        self.absolute_table = self.date_casting(self.absolute_table)
        self.absolute_table.to_csv(self.path + "Data_Visuals/mentions_absolute", index=False)

    def relative_count(self, who: str = "individual_politicians"):
        def select(selection: str = "individual_politicians"):
            if selection == "parties":
                return True
            else:
                return False

        def separate(parties: bool = False):
            if parties:
                # returns absolute counts for parties
                return self.absolute_table.iloc[:, 2:8]
            else:
                # returns absolute counts for individual politicians
                return self.absolute_table.iloc[:, 8:]

        def sumof(separate, parties: bool = False):
            return separate(parties).sum(axis=1)

        def divideby(separate, parties: bool = False):
            return separate(parties).div(sumof(separate, parties), axis=0)

        def round_and_remove_missing_values(frame):
            return frame.round(4).fillna(0)

        clean = round_and_remove_missing_values
        get_percentage = divideby
        return clean(get_percentage(separate, select(who)))

    def create_relative_frame(self):
        parties = self.relative_count("parties")
        individual_politicians = self.relative_count("individual_politicians")
        self.relative_table = pd.concat(
            [self.absolute_table.loc[:, ["date", "newspaper"]], parties, individual_politicians], axis=1)
        self.relative_table.to_csv(self.path + "Data_Visuals/mentions_relative", index=False)

    def date_casting(self, df, earliest_date:str = "06.01.2021"):
        earliest_date = pendulum.parse(earliest_date, strict=False).format("YYYY-MM-DD")
        today = pendulum.now().format("YYYY-MM-DD")
        df["date"] = \
            df.apply(lambda row: pendulum.parse
                (row["date"], strict=False).format("YYYY-MM-DD") if row["date"] != "No.Date" else "No.Date", axis=1)
        df.drop(df[df.date < earliest_date].index, inplace=True)
        df.drop(df[df.date > today].index, inplace=True)
        df.sort_values(by="date", axis=0, inplace=True, ignore_index=True)
        return df

    def fit(self):
        self.count()
        self.save_freq_count()
        self.party_count()
        self.absolute_count()
        self.create_relative_frame()


if __name__ == "__main__":
    counter = Newscounter()
    counter.fit()

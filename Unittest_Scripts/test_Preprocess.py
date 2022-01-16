import unittest
from Scripts.Preprocess import Poll, Keywords, Relevance, Frequency_Table

class MyTestCase(unittest.TestCase):

    def test_poll(self):
        poll = Poll(refresh=True, path ="/Users/macbook/Desktop/Python_Files/NewsPoll/Data/")

        ## Test if poll data is succesfully scraped.
        poll.parse_poll()
        self.assertIsNotNone(poll.poll_frame)

        ## Test if the poll data is 2021 only.
        poll.select_relevant_polls()
        self.assertNotIn("2020-01-01", poll.poll_frame)
        self.assertNotIn("2019-01-01", poll.poll_frame)
        self.assertNotIn("2018-01-01", poll.poll_frame)

    def test_keywords(self):
        keywords = Keywords("/Users/macbook/Desktop/Python_Files/NewsPoll/Data/")
        keywords.create_searchterms()
        self.assertIsNotNone(keywords.party_dict)

    def test_relevance(self):
        relevance = Relevance("/Users/macbook/Desktop/Python_Files/NewsPoll/Data/")
        relevance.search()
        ## Test if all articles have been searched for keywords and marked either True or False
        self.assertIsNotNone(relevance.newscollection["Contains.Keyword"])

    def test_frequency_table(self):
        freq = Frequency_Table("/Users/macbook/Desktop/Python_Files/NewsPoll/Data/")
        freq.compute_table_shape()
        ## Test if frequency table was created
        self.assertIsNotNone(freq.frequency_table)

if __name__ == '__main__':
    unittest.main()

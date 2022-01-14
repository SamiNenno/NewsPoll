import pandas as pd
import re

def get_articles(name:str):
    '''
    Get newspaper and date of all articles that mention a politician.

    :param name: Name of politican the user searches for
    :return: pd.Dataframe with columns newspaper and date
    '''
    df = pd.read_csv("/Users/macbook/Desktop/Python_Files/NewsPoll/Data/Base_Data/searchterm_mentions_count")
    return df[df[name] > 0][["newspaper", "date"]]

def get_content(relevant_articles):
    '''
    Get articles of certain newspaper at certain date that also include the text of the article.

    :param relevant_articles: pd.Dataframe with columns newspaper and date
    :return: pd.Dataframe of all articles from certain newspaper at certain date
    '''
    all_articles = pd.read_csv("/Users/macbook/Desktop/Python_Files/NewsPoll/Data/Newscollection/articles.csv")
    return pd.merge(all_articles, relevant_articles, how = 'inner', on = ["newspaper", "date"])

def limit_articles(name:str):
    '''
    Wrapper to limit the articles one has to search for a specific politician.

    :param name: Name of politican the user searches for
    :return: pd.Dataframe of all articles from certain newspaper at certain date
    '''
    return get_content(get_articles(name))

def object(subject, object):
    '''
    Creates searchphrase with subject object structure

    :param subject: Name of politician
    :param object: Name of object in sentence
    :return: Function for matching the searchphrase
    '''
    phrase = re.compile(r"\b((?:\w+\W+){0,5000}(?:"+subject+")\W+(?:\w+\W+){0,8}?(?:"+object+")(?:\w+\W+){0,5000})")
    return phrase.match

def onlyverb(subject, verb):
    '''
    Creates searchphrase with subject verb structure

    :param subject: Name of politician
    :param verb: Verb of what politician is doing
    :return: Function for matching the searchphrase
    '''
    phrase = re.compile(
        r"\b((?:\w+\W+){0,5000}(?:" + subject + ")\W+(?:\w+\W+){0,8}?(?:" + verb + ")(?:\w+\W+){0,5000})")
    return phrase.match

def adjective(subject, adjective):
    '''
    Creates searchphrase with subject verb structure

    :param subject: Name of politician
    :param adjective: Adjective that describes the politician
    :return: Function for matching the searchphrase
    '''
    phrase = re.compile(
        r"\b((?:\w+\W+){0,5000}(?:" + subject + ")\W+(?:\w+\W+){0,8}?(?:" + adjective + ")(?:\w+\W+){0,5000})")
    return phrase.match

def verbobject(subject, verb, object):
    '''
    Creates searchphrase with subject verb object structure

    :param subject: Name of politician
    :param verb: Verb of what politician is doing
    :param object: Object to what the politician is doint something
    :return: Function for matching the searchphrase
    '''
    phrase = re.compile(
        r"\b((?:\w+\W+){0,5000}(?:" + subject + ")\W+(?:\w+\W+){0,6}?(?:" + verb + ")\W+(?:\w+\W+){0,8}?(?:" + object + ")(?:\w+\W+){0,5000})")
    return phrase.match

def verbadjective(subject, verb, adjective):
    '''
    Creates searchphrase with subject verb structure

    :param subject: Name of politician
    :param verb: Verb of what politician is doing
    :param adjective: Adjective that describes the politician
    :return: Function for matching the searchphrase
    '''
    phrase = re.compile(
        r"\b((?:\w+\W+){0,5000}(?:" + subject + ")\W+(?:\w+\W+){0,6}?(?:" + verb + ")\W+(?:\w+\W+){0,8}?(?:" + adjective + ")(?:\w+\W+){0,5000})")
    return phrase.match

def match_phrase(subject:str, verb_ = None, adjective_ = None, object_ = None):
    '''
    Retrieves all articles that match a given searchphrase
    :param subject: Name of politician (required)
    :param verb: Verb of what politician is doing (optional)
    :param adjective: Adjective that describes the politician (optional)
    :param object: Object to what the politician is doing something (optional)
    :return:
    '''
    df = limit_articles(subject)
    if verb_ is None:
        if object_ is not None:
            check = object(subject, object_)
        else:
            check = adjective(subject, adjective_)
    else:
        if object_ is not None:
            check = verbobject(subject, verb_, object_)
        elif adjective_ is not None:
            check = verbadjective(subject, verb_, adjective_)
        else:
            check = onlyverb(subject, verb_)

    matches = []
    for idx, article in enumerate(df.itertuples(index=False, name=None)):
        if check(article[3]) is not None:
            matches.append(idx)
        else:
            continue
    print("KATSCHING", subject)
    return df.iloc[matches,:][["newspaper", "teaser", "date", "url"]]

if __name__ == "__main__":

    subject = "Merkel"
    verb = "war"
    object = "Kanzlerin"
    phrase = subject + verb + object
    match_phrase(subject=subject, verb_=verb, object_=object).to_csv("/Users/macbook/Desktop/Python_Files/NewsPoll/DSL/" + phrase + ".csv", index=False)

    subject = "Laschet"
    verb_ = "lacht"
    phrase = subject + verb_
    match_phrase(subject=subject, verb_=verb_).to_csv("/Users/macbook/Desktop/Python_Files/NewsPoll/DSL/" + phrase + ".csv", index=False)

    subject = "Baerbock"
    adjective_ = "vorsichtig"
    phrase = subject + adjective_
    match_phrase(subject, adjective_=adjective_).to_csv("/Users/macbook/Desktop/Python_Files/NewsPoll/DSL/" + phrase + ".csv", index=False)



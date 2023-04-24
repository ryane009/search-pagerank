import pytest
from index import Indexer

# Here's an example test case to make sure your tests are working
# Remember that all test functions must start with "test"
def test_example():
    assert 2 == 1 + 1

'''
Uncomment when ready to use!

def file_as_set(filename):
    """
    Returns all of the non-empty lines in the file, as strings in a set.
    """
    line_set = set()
    with open(filename, "r") as file:
        line = file.readline()
        while line and len(line.strip()) > 0:
            line_set.add(line.strip())
            line = file.readline()
    return line_set

def test_file_contents():
    simple_index = Indexer("wikis/SimpleWiki.xml", "simple_titles.txt",
       "simple_docs.txt", "simple_words.txt")
    simple_index.run() # run the indexer to write to the files
    titles_contents = file_as_set("simple_titles.txt")
    assert len(titles_contents) == 2
    assert "200::Example page" in titles_contents
    assert "30::Page with links" in titles_contents
'''
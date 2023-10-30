import pytest

from DOMs.search_results import SearchResult


def test_search(page):
    searchTest = SearchResult(page)
    #Szukany tekst
    searchTest.searchtest("camera")
class SearchResult:
    def __init__(self, page) -> None:
        self.search_input = page.get_by_placeholder("Search")
        self.search_btn = page.get_by_role("button", name="")

    def searchtest(self, input) -> None:
        self.search_input.fill(input)
        self.search_btn.click()

        # wiecej testów nie zrobię, ponieważ strona nie działa

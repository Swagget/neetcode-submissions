class Page:
    def __init__(self, page = "None", next_page = None, prev_page = None):
        self.page = page
        self.next_page = next_page
        self.prev_page = prev_page

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_page = Page(page = homepage)

    def visit(self, url: str) -> None:
        new_page = Page(url, prev_page = self.current_page)
        self.current_page.next_page = new_page
        self.current_page = new_page

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current_page.prev_page is not None:
                self.current_page = self.current_page.prev_page
        return self.current_page.page
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current_page.next_page is not None:
                self.current_page = self.current_page.next_page
        return self.current_page.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
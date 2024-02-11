class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0
        self.current_length = len(self.history)

    def visit(self, url: str) -> None:
        self.current_index += 1
        self.history.insert(self.current_index,url)
        self.current_length = self.current_index + 1
        
    def back(self, steps: int) -> str:
        self.current_index =  max(self.current_index - steps, 0)
        return self.history[self.current_index]
    
    def forward(self, steps: int) -> str:
        self.current_index = min(self.current_length-1, self.current_index + steps)
        return self.history[self.current_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
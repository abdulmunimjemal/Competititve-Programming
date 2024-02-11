class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0
        self.current_length = len(self.history)

    def visit(self, url: str) -> None:
        self.history.insert(self.current_index+1,url)
        self.current_index += 1
        self.current_length = self.current_index + 1
        
    def back(self, steps: int) -> str:
        n = self.current_index - steps
        new_place =  max(n, 0)
        self.current_index = new_place
        return self.history[self.current_index]
    
    def forward(self, steps: int) -> str:
         n = self.current_index + steps
         new_place = min(self.current_length-1, n)
         self.current_index = new_place
         return self.history[self.current_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
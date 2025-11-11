

class FramesPage:
    
    def __init__(self, page):
        self.page = page
       
        self.FRAMES_LINK = self.page.get_by_text("Frames", exact=True)
        self.NESTED_FRAMES_LINK = self.page.get_by_text("Nested Frames")
        
       

    def goto_homepage(self, url="https://the-internet.herokuapp.com"):
        print(f"Opening URL: {url}")
        self.page.goto(url)

    
    def click_frames_link(self):
        print("Clicking 'Frames' link.")
        self.FRAMES_LINK.click()

   
    def click_nested_frames_link(self):
        print("Clicking 'Nested Frames' link.")
        self.NESTED_FRAMES_LINK.click()

   
    def go_back(self):
        print("Going back to the previous page.")
        self.page.go_back()

    
    def is_nested_frames_link_displayed(self):
        return self.NESTED_FRAMES_LINK.is_visible()
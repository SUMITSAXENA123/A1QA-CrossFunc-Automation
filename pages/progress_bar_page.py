# progress_bar_page.py

from playwright.sync_api import Page, expect

class ProgressBarPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.WIDGETS_CARD = self.page.locator(".card-body").filter(has_text="Widgets")
        self.PROGRESS_BAR_OPTION = self.page.get_by_text("Progress Bar", exact=True)
        self.START_BUTTON = self.page.get_by_role("button", name="Start")
        self.RESET_BUTTON = self.page.get_by_role("button", name="Reset")
        
    def goto_homepage(self, url="https://demoqa.com"):
        print(f"Opening DemoQA URL: {url}")
        self.page.goto(url)

    # Step 1: Click Widgets card
    def click_widgets_card(self):
        print("Clicking Widgets card.")
        self.WIDGETS_CARD.click()
        
    # Step 2: Click Progress Bar option
    def click_progress_bar_option(self):
        print("Selecting Progress Bar option.")
        self.PROGRESS_BAR_OPTION.click()
        
    # Step 3: Click Start button
    def click_start_button(self):
        print("Clicking Start button.")
        self.START_BUTTON.click()
        
    # Verification: Progress Bar page is displayed
    # pages/progress_bar_page.py
# ...
    def is_progress_bar_page_displayed(self):
       
        heading = self.page.get_by_role("heading", name="Progress Bar")
        expect(heading).to_be_visible(timeout=10000) 
        print("Verification: Progress Bar page is displayed.")
# ...
    # Step 4: Refresh the page
    def refresh_page(self):
        print("Refreshing the page.")
        self.page.reload()

    # Verification: Check if Reset button is displayed/not displayed
    def is_reset_button_displayed(self):
        return self.RESET_BUTTON.is_visible()
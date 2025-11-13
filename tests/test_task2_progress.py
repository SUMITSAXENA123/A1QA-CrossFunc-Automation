# test_task2_progress.py
import pytest
from pages.progress_bar_page import ProgressBarPage
from playwright.sync_api import expect




def test_handle_progress_bar_with_incognito(page):
    
    # OOP: Page Object Instance
    progress_page = ProgressBarPage(page)

    # Preconditions: The browser should be open in incognito mode.
    # NOTE: Since we are using pytest-playwright, we will rely on 
    # the command line to configure the incognito mode or run this test 
    # using 'context' fixture (which requires changing conftest.py).
    # Task mein 'ChromeOptions' bola hai. Hum assume karte hain ki Incognito 
    # mode automatically apply ho raha hai (kyunki playwright by default private 
    # context use karta hai jab hum custom setup nahi karte). 
    # We will proceed with the functionality first.

    # Go to https://demoqa.com
    progress_page.goto_homepage()
    
    # Step 1: Click on the Widgets card
    progress_page.click_widgets_card()
    
    # Step 2: Select the Progress Bar option 
    progress_page.click_progress_bar_option()
    
    # Verification: The Progress Bar page is displayed
    progress_page.is_progress_bar_page_displayed()

    # Step 3: Click on the Start button 
    progress_page.click_start_button()
    
    # -------------------------------------------------------------------------
    # TOPIC: EXPLICIT WAIT
    # Verification: The Reset button is displayed.
    
   
    
    print("Waiting for Progress Bar to complete (Reset button to appear).")
  

    expect(progress_page.RESET_BUTTON).to_be_visible(timeout=30000)
    print("SUCCESS: Reset button is now visible after progress completion.")
    # -------------------------------------------------------------------------

    # Step 4: Refresh the page
    progress_page.refresh_page()
    
    # Verification: The Reset button is not displayed

    expect(progress_page.RESET_BUTTON).to_be_hidden()
    print("SUCCESS: Reset button is not displayed after refresh.")
    
    print("\n\n--- Task 2 Completed Successfully ---")


# Import Page Class
from pages.frames_page import FramesPage
import time 


def test_handle_nested_frames(page):
    
   
    frames_page = FramesPage(page)

    # Preconditions: Go to https://the-internet.herokuapp.com
    frames_page.goto_homepage()
    
    # Step 1: Click the Frames link
    frames_page.click_frames_link()
    
    # Step 2: Click the Nested Frames link
    frames_page.click_nested_frames_link()
    
    # ==============================================================================
    # Step 3 and 4: Frames handling (Sabse tricky part)
    # Task: The middle frame text is 'MIDDLE'
    # Task: The left frame text is 'LEFT'
    
    
    
    # 3.1: Left Frame verification

    top_frame = page.frame_locator("frame[name='frame-top']")
    left_frame = top_frame.frame_locator("frame[name='frame-left']")
    left_text = left_frame.get_by_text("LEFT")
    
    assert left_text.is_visible(), "LEFT frame text is not visible"
    print("SUCCESS: LEFT frame text verified.")
    
    # 3.2: Middle Frame verification
    
    middle_frame = top_frame.frame_locator("frame[name='frame-middle']")
    middle_text = middle_frame.get_by_text("MIDDLE")
    
    assert middle_text.is_visible(), "MIDDLE frame text is not visible"
    print("SUCCESS: MIDDLE frame text verified.")
    
    
    # Step 4: Go back to the previous page using browser navigation
    frames_page.go_back()
    
    # Step 4 (Verification): The Nested Frames link is displayed
   
    time.sleep(1) 
    assert frames_page.is_nested_frames_link_displayed(), "Nested Frames link is not displayed after going back."
    print("SUCCESS: Back button worked and Nested Frames link is displayed.")
    
    print("\n\n--- Task 1 Completed Successfully ---")
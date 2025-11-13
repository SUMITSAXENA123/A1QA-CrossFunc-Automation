# conftest.py (Yeh file Pytest ko Playwright ke tools deti hai)
# Playwright ne isko aasan kar diya hai, humein zyada code nahi likhna padta.

# Is file mein abhi hum kuch nahi likhenge. 
# Pytest-Playwright plugin automatically Page Object Model ke liye zaroori 'page' object 
# aur dusre tools, jaise 'context' aur 'browser', provide kar dega.
# Yeh 'conftest.py' Pytest ka special naam hai.

# Agar aapko future mein koi custom settings karni hogi, toh hum yahan karenge.
# Abhi ke liye, bas yeh file bana do (chahe toh empty rakh do).# E:\A1QA\automation\conftest.py
# Hum Playwright ke features ko import kar rahe hain
from playwright.sync_api import sync_playwright

# Pytest khud se 'page' fixture provide karta hai jab Playwright plugin load hota hai.
# Agar abhi bhi page error aaye, toh hum yahan custom fixture banaenge.
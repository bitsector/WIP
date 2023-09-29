#!/usr/bin/env python3

from selenium import webdriver
import sys
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: ask_chatgpt.py <question_for_chatgpt4>")
        sys.exit(1)

    QUESTION = sys.argv[1]
    URL = 'https://chat.openai.com/?model=gpt-4'

    # Paths
    BRAVE_PATH = "/usr/bin/brave-browser"
    CHROMEDRIVER_PATH = "/path/to/chromedriver"  # Remember to replace this with your actual path

    # Set Brave as the browser for ChromeDriver
    options = webdriver.ChromeOptions()
    options.binary_location = BRAVE_PATH

    # Initialize the driver
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

    # Open the URL
    driver.get(URL)

    # Send the question (adjust the selector to match the actual input box on the chat page)
    input_box = driver.find_element_by_id("chat_input_placeholder")  # Placeholder, adjust as needed
    input_box.send_keys(QUESTION)
    input_box.submit()  # or use another method to send the question if needed

    # For demonstration, waiting 15 seconds (assuming some time for ChatGPT to respond)
    time.sleep(15)

    # Fetch current URL
    current_url = driver.current_url
    print("Current URL:", current_url)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()

from seleniumbase import sb_cdp

try:
    url = "https://copilot.microsoft.com/"
    sb = sb_cdp.Chrome(url, locale="en", guest=True)
    textarea = "textarea#userInput"
    sb.wait_for_element(textarea)
    sb.sleep(1.5)
    sb.click_if_visible('[aria-label="Dismiss"]')
    sb.sleep(0.5)
    sb.click('button[data-testid*="chat-mode-"]')
    sb.sleep(1.1)
    sb.click('button[title="Think Deeper"]')
    sb.sleep(1.1)
    query = "How to start automating with SeleniumBase?"
    sb.press_keys(textarea, query)
    sb.sleep(1.1)
    sb.click('button[data-testid="submit-button"]')
    sb.sleep(2.5)
    sb.gui_click_captcha()
    sb.sleep(2.5)
    sb.gui_click_captcha()
    sb.sleep(3.5)
    stop_button = '[data-testid="stop-button"]'
    thumbs_up = 'button[data-testid*="-thumbs-up-"]'
    sb.wait_for_element_absent(stop_button, timeout=45)
    sb.wait_for_element(thumbs_up, timeout=20)
    sb.sleep(0.6)
    sb.click('button[data-testid*="scroll-to-bottom"]')
    sb.sleep(2.2)
    folder = "downloaded_files"
    file_name = "copilot_results.html"
    sb.save_as_html(file_name, folder)
    print('"./%s/%s" was saved!' % (folder, file_name))
    print()
    text = sb.get_text('[data-testid="highlighted-chats"]')
    print(text.replace("  ", " ").replace(" . ", ". "))
    sb.driver.stop()
except Exception:
    print("Something failed!")

from seleniumbase import sb_cdp

try:
    url = "https://example.com"
    sb = sb_cdp.Chrome(url)
    print(sb.get_current_url())
    sb.driver.stop()
except Exception as e:
    print(e)

try:
    url = "https://example.com"
    sb = sb_cdp.Chrome(url)
    print(sb.get_current_url())
except Exception as e:
    print(e)

try:
    url = "https://example.com"
    sb = sb_cdp.Chrome(url)
    print(sb.get_current_url())
    sb.driver.stop()
except Exception as e:
    print(e)

try:
    url = "https://example.com"
    sb = sb_cdp.Chrome(url)
    print(sb.get_current_url())
except Exception as e:
    print(e)

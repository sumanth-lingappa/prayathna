import urllib.request
page = urllib.request.urlopen("https://www.google.com")
text = page.read().decode("utf8")
print(text)

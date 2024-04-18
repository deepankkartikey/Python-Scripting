import webbrowser

with open('bookmark.txt') as file:
    links = file.readlines()
    for link in links:
        webbrowser.open(link)
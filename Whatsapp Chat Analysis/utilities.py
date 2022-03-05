import re

mediaPattern = r"(\<Media omitted\>)" # Because it serves no purpose
regexMedia = re.compile(mediaPattern, flags=re.M)

dateAndTimepattern = r"(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(-)(\s\w+)*(:)"
regexDate = re.compile(dateAndTimepattern, flags=re.M)

def cleanText(filename):    
    with open(filename, "r", encoding="utf8") as chat:
        chatText = chat.read()
    # 01/09/17, 11:34 PM - Amfa:

    """
    Removes the matches and 
    replace them with an empty string
    """
    chatText = regexMedia.sub("", chatText)
    chatText = regexDate.sub("", chatText)

    return [
        line.strip()
        for line in chatText.splitlines()
        if line.strip() is not ""
    ]

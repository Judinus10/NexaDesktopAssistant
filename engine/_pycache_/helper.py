import re


def extract_yt_term(command):
    #define regular expression pattern to capture the song name
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    #use re.search to find the match in the command
    match = re.search(pattern,command,re.IGNORECASE)
    #if a match is found, returnde the extract song name, otherwise return none  
    return match.group(1) if match else None
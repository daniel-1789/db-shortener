slug_num = 0
short_base = "https://shrt.io/"
expansion_dict = dict()
contraction_dict = dict()

def shorten_ignore_user(url: str) -> str:
    curr_contraction = contraction_dict.get(url)
    global slug_num

    if curr_contraction is None:
        slug_num+=1
        curr_contraction = f"{short_base}{slug_num}"
        expansion_dict[slug_num] = url
        contraction_dict[url] = curr_contraction

    return curr_contraction

def shorten_url(url: str, user: str) -> str:
    return shorten_ignore_user(url)

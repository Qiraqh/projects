import re




def main():
    html_input = input("HTML: ").strip()
    parse(html_input)




def parse(s):

    url = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"', s)
    if url:

        y = url.group(1)
        y = re.sub(r"^http:", "https:", y)
        y = re.sub(r"(www\.)?youtube\.com/embed","youtu.be", y)
        return y
    else:
        return None
if __name__ == "__main__":
    main()




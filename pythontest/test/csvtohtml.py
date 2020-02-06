import pandas as panda

def convert_csv_to_html(csv_file : str = "100records.csv", html_file : str = "pakkarans.html"):
    reader = panda.read_csv(csv_file)
    reader.to_html(html_file)

if __name__ == '__main__':
    convert_csv_to_html("100records.csv", "pakkarans.html")





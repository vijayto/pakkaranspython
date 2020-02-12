import csv
from prettytable import PrettyTable, MSWORD_FRIENDLY, FRAME, RANDOM, DEFAULT
from prettytable import from_csv
from bs4 import BeautifulSoup

def csv_to_html(csv_file : str ="100records.csv", destination_html : str = "pakkarans_new_table.html"):
    with open(csv_file, 'r') as file:
        csv_read = csv.reader(file, delimiter=',')
        pretty_table = PrettyTable(next(csv_read))
        for row in csv_read:
            pretty_table.add_row(row)
        # print(pretty_table)
        pretty_table.set_style(DEFAULT)
        pretty_table.header_style="title"
        pretty_table.border=True
        # pretty_table.format=True
        content= pretty_table.get_html_string(attributes = {"border": "1", "class":"dataframe"})
        content2 = pretty_table.get_html_string(attributes={"border": "1", "class": "dataframe"})
        print(content)
        html_header = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
        font-family: arial, sans-serif;
                              border-collapse: collapse;
                              width: 100%;
                            }
                            
                            td, th {
                              border: 1px solid #dddddd;
                              text-align: left;
                              padding: 8px;
                            }
                            
                            tr:nth-child(even) {
                              background-color: #dddddd;
                            }
                            </style>
                            </head>
                            <body>
                            """

        html_footer="""
        </body>
        </html>
        """
        html_content = ''.join((html_header, content, '<br>', '<br>', content2, html_footer))
        print(html_content)
        file = open(destination_html, "w")
        file.writelines(html_content)
        file.close()




if __name__ == '__main__':
    csv_to_html()
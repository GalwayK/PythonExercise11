import pandas
import fpdf


class Item:
    def __init__(self, user_id, price, name, in_stock, headers):
        self.id = user_id
        self.price = price
        self.name = name
        self.in_stock = in_stock
        self.headers = headers

    def __str__(self):
        return f"Item Name: {self.name} Item Price: {self.price}"

    def write_items_to_pdf(self):
        pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.add_page()

        pdf.set_font(family="Times", size=14, style="B")
        pdf.set_text_color(0, 0, 0)

        pdf.cell(w=0, h=10, txt=f"Item ordered: {self.name}", ln=1)

        pdf.cell(w=35, h=10, txt=self.headers[0].title(), ln=0, border=1)
        pdf.cell(w=55, h=10, txt=self.headers[1].title(), ln=0, border=1)
        pdf.cell(w=40, h=10, txt=self.headers[2].title(), ln=0, border=1)
        pdf.cell(w=30, h=10, txt=self.headers[3].title(), ln=1, border=1)

        pdf.set_font(family="Times", size=14)

        pdf.cell(35, h=10, txt=f"{self.id}", ln=0, border=1)
        pdf.cell(55, h=10, txt=f"{self.price}", ln=0, border=1)
        pdf.cell(40, h=10, txt=f"{self.name}", ln=0, border=1)
        pdf.cell(30, h=10, txt=f"{self.in_stock}", ln=1, border=1)

        pdf.output("files/pdf.pdf")


def create_items(items_df):
    items = []
    headers = list(items_df.columns)
    for index, item in items_df.iterrows():
        item_id = item["id"]
        price = item["price"]
        name = item["name"]
        in_stock = item["in_stock"]
        item = Item(item_id, price, name, in_stock, headers)
        items.append(item)
    return items


if __name__ == "__main__":
    items_dataframe = pandas.read_csv("files/articles.csv")
    item_list = create_items(items_dataframe)

    for index, item in enumerate(item_list):
        print(f"{index + 1}. {item}")
    while True:
        try:
            selected_index = input("Please select the number of the item you would like: ")
            selected_index = int(selected_index) - 1
            selected_item = item_list[selected_index]
            break
        except Exception as error:
            print("Please select a valid item.")

    selected_item.write_items_to_pdf()
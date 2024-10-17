from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf_ = PDF(pdf)
    pdf.add_page()
    pdf_.set_page()
    pdf_.get_name(input("Name: "))
    pdf.output("shirtificate.pdf")



class PDF:
    def __init__(self, pdf):
        self.pdf = pdf


    def set_page(self):
        self.pdf.set_font("helvetica", "B", 24)
        #print {text} as a headline
        self.pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN")
        self.pdf.ln(10)


    def get_name(self, name):
        #image on the pdf
        image_path = "shirtificate.png"
        image_width = 100
        page_width = self.pdf.w
        x_position = (page_width - image_width) / 2
        self.pdf.image(image_path, x=x_position, y=50, w=image_width)
        self.pdf.set_text_color(160,32,240)
        self.pdf.set_font("helvetica", "B", 16)
        self.pdf.set_y(80)
        self.pdf.cell(0, 10, name, align="C")


if __name__ == "__main__":
    main()




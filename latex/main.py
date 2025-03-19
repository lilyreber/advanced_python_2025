import os

from latex_generator import *

def main():
    table = [
        ["Species", "Average duration of one sleep cycle, minutes", "REM sleep as \% of total sleep duration"],
        ["Human", 90, 25],
        ["Cat", 26, 30],
        ["Rabbit", 24, 3],
        ["Rat", 13, 20]
    ]



    if not os.path.exists("artifacts"):
        os.makedirs("artifacts")


    with open("artifacts/table.tex", "w") as file:
        file.write(generate_doc([generate_table(table)]))

    blocks = [generate_image("cat.png"), generate_table(table)]
    with open("artifacts/table_image.tex", "w") as file:
        file.write(generate_doc(blocks, packages=["graphicx"]))

    os.system("pdflatex -output-directory=artifacts artifacts/table_image.tex")

if __name__ == "__main__":
    main()

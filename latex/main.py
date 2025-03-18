from latex.latex_generator.latex_generator import generate_table, generate_doc

def main():
    table = [
        ["Col1", "Col2", "Col3"],
        ["Row1", 1, 2],
        ["Row2", 3, 4],
        ["Row3", 5, 6],
        ["Row4", 7, 8]
    ]
    blocks = [generate_table(table)]

    with open("artifacts/table.tex", "w") as file:
        file.write(generate_doc(blocks))

if __name__ == "__main__":
    main()

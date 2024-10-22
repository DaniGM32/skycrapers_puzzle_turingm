def generate_output():
    for i in range(1, 12):
        print(f"goLeftThirdDigit{i},1")
        print(f"goLeftThirdDigit{i+1},1,<\n")

        print(f"goLeftThirdDigit{i},2")
        print(f"goLeftThirdDigit{i+1},2,<\n")

        print(f"goLeftThirdDigit{i},3")
        print(f"goLeftThirdDigit{i+1},3,<\n")

        print(f"goLeftThirdDigit{i},4")
        print(f"goLeftThirdDigit{i+1},4,<\n")

        print(f"goLeftThirdDigit{i},#")
        print(f"goLeftThirdDigit{i+1},#,<\n")

        print(f"goLeftThirdDigit{i},:")
        print(f"goLeftThirdDigit{i+1},:,<\n")

        print("//------------\n")


if __name__ == "__main__":
    generate_output()
import sys

def convert_to_pseudocode(python_code: str) -> str:
    pseudocode = ""

    lines = python_code.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("def"):
            pseudocode += "function " + line[3:] + "\n"
        elif line.startswith("if"):
            pseudocode += "if " + line[2:] + "\n"
        elif line.startswith("else"):
            pseudocode += "else" + "\n"
        elif line.startswith("for"):
            pseudocode += "for " + line[3:] + "\n"
        elif line.startswith("while"):
            pseudocode += "while " + line[5:] + "\n"
        elif line.endswith(":"):
            pseudocode += line[:-1] + " ->" + "\n"
        else:
            pseudocode += "do " + line + "\n"

    return pseudocode

def main():
    if len(sys.argv) != 2:
        print("Usage: python pseudocode_converter.py <filename>")
        return

    with open(sys.argv[1], "r") as f:
        python_code = f.read()

    pseudocode = convert_to_pseudocode(python_code)
    with open(sys.argv[1] + ".pseudocode", "w") as f:
        f.write(pseudocode)

if __name__ == "__main__":
    main()

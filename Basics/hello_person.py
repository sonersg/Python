

def hello(name, lang):
    langs = {
        "Turkish" : "Merhaba",
        "Spanish" : "Hola",
        "English" : "Hello"
    }

    print(f"{langs[lang]} {name}!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["Turkish", "Spanish", "English"]
    )

    args = parser.parse_args()

    hello(args.name, args.lang)

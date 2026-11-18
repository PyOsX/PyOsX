from parser import ParseError, parse_command


def shell_loop():
    """Main interactive loop of PyOsX."""

    print("Welcome to PyOsX!")
    print("Type Ctrl+D to exit.")

    while True:
        try:
            command = input("pyosx> ")

            if not command.strip():
                continue

            try:
                tokens = parse_command(command)

                if not tokens:
                    continue

                # Temporary output for parser testing
                print(
                    "Parsed tokens:",
                    [(token.kind, token.value) for token in tokens]
                )

            except ParseError as error:
                print(f"pyosx: syntax error: {error}")

        except KeyboardInterrupt:
            print("\nUse Ctrl+D to exit.")

        except EOFError:
            print("\nGoodbye!")
            break

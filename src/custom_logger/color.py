from colorama import Fore, Style, init

init(autoreset=True)

LEVEL_COLOURS = {
    "DEBUG": Fore.CYAN,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.MAGENTA,
}


def colour_text(level, message):
    colour = LEVEL_COLOURS.get(level, "")
    return f"{colour}{message}{Style.RESET_ALL}"

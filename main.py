
from config/menu_config.py import print_menu_box
menu_title="📱 SOCIAL MEDIA SCHEDULER"

def main():
    while True :
        print_menu_box(menu_title,)

def print_menu_box(title, options, width=50):
    """Print a complete menu box with options"""
    # Top border
    print(BOX_CHARS['tl'] + BOX_CHARS['h'] * width + BOX_CHARS['tr'])

    # Title (centered)
    title_padding = (width - len(title)) // 2
    print(f"{BOX_CHARS['v']}{' ' * title_padding}{title}{' ' * (width - title_padding - len(title))}{BOX_CHARS['v']}")

    # Middle divider
    print(BOX_CHARS['ml'] + BOX_CHARS['h'] * width + BOX_CHARS['mr'])

    # Options
    for option in options:
        print(f"{BOX_CHARS['v']}  {option.ljust(width-4)}  {BOX_CHARS['v']}")

    # Bottom border
    print(BOX_CHARS['bl'] + BOX_CHARS['h'] * width + BOX_CHARS['br'])
if __name__ == "__main__":
    main()

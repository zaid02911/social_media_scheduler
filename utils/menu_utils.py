from config import *
import time
class UI : 
    @staticmethod
    def display_main_menu():
        time.sleep(1) 
        menu_title="📱 SOCIAL MEDIA SCHEDULER"
        print_menu_box(menu_title,MAIN_MENU_OPTIONS)
        choice=input("🎯 Enter your choice (0-6) :")
        while choice not in ['0','1','5','3','2','4','6']:
                print(f" {STATUS_ICONS["error"]} Invalid choice. Please try again.")
                choice=input("🎯 Enter your choice (0-6) :")


        return choice
    @staticmethod
    def display_post_menu():
        time.sleep(1) 
        menu_title="Post Menu"
        while True:
            print_menu_box(menu_title,POST_MENU_OPTIONS)

            choice = input("\n🎯 Enter your choice (0-4) :  ")

            # Validate input (optional)
            while choice not in ['0','1','3','2','4']:
                print("Invalid choice. Please choose again.")
                choice = input("\n🎯 Enter your choice (0-4) :  ")
            match choice:
                case "0":
                    return
            
    @staticmethod
    def display_schedule_menu():
        time.sleep(1) 
        menu_title="Schedule Menu"
        while True:
            print_menu_box(menu_title,SCHEDULE_MENU_OPTIONS)

            choice = input("\n🎯 Enter your choice (0-6) : ")

            # Validate input (optional)
            while choice not in ['0','1','3','2','4','5','6']:
                print("Invalid choice. Please choose again.")
                choice = input("\n🎯 Enter your choice (0-6) : ")
            match choice:
                case "0":
                    return

    @staticmethod
    def display_platform_settings_menu():
        time.sleep(1) 
        
        time.sleep(1) 
        menu_title="Platforms Menu"
        while True:
            print_menu_box(menu_title,PLATFORM_MENU_OPTIONS)

            choice = input("\n🎯 Enter your choice (0-6) : ")

            # Validate input (optional)
            while choice not in ['0','1','3','2','4','5','6']:
                print("Invalid choice. Please choose again.")
                choice = input("\n🎯 Enter your choice (0-6) : ")
            match choice:
                case "0":
                    return

    @staticmethod
    def display_analytics_menu():
        time.sleep(1)         
        menu_title="Analytics Menu"
        while True:
            print_menu_box(menu_title,ANALYTICS_MENU_OPTIONS)

            choice = input("\n🎯 Enter your choice (0-6) : ")

            # Validate input (optional)
            while choice not in ['0','1','3','2','4','5','6']:
                print("Invalid choice. Please choose again.")
                choice = input("\n🎯 Enter your choice (0-6) : ")
            match choice:
                case "0":
                    return

    @staticmethod
    def display_settings_menu():
        time.sleep(1)         
        menu_title="Settings Menu"
        while True:
            print_menu_box(menu_title,SETTINGS_MENU_OPTIONS)

            choice = input("\n🎯 Enter your choice (0-5) : ")

            # Validate input (optional)
            while choice not in ['0','1','3','2','4','5']:
                print("Invalid choice. Please choose again.")
                choice = input("\n🎯 Enter your choice (0-5) : ")
            match choice:
                case "0":
                    return    
                


    @staticmethod
    def display_help_menu():
        time.sleep(1)         
        menu_title="Help Menu"
        while True:
            print_menu_box(menu_title,HELP_MENU_OPTIONS)

            choice = input("\n🎯 Enter your choice (0-5) : ")

            # Validate input (optional)
            while choice not in ['0','1','3','2','4','5']:
                print("Invalid choice. Please choose again.")
                choice = input("\n🎯 Enter your choice (0-5) : ")
            match choice:
                case "0":
                    return
                


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
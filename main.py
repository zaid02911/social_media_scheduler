
from utils import UI

def main():
    while True :
        choice=UI.display_main_menu()
        match choice: 
            case '0':
                print("👋 Good Bye")
                return
            case '1':                     
                UI.display_post_menu()
            case '2':
                UI.display_schedule_menu()
            case '3':
                UI.display_platform_settings_menu()
            case '4':
                UI.display_analytics_menu()
            case '5':
                UI.display_settings_menu()
            case '6':
                UI.display_help_menu()

if __name__ == "__main__":
    main()

#!/usr/bin/python3

import readline
from toolbox import dissector


# TODO place package in /usr/local/bin
# TODO chmod +x apps.py
# TODO get package via scp into current directory (.)
# TODO scp -r username@ip:/path/to/remote/server/source/folder .

index = {
    1: 'Available service areas and display names.',
    2: 'Raw and complete source JSON.',
    3: 'Express Route exceptions.',
    4: 'All items from source JSON containing IPs.',
    5: 'IPv4 networks for Microsoft 365 Common and Office Online.',
    6: 'IPv6 networks for Microsoft 365 Common and Office Online.',
    7: 'IPv4 networks for Exchange Online.',
    8: 'IPv6 networks for Exchange Online.',
    9: 'IPv4 networks for SharePoint Online and OneDrive for Business.',
    10: 'IPv6 networks for SharePoint Online and OneDrive for Business',
    11: 'IPv4 networks for Skype for Business Online and Microsoft Teams.',
    12: 'IPv6 networks for Skype for Business Online and Microsoft Teams.'
}

intro = '''\nWelcome to O365 dissector.\n
Enter the number of the system you wish to test or Ctrl+C to exit:'''


def main():
    """ List a number of possibilities where each is a system test script."""

    while True:
        try:
            print(intro)

            for k, v in sorted(index.items()):
                print('\t', k, ': ', v, sep='')

            choice = int(input('\nEnter a number> '))
            funct = index.get(choice, 'Not a valid selection!')

            if funct == 'Available service areas and display names.':
                print(dissector.get_service_areas())

            elif funct == 'Raw and complete source JSON.':
                print(dissector.get_all_items())

            elif funct == 'Express Route exceptions.':
                print(dissector.get_er_exceptions())

            elif funct == 'All items from source JSON containing IPs.':
                print(dissector.get_items_with_ips())

            elif funct == 'IPv4 networks for Microsoft 365 Common and Office Online.':
                print(dissector.get_common_ipv4())

            elif funct == 'IPv6 networks for Microsoft 365 Common and Office Online.':
                print(dissector.get_common_ipv6())

            elif funct == 'IPv4 networks for Exchange Online.':
                print(dissector.get_exchange_ipv4())

            elif funct == 'IPv6 networks for Exchange Online.':
                print(dissector.get_exchange_ipv6())

            elif funct == 'IPv4 networks for SharePoint Online and OneDrive for Business.':
                print(dissector.get_sharepoint_ipv4())

            elif funct == 'IPv6 networks for SharePoint Online and OneDrive for Business':
                print(dissector.get_sharepoint_ipv6())

            elif funct == 'IPv4 networks for Skype for Business Online and Microsoft Teams.':
                print(dissector.get_skype_ipv4())

            elif funct == 'IPv6 networks for Skype for Business Online and Microsoft Teams.':
                print(dissector.get_skype_ipv6())

            else:
                print('\n'+funct)
                main()
        except ValueError:
            print('Not a valid selection; enter a valid number.')
        except KeyboardInterrupt:
            print('\n\nThank you for using O365 Dissector.')
            exit()

if __name__ == "__main__":
    main()


#!/usr/bin/python3

import readline
from azure_endpoints import dissector


# TODO place package in /usr/local/bin
# TODO chmod +x apps.py
# TODO get package via scp into current directory (.)
# TODO scp -r username@ip:/path/to/remote/server/source/folder .

index = {
    1: 'Available service areas and display names.',
    2: 'Raw and complete source JSON.',
    3: 'All Exchange Online Items',
    4: 'All Skype for Business Online and Microsoft Teams Items',
    5: 'All SharePoint Online and OneDrive for Business Items',
    6: 'All Microsoft 365 Common and Office Online Items',
    7: 'Express Route exceptions.',
    8: 'All items from source JSON containing IPs.',
    9: 'IPv4 networks for Microsoft 365 Common and Office Online.',
    10: 'IPv6 networks for Microsoft 365 Common and Office Online.',
    11: 'IPv4 networks for Exchange Online.',
    12: 'IPv6 networks for Exchange Online.',
    13: 'IPv4 networks for SharePoint Online and OneDrive for Business.',
    14: 'IPv6 networks for SharePoint Online and OneDrive for Business',
    15: 'IPv4 networks for Skype for Business Online and Microsoft Teams.',
    16: 'IPv6 networks for Skype for Business Online and Microsoft Teams.'
}

intro = '''\nWelcome to O365 dissector.\n
Enter filter number or Ctrl+C to exit:'''


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

            elif funct == 'All Exchange Online Items':
                print(dissector.get_exchange_all())

            elif funct == 'All Skype for Business Online and Microsoft Teams Items':
                print(dissector.get_skype_all())

            elif funct == 'All SharePoint Online and OneDrive for Business Items':
                print(dissector.get_sharepoint_all())

            elif funct == 'All Microsoft 365 Common and Office Online Items':
                print(dissector.get_common_all())

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

#!/usr/bin/python3
"""This modules provides JSON encoded network information for O365.

The purpose of this module is to provide network information for Office 365 in
particular IPv4 and IPv6 route information for each service areas.

This modules parses the source JSON with filter functions. Each filter function
provides interesting data from a pre-defined set rules.

Web page:
https://docs.microsoft.com/en-us/office365/enterprise/office-365-u-s-government-gcc-high-endpoints

The source JSON is:
    https://endpoints.office.com/endpoints/USGovGCCHigh/?ClientRequestId=uuid

Module functions and information they provide:
    get_service_areas()
        Available service areas and display names

    get_all_items()
        Raw and complete source JSON

    get_er_exceptions()
        Express Route exceptions

    get_items_with_ips()
        All items from source JSON containing IPs

    get_common_ipv4()
        IPv4 networks for Microsoft 365 Common and Office Online

    get_common_ipv6()
        IPv6 networks for Microsoft 365 Common and Office Online

    get_exchange_ipv4()
        IPv4 networks for Exchange Online

    get_exchange_ipv6()
        IPv6 networks for Exchange Online

    get_sharepoint_ipv4()
        IPv4 networks for SharePoint Online and OneDrive for Business

    get_sharepoint_ipv6()
        IPv6 networks for SharePoint Online and OneDrive for Business

    get_skype_ipv4()
        IPv4 networks for Skype for Business Online and Microsoft Teams

    get_skype_ipv6()
        IPv6 networks for Skype for Business Online and Microsoft Teams

Example:
    from azure_endpoints import o365
    print(o365.get_service_areas())

Todo: Remove print statement from each

"""

import json
import requests
import ipaddress
import uuid

# Declare URL for source JSON and generate a random uuid for a complete URI
url = 'https://endpoints.office.com/endpoints/USGOVGCCHigh/?clientrequestid='
guid = str(uuid.uuid4())
uri = url+guid


def get_json(payload):
    """Select items with IP information and in the Common service area and fill
    set.

    Usage:
        get_common_ipv4()

    :return: JSON with Microsoft 365 Common and Office Online service IPv4 routes
    """
    try:
        the_json = json.dumps(payload, indent=4, sort_keys=True)
        return the_json
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_data():
    """json_data is raw data; a list with all dict items.

    Usage:
        get_data():

    :return: JSON with O365 network information
    """
    try:
        response = requests.get(uri)
        json_data = response.json()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    return json_data


def get_service_areas():
    """Declare the known service areas in a set and creates sets for service
    areas and service areas display names containers.

    Usage:
        get_service_areas()

    :return: JSON with service areas and service areas display names
    """
    known_service_areas = {'Exchange', 'Skype', 'SharePoint', 'Common'}
    service_areas_display = set()
    service_areas = set()
    try:
        for i in get_data():
            service_areas_display.add(i['serviceAreaDisplayName'])
            service_areas.add(i['serviceArea'])
        if known_service_areas != service_areas:
            print('Warning; known service areas does not mach available service areas!')
        service_areas_display_lst = list(service_areas_display)
        service_areas_display_dic = {'serviceAreaDisplayNames': service_areas_display_lst}
        service_areas_lst = list(service_areas)
        service_areas_dic = {'serviceAreas': service_areas_lst}
        all_service_areas_lst = [service_areas_dic, service_areas_display_dic]
        main_dic = {'serviceAreaInfo': all_service_areas_lst}
        return get_json(main_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_er_exceptions():
    """Provides items with Express Route exceptions
    Usage:
        get_er_exceptions()

    :return: JSON for items with ExpressRoute exceptions
    """
    express_route_exceptions_lst = []
    try:
        for i in get_data():
            if i['expressRoute'] is False:
                express_route_exceptions_lst.append(i)
        express_route_exceptions_dic = {'expressRoutesExceptions': express_route_exceptions_lst}
        return get_json(express_route_exceptions_dic)
    except ValueError as e:
        print(e)


def get_all_items():
    """Raw JSON for a given URI

    Usage:
        get_all_items()

    :return: Raw JSON from given IRI
    """
    try:
        return get_json(get_data())
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_items_with_ips():
    """Select items with IP prefixes and create a formatted JSON file

    Usage:
        get_items_with_ips()

    :return: JSON with all items with IPs
    """
    all_items_with_ips_lst = []
    try:
        for i in get_data():
            if 'ips' in i:
                all_items_with_ips_lst.append(i)
        all_items_with_ips_dic = {'allItemsWithIPs': all_items_with_ips_lst}
        return get_json(all_items_with_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_common_ipv4():
    """Select items with IP information and in the Common service area and fill
    set.

    Usage:
        get_common_ipv4()

    :return: JSON with Microsoft 365 Common and Office Online service IPv4 routes
    """
    common_ips_set = set()  # Set to eliminate duplicates
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Common' and i["expressRoute"] == True:
                common_ips = i['ips']
                for j in common_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        common_ips_set.add(j)
        common_ips_lst = list(common_ips_set)
        common_ips_dic = {'microsoft365CommonAndOfficeOnlineIPv4': common_ips_lst}
        return get_json(common_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_common_ipv6():
    """Select items with IP information and in the Common service area and fill
     set.

    Usage:
        get_common_ipv6()

    :return: JSON with Microsoft 365 Common and Office Online service IPv6 routes
    """
    common_ips_set = set()  # Set to eliminate duplicates
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Common' and i["expressRoute"] == True:
                common_ips = i['ips']
                for j in common_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        common_ips_set.add(j)
        common_ips_lst = list(common_ips_set)
        common_ips_dic = {'microsoft365CommonAndOfficeOnlineIPv6': common_ips_lst}
        return get_json(common_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_exchange_ipv4():
    """Select items with IP information and in the Exchange service area and
     fill set.

    Usage:
        get_exchange_ipv4()

    :return: JSON with Exchange Online service IPv4 routes
    """
    exchange_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Exchange' and i['expressRoute'] == True:
                exchange_ips = i['ips']
                for j in exchange_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        exchange_ips_set.add(j)
        exchange_ips_lst = list(exchange_ips_set)
        exchange_ips_dic = {'exchangeOnlineIPv4': exchange_ips_lst}
        return get_json(exchange_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_exchange_ipv6():
    """Select items with IP information and in the Exchange service area and
    fill set.

    Usage:
        get_exchange_ipv6()

    :return: JSON with Exchange Online service IPv6 routes
    """
    exchange_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Exchange' and i['expressRoute'] == True:
                exchange_ips = i['ips']
                for j in exchange_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        exchange_ips_set.add(j)
        exchange_ips_lst = list(exchange_ips_set)
        exchange_ips_dic = {'exchangeOnlineIPv6': exchange_ips_lst}
        return get_json(exchange_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_sharepoint_ipv4():
    """Select items with IP information and in the 'SharePoint' service area
    and fill set.

    Usage:
        get_sharepoint_ipv4()

    :return: JSON with SharePoint Online and OneDrive for Business service IPv4 routes
    """
    sharepoint_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'SharePoint' and i['expressRoute'] == True:
                sharepoint_ips = i['ips']
                for j in sharepoint_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        sharepoint_ips_set.add(j)
        sharepoint_ips_lst = list(sharepoint_ips_set)
        sharepoint_ips_dic = {'sharePointOnlineAndOneDriveForBusinessIPv4': sharepoint_ips_lst}
        return get_json(sharepoint_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_sharepoint_ipv6():
    """Select items with IP information and in the 'SharePoint' service area
    and fill set.

    Usage:
        get_sharepoint_ipv6()

    :return: JSON with SharePoint Online and OneDrive for Business service IPv6 routes
    """
    sharepoint_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'SharePoint' and i['expressRoute'] == True:
                sharepoint_ips = i['ips']
                for j in sharepoint_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        sharepoint_ips_set.add(j)
        sharepoint_ips_lst = list(sharepoint_ips_set)
        sharepoint_ips_dic = {'sharePointOnlineAndOneDriveForBusinessIPv6': sharepoint_ips_lst}
        return get_json(sharepoint_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_skype_ipv4():
    """Select items with IP information and in the 'Skype' service area and
    fill set.

    Usage:
        get_skype_ipv4()

    :return: JSON with Skype for Business Online and Microsoft Teams IPv4 routes
    """
    skype_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Skype' and i['expressRoute'] == True:
                skype_ips = i['ips']
                for j in skype_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        skype_ips_set.add(j)
        skype_ips_lst = list(skype_ips_set)
        skype_ips_dic = {'skypeForBusinessOnlineAndMicrosoftTeamsIPv4': skype_ips_lst}
        return get_json(skype_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_skype_ipv6():
    """Select items with IP information and in the 'Skype' service area and
    fill set.

    Usage:
        get_skype_ipv6()

    :return: JSON with Skype for Business Online and Microsoft Teams IPv6 routes
    """
    skype_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Skype' and i['expressRoute'] == True:
                skype_ips = i['ips']
                for j in skype_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        skype_ips_set.add(j)
        skype_ips_lst = list(skype_ips_set)
        skype_ips_dic = {'skypeForBusinessOnlineAndMicrosoftTeamsIPv6': skype_ips_lst}
        return get_json(skype_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def main():
    print(get_service_areas())
    print(get_all_items())
    print(get_er_exceptions())
    print(get_items_with_ips())
    print(get_common_ipv4())
    print(get_common_ipv6())
    print(get_exchange_ipv4())
    print(get_exchange_ipv6())
    print(get_sharepoint_ipv4())
    print(get_sharepoint_ipv6())
    print(get_skype_ipv4())
    print(get_skype_ipv6())

if __name__ == "__main__":
    main()

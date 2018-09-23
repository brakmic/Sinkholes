#!/usr/bin/env python3
"""
    Simple python file allowing one to add a row (or multiple rows) into the
    sinkhole list in one fell swoop in combination with the add_rows.py file.

    Simply populate this data structure and run add_rows.py at the terminal to
    add rows to the sinkhole list.
"""

# Example. Only the bottom most "addition(s)" will be added in.
addition = [{
    'Organization': 'OpenDNS',
    'IP Range': '146.112.61.104-110',
    'Whois': 'hit-{block,botnet,adult,malware,phish,block,malware}.opendns.com',
    'Notes': 'https://support.opendns.com/hc/en-us/articles/227986927-What-are-the-Cisco-Umbrella-Block-Page-IP-Addresses-'
}]


addition = [{
    # The Organization responsible / running the sinkholes specified in the IP
    # Ranges section
	'Organization': '',

    # The IP ranges that are part of the sinkhole. Formats include CIDR
    # notation, singular IP addresses, or a small range of IPs designated with
    # a dash character (e.g. 192.168.0.1-10 to indicate all IPs starting at
    # 192.168.0.1 and incrementing up to 192.168.0.10 are sinkhole IPs)
	'IP Range': '',

    # Fill this in with either the organization name or any DNS name for the IP
    # ranges listed above.
	'Whois': '',

    # Generally, fill this in with any reference URLs, additional information
    # regarding the IP range, etc.
	'Notes': ''
}]


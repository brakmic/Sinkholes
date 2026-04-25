# Malware Sinkhole List

A community-curated list of known malware/research sinkhole IP ranges and the
organisations that run them, published in CSV, JSON, XLSX, ODS, and the
Markdown table further down this file.

![sinkhole_image](https://raw.githubusercontent.com/brakmic/Sinkholes/master/sinkhole.jpg)

## Sources and credits

- Lesley Carhart's [Consolidated Malware Sinkhole List](https://tisiphone.net/2017/05/16/consolidated-malware-sinkhole-list/) seeded the original dataset. The bulk of the original work is hers.
- The 2026 refresh draws from the public OSINT list at [grettir/malware-sinkholes](https://github.com/grettir/malware-sinkholes).
- Original Python tooling by [@masq](https://github.com/masq).

## What changed in the 2026 refresh

- 98 additional rows covering AnubisNetworks PT, Bitdefender, Blue Coat, CERT
  Australia, Check Point, Dell SecureWorks, Now-DNS, RSA Research,
  SecurityScorecard, Vicheck.ca, plus expanded coverage for existing
  organisations (Farsight, Georgia Tech, Shadowserver, Spamhaus, Malware/Torpig
  Cabal, Zinkhole.org, and others).
- The Python tooling has been rewritten to drop the unmaintained `pyexcel`
  stack. Output formats are now produced by `csv` and `json` from the standard
  library, [openpyxl](https://pypi.org/project/openpyxl/) for XLSX, and
  [odfpy](https://pypi.org/project/odfpy/) for ODS.
- The legacy `.xls` format has been dropped. The modern `.xlsx` is the
  replacement; every spreadsheet application released in the last decade reads
  it.
- The Markdown table below is now generated directly from the CSV by
  `add_rows.py --readme`, so it stays in sync with the authoritative data.

## Data file

`Sinkholes_List.csv` is the authoritative source. All other formats are
regenerated from it.

| Field        | Description                                                                                  |
|--------------|----------------------------------------------------------------------------------------------|
| Organization | The organisation operating the sinkhole.                                                     |
| IP Range     | A single IP, a CIDR block, or a short last-octet range like `192.168.0.1-10`.                |
| Whois        | The DNS name or organisation visible from the IP's whois or PTR lookup.                      |
| Notes        | A reference URL or short note explaining the entry.                                          |

## Tooling

Install dependencies:

```sh
pip install -r requirements.txt
```

Common workflows:

```sh
# Validate every row in Sinkholes_List.csv (schema and IP parsing).
python add_rows.py --validate --sync

# Append rows defined in addition.py, then regenerate every output format
# and refresh the table embedded in this README.
python add_rows.py --readme

# Just regenerate output formats from the CSV without adding anything.
python add_rows.py --sync --readme
```

Flags:

| Flag         | Effect                                                                                  |
|--------------|-----------------------------------------------------------------------------------------|
| `--sync`     | Skip `addition.py`. Regenerate JSON, XLSX, and ODS from the CSV as it stands.           |
| `--validate` | Run schema and IP-range validation. Exits non-zero on any failure.                      |
| `--readme`   | Rewrite the table block in `README.md` between the start and end markers.               |
| `--debug`    | Print rows to stdout. Write nothing.                                                    |

## Sinkholes

<!-- sinkholes-table:start -->

| Organization            | IP Range           | Whois                                                            | Notes                                                                                                                 |
| ----------------------- | ------------------ | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Anubis                  | 195.22.26.192/26   | anubisnetworks.com                                               | https://www.proofpoint.com/us/daily-ruleset-update-summary-2015-08-14                                                 |
| Arbor Networks ASERT    | 23.253.126.58      | arbor-sinkhole.net                                               | http://www.malwareurl.com/ns_listing.php?ns=ns1.arbor-sinkhole.net                                                    |
| Arbor Networks ASERT    | 168.181.184.35     | arbor-sinkhole.net                                               | http://www.malwareurl.com/ns_listing.php?ns=ns1.arbor-sinkhole.net                                                    |
| Blacklab.io             | 67.215.255.139     | sinkhole.blacklab.io                                             |                                                                                                                       |
| blacklistthisdomain     | 106.187.96.49      | sinkhole.blacklistthisdomain.com                                 |                                                                                                                       |
| blacklistthisdomain     | 81.166.122.234     | sinkhole.blacklistthisdomain.com                                 |                                                                                                                       |
| Botnet Hunter           | 52.5.245.208       | ec2-52-5-245-208.compute-1.amazonaws.com                         |                                                                                                                       |
| CERT Polska             | 148.81.111.111     | sinkhole.cert.pl                                                 |                                                                                                                       |
| CERT Polska             | 148.81.111.91      | sinkhole.cert.pl                                                 |                                                                                                                       |
| CERT Polska             | 148.81.111.114     | sinkhole.cert.pl                                                 |                                                                                                                       |
| Conficker Working Group | 136.161.101.53     | conficker-sinkhole.com                                           |                                                                                                                       |
| Dr. Web                 | 91.233.244.106     | http://doc.emergingthreats.net/bin/view/Main/2016997             |                                                                                                                       |
| Endgame                 | 166.78.144.80      | s01.snkhole.mal-ware.susp-nded.domain                            | http://www.kleissner.org                                                                                              |
| Farsight                | 104.244.12.0/22    | sinkhole-iad1-2.cwg.fsi.io                                       |                                                                                                                       |
| FBI                     | 142.0.36.234       | VolumeDrive                                                      |                                                                                                                       |
| Fitsec                  | 193.166.255.171    | Funet CERT                                                       |                                                                                                                       |
| Georgia Tech            | 143.215.130.0/24   | Georgia Institute of Technology                                  |                                                                                                                       |
| Georgia Tech            | 198.61.227.6       | Rackspace                                                        | www.kleissner.org                                                                                                     |
| Georgia Tech            | 50.57.148.87       | Slicehost                                                        | www.kleissner.org                                                                                                     |
| Gladtech                | 74.200.48.169      | sinkhole.gladtech.net                                            |                                                                                                                       |
| Helse CSIRT             | 91.186.66.36       | NORWEGIAN-HEALTH-NETWORK                                         |                                                                                                                       |
| Hyas                    | 192.169.69.25      | sinkhole.hyas.com                                                |                                                                                                                       |
| Kaspersky               | 93.159.228.22      | sinkhole.kaspersky.com                                           |                                                                                                                       |
| Kaspersky               | 95.211.172.143     | sinkhole.kaspersky.com                                           |                                                                                                                       |
| MalwareDomains          | 139.146.167.25     | Computer Problem Solving (CPS)                                   |                                                                                                                       |
| Microsoft               | 131.253.18.11-12   | Microsoft                                                        | http://doc.emergingthreats.net/bin/view/Main/2016101                                                                  |
| Microsoft               | 199.2.137.0/24     | Microsoft                                                        | https://lists.emergingthreats.net/pipermail/emerging-sigs/2013-June/022148.html                                       |
| Microsoft               | 204.95.99.59       | Microsoft                                                        | https://lists.emergingthreats.net/pipermail/emerging-sigs/2013-June/022148.html                                       |
| Microsoft               | 207.46.90.0/24     | Microsoft                                                        | https://lists.emergingthreats.net/pipermail/emerging-sigs/2013-June/022148.html                                       |
| PublicDomainRegistry    | 109.74.196.143     | Linode                                                           | www.kleissner.org                                                                                                     |
| PublicDomainRegistry    | 50.116.56.144      | Linode                                                           | www.kleissner.org                                                                                                     |
| PublicDomainRegistry    | 50.116.32.177      | Linode                                                           | www.kleissner.org                                                                                                     |
| PublicDomainRegistry    | 178.79.190.156     | Linode                                                           | www.kleissner.org                                                                                                     |
| Shadowserver            | 87.106.24.200      | sinkhole-00.shadowserver.org                                     |                                                                                                                       |
| Shadowserver            | 87.106.26.9        | sinkhole-01.shadowserver.org                                     | http://marc.info/?l=emerging-sigs&m=135764068231008&w=2                                                               |
| Shadowserver            | 74.208.64.145      | sinkhole-02.shadowserver.org                                     |                                                                                                                       |
| Shadowserver            | 74.208.64.191      | sinkhole-03.shadowserver.org                                     |                                                                                                                       |
| Shadowserver            | 74.208.164.166     | sinkhole-04.shadowserver.org                                     |                                                                                                                       |
| Shadowserver            | 212.227.55.84      | sinkhole.shadowserver.org                                        |                                                                                                                       |
| Shadowserver            | 74.208.15.160      | sinkhole.shadowserver.org                                        |                                                                                                                       |
| Shadowserver            | 74.208.15.97       | sinkhole.shadowserver.org                                        |                                                                                                                       |
| Shadowserver            | 87.106.250.34      | sinkhole.shadowserver.org                                        | http://marc.info/?l=emerging-sigs&m=135764068231008&w=2                                                               |
| Shadowserver            | 87.106.86.28       | sinkhole.shadowserver.org                                        | http://marc.info/?l=emerging-sigs&m=135764068231008&w=2                                                               |
| SIDN Labs               | 176.58.104.168     | sinkhole.sidnlabs.nl                                             |                                                                                                                       |
| sinkhole.DK             | 212.227.20.19      | sinkhole.dk                                                      |                                                                                                                       |
| sinkhole.in             | 86.124.164.25      | sinkhole.in                                                      |                                                                                                                       |
| sinkhole.tech           | 79.137.66.14       | http3.sinkhole.tech                                              |                                                                                                                       |
| sinkhole.tech           | 95.211.174.92      | sinkhole.tech                                                    |                                                                                                                       |
| sinkhole.tech           | 144.217.254.3      | http4.sinkhole.tech                                              |                                                                                                                       |
| sinkhole.tech           | 217.182.172.139    | http1.sinkhole.tech                                              |                                                                                                                       |
| sinkhole.tech           | 144.217.74.156     | http2.sinkhole.tech                                              |                                                                                                                       |
| SISRA / Abuse.ch        | 104.155.11.149     | this-domain-is-sinkholed-by.abuse.ch                             |                                                                                                                       |
| Spamhaus                | 208.43.245.213     | sl-reverse.com                                                   |                                                                                                                       |
| Spamhaus                | 173.192.192.10     | sl-reverse.com                                                   |                                                                                                                       |
| Spamhaus                | 199.231.211.108    | sl-reverse.com                                                   |                                                                                                                       |
| Spamhaus                | 198.98.120.157     | sl-reverse.com                                                   |                                                                                                                       |
| Spamhaus                | 192.42.116.41      | sl-reverse.com                                                   |                                                                                                                       |
| Spamhaus                | 87.255.51.229      | sl-reverse.com                                                   |                                                                                                                       |
| Team Cymru              | 38.102.150.29      | conficker-sinkhole.net                                           |                                                                                                                       |
| Team Cymru              | 38.229.70.125      | conficker-sinkhole.net                                           |                                                                                                                       |
| Torpig-Sinkhole         | 212.227.55.84      | torpig-sinkhole.org                                              |                                                                                                                       |
| Torpig-Sinkhole         | 87.106.240.162     | torpig-sinkhole.org                                              |                                                                                                                       |
| Torpig-Sinkhole         | 87.106.140.254     | torpig-sinkhole.org                                              |                                                                                                                       |
| Torpig-Sinkhole         | 87.106.141.15      | torpig-sinkhole.org                                              |                                                                                                                       |
| Wapack Labs             | 23.253.46.64       |                                                                  | https://wapacklabs.blogspot.com/2016/07/wapack-labs-sinkhole-results-18.html                                          |
| Zinkhole.org            | 176.31.62.76       | suspended-domain.org                                             |                                                                                                                       |
| Zinkhole.org            | 178.32.140.251     | suspended-domain.org                                             |                                                                                                                       |
| Zinkhole.org            | 94.23.175.2        | suspended-domain.org                                             |                                                                                                                       |
| OpenDNS                 | 146.112.61.104-110 | hit-{block,botnet,adult,malware,phish,block,malware}.opendns.com | https://support.opendns.com/hc/en-us/articles/227986927-What-are-the-Cisco-Umbrella-Block-Page-IP-Addresses-          |
| infosec.jp              | 58.158.177.102     | UCOM Corp.                                                       | https://github.com/grettir/malware-sinkholes/blob/905841db3b3cd86052d577c137ac9868c92dcb3b/malware_sinkholes.txt#L256 |
| CNCERT/CC               | 183.236.2.18       | China Mobile communications corporation                          |                                                                                                                       |
| AnubisNetworks PT       | 62.28.241.21       | anbtr.com                                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| AnubisNetworks PT       | 89.115.44.100      | anbtr.com                                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| AnubisNetworks PT       | 195.22.4.21        | anbtr.com                                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| AnubisNetworks PT       | 195.22.28.192/27   | anbtr.com                                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| AnubisNetworks PT       | 195.38.137.100     | anbtr.com                                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| AnubisNetworks PT       | 195.157.15.100     | anbtr.com                                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| AnubisNetworks PT       | 212.61.180.100     | anbtr.com                                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Arbor Networks ASERT    | 104.239.157.210    | arbor-sinkhole.net                                               | https://github.com/grettir/malware-sinkholes                                                                          |
| Bitdefender             | 5.2.189.251        | Bitdefender                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Blue Coat               | 54.208.168.113     | sinkhole1.bc-gin.com                                             | https://github.com/grettir/malware-sinkholes                                                                          |
| CERT Australia          | 150.101.125.42     | cert.gov.au                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| CERT Polska             | 148.81.111.64/26   | sinkhole.cert.pl                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| Check Point             | 62.0.58.94         | Check Point                                                      | https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk74060     |
| CNCERT/CC               | 221.8.69.25        | CNCERT/CC Conficker Sinkhole                                     | http://www.cert.org.cn/publish/main/10/2012/20120330183823753875835/20120330183823753875835_.html                     |
| Dell SecureWorks        | 45.56.77.175       | ctu-sinkhole@secureworks.com                                     | https://github.com/grettir/malware-sinkholes                                                                          |
| Farsight                | 38.102.150.27      | conficker-sinkhole.net                                           | https://github.com/grettir/malware-sinkholes                                                                          |
| Farsight                | 38.102.150.28/31   | conficker-sinkhole.net                                           | https://github.com/grettir/malware-sinkholes                                                                          |
| Farsight                | 104.244.14.252/31  | sinkhole-iad1-1.cwg.fsi.io                                       | https://github.com/grettir/malware-sinkholes                                                                          |
| Farsight                | 216.66.15.109      | Farsight Security                                                | https://github.com/grettir/malware-sinkholes                                                                          |
| FBI                     | 54.83.43.69        | Gameover ZeuS Sinkhole                                           | https://www.cybereason.com/the-fbi-vs-gameover-zeus-why-the-dga-based-botnet-wins/                                    |
| Fitsec                  | 193.166.255.170    | sinkhole.fitsec.com                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 23.92.16.214       | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 23.92.24.20        | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 23.239.17.167      | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 23.239.18.116      | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 45.79.141.164      | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 50.116.57.116      | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 69.61.12.90        | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 85.159.211.21      | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 85.159.211.119     | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 96.126.112.224     | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 106.186.21.174     | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 143.215.15.2       | Georgia Institute of Technology                                  | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 143.215.130.42     | Georgia Institute of Technology                                  | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 143.215.130.46     | Georgia Institute of Technology                                  | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 178.79.159.82      | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 199.168.91.20      | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 212.71.250.4       | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Georgia Tech            | 213.219.37.5       | sinkdns.org                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Kaspersky               | 128.199.34.140     | sinkhole.kaspersky.com                                           | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 85.214.50.92       | torpig-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 85.214.83.150      | torpig-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.18.112      | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.18.116      | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.18.122      | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.18.136      | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.18.141      | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.18.146      | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.190.153     | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.190.154     | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.190.157     | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.190.163     | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.190.165     | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.190.167     | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 87.106.190.169     | spyeye-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 212.227.20.93      | torpig-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 212.227.20.116     | torpig-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 212.227.20.164     | torpig-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Malware/Torpig Cabal    | 212.227.252.198    | torpig-sinkhole.org                                              | https://github.com/grettir/malware-sinkholes                                                                          |
| Now-DNS                 | 158.69.201.47      | Now-DNS.com Sinkhole                                             | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 67.205.153.100     | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 104.236.150.45     | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 104.236.158.189    | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 128.199.76.241     | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 128.199.108.0      | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 159.203.210.188    | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 159.203.214.47     | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 192.241.211.14     | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 198.199.105.129    | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 209.249.180.243    | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| RSA Research            | 209.249.180.246    | notasinkhole.com                                                 | https://github.com/grettir/malware-sinkholes                                                                          |
| SecurityScorecard       | 208.100.26.234     | honeybot.us                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| SecurityScorecard       | 208.100.26.251     | honeybot.us                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 5.79.71.205        | sc-a.sinkhole.shadowserver.org                                   | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 5.79.71.225        | sc-b.sinkhole.shadowserver.org                                   | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 50.21.181.152      | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 74.208.153.9       | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 85.17.31.82        | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 85.17.31.122       | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 87.106.20.192      | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 87.106.34.1        | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 87.106.149.145     | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 87.106.149.153     | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 87.106.253.18      | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 178.162.203.202    | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 178.162.203.211    | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 178.162.203.226    | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 178.162.217.107    | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 184.105.192.2      | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 213.165.83.176     | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 216.218.135.114    | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 216.218.185.162    | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Shadowserver            | 217.160.6.63       | sinkhole.shadowserver.org                                        | https://github.com/grettir/malware-sinkholes                                                                          |
| Spamhaus                | 46.148.120.173     | sinkhole.ch                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Spamhaus                | 192.42.119.41      | sinkhole.ch                                                      | https://github.com/grettir/malware-sinkholes                                                                          |
| Vicheck.ca              | 54.248.229.24/31   | Vicheck.ca                                                       | https://github.com/grettir/malware-sinkholes                                                                          |
| Zinkhole.org            | 87.98.254.64       | zinkhole.org                                                     | https://github.com/grettir/malware-sinkholes                                                                          |
| Zinkhole.org            | 151.80.78.61       | zinkhole.org                                                     | https://github.com/grettir/malware-sinkholes                                                                          |

<!-- sinkholes-table:end -->

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE)

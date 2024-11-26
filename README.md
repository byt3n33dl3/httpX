<h1 align="center">
  <a href=https://github.com/byt3n33dl3/httpX><img src="/doc/yari.webp" alt="httpX" width="280px">
  <br>
</h1>

<p align="center">
  <a href="#sharp-karambit">Karambit</a> •
  <a href="#probes">Capability</a> •
  <a href="#notes">Usage</a> •
  <a href="#credits">Master</a>
</p>

<h2 align="center">
  <img src="/doc/red-logo.png" alt="httpx" width="200px">
</h2>

Fast and multi purpose HTTP toolkit that allows running multiple probes using the retryable HTTP library. It is designed to maintain result `reliability` with an increased number of threads. httpX has been an essential asset in the arsenal of `Security` professionals and researchers.

# [httpX](https://github.com/byt3n33dl3/httpX/) / `Assessor`

```hs
    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \/ __/ __/ __ \|   / 
 / / / / /_/ /_/ /_/ /   |  
/_/ /_/\__/\__/ .___/_/|_|v2  
             /_/

```

<div align="center">
<h1>httpX</h1>
httpX can be used as a library by creating an instance of the Option struct and populating it with the same options that would be specified via CLI. Once validated, the struct should be passed to a runner instance to be closed at the end of the program and the RunEnumeration method should be called.
<p></div>

<p align="center">
<a href="https://opensource.org/licenses/AGPL"><img src="https://img.shields.io/badge/license-AGPL-_red.svg"></a>
<a href="https://github.com/byt3n33dl3/httpx/releases"><img src="https://img.shields.io/github/release/byt3n33dl3/httpx"></a>
<a href="https://github.com/byt3n33dl3/"><img src="https://img.shields.io/badge/Offensive httpX-_red.svg"></a>
</p>

# Sharp Karambit 
A CLI software for Web `Domain` Crucifixion and `Account` Takeover.

An Open source Penetration Testing tool that automates the process of detecting and exploiting `HTTP` and `HTTPs` flaws and taking over of the Insecure Domain services. It comes with a powerful detection engine, many niche features for the ultimate Penetration Tester, and a broad range of switches including Domain fingerprinting, over data fetching from any services, accessing the underlying file systems.

 - Simple and modular code base making it easy to contribute.
 - Fast And fully configurable flags to probe multiple elements.
 - Supports multiple `HTTP` based probings.
 - Smart auto fallback from https to http as default. 
 - Supports hosts, URLs and CIDR as input.
 - Account Takeover
 - Handles edge cases doing retries, backoffs etc for handling WAFs.

| :vampire:  **Disclaimer**  |
|---------------------------------|
| **This project is in active development**. Expect breaking changes with releases. Review the changelog before updating. |
| This project was primarily built to be used as a standalone CLI tool. **Running it as a service may pose security risks.** It's recommended to use with caution and additional security measures. |


# Interface

<h1 align="center">
  <img src="/doc/show.png" alt="httpx" width="700px">
  <br>
</h1>

# Probes

| Probes          | Default check | Probes         | Default check |
|-----------------|---------------|----------------|---------------|
| URL             | true          | IP             | true          |
| Title           | true          | CNAME          | true          |
| Status Code     | true          | Raw HTTP       | true          |
| Content Length  | true          | HTTP2          | true          |
| TLS Certificate | true          | HTTP Pipeline  | true          |
| CSP Header      | true          | Virtual host   | true          |
| Line Count      | true          | Word Count     | true          |
| Location Header | true          | CDN            | true          |
| Web Server      | true          | Paths          | true          |
| Web Socket      | true          | Ports          | true          |
| Response Time   | true          | Request Method | true          |
| Favicon Hash    | false         | Probe  Status  | true          |
| Body Hash       | true          | Header  Hash   | true          |
| Redirect chain  | false         | URL Scheme     | true          |
| JARM Hash       | false         | ASN            | true          |

# Notes

- As default, `httpx` probe with **HTTPs** scheme and fall-back to **HTTP** only if **HTTPs** is not reachable.
- The `-no-fallback` flag can be used to probe and display both **HTTP** and **HTTPs** result.
- Custom scheme for ports can be defined, for example `-ports` http:443,http:80,https:8443
- Custom resolver supports multiple protocol (**doh|tcp|udp**) in form of `protocol:`resolver:port (e.g. `udp:`127.0.0.1:53)
- The following flags should be used for specific use cases instead of running them as default with other probes:
   - `-ports`
   - `-path`
   - `-vhost`
   - `-screenshot`
   - `-csp-probe`
   - `-tls-probe`
   - `-favicon`
   - `-http2`
   - `-pipeline`
   - `-tls-impersonate`
 
# Credits / `Master`

<p align="left">
<a href="https://github.com/byt3n33dl3"><img src="https://avatars.githubusercontent.com/u/151133481?v=4" width="50" height="50" alt="" style="max-width: 100%;"></a>
<a href="https://github.com/projectdiscovery"><img src="https://avatars.githubusercontent.com/u/50994705?s=200&v=4" width="50" height="50" alt="" style="max-width: 100%;"></a>
<a href="https://github.com/apps/dependabot"><img src="https://avatars.githubusercontent.com/in/29110?v=4" width="50" height="50" alt="" style="max-width: 100%;"></a>
<a href="https://github.com/ehsandeep"><img src="https://avatars.githubusercontent.com/u/8293321?v=4" width="50" height="50" alt="" style="max-width: 100%;"></a>
<a href="https://github.com/Mzack9999"><img src="https://avatars.githubusercontent.com/u/13421144?v=4" width="50" height="50" alt="" style="max-width: 100%;"></a>
<a href="https://github.com/OceanExec"><img src="https://avatars.githubusercontent.com/u/171657497?s=200&v=4" width="50" height="50" alt="" style="max-width: 100%;"></a>
</p>

>- Projectdiscovery [projectdiscovery.io](https://docs.projectdiscovery.io/tools/httpx)

## `AGPL` / [LICENSE](https://github.com/byt3n33dl3/httpX/main/LICENSE.md)

GNU AFFERO GENERAL `PUBLIC` LICENSE 3.0

```
The GNU Affero General Public License is a free, copyleft license for software and other kinds of works, 
specifically designed to ensure cooperation with the community in the case of network server software. 
The licenses for most software and other practical works are designed to take away your freedom to 
share and change the works. By contrast, our General Public Licenses are intended to guarantee your 
freedom to share and change all versions of a program--to make sure it remains free software for all its users.
```

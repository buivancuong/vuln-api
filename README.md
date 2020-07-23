Exec file on ./dist

### Search with any keyword
* Using:
```bash
$ ./vuln_search_keyword {keyword} {limit result}
```
* Example
```bash
$ ./vuln_search_keyword ransomware 10 > result
```

### Search for documentation

* Using:
```bash
$ ./vuln_search_doc {CVE identification}
```
* Example
```bash
$ ./vuln_search_doc CVE-2017-14174 > result
```

### Search for exploit

* Using:
```bash
$ ./vuln_search_exploit {exploit keyword} {limit result}
```
* Example
```bash
$ ./vuln_search_exploit xss 2 > result
```

### Search for software vulnerability

* Using:
```bash
$ ./vuln_search_exploit {software name} {software version}
```
* Example
```bash
$ ./vuln_search_software httpd 1.2 > result
```

### Search for OS vulnerability

* Using:
```bash
$ ./vuln_search_os {OS name} {OS version}
```
* Example
```bash
$ ./vuln_search_os centos 7 > result
```
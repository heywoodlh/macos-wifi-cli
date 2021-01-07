# MacOS Wifi CLI:

This is a command line client for interacting with wifi on MacOS.


## Installation:

```bash
sudo pip3 install macos-wifi-cli
```


## Usage:

```bash
$ wifi --help

usage: wifi [-h] [-d DEVICE] {on,off,scan,connect,info,pass} ...

MacOS CLI tool for managing wifi connections

positional arguments:
  {on,off,scan,connect,info,pass}
                        commands
    on                  Turn on wifi
    off                 Turn off wifi
    scan                Scan for wifi networks
    connect             Connect to wifi network
    info                Fetch current wifi info
    pass                Retrieve stored wifi passphrase

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE, --device DEVICE Device

```

### Turn wifi off and on:

```bash
wifi on
```

```bash
wifi off
```

### Scan for networks:

```bash
wifi scan
```

### Connect to a network:

```bash
wifi connect --network "mynetwork" --password "mypassword"
```

Help:

```bash
$ wifi connect --help
usage: wifi connect [-h] -n NETWORK -p PASSWORD

optional arguments:
  -h, --help            show this help message and exit
  -n NETWORK, --network NETWORK
                        SSID name
  -p PASSWORD, --password PASSWORD
                        Wifi passphrase
```

Tip:

Use [command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) to retrieve the password securely so it's not saved in plaintext in your shell history.

For example, using [pass](https://www.passwordstore.org/):

```bash
wifi connect -n "mynetwork" -p $(pass wifi/home)
```


### Get current wifi info:

```bash
wifi info
```

### Get password for previously connect wifi network:

```bash
wifi pass --network 'mynetwork'
```

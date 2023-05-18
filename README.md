# MitmWs Updates
This repository is a collection of updates for mitm-ws's payloads and detection rules. Supplemental scripts are provided
for upgrade scripts, event scripts, variables and HTTP handlers but they're currently not automatically installed.

# Update types
- DAST active rules
- Passive rules
- Payloads

# Supplemental content
- Script variables
- HTTP / Websocket endpoints
- Websocket upgrade HTTP request
- Event scripts

Note: Supplemental content can be installed by manually downloading and copying the files to the `.mitmws/scripts` directory

# Update site configuration

Follow the steps below to configure mitmws to use this update repo. By default, mitmws is configured to use this repository
for updates.

1. Click Proxy -> Settings
2. Set the `updates.url` property to `https://github.com/softwaresecured/mitmws-updates`
3. Set the `updates.public_key` property to the contents of the [updatesite.public](https://github.com/softwaresecured/mitmws-updates/blob/main/updatesite.public) file
4. Click Apply

# Required libraries / programs

Some rules require additional programs to function. Below is a list of programs required by rules within this update
repository.

- [zzuf](https://github.com/samhocevar/zzuf)
- [xxd](https://linux.die.net/man/1/xxd)
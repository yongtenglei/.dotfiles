#!/usr/bin/bash
# Connect to eduroam by network manager cli
# change <placeholder> to yours
nmcli con add type wifi con-name "eduroam" ifname wlan0 ssid "eduroam" wifi-sec.key-mgmt wpa-eap 802-1x.identity "<your_account>" 802-1x.password "<your_password>" 802-1x.system-ca-certs yes 802-1x.eap "peap" 802-1x.phase2-auth mschapv2

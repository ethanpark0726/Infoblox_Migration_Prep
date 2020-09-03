# Infoblox_Migration_Prep

  - In order to migrate to new DDI, Infoblox, this script was written to add new helper addresses
  - I used AKiPS, network monitoring tool, to get a device list
  
## Main Logic of this script  
  - Reqeust a device list to AKiPS  
  - Access to the jumpbox  
  - Access to the device  
  - Gather a vlan list with "up" status from each device
  - Using this vlan to retrieve running-configuration (sh run int vlan xxx)
  - Gathering ip helper-address or ip dhcp realy address depends on the OS
  - Save as a xlsx file
  - Using this file to add new helper addresses

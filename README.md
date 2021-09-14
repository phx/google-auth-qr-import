# MFA Importer

This provides a quick way to re-import your MFA backups to mobile MFA tools such as Google Authenticator or Authy by re-converting your text file backup files into QR codes.

The entire process takes less than a minute.  You can import MFA tokens as quickly as you can scan QR codes.

## Usage

```
git clone https://github.com/phx/mfa-importer
cd mfa-importer
pip3 install qrcode
./import.py -f /path/to/exported_file.txt
```


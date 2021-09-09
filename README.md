# Google Authenticator QR Importer

This provides a quick way to re-import your Google Authenticator MFA codes to your mobile device by creating QR codes from the exported `authenticator.txt`.


## Usage

```
git clone https://github.com/phx/google-auth-qr-import
cd google-auth-qr-import
pip3 install qrcode
./import.py -f /path/to/exported_file.txt
```


# certbot-get-certificates
Script to get Let's Encrypt certificates using the certbot Docker image

## Before use
Change the `EMAIL` variable in the `certbot-get-certificates.py` file to your email.

## Usage
Just pass the list of domains you want to obtain a certificate for as command line arguments
### Example
`./certbot-get-certificates.py testdomain.com ciao.testdomain.com www.testdomain2.com`

## Notes
- This script saves the obtained certificates in the `./certbot/conf/` folder
- For every second level domain passed as command line argument, a single certificate containing the second level domain and the `www` third level domain will be created.


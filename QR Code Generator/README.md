# 🔳 QR Code Generator

A Python program that generates **QR codes for different types of information**. Users can create QR codes for **websites, text, contact details, Wi-Fi credentials, or SMS messages**.

---

## **Features**

* Generate QR codes for:

  * Website links
  * Plain text
  * Contact information
  * Wi-Fi credentials
  * SMS messages
* Automatically saves the generated QR code as an image.
* Simple and interactive console interface.
* Validates website domains before generating QR codes.

---

## **Usage**

1. Clone the repository or download `generator.py`.
2. Install the required libraries:

```bash
pip install qrcode[pil] validators
```

3. Run the program:

```bash
python generator.py
```

4. Choose what type of information you want to store in the QR code.
5. Enter the requested information and the program will generate a QR code image.

---

## **Generated Files**

The program saves QR code images with the following names:

* `website_link.png`
* `plain_text.png`
* `contact_info.png`
* `wifi_credentials.png`
* `sms_message.png`

---

## **Technologies Used**

* Python
* qrcode library
* validators library

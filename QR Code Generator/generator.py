# Importing required modules and libraries
import qrcode
import validators

def main():

    while True:
        print("=============================")
        print("QR Code Generator")
        print("=============================")
        print()

        option = int(input(
            "What would you like to store using a QR code?\n"
            "1. Website Link\n"
            "2. Plain Text\n"
            "3. Contact Information\n"
            "4. Wi-Fi Credentials\n"
            "5. SMS Message\n"

        ))

        if option == 1:
            website_link()
            break

        elif option == 2:
            plain_text()
            break

        elif option == 3:
            contact_info()
            break

        elif option == 4:
            wifi_credentials()
            break

        elif option == 5:
            sms_message()
            break

        else:
            print("Select an option between 1 and 5")


def website_link():
    while True:
        domain = input("Enter domain: ")

        if validators.domain(domain):
            image = qrcode.make(domain)
            image.save("website_link.png")
            break
        else:
            print("Enter a valid domain")
            continue


def plain_text():
    text = input("Enter plain text: ")
    image = qrcode.make(text)
    image.save("plain_text.png")


def contact_info():
    full_name = input("Your full name: ")
    phone = input("Your phone number: ")
    email_address = input("Your email address (optional): ")
    image = qrcode.make(f"Full Name: {full_name}\nCell Number: {phone}\nEmail Address: {email_address}")
    image.save("contact_info.png")


def wifi_credentials():
    ssid = input("Wifi Name: ")
    password = input("Wifi Password: ")
    image = qrcode.make(f"Wifi Name: {ssid}\n Wifi Password: {password}")
    image.save("wifi_credentials.png")

def sms_message():
    sms = input("Enter text message: ")
    number = input("Enter phone number (e.g +263773955509): ")
    image = qrcode.make(f"SMSTO:{number}:{sms}")
    image.save("sms_message.png")


main()


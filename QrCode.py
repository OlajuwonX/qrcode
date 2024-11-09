import qrcode

#Data to encode in the Qr code i.e the  website or anything you want to link to the qr code you want to generate.
data = 'https://github.com/OlajuwonX'

#Create a qrcode object with custom prameters
qr = qrcode.QRCode(
    version=2,  # Version 1 is the smallest QR code; increase between 1-40 for larger data capacity (more data can be included)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction level
    box_size=15,  # Size of each box in the QR code (can be more than 13 or lesser, depending on how larger you want the box to be)
    border=8,  # Border thickness (minimum is 4, white space area around the boxes)
)

# Add data to the QR code object
qr.add_data(data)
qr.make(fit=True)  # Automatically adjust size based on the data.

# Create an image from the QR code
img = qr.make_image(fill="black", back_color="white")


# Save the image as a PNG file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
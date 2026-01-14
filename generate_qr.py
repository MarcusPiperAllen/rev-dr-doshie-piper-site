import qrcode
from PIL import Image

# QR Code configuration
url = 'https://drdoshiepiper.com'
fill_color = '#2a2a6c'  # Indigo
back_color = 'white'
output_path = 'images/site-qr-code.png'

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save the QR code
img.save(output_path)
print(f"✅ QR code generated successfully!")
print(f"   URL: {url}")
print(f"   Saved to: {output_path}")
print(f"   Colors: Fill={fill_color}, Background={back_color}")

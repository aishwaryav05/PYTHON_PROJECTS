import qrcode
fill_color = input('Enter the qrcode color(default: black) ') or 'black'
back_color = input('Enter the background color(default: white) ') or 'white'

print(("Enter multiple texts or URLS(type 'done' when finished):"))
data_list = []
while True:

    data = input('Enter the text or url: ').strip()
    if data.lower() == 'done':
        break
    else:
        data_list.append(data)
    
if not data_list:
    print("❌ No data entered. Exiting...")
    exit()

for i, data in enumerate(data_list, start=1):
    filename = f"qr_code_{i}.png"
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=fill_color, back_color = back_color)
    image.save(filename)
    print(f"✅ QR code saved as {filename} (for '{data}')")

print("\n🎉 All QR codes generated successfully!")

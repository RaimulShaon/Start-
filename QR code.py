
# import qrcode as qr
# img = qr.make("https://mail.google.com/mail/u/0/?ogbl#inbox")
# img.save("raimul mail.png")

import qrcode
from PIL import Image
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/watch?v=OKuiyX5k6zg&t=3890s')
qr.make(fit=True)

img = qr.make_image(fill_color="Blue", back_color="white")
img.save("Zandu Balm.png")


    # For More Detail " https://pypi.org/project/qrcode/ "
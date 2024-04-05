from PIL import Image
import qrcode
import requests
from io import BytesIO

# def get_facebook_profile_picture_url(user_id):

#     url = f"https://graph.facebook.com/{user_id}/picture?type=large"

#     response = requests.get(url,allow_redirects=True)
#     print("Respones:" , response.content)
#     if response.status_code == 200:
#         return response.status_code
#     else:
#         print("Error:",response.status_code)
#         return None

def generate_qrcode():
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    data = "https://www.facebook.com/KAYKHAINGOO.kko"

    qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(fill_color="darkblue", back_color="white")

    logo = Image.open("/home/msis/Python/pure_python_projects/QR Code/img/logo.jpg")
    logo = logo.resize((50,50))
    img_w,img_h = img.size
    logo_w,logo_h  = logo.size
    position = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
    img.paste(logo,position)
    img.save("/home/msis/Python/pure_python_projects/QR Code/img/fbprofileqr.jpg")

    # user_id = "KAYKHAINGOO.kko"
    # logo_url = get_facebook_profile_picture_url(user_id)

    # if logo_url:
    #     response = requests.get(logo_url)
    #     if response.status_code == 200:
    #         logo_image = Image.open(BytesIO(response.content))
    #         logo_image = logo_image.resize((50, 50))
    #         img_w, img_h = img.size
    #         logo_w, logo_h = logo_image.size
    #         position = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
    #         img.paste(logo_image, position)
    #         img.save("/home/msis/Python/pure_python_projects/QR Code/img/myprofileqr.png")
    #     else:
    #         print("Error downloading profile picture:", response.status_code)
    # else:
    #     print("Unable to get profile picture URL.")

generate_qrcode()



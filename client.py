import argparse
import requests


def post_requests(image_path, url):
    image = None

    with open(image_path, "rb") as f:
        image = f
        res = requests.post(url, files = {"file" : image})

        if res.status_code != 200:
            print("Error status code {res.status_code}")
            return

        return res.json()


def generate_html(image_src, dst_path = "image.html"):

    html = f'''
    <html>
        <head>
             <title>This is the title</title>
        </head>
        <body>
            <img src = '{image_src}'/>
        </body>
    </html>

    '''
    with open(dst_path, "w") as f:
        f.write(html)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_path", required = True, help = "The path of the test image")
    parser.add_argument("-u", "--url", default = "http://127.0.0.1:5000",  help = "Giving the url")
    args = parser.parse_args()


    result = post_requests(image_path = args.image_path, url = args.url)

    if result is None:
        return
    generate_html(image_src = result["image"])

    print("Done")



if __name__ == "__main__":
    main()

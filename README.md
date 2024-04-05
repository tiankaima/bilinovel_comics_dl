# Bilinovel comics crawler

## Guide

Replace url in `get_urls.py` to your own, example: <https://www.bilinovel.com/novel/2597/catalog>

Then you need to copy two headers from your browser to `get_urls.py` & `download_imgs.py`, the first is to `www.bilinovel.com` and the second is to `img3.readpai.com`.

> [!IMPORTANT]
> Both headers must be set, the first checks UA header to indicate whether or not your browser is supported, the second use Cloudflare so you need to pass the cookie to bypass the check.

Instal required dependencies:

```bash
pip install -r requirements.txt
```

Run `get_urls.py` to get all urls of the comics:

```bash
python get_urls.py
```

Run `download_imgs.py` to download all images:

```bash
mkdir imgs
python download_imgs.py
```

Then use your own tool to make a pdf or cbz...

## License

USE AT YOUR OWN RISK, I'M NOT RESPONSIBLE FOR ANYTHING.

CODE AND REPO MIGHT BE REMOVED IF REQUESTED BY THE COPYRIGHT HOLDER.

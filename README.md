# clipboard-ocr
Perform OCR (Optical Character Recognition) on image present on clipboard

- current implementation requires `xclip` to be installed.
  - On Arch Linux: `sudo pacman -S xclip`
  - On Debian based distros (eg: Ubuntu): `sudo apt install xclip`
- Currently supported OS: Linux

## Usage

```bash
    pip install -r requirements.txt
```
- copy portion of image you want to run OCR on, onto clipboard
- run `program.py`
- OCR will be generated and copied to your clipboard, paste in any text editor to verify

## Upcoming fixes:
- fix issue: will fail if latest clipboard entry is not an image
- fix: don't create temporary files
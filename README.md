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

# Tips:
- use [flameshot](https://flameshot.org/) or [ksnip](https://github.com/ksnip/ksnip) for your screenshot needs.
- If you use KDE, you can set custom shortcuts to run this program whenever you press a keyboard shortcut. You can set this up in the KDE settings. (google KDE custom shortcuts)
  - for other Desktop Environments, do some research.
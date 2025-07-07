# Add White Background to GIF

This script adds a white background to a GIF file, removing any transparency. It works on Windows, macOS, and Linux.

## Requirements
- Python 3.x
- Pillow (https://pypi.org/project/pillow)

## Installation
1. Clone or download this repository.
2. Install dependency:
   ```sh
   pip install pillow
   ```

## Usage
Run the script from the command line:

```sh
python add_white_bg_to_gif.py input.gif output.gif
```
- `input.gif`: The file path to the source GIF file
- `output.gif`: The file path where the new GIF with a background will be saved

## Example
```sh
python add_white_bg_to_gif.py my_animation.gif my_animation_white_bg.gif
```

## Notes
- The script preserves animation, duration, and loop settings of the original GIF.
- If the input file doesn't exist or is not a GIF, an error will be shown. 

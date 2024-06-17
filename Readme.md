# Image Processing and RGB Plot

This Python script opens an image, performs downsampling, and generates RGB scatter plots using Matplotlib. It provides
a simple yet effective way to visualize image data.

## Features

- Opens an image and converts it to a NumPy array.
- Performs downsampling based on a specified factor.
- Generates RGB scatter plots for visualization.
- Supports images in various formats (JPG, JPEG, PNG).
- Support for RGB and RGB + Alpha Channels: Whether your image has RGB channels only or includes an Alpha channel, the
  script can handle both cases for accurate plotting.
- Customizable Downsampling Factor: You can adjust the downsampling factor to fine-tune the level of detail in the
  plotted RGB components, ensuring optimal visualization.
- Simple Usage: With clear instructions and minimal dependencies, the script is easy to use and integrate into your
  image processing workflows.

## Requirements

- Python 3.7+
- NumPy
- PIL (Pillow)
- Matplotlib

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/osstd/plot_rgb_.git
    cd rgb-plot
    ```

2. Install the required packages:

    ```bash
    pip install numpy pillow matplotlib
    ```

3. Edit the main.py file to specify the path to your image:

    ```bash
    image_path = "path/to/your/image"
    ```

4. Run the script:

    ```bash
    python main.py
    ```
   
5. Additional Notes

   Adjust the:
   ```bash 
   downsampling_factor 
   ```
   variable for better readability of pixel values.


## Functionality

- `open_image()` reads the specified image, converts it to a NumPy array, performs downsampling, and extracts RGB values
  for plotting.
- `plot()` generates scatter plots for each RGB channel based on the down sampled image data.

## Example
![Demonstration](https://i.imgur.com/mac8amv.png)

![Demonstration](https://i.imgur.com/B4ZJuDS.png)

## Live Usage
[To Test Live](https://what-is-a-pixel-vercel.vercel.app/upload)
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

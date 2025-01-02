import numpy as np # type: ignore
from PIL import Image # type: ignore


def ft_load(path: str) -> np.array:
    """
    Load an image and return its pixel content as a numpy array.
    The function prints the image format before returning the array.
    
    Parameters:
        path (str): The path to the image file
        
    Returns:
        numpy.array: Array containing the RGB pixel values
        
    Raises:
        Various exceptions with descriptive error messages
    """
    try:
        print(help(Image))
        img = Image.open(path)

        print(f'The image format is: {img.format}')
        if img.mode != 'RGB':
            img = img.convert('RGB')
        return np.array(img)
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")
        raise
#!/usr/bin/python3
"""Image processing module"""
import io
from models.log.error_log import Logger
from PIL import Image


class ImageProcessor:
    """class ImageProcessor - Manipulates images uploaded by user"""
    def __init__(self, image_path=None):
        """
        Instantiates the ImageProcessor class
        
        Args:
            image_path (str): The path to the image file
        """
        self.image = image_path if image_path else None
    
    def resize(self, size=(125, 125)):
        """
        Resizes an image
        
        Args:
            size (tuple): The size of the image to be resized to
        Returns:
            img_byte (bytes): The resized image
        """
        with Image.open(self.image) as img:
            try:
                resized_img = img.resize(size, Image.LANCZOS)
                img_byte = io.BytesIO()
                resized_img.save(img_byte, format='JPEG')
                self.image = img_byte.getvalue()
            except Exception as e:
                Logger.save_log(str(e), __class__.__name__, "Image_Error")
        return self.image

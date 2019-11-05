# Image Load by OpenCV

[Back To Main](../README.md)

1. Prepare your own face photo
    * Notice: You should use your own face picture.
        * Malfunctions can occur if you use a celebrity's face.
    * You can take a picture by using the camera of a cell phone camera or a laptop.
    ~~~
    docker container cp junface.jpg lecture:/git/
    ~~~
2. Code for loading a face photo
    * import opencv
    * set the image path
    * load the image by opencv
    ~~~
    import cv2
    ~~~
# Image Load by OpenCV

[Back To Main](../../README.md)

1. Prepare your own face photo
    * Notice: You should use your own face picture.
        * Malfunctions can occur if you use a celebrity's face.
    * You can take a picture by using the camera of a cell phone camera or a laptop.
    * Let's move our face photos to a shared folder, for example '/c/git/picture'.
    ~~~
    mkdir /c/git/picture
    cp face.jpg /c/git/picture/
    ~~~
2. Code for loading a face photo
    * import opencv
    * set the image path
    * load the image by opencv
    ~~~
    import cv2
    ~~~
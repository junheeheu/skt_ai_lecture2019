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
    imgpath = '../../../junface.jpg'
    savepath = '../../../save_junface.jpg'
    img = cv2.imread(imgpath)
    cv2.imwrite(savepath, img)
    ~~~

3. check saved image
    * copy save image to local
    ~~~
    docker container cp lecture:/git/save_junface.jpg ./
    ~~~
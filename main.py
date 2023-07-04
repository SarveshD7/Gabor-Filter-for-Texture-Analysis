import cv2

def gabor_filter(image):
    filter_1 = cv2.getGaborKernel((50, 50), theta=0, psi=0, lambd=1, sigma=1,gamma=2)
    output = cv2.filter2D(image, -1, filter_1)
    cv2.imshow("Gabor Filter", filter_1)
    cv2.imshow("Output", output)

if __name__ == '__main__':
    image = cv2.imread("T_texture.jpg")
    cv2.imshow("Input", image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gabor_filter(image)
    cv2.waitKey(0)
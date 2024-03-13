# Gradient-based edge detection : Prewitt, Sobel, Kirsch, Roberts operators

A group of edge detection methods using an image intensity gradient - a measure of the intensity change over a specific area. Edges are often characterised by steep gradients. The gradient magnitude and direction at each pixel is computed by convolving the image with a collection of kernels that highlight the horizontal or vertical gradients. Higher gradient magnitudes indicate stronger edges. Various operators with different kernels are used to calculate the gradient magnitude. The Sum of the mask values must be equal to zero.

**Prewitt operator**
Two 3x3 kernels:


**Sobel operator**
Two 3x3 kernels:


At each pixel, the gradient magnitude is obtained by combining all gradient approximations:

The gradient direction is determined using:




**Kirsch operator**
Eight 3x3 kernels with different orientations (0°, 45°, 90°, etc.) to detect edges at multiple angles.


The edge magnitude is calculated as the maximum magnitude across all directions:

The edge direction is determined by the mask producing the maximum magnitude. 

**Roberts cross operator**
two 2x2 kernels, used to detect edges running at 45° to the pixel grid:

The gradient magnitude is given by 

The direction of the gradient is defined as: 











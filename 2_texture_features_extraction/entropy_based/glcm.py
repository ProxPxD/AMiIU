import numpy as np
import mahotas

def glcm(f, ignore_zeros=True):
    '''
    Parameters
    ----------
    f : numpy ndarray
        Image of dimensions N1 x N2.
    ignore_zeros : int, optional
        Ignore zeros in image f. The default is True.

    Returns
    -------
    features_mean : numpy ndarray
        Haralick's 1)Angular Second Moment, 2)Contrast, 
        3)Correlation, 4)Sum of Squares: Variance, 5)Inverse 
        Difference Moment 6)Sum Average, 7)Sum Variance, 8)Sum 
        Entropy, 9)Entropy, 10)Difference Variance, 11)Difference 
        Entropy, 12)Information Measure of Correlation 1, 
        13)Information Measure of Correlation 2, 14)Maximal 
        Correlation Coefficient, mean
    features_range : numpy ndarray
        Haralick's features, same as before but range
    labels_mean : list
        Labels of features_mean.
    labels_range: list
        Labels of features_range.
    '''
       
    # 1) Labels
    labels = ["GLCM_ASM", "GLCM_Contrast", "GLCM_Correlation",
              "GLCM_SumOfSquaresVariance", "GLCM_InverseDifferenceMoment",
               "GLCM_SumAverage", "GLCM_SumVariance", "GLCM_SumEntropy",
               "GLCM_Entropy", "GLCM_DifferenceVariance",
               "GLCM_DifferenceEntropy", "GLCM_Information1",
               "GLCM_Information2", "GLCM_MaximalCorrelationCoefficient"]
    labels_mean = [label + "_Mean" for label in labels]
    labels_range = [label + "_Range" for label in labels]
    
    # 2) Parameters
    f = f.astype(np.uint8)
    
    # 3) Calculate Features: Mean and Range
    features = mahotas.features.haralick(f, 
                                         ignore_zeros=ignore_zeros, 
                                         compute_14th_feature=True,
                                         return_mean_ptp=True)
    features_mean = features[0:14]
    features_range = features[14:]
    
    return features_mean, features_range, labels_mean, labels_range


# Instead of using "mahotas.features.haralick", this implementation can be used to calculate using the co-occurence matrix

# from skimage.feature import greycomatrix, greycoprops

def compute_haralick_features(image_gray):
    # Compute the co-occurrence matrix
    distances = [1]  # Change this to specify different distances
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Change this to specify different angles
    co_occurrence_matrix = greycomatrix(image_gray, distances=distances, angles=angles)

    # Compute Haralick texture features
    properties = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
    haralick_features = []

    for prop in properties:
        feature_mean = np.mean(greycoprops(co_occurrence_matrix, prop))
        feature_range = np.ptp(greycoprops(co_occurrence_matrix, prop))
        haralick_features.extend([feature_mean, feature_range])

    # Return the computed features
    return haralick_features



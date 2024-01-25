# Denoising_using_Autoencoder
Autoencoder is a deep learning architecture (Fig. 1) specifically applied for noise reduction, anomaly detection, domain adaptation, image colorization, etc. [1]. Autoencoders are considered unsupervised learning algorithms. Nonetheless, they are more precisely categorized as self supervised algorithms since they create their own labels from the training dataset [2]. Autoencoders consist of three main components: encoder, latent representation, and decoder. The encoder compresses the input to produce latent representation, which is used in the decoder to reconstruct the input back to the original size of the input. 

![Fig  1](https://user-images.githubusercontent.com/54812742/136612646-44666780-5ab5-4b35-be2c-bd40b56531ee.PNG)

In this project, the Street View House Numbers (SVHN) Dataset - format 2 (i.e., the cropped images) (http://ufldl.stanford.edu/housenumbers/) was used to generate the noisy images (Fig. 2). 

![fig  2](https://user-images.githubusercontent.com/54812742/136611358-62b788a0-ad27-412a-a651-879e76a536aa.PNG)

73,257 RGB noisy images of size 32*32 along with their corresponding raw/clean images, i.e, the SVHN images with no processing, were used to train the model. The Sequential API was used to build the model layer by layer. The random images from the noisy testing dataset, which are not seen by the model, were used to test the model performance. The generated results are shown in Fig. 3. As shown in Fig. 3, the noisy images were remarkably denoised/cleaned through applying autoencoder model.   

![fig  3](https://user-images.githubusercontent.com/54812742/136611938-83f9aa00-7598-4567-8170-c9558793df92.PNG)


# References:
[1] Sreenivas Bhattiprolu's youtube channel (86 - Applications of Autoencoders - Denoising using MNIST dataset), https://www.youtube.com/watch?v=Sm54KXD-L1k

[2] Dertat, 2017: https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798

[3] Naseer, M., Khan, S., Porikli, F. (2018). Indoor scene understanding in 2.5/3d for autonomous agents: A survey. IEEE access, 7, 1859-1887.

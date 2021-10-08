# Denoising_using_Autoencoder
Autoencoder is a deep learning architecture (Fig. 1) specifically applied for noise reduction, anomaly detection, domain adaptation, image colorization, etc. Autoencoders are considered unsupervised learning algorithm. Although they are more precisely categorized as self supervised algorithms since they create their own labels from the training dataset (Dertat, 2017). Autoencoders consist of three main components: encoder, latent representation, and decoder. The encoder compresses the input to preduce latent representation, which is used in the decoder to reconstruct the input back to the original size of the input. 

![image](https://user-images.githubusercontent.com/54812742/136597246-f444232f-f357-4611-9794-255087b46ece.png)




In this project, the Street View House Numbers (SVHN) Dataset - format 2 (i.e., the cropped images) (http://ufldl.stanford.edu/housenumbers/) was used to generate the noisy images (Fig. 2). 

![image](https://user-images.githubusercontent.com/54812742/136598712-5abfc981-82ba-41e2-93f3-5ca2d68ec11a.png)

73257 RGB noisy images of size 32*32 along with their corresponding raw/clean images, i.e, the SVHN images with no processing, were used to train the model. The Sequential API was used, where ...

Then the random images from the noisy testing dataset, which is not seen by the model, were used to test the model performance. The generated results are shown in Fig. 3. As shown in Fig. 3, the noisy images were denoised/cleaned through autoencoder model.   

References:
https://www.youtube.com/watch?v=Sm54KXD-L1k

Naseer, M., Khan, S., Porikli, F. (2018). Indoor scene understanding in 2.5/3d for autonomous agents: A survey. IEEE access, 7, 1859-1887.

Dertat, 2017: https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798

The Street View House Numbers (SVHN) Dataset (http://ufldl.stanford.edu/housenumbers/)

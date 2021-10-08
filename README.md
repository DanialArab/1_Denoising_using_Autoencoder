# Denoising_using_Autoencoder
Autoencoder is a deep learning architecture (Fig. 1) specifically applied for noise reduction, anomaly detection, domain adaptation, image colorization, etc. Autoencoders are considered unsupervised learning algorithm. Although they are more precisely categorized as self supervised algorithms since they create their own labels from the training dataset (https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798). Autoencoders consist of three main components: encoder, latent representation, and decoder. The encoder compresses the input to preduce latent representation, which is used in the decoder to reconstruct the input back to the original size of the input. 

![image](https://user-images.githubusercontent.com/54812742/136597246-f444232f-f357-4611-9794-255087b46ece.png)




In this project, the Street View House Numbers (SVHN)Dataset (http://ufldl.stanford.edu/housenumbers/) was used to generate the noisy images (Fig. 2). 

![image](https://user-images.githubusercontent.com/54812742/136598712-5abfc981-82ba-41e2-93f3-5ca2d68ec11a.png)

Based on the noisy images and the corresponding clean images the model was trained. The trained model was used to 

Sequential model was used, where ...




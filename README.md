# TensorFlow js Example: Classify Gutenberg books 

This project uses Layers API of TensorFlow.js to create a text classifier for three books from [Project Gutenberg](https://www.gutenberg.org/)

* The three books I picked are: Paradise Lost, Macbeth and Bible, each with the first 1000 sentences. 
* All the details are shown in the jupyter notebook.
* Gutenberg-LSTM/index.html and Gutenberg-LSTM/index.js include the JavaScript to launch the demo
* Gutenberg-LSTM/python/ contains my preprocessing, Keras model with LSTM layer and the code for history callback plot
* Gutenberg-LSTM/model_js/ contains my TensorFlow.js model (model.json + shards) and metadata.json

[See the demo live!](https://jielulovesdessert.github.io/Gutenberg-LSTM/)

from keras.src.saving import load_model

model = load_model('afrafck_model/thisworks.h5')
import tensorflowjs as tfjs

tfjs.converters.save_keras_model(model, 'your_model_js')
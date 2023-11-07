import numpy as np

classS = {
        0: 'astilbe',
        1: 'bellflower',
        2: 'black_eyed_susan',
        3: 'calendula',
        4: 'california_poppy',
        5: 'carnation',
        6: 'common_daisy',
        7: 'coreopsis',
        8: 'dandelion',
        9: 'iris',
        10: 'rose',
        11: 'sunflower',
        12: 'tulip',
        13: 'water_lily'
    }

def predict_carsband(model,img):
    image=np.expand_dims(img,axis=0)
    flower = model.predict(image)
    return {'flower':classS[np.argmax([flower[0]])]}

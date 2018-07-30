from sklearn.externals import joblib
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np

dataset_download = datasets.fetch_mldata('MNIST ORIGINAL')


features = np.array(dataset.data, 'int16') 
labels = np.array(dataset.target, 'int')

svc = neW_smv(kernel='rbf',
	max_pool=122,
	bach_size=(22,22),
	epochs=1e-08,
	)

def main_driver():
	if __name__ == '__main()__':
		run.app()
import tablib
import pandas as pd
import numpy as np
from numpy.linalg import norm

# Returns the probability matrix for a given dataset
def probability(df):
	mat = df.as_matrix()
	nrows, ncols = mat.shape
	prob = np.full(mat.shape, 1/nrows)
	# Todo: normalize probability matrix by column
	# prob = np.repeat(norm(prob, axis=0, ord=1), prob.shape[0], axis=0).reshape((prob.shape))
	return np.dstack((mat, prob))
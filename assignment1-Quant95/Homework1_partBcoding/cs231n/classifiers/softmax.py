import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  num_train = X.shape[0]
  num_classes = W.shape[1]
  
  for i in range(num_train):
    scores = np.dot(X[i,:], W)
    exp_scores = np.exp(scores)
    sum_exp = np.sum(exp_scores)
    correct_score = scores[y[i]]
    loss = loss - correct_score + np.log(sum_exp) 
    
    dW[:,y[i]] += -X[i,:]
    for k in range(num_classes):        
        dW[:,k] += (np.exp(np.dot(X[i,:],W[:,k]))/ sum_exp) *X[i,:]
    
  loss /= num_train
  dW /= num_train
    
  loss += 0.5*reg*np.sum(W*W)
  dW += reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  num_train = X.shape[0]
  scores = np.dot(X,W)
  correct_scores = scores[np.arange(num_train), y].reshape(num_train,1)
  sum_exp = np.sum(np.exp(scores), axis=1).reshape(num_train,1)
  loss += np.sum(-correct_scores + np.log(sum_exp))
    
  margin = np.exp(scores)/sum_exp
  margin[np.arange(num_train), y] += -1
  dW = np.dot(X.T, margin)
 
  loss /= num_train
  dW /= num_train
    
  loss += 0.5*reg*np.sum(W*W)
  dW += reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


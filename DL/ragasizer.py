import IPython
import sys
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd

#from music21 import *
#from grammar import *
#from qa import *
#from preprocess import * 
#from music_utils import *
#from data_utils import *
#from outputs import *
#from test_utils import *

from tensorflow.keras.layers import Dense, Activation, Dropout, Input, LSTM, Reshape, Lambda, RepeatVector
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder



x1="""s s r r | g g | m m || p p d d | n n | S S ||"""

x2="""s s r r | g g | m m ||
      r r g g | m m | p p ||
      g g m m | p p | d d ||
      m m p p | d d | n n ||
      p p d d | n n | S S ||
      S S n n | d d | p p ||
      n n d d | p p | m m ||
      d d p p | m m | g g ||
      p p m m | g g | r r ||
      m m g g | r r | s s ||""".replace("\n"," ")

x3="""s s r r | g g | r r ||
      s s r r | g g | m m ||
      r r g g | m m | g g ||
      r r g g | m m | p p ||
      g g m m | p p | m m ||
      g g m m | p p | d d ||
      m m p p | d d | p p ||
      m m p p | d d | n n ||
      p p d d | n n | d d ||
      p p d d | n n | S S ||
      S S n n | d d | n n ||
      S S n n | d d | p p ||
      n n d d | p p | d d ||
      n n d d | p p | m m ||
      d d p p | m m | p p ||
      d d p p | m m | g g ||
      p p m m | g g | m m ||
      p p m m | g g | r r ||
      m m g g | r r | g g ||
      m m g g | r r | s s ||""".replace("\n"," ")

x4="""s s r - s | s r | s r ||
      s s r r | g g | m m ||
      r r g - r | r g | r g ||
      r r g g | m m | p p ||
      g g m - g | g m | g m ||
      g g m m | p p | d d ||
      m m p - m | m p | m p ||
      m m p p | d d | n n ||
      p p d - p | p d | p d ||
      p p d d | n n | S S ||
      S S n - S | S n | S n ||
      S S n n | d d | p p ||
      n n d - n | n d | n d ||
      n n d d | p p | m m ||
      d d p - d | d p | d p ||
      d d p p | m m | g g ||
      p p m - p | p m | p m ||
      p p m m | g g | r r ||
      m m g - m | m g | m g ||
      m m g g | r r | s s ||""".replace("\n"," ")

x5="""s s r r | g - s | r g ||
      s s r r | g g | m m ||
      r r g g | m - r | g m ||
      r r g g | m m | p p ||
      g g m m | p - g | m p ||
      g g m m | p p | d d ||
      m m p p | d - m | p d ||
      m m p p | d d | n n ||
      p p d d | n - p | d n ||
      p p d d | n n | S S ||
      S S n n | d - S | n d ||
      S S n n | d d | p p ||
      n n d d | p - n | d p ||
      n n d d | p p | m m ||
      d d p p | m - d | p m ||
      d d p p | m m | g g ||
      p p m m | g - p | m g ||
      p p m m | g g | r r ||
      m m g g | r - m | g r ||
      m m g g | r r | s s ||""".replace("\n"," ")

x6= """s s , r | r , | g g ||
      s s r r | g g | m m ||
      r r , g | g , | m m ||
      r r g g | m m | p p ||
      g g , m | m , | p p ||
      g g m m | p p | d d ||
      m m , p | p , | d d ||
      m m p p | d d | n n ||
      p p , d | d , | n n ||
      p p d d | n n | S S ||
      S S , n | n , | d d ||
      S S n n | d d | p p ||
      n n , d | d , | p p ||
      n n d d | p p | m m ||
      d d , p | p , | m m ||
      d d p p | m m | g g ||
      p p , m | m , | g g ||
      p p m m | g g | r r ||
      m m , g | g , | r r ||
      m m g g | r r | s s ||""".replace("\n"," ")

x7="""s , s r | , r | g g ||
      s s r r | g g | m m ||
      r , r g | , g | m m ||
      r r g g | m m | p p ||
      g , g m | , m | p p ||
      g g m m | p p | d d ||
      m , m p | , p | d d ||
      m m p p | d d | n n ||
      p , p d | , d | n n ||
      p p d d | n n | S S ||
      S , S n | , n | d d ||
      S S n n | d d | p p ||
      n , n d | , d | p p ||
      n n d d | p p | m m ||
      d , d p | , p | m m ||
      d d p p | m m | g g ||
      p , p m | , m | g g ||
      p p m m | g g | r r ||
      m , m g | , g | r r ||
      m m g g | r r | s s ||""".replace("\n"," ")
x8="""s s s r | r r | g g ||
      s s r r | g g | m m ||
      r r r g | g g | m m ||
      r r g g | m m | p p ||
      g g g m | m m | p p ||
      g g m m | p p | d d ||
      m m m p | p p | d d ||
      m m p p | d d | n n ||
      p p p d | d d | n n ||
      p p d d | n n | S S ||
      S S S n | n n | d d ||
      S S n n | d d | p p ||
      n n n d | d d | p p ||
      n n d d | p p | m m ||
      d d d p | p p | m m ||
      d d p p | m m | g g ||
      p p p m | m m | g g ||
      p p m m | g g | r r ||
      m m m g | g g | r r ||
      m m g g | r r | s s ||""".replace("\n"," ")

x9="""s , r g | , - s | r g ||
      s s r r | g g | m m ||
      r , g m | , - r | g m ||
      r r g g | m m | p p ||
      g , m p | , - g | m p ||
      g g m m | p p | d d ||
      m , p d | , - m | p d ||
      m m p p | d d | n n ||
      p , d n | , - p | d n ||
      p p d d | n n | S S ||
      S , n d | , - S | n d ||
      S S n n | d d | p p ||
      n , d p | , - n | d p ||
      n n d d | p p | m m ||
      d , p m | , - d | p m ||
      d d p p | m m | g g ||
      p , m g | , - p | m g ||
      p p m m | g g | r r ||
      m , g r | , - m | g r ||
      m m g g | r r | s s ||""".replace("\n"," ")

x10= """s r , g | , - s | r g ||
        s s r r | g g | m m ||
        r g , m | , - r | g m ||
        r r g g | m m | p p ||
        g m , p | , - g | m p ||
        g g m m | p p | d d ||
        m p , d | , - m | p d ||
        m m p p | d d | n n ||
        p d , n | , - p | d n ||
        p p d d | n n | S S ||
        S n , d | , - S | n d ||
        S S n n | d d | p p ||
        n d , p | , - n | d p ||
        n n d d | p p | m m ||
        d p , m | , - d | p m ||
        d d p p | m m | g g ||
        p m , g | , - p | m g ||
        p p m m | g g | r r ||
        m g , r | , - m | g r ||
        m m g g | r r | s s ||""".replace("\n"," ")

x11="""s , r , | g - s | r g ||
      s s r r | g g | m m ||
      r , g , | m - r | g m ||
      r r g g | m m | p p ||
      g , m , | p - g | m p ||
      g g m m | p p | d d ||
      m , p , | d - m | p d ||
      m m p p | d d | n n ||
      p , d , | n - p | d n ||
      p p d d | n n | S S ||
      S , n , | d - S | n d ||
      S S n n | d d | p p ||
      n , d , | p - n | d p ||
      n n d d | p p | m m ||
      d , p , | m - d | p m ||
      d d p p | m m | g g ||
      p , m , | g - p | m g ||
      p p m m | g g | r r ||
      m , g , | r - m | g r ||
      m m g g | r r | s s ||""".replace("\n"," ")

x12 = """s s m m | g g | r r ||
        s s r r | g g | m m ||
        r r p p | m m | g g ||
        r r g g | m m | p p ||
        g g d d | p p | m m ||
        g g m m | p p | d d ||
        m m n n | d d | p p ||
        m m p p | d d | n n ||
        p p S S | n n | d d ||
        p p d d | n n | S S ||
        S S p p | d d | n n ||
        S S n n | d d | p p ||
        n n m m | p p | d d ||
        n n d d | p p | m m ||
        d d g g | m m | p p ||
        d d p p | m m | g g ||
        p p r r | g g | m m ||
        p p m m | g g | r r ||
        m m s s | r r | g g ||
        m m g g | r r | s s ||""".replace("\n"," ")


l1=[]
l1.append([i for i in x2.split(" ") if i])
l1.append([i for i in x3.split(" ") if i])
l1.append([i for i in x4.split(" ") if i])
l1.append([i for i in x5.split(" ") if i])
l1.append([i for i in x6.split(" ") if i])
l1.append([i for i in x7.split(" ") if i])
l1.append([i for i in x8.split(" ") if i])
l1.append([i for i in x9.split(" ") if i])
l1.append([i for i in x10.split(" ") if i])
l1.append([i for i in x11.split(" ") if i])
l1.append([i for i in x12.split(" ") if i])



maxLen = float('-inf')
for i in l1:
  if maxLen < len(i):
    maxLen = len(i)
for i in range(len(l1)):
  if len(l1[i])<maxLen:
    l1[i]=l1[i]+[" "]*(maxLen-len(l1[i]))
for i in l1:
  print(len(i))
lo=np.array(l1)




# define example
data = l1[3]
values = array(data)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False,handle_unknown = 'ignore')
#integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(values.reshape(len(values), 1))
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[20, :])])
print(inverted)


X=np.zeros([11,230,11])

Y=np.zeros([230,11,11])


for i in range(0,len(l1)):
    values = array(l1[i])
    onehot_encoded = onehot_encoder.transform(values.reshape(len(values), 1))
    X[i,:]=onehot_encoded
    
    values=np.roll(values,-1)
    onehot_encoded = onehot_encoder.transform(values.reshape(len(values), 1))
    Y[:,i,:]=onehot_encoded

# number of dimensions for the hidden state of each LSTM cell.
n_a = 64 


n_values = 11 # number of music values
reshaper = Reshape((1, n_values))                  # Used in Step 2.B of djmodel(), below
LSTM_cell = LSTM(n_a, return_state = True)         # Used in Step 2.C
densor = Dense(n_values, activation='softmax')     # Used in Step 2.D

def djmodel(Tx, LSTM_cell, densor, reshaper):
    """
    Implement the djmodel composed of Tx LSTM cells where each cell is responsible
    for learning the following note based on the previous note and context.
    Each cell has the following schema: 
            [X_{t}, a_{t-1}, c0_{t-1}] -> RESHAPE() -> LSTM() -> DENSE()
    Arguments:
        Tx -- length of the sequences in the corpus
        LSTM_cell -- LSTM layer instance
        densor -- Dense layer instance
        reshaper -- Reshape layer instance
    
    Returns:
        model -- a keras instance model with inputs [X, a0, c0]
    """
    # Get the shape of input values
    n_values = densor.units
    
    # Get the number of the hidden state vector
    n_a = LSTM_cell.units
    
    # Define the input layer and specify the shape
    X = Input(shape=(Tx, n_values)) 
    
    # Define the initial hidden state a0 and initial cell state c0
    # using `Input`
    a0 = Input(shape=(n_a,), name='a0')
    c0 = Input(shape=(n_a,), name='c0')
    a = a0
    c = c0
    ### START CODE HERE ### 
    # Step 1: Create empty list to append the outputs while you iterate (≈1 line)
    outputs = []
    
    # Step 2: Loop over tx
    for t in range(Tx):
        
        # Step 2.A: select the "t"th time step vector from X. 
        x = X[:,t,:]
        # Step 2.B: Use reshaper to reshape x to be (1, n_values) (≈1 line)
        x = reshaper(x)
        #print(x.shape)
        # Step 2.C: Perform one step of the LSTM_cell
        a, _, c = LSTM_cell(inputs=x, initial_state=[a,c])
        # Step 2.D: Apply densor to the hidden state output of LSTM_Cell
        out = densor(a)
        # Step 2.E: add the output to "outputs"
        outputs=outputs+[out]
        
        # Step 3: Create model instance
        model = Model(inputs=[X, a0, c0], outputs=outputs)
    
    
    return model
model = djmodel(Tx=230, LSTM_cell=LSTM_cell, densor=densor, reshaper=reshaper)


opt = Adam(learning_rate=0.1, beta_1=0.9, beta_2=0.999)

model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

m = 11
a0 = np.zeros((m, n_a))
c0 = np.zeros((m, n_a))
print(len(X[1]))
print(len(a0))
print(len(c0))

history = model.fit([X, a0, c0], list(Y), epochs=200, verbose = 1)

print(f"loss at epoch 1: {history.history['loss'][0]}")
print(f"loss at epoch 100: {history.history['loss'][99]}")
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')

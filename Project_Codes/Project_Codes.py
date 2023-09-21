#!/usr/bin/env python
# coding: utf-8

# In[1]:


#############################################################################
###            IMPORTING THE REQUIRED LIBRARIES
#############################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sgnl
from IPython.lib.display import Audio
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import zplane
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


#############################################################################
###            3 Types of Frying Sounds Were Used in Our Project
#############################################################################
# We can get their size information and sampling frequencies
# by reading the frying sound files in the background.
Fs_Frying1, Frying1 = read('frying_potatoes.wav')
Fs_Frying2, Frying2 = read('frying_fish.wav')
Fs_Frying3 ,Frying3 = read('frying_chicken.wav')


# In[3]:


#############################################################################
###           Size information of the frying sounds we used
#############################################################################
print('Size of French fries sound',Frying1.shape)
print('Size of fish fry sound',Frying2.shape)
print('Size of fried chicken sound',Frying3.shape)


# In[4]:


#############################################################################
###    Sampling frequency information of the frying sounds we used
#############################################################################
print('Sampling Frequency of French Fries Sound',Fs_Frying1)
print('Sampling Frequency of Fish Fry Sound',Fs_Frying2)
print('Sampling Frequency of Chicken Frying Sound',Fs_Frying3)


# ### Our frying sound files are 2-channel and there are 882000 samples in each channel. The sampling frequency of these sounds is 44100 Hz.

# In[5]:


#############################################################################
###       We only need to use 1 of the frying audio channels
#############################################################################
Frying_xn1 = Frying1[:,1]
Frying_xn2 = Frying2[:,1]
Frying_xn3 = Frying3[:,1]


# In[6]:


#############################################################################
###                Defining n and N's for frying sounds
#############################################################################
Frying_N1 = len(Frying1)
Frying_N2 = len(Frying2)
Frying_N3 = len(Frying3)
# yatay eksen aralıkları
Frying_n1=np.arange(0,Frying_N1)
Frying_n2=np.arange(0,Frying_N2)
Frying_n3=np.arange(0,Frying_N3)


# In[7]:


#########################################
#  Let's draw the sound of french fries
#########################################
plt.figure()
plt.stem(Frying_n1,Frying_xn1)
plt.xlabel("Sample")
plt.ylabel("Frying_Potatoes_x1[n]")
plt.show()


# In[8]:


#########################################
#    Let's draw the fish fry sound
#########################################
plt.figure()
plt.stem(Frying_n2,Frying_xn2)
plt.xlabel("Sample")
plt.ylabel("Frying_Fish_x2[n]")
plt.show()


# In[9]:


#########################################
# Let's draw the sound of fried chicken
#########################################
plt.figure()
plt.stem(Frying_n3,Frying_xn3)
plt.xlabel("Sample")
plt.ylabel("Frying_Chicken_x3[n]")
plt.show()


# ### Kızartma seslerinin fourier dönüşümlerini alarak bu seslerin frekans spektrumlarını inceleyelim

# In[10]:


N = 200
w=np.linspace(-np.pi,np.pi-(2*np.pi/N),N)

Frying_xw1=np.fft.fftshift(np.fft.fft(Frying_xn1,N)/N)
Frying_xw2=np.fft.fftshift(np.fft.fft(Frying_xn2,N)/N)
Frying_xw3=np.fft.fftshift(np.fft.fft(Frying_xn3,N)/N)


# In[11]:


plt.figure()
plt.plot(w/np.pi,np.abs(Frying_xw1))
plt.title("French fries sound spectrum")
plt.xlabel("Frequency x$\\pi$ rad/sample")
plt.show()


# In[12]:


plt.figure()
plt.plot(w/np.pi,np.abs(Frying_xw2))
plt.title("Fish fry sound spectrum")
plt.xlabel("Frequency x$\\pi$ rad/sample")
plt.show()


# In[13]:


plt.figure()
plt.plot(w/np.pi,np.abs(Frying_xw3))
plt.title("Chicken fry sound spectrum")
plt.xlabel("Frequency x$\\pi$ rad/sample")
plt.show()


# In[14]:


#############################################################################
###            Let's add Frying + Speech Sounds to our PROJECT
#############################################################################
# Let's get the size information and sampling frequencies
Fs_Frying_Speech1, Frying_Speech1 = read('Speech_plus_Frying1.wav')
Fs_Frying_Speech2, Frying_Speech2 = read('Speech_plus_Frying2.wav')
Fs_Frying_Speech3 ,Frying_Speech3 = read('Speech_plus_Frying3.wav')


# In[15]:


#############################################################################
###    Sampling Frequency Information of Frying + Speech Sounds We Used
#############################################################################
print('Sampling Frequency of French Fries + Speech Audio',Fs_Frying_Speech1)
print('Sampling Frequency of Fish Fry + Speech Audio',Fs_Frying_Speech2)
print('Sampling Frequency of Fried Chicken + Speech Audio',Fs_Frying_Speech3)


# In[16]:


#############################################################################
###    It is Enough to Use Only 1 of the Frying + Talking Audio Channels
#############################################################################
Frying_Speech_xn1 = Frying_Speech1[:,1]
Frying_Speech_xn2 = Frying_Speech2[:,1]
Frying_Speech_xn3 = Frying_Speech3[:,1]


# In[17]:


#############################################################################
###          Identifying n's and N's for Roast + Speech Sounds
#############################################################################
Frying_Speech_N1 = len(Frying_Speech1)
Frying_Speech_N2 = len(Frying_Speech2)
Frying_Speech_N3 = len(Frying_Speech3)


# In[18]:


# horizontal axis ranges
Frying_Speech_n1=np.arange(0,Frying_Speech_N1)
Frying_Speech_n2=np.arange(0,Frying_Speech_N2)
Frying_Speech_n3=np.arange(0,Frying_Speech_N3)


# In[19]:


Fs_Speech_and_Frying1, Speech_and_Frying1 = read('Speech_plus_Frying1.wav')
print('Speech Voice 1 Sampling Frequency',Fs_Speech_and_Frying1)
Speech_and_Frying11 = Speech_and_Frying1[:,1]
print("Unfiltered speaking voice 1")
display(Audio(Speech_and_Frying11, rate=44100))


# In[20]:


b,a = sgnl.butter(10 , 0.06, 'lowpass')
filtered1 = sgnl.lfilter(b, a, Speech_and_Frying11)
print("Filtered speech audio")
display(Audio(filtered1, rate=44100))


# In[21]:


Fs_Speech_and_Frying2, Speech_and_Frying2 = read('Speech_plus_Frying2.wav')
print('Speech Voice 2 Sampling Frequency',Fs_Speech_and_Frying2)
Speech_and_Frying22 = Speech_and_Frying2[:,1]
print("Unfiltered speaking voice 2")
display(Audio(Speech_and_Frying22, rate=44100))


# In[22]:


b,a = sgnl.butter(10 , 0.06, 'lowpass')
filtered2 = sgnl.lfilter(b, a, Speech_and_Frying22)
print("Filtered speech audio 2")
display(Audio(filtered2, rate=44100))


# In[23]:


Fs_Speech_and_Frying3, Speech_and_Frying3 = read('Speech_plus_Frying3.wav')
print('Speech Voice 3 Sampling Frequency',Fs_Speech_and_Frying3)
Speech_and_Frying33 = Speech_and_Frying3[:,1]
print("Unfiltered speaking voice 3")
display(Audio(Speech_and_Frying33, rate=44100))


# In[24]:


b,a = sgnl.butter(10 , 0.06, 'lowpass')
filtered3 = sgnl.lfilter(b, a, Speech_and_Frying33)
print("Filtered speech audio 3")
display(Audio(filtered3, rate=44100))


# In[25]:


print(b)


# In[26]:


print(a)


# In[27]:


w, hw = sgnl.freqz(b, a)
plt.figure()
plt.semilogx(w / np.pi, 20 * np.log10(abs(hw)))
plt.title("Butterworth filter frequency response")
plt.xlabel("Frequency x$\\pi$ rad/sample")
plt.ylabel("Amplitude [dB]")
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(0.06, color='green') # cutoff radian frequency
plt.show()


# In[28]:


hw_phs = np.unwrap(np.angle(hw))
plt.figure()
plt.title("Butterworth filter phase response")
plt.plot(w/np.pi, hw_phs)
plt.ylabel("Degrees")
plt.xlabel("Frequency x$\\pi$ rad/sample")


# In[29]:


tau_w = -np.diff(hw_phs)*(N/(2*np.pi))
plt.figure()
plt.title("Butterworth group delay")
plt.plot(w[1::]/np.pi, tau_w)
plt.ylabel("samples"), plt.xlabel("Frequency x$\\pi$ rad/sample")
plt.grid()


# In[30]:


z,p,k = sgnl.butter(10 , 0.06, 'lowpass',output='zpk')
b,a = sgnl.zpk2tf(z,p,k)
zplane.zplane(b,a)


# In[31]:


n, hn = sgnl.dimpulse((b,a,1), n=100)
plt.figure()
plt.stem(n, np.squeeze(hn))
plt.title("Filter impulse response")
plt.xlabel("Sample")
plt.show()


# ### As can be seen from the graphs, the phase response of the filter is not linear, therefore the group delay is not constant. These features are IIR filter features. Since the Butterworth filter has been designed, such graphs are expected to appear.

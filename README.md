# "Reducing Speech Noise"

## Objective:
The primary objective of this project is to minimize noise in an audio signal contaminated with noise, striving to attain the cleanest possible output.

## Methodology:
In this project, we tackle the challenge of reducing noise in an audio signal that has been marred by unwanted interference. The key element in this endeavor is a filtering system enclosed within a box. Its primary role is to diligently eliminate as much noise as possible, resulting in a clearer rendition of the spoken word. Therefore, at its core, this system revolves around the implementation of a filtering mechanism.

As a practical application within this project, we introduced the sizzling sounds of various foods into the voices of different adult speakers. Our objective is to effectively suppress the background noise caused by these frying sounds during conversations.

The project is executed using Python on the Anaconda platform. The process involves an initial analysis of the amplitude spectrum of the noise-contaminated audio signal. Subsequently, a tailored filter is designed to cover the bandwidth of the noise, aiming to reduce its impact.

## Results:
The application of a low-pass filter did succeed in reducing the frying noise to a certain extent. However, it was unable to entirely eliminate the noise. One possible explanation for this incomplete noise suppression might be the presence of noise components within the filter's passband.

Furthermore, since certain components of the speech signals extended beyond the passband of the filter, some distortion in the speech sound occurred.

## Challenges:
The most daunting aspect of noise reduction typically revolves around determining the precise parameters and thresholds for the gating process. This entails careful selection of window sizes, overlap, and the establishment of threshold levels to differentiate between noise and signal components within the spectral domain. Moreover, managing complex audio signals characterized by diverse noise characteristics and ensuring that the gating process doesn't compromise the quality of the desired signal can present significant challenges.2

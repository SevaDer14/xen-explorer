# Xen Explorer

## About
This is the simple program to generate inharmonic spectrum, calculate its dissonance curve and save it as an audio sample. The dissonance curve calculation is based on William Sethares work from book 'Tuning, Timbre. Spectrum, Scale'. It allows to generate samples that harmonize in unusual tunings in which usual harmonic sounds will sound out of tune. The code is open, feel free to fork it and suggest your changes. But the plan is to make a web version of it, for ease of use of everybody.

Used for some vids on Objetive Harmony YT channel https://www.youtube.com/channel/UCPDmqGWT3zj9m6EMznlEvEA

## Contact for Qustions and Suggestions
email: objectiveharmony@gmail.com

## How To Use
### Installation (Windows)

The program is written in Python programming language, so you need to have it installed. Download and install latest version from https://www.python.org/downloads/

Next download and unzip Xen Explorer files
![image](https://user-images.githubusercontent.com/79849155/164470409-cf0889d7-b846-40b2-850c-09e0f8c857ec.png)

There are two files. To run the program double click the GUI.py. It contains user interface and imports XenToolkin.py that contains all functions to perform calculations. If all is good, it will open a console and Xen Explorer user interface.

![image](https://user-images.githubusercontent.com/79849155/164472328-eeb15bb0-6617-4e21-a688-b9ce8891ae67.png)

### Generating Spectrum
#### Manual Entry
First you need to generate a spectrum. You can do it manually in the section on the left. Enter frequency in Hertz and Amplitude as a number from 0 to 1 and press `Add`.

![image](https://user-images.githubusercontent.com/79849155/164473330-447ab766-fd27-42c6-b062-4654ffb1daaa.png)

This will add partial to the spectrum

![image](https://user-images.githubusercontent.com/79849155/164473983-7692f4bb-5b42-48e0-9fba-66df79ea541a.png)

To remove partial, select frequency and amplitude you want to remove and press `Remove`

![image](https://user-images.githubusercontent.com/79849155/164474599-551995ea-c18b-454d-888d-b5a7e0d94f2a.png)

Pressing `Clear` will remove all partials.

![image](https://user-images.githubusercontent.com/79849155/164475081-a2e5d81f-8fcf-43f8-b67e-fe3abf5e0f6c.png)

#### Importing Spectrum
Another way is to import spectrum using `Import Spectrum` button. It will ask you to select text file from which to import spectrum. File should be a plain text file (ex .txt) with "." (dot) as decimal separator and tab as column separator.

#### Calculating spectrum

You can also use an algorithm to generate spectrum. There are three parameters that you can tweak. 
1) `Spectrum type` can be *harmonic* (usual musical instruments and voice have that spectrum) or *m-tet (edo)*. Latter is for generating spectrum that relates to tuning with steps that equally divide an octave. Contemporary pianos are tuned to 12-tet or 12-edo meaning they have 12 notes withing 1 octave that are the same distance from each other. You can generate spectrums for 3, 5, 7, 13 , 42 or any number of equally spaced notes in octave.
2) `Fundamental` is responsible for the pitch of note spectrum of which is generated. By default it is set to A 440Hz. You can specify exact number in Hertz or choose C0 which is the lowest note human ear can hear.
3) `Number of partials` defines how much partials (harmonics) a generated spectrum will have. It is useful if you are analyzing spectrum using dissonance curves, as having too much partials is not desired. Otherwise, you can choose *All* which will generate partials up until 20000Hz.

After setting desired parameters press `Calculate Spectrum`.

![image](https://user-images.githubusercontent.com/79849155/164502579-bd625d35-6f39-491d-a00a-a74c436135c6.png)

### Plotting Spectrum
When having some spectrum, press `Plot Spectrum` to plot it. It will open a window with the graph in which Y-axis is amplitude and X-axis is frequency (in Hertz), blue lines represent partials of the spectrum and dashed grey lines frequencies of harmonic spectrum for given fundamental.

**Here is 6 first partials of harmonic spectrum for note A 440Hz**
![image](https://user-images.githubusercontent.com/79849155/164503711-689f431c-7117-419c-94b7-46792dcec594.png)

**Here is full 12-tet spectrum for A 440Hz**
![image](https://user-images.githubusercontent.com/79849155/164504077-c4b18f7c-23d8-42ff-8d19-d1a3f83d024b.png)

You can see that if blue lines do not coincide with dashed grey lines, generated spectrum deviates from harmonic spectrum and thus is inharmonic.

### Calculating and plotting Dissonance Curve
Dissonance curve is the way to graphically find pitches at which the spectrum harmonizes  with itself or other spectrums. Minimums in dissonance curve mark the intervals at which partials of two spectrums coincide thus creating a harmony with each other.

You can calculate dissonance curve for your spectrum. It has 2 parameters:
1) `Dissonance Type` is type of algorithm to calculate dissonance curve (Sethares 2 is tested to give correct results)
2) `Sweep Type` is type of spectrum that is swept against the one you generated when calculating dissonance curve. *Same* will use the same spectrum as yours. This way you test your spectrum against itself to find related tuning for that spectrum. However sometimes you may want to test is against harmonic spectrum. For that matter choose *Harmonic* and specify number of harmonics. Try that if you plan to have inharmonic and harmonic instruments playing at the same time in you composition.

**Dissonance curve for note A 440Hz with harmonic spectrum with 6 partials**
![image](https://user-images.githubusercontent.com/79849155/164507575-e1117319-1ec7-4acd-b346-32ed31d32e5f.png)

### Export
You can export Spectrum and Dissonance Curve as text files to use elsewhere. To do it type `File Name Prefix` and press `Export Data`. That will generate 2 files in the directory of Xen Explorer program.

![image](https://user-images.githubusercontent.com/79849155/164508181-d82a2c66-1996-4b93-b80c-b6b396461006.png)

To save .wav sample of your spectrum, enter `Sample Rate` and `Duration` (duration of sample in seconds) and press `Export .wav`

![image](https://user-images.githubusercontent.com/79849155/164508477-93ecb20b-c43e-4530-89ed-f4361685604c.png)

Calculation goes a bit slow. You can see the progress in the console and when the export is finished it will alert you that all is done. Reducing Sample Rate and duration helps to speed things up.

![image](https://user-images.githubusercontent.com/79849155/164509033-63850c64-1be2-4645-beda-a510af3a1fd7.png)


## Plans To Do
- add stretched spectrum option to spectrum type
- clean up the code
- dissonance curve 12-tet bug
- option to calculate dissonance curve for 1 octave

End goal is to have web app with extended functionality. 

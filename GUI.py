import XenToolkit as xen
from tkinter import *

root = Tk()
root.title('Xen Explorer')
spectrum = []
dissonance_curve = []
SpectrumTypeMethod = IntVar()
FundamentslMethod = IntVar()
NumberofPartialsMethod = IntVar()
DissonanceTypeMethod = IntVar()
SweepTypeMethod = IntVar()
calculated_key = 0

# PROCEDURES

def add_to_listboxes():
    spectrum = []
    for i in range(len(frequeny_listbox.get(0, "end"))):
        spectrum.append([float(frequeny_listbox.get(i)), float(amplitude_listbox.get(i))])

    spectrum.append([float(frequency_entry.get()), float(amplitude_entry.get())])
    spectrum.sort()

    frequeny_listbox.delete(0, END)
    amplitude_listbox.delete(0, END)

    for partial in spectrum:
        frequeny_listbox.insert(END, float(partial[0]))
        amplitude_listbox.insert(END, float(partial[1]))


def remove_from_listboxes():
    frequeny_listbox.delete(ANCHOR)
    amplitude_listbox.delete(ANCHOR)


def clear_listboxes():
    frequeny_listbox.delete(0, END)
    amplitude_listbox.delete(0, END)


def calculate_spectrum():
    #global spectrum, octave

    if SpectrumTypeMethod.get() == 1:
        spectrum_type = 'h'
    else:
        spectrum_type = mtet_entry.get()
    if FundamentslMethod.get() == 1:
        fundamental = 32.70
    else:
        fundamental = float(fundamental_entry.get())
    if NumberofPartialsMethod.get() == 1:
        numberofpartials = int(round(20000 / fundamental, 0))
    else:
        numberofpartials = numberofpartials_entry.get()

    spectrum = xen.calculate_spectrum(spectrum_type, fundamental, numberofpartials, DissonanceTypeMethod.get())

    frequeny_listbox.delete(0, END)
    amplitude_listbox.delete(0, END)

    for partial in spectrum:
        frequeny_listbox.insert(END, float(partial[0]))
        amplitude_listbox.insert(END, float(partial[1]))

    # if int(numberofpartials_entry.get()) == 1:
    #     octave = 2
    # else:
    #     octave = spectrum[1][0]/spectrum[0][0]


def import_spectrum():
    frequeny_listbox.delete(0, END)
    amplitude_listbox.delete(0, END)

    file_path = filedialog.askopenfilename()

    f = open(file_path, 'r')
    for line in f:
        line = line.strip()
        string = line.split()
        freq = string[0]
        amp = string[1]
        frequeny_listbox.insert(END, float(freq))
        amplitude_listbox.insert(END, float(amp))


def plot_spectrum():
    spectrum = []

    for i in range(len(frequeny_listbox.get(0, "end"))):
        spectrum.append([float(frequeny_listbox.get(i)), float(amplitude_listbox.get(i))])

    xen.plot_spectrum(spectrum)


def calculate_dissonance_curve():
    # global dissonance_curve
    spectrum = []

    if float(numberofpartials_entry.get()) == 1:
        octave = 2
    else:
        octave = frequeny_listbox.get(1)/frequeny_listbox.get(0)

    for i in range(len(frequeny_listbox.get(0, "end"))):
        spectrum.append([float(frequeny_listbox.get(i)), float(amplitude_listbox.get(i))])

    dissonance_curve = xen.normalization_to_one(
        xen.calculate_dissonance_curve(spectrum, DissonanceTypeMethod.get(), 10, octave, SweepTypeMethod.get(),
                                       int(sweepnumberofpartials_entry.get())))
    return dissonance_curve


def show_dissonance_curve():
    if float(numberofpartials_entry.get()) == 1:
        octave = 2
    else:
        octave = frequeny_listbox.get(1)/frequeny_listbox.get(0)
    #octave = frequeny_listbox.get(1)/frequeny_listbox.get(0)
    dissonance_curve = calculate_dissonance_curve()
    xen.plot_dissonance_curve(dissonance_curve, octave)


def export_to_wav():
    spectrum = []

    for i in range(len(frequeny_listbox.get(0, "end"))):
        spectrum.append([float(frequeny_listbox.get(i)), float(amplitude_listbox.get(i))])

    xen.export_wave_file(spectrum, int(samplerate_entry.get()), float(duration_entry.get()),
                         str(filenameprefix_entry.get()) + ' (' + duration_entry.get() + ' second sample)')


def export_dissonance_curve():
    dissonance_curve = calculate_dissonance_curve()
    filename = filenameprefix_entry.get() + ' (dissonance curve).txt'
    with open(filename, "w") as txt_file:
        for line in dissonance_curve:
            txt_file.write(str(line[0]) + ', ' + str(line[1]) + "\n")
    print('Dissonance Curve Export Finished')


def export_spectrum_data():
    spectrum = []

    for i in range(len(frequeny_listbox.get(0, "end"))):
        spectrum.append([float(frequeny_listbox.get(i)), float(amplitude_listbox.get(i))])

    filename = filenameprefix_entry.get() + ' (spectrum).txt'
    with open(filename, "w") as txt_file:
        for line in spectrum:
            txt_file.write(str(line[0]) + ', ' + str(line[1]) + "\n")
    print('Spectrum Export Finished')


def export_data():
    export_dissonance_curve()
    export_spectrum_data()

                                                    # CREATING WIDGETS


#              LISTBOXES
frequeny_listbox = Listbox(root, height=12, width=10, bg='gray85', exportselection=0)
frequeny_listbox.grid(row=1, rowspan=5, column=0, sticky=N)

amplitude_listbox = Listbox(root, height=12, width=10,  bg='gray85', exportselection=0)
amplitude_listbox.grid(row=1, rowspan=5, column=1, sticky=N)


#             TEXT LABELS
lable_Frequency = Label(root, text='Frequency', font='Helvetica 9 bold')
lable_Frequency.grid(row=0, column=0, columnspan=4, sticky=W)

lable_Amplitude = Label(root, text='Amplitude', font='Helvetica 9 bold')
lable_Amplitude.grid(row=0, column=1, columnspan=4, sticky=W)

lable_SpectrumType = Label(root, text="Spectrum Type:", font='Helvetica 9 bold')
lable_SpectrumType.grid(row=1, column=3, sticky = E)

lable_Steps = Label(root, text="Steps")
lable_Steps.grid(row=1, column=7)

lable_Fundamental = Label(root, text="Fundamental:", font='Helvetica 9 bold')
lable_Fundamental.grid(row=2, column=3, sticky = E)

lable_Hz1 = Label(root, text="Hz")
lable_Hz1.grid(row=2, column=7, sticky = W)

lable_NumberofPartials = Label(root, text="Number of partials:", font='Helvetica 9 bold')
lable_NumberofPartials.grid(row=3, column=3, sticky = E)

lable_DissonanceType = Label(root, text="Dissonance Type:", font='Helvetica 9 bold')
lable_DissonanceType.grid(row=4, column=3, sticky = E)

lable_SweepType = Label(root, text='Sweep Type:', font='Helvetica 9 bold')
lable_SweepType.grid(row=5, column=3, sticky = E)

lable_ExportOptions = Label(root, text="Export Options:", font='Helvetica 9 bold')
lable_ExportOptions.grid(row=6, rowspan=2, column=3, sticky = E)

lable_SampleRate = Label(root, text="Sample Rate (Hz)", font='Helvetica 6 bold')
lable_SampleRate.grid(row=6, column=4, sticky = S)

lable_Duration = Label(root, text="Duration (s)", font='Helvetica 6 bold')
lable_Duration.grid(row=6, column=5, sticky = S)

lable_FileNamePrefix = Label(root, text="File Name Prefix", font='Helvetica 6 bold')
lable_FileNamePrefix.grid(row=6, column=6, sticky = S)


#         ENTRIES AND GUI VARIABLES
mtet_entry = StringVar()
entry_mtet = Entry(root, textvariable=mtet_entry)
entry_mtet.insert(END, '12')
entry_mtet.grid(row=1, column=6)
entry_mtet.config(width=12)

frequency_entry = StringVar()
frequency_entry = Entry(root, textvariable=frequency_entry)
frequency_entry.grid(row=5, column=0, sticky=N)
frequency_entry.config(width=9)

amplitude_entry = StringVar()
amplitude_entry = Entry(root, textvariable=amplitude_entry)
amplitude_entry.grid(row=5, column=1, sticky=N)
amplitude_entry.config(width=9)

fundamental_entry = StringVar()
fundamental_entry = Entry(root, textvariable=fundamental_entry)
fundamental_entry.insert(END, '440')
fundamental_entry.grid(row=2, column=6)
fundamental_entry.config(width=12)

numberofpartials_entry = StringVar()
numberofpartials_entry = Entry(root, textvariable=numberofpartials_entry)
numberofpartials_entry.insert(END, '6')
numberofpartials_entry.grid(row=3, column=6)
numberofpartials_entry.config(width=12)

sweepnumberofpartials_entry = StringVar()
sweepnumberofpartials_entry = Entry(root, textvariable=numberofpartials_entry)
sweepnumberofpartials_entry.insert(END, '6')
sweepnumberofpartials_entry.grid(row=5, column=6)
sweepnumberofpartials_entry.config(width=12)

samplerate_entry = StringVar()
samplerate_entry = Entry(root, textvariable=samplerate_entry)
samplerate_entry.insert(END, '96000')
samplerate_entry.grid(row=7, column=4, sticky=N)
samplerate_entry.config(width=12)

duration_entry = StringVar()
duration_entry = Entry(root, textvariable=duration_entry)
duration_entry.insert(END, '10')
duration_entry.grid(row=7, column=5, sticky=N)
duration_entry.config(width=12)

filenameprefix_entry = StringVar()
filenameprefix_entry = Entry(root, textvariable=filenameprefix_entry)
filenameprefix_entry.insert(END, 'Test')
filenameprefix_entry.grid(row=7, column=6, sticky=N)
filenameprefix_entry.config(width=12)


#                                               CREATING BUTTONS
button_width = 20
button_height = 2

button_Add = Button(root, text="Add", font=('bold', 8), bg='lavender', command=add_to_listboxes)
button_Add.grid(row=5, column=0, columnspan=2, sticky=S)
button_Add.config(width=18, height=1)

button_Remove = Button(root, text="Remove", font=('bold', 8), bg='lavender', command=remove_from_listboxes)
button_Remove.grid(row=6, column=0, columnspan=2, sticky=N)
button_Remove.config(width=18, height=1)

button_Clear = Button(root, text="Clear", font=('bold', 8), bg='lavender', command=clear_listboxes)
button_Clear.grid(row=7, column=0, columnspan=2, sticky=S)
button_Clear.config(width=18, height=1)

button_ImportSpectrum = Button(root, text="Import Spectrum", font=('bold', 12), bg='lavender', command=import_spectrum)
button_ImportSpectrum.grid(row=1, column=2, sticky=N)
button_ImportSpectrum.config(width=button_width, height=button_height)

button_CalculateSpectrum = Button(root, text="Calculate Spectrum", font=('bold', 12), bg='lavender', command=calculate_spectrum)
button_CalculateSpectrum.grid(row=2, column=2, sticky=N)
button_CalculateSpectrum.config(width=button_width, height=button_height)

button_PlotSpectrum = Button(root, text="Plot Spectrum", font=('bold', 12), bg='light goldenrod yellow', command=plot_spectrum)
button_PlotSpectrum.grid(row=3, column=2, sticky=N)
button_PlotSpectrum.config(width=button_width, height=button_height)

button_PlotDissonanceCurve = Button(root, text="Plot Dissonance Curve", font=('bold', 12), bg='light goldenrod yellow', command=show_dissonance_curve)
button_PlotDissonanceCurve.grid(row=4, column=2, sticky=N)
button_PlotDissonanceCurve.config(width=button_width, height=button_height)

button_ExportWav = Button(root, text="Export .wav", font=('bold', 12), bg='pale green', command=export_to_wav)
button_ExportWav.grid(row=5, rowspan=1, column=2, sticky=N)
button_ExportWav.config(width=button_width, height=button_height)

button_ExportData = Button(root, text="Export Data", font=('bold', 12), bg='pale green', command=export_data)
button_ExportData.grid(row=6, rowspan=2, column=2, sticky=N)
button_ExportData.config(width=button_width, height=button_height)


#                                                    CREATING RADIO BUTTONS

radiobutton_Harmonic = Radiobutton(root, text="Harmonic", variable=SpectrumTypeMethod, value=1)
radiobutton_Harmonic.grid(row=1, column=4, sticky=E)
radiobutton_mtet = Radiobutton(root, text="m-tet (edo)", variable=SpectrumTypeMethod, value=2)
radiobutton_mtet.grid(row=1, column=5, sticky=W)
radiobutton_Harmonic.select()

radiobutton_C0 = Radiobutton(root, text="C0             ", variable=FundamentslMethod, value=1)
radiobutton_C0.grid(row=2, column=4, sticky=E)
radiobutton_Custom1 = Radiobutton(root, text="Custom", variable=FundamentslMethod, value=2)
radiobutton_Custom1.grid(row=2, column=5, sticky=W)
radiobutton_Custom1.select()

radiobutton_All = Radiobutton(root, text="All             ", variable=NumberofPartialsMethod, value=1)
radiobutton_All.grid(row=3, column=4, sticky=E)
radiobutton_Custom2 = Radiobutton(root, text="Custom", variable=NumberofPartialsMethod, value=2)
radiobutton_Custom2.grid(row=3, column=5, sticky=W)
radiobutton_Custom2.select()

radiobutton_Sethares1 = Radiobutton(root, text="Sethares 1", variable=DissonanceTypeMethod, value=1)
radiobutton_Sethares1.grid(row=4, column=4, sticky=E)
radiobutton_Sethares2 = Radiobutton(root, text="Sethares 2", variable=DissonanceTypeMethod, value=2)
radiobutton_Sethares2.grid(row=4, column=5, sticky=W)
radiobutton_Vassilakis = Radiobutton(root, text="Vassilakis", variable=DissonanceTypeMethod, value=3)
radiobutton_Vassilakis.grid(row=4, column=6, sticky=W)
radiobutton_Sethares2.select()

radiobutton_SweepSame = Radiobutton(root, text="Same", variable=SweepTypeMethod, value=1)
radiobutton_SweepSame.grid(row=5, column=4, sticky=W)
radiobutton_SweepHarmonic = Radiobutton(root, text="Harmonic", variable=SweepTypeMethod, value=2)
radiobutton_SweepHarmonic.grid(row=5, column=5, sticky=W)
radiobutton_SweepSame.select()


root.mainloop()

import matplotlib
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from scipy import stats
import matplotlib.pyplot as plt
import copy
from sklearn import preprocessing
import scipy.signal


def snv(input_data):
    # Define a new array and populate it with the corrected data
    data_snv = np.zeros_like(input_data)
    for i in range(299):
        # Apply correction
        data_snv[i, :] = (input_data[i, :] - np.mean(input_data[i, :])) / np.std(input_data[i, :])

    return data_snv

def msc(input_data, reference=None):
    ''' Perform Multiplicative scatter correction'''

    # mean centre correction
    for i in range(input_data.shape[0]):
        input_data[i,:] -= input_data[i,:].mean()

    # Get the reference spectrum. If not given, estimate it from the mean
    if reference is None:
        # Calculate mean
        ref = np.mean(input_data, axis=0)
    else:
        ref = reference

    # Define a new array and populate it with the corrected data
    data_msc = np.zeros_like(input_data)
    for i in range(input_data.shape[0]):
        # Run regression
        fit = np.polyfit(ref, input_data[i,:], 1, full=True)
        # Apply correction
        data_msc[i,:] = (input_data[i,:] - fit[0][1]) / fit[0][0]

    return (data_msc, ref)

X = np.loadtxt("glass_p.csv", delimiter=",")
'''
x_msc = copy.deepcopy(X)
x_snv = copy.deepcopy(X)
x_sgf = copy.deepcopy(X)
x_fd = copy.deepcopy(X)


#sgf_msc = copy.deepcopy(x_msc)
#sgf_snv = copy.deepcopy(x_snv)
#sgf_fd = copy.deepcopy(x_fd)

msc = msc(x_msc)[0]
snv = snv(x_snv)
sgf = scipy.signal.savgol_filter(x_sgf, 31, 12)
fd = np.gradient(x_fd)
x_sd = copy.deepcopy(fd)
sd = np.gradient(x_sd)


fd = np.gradient(sgf_fd)
sd_fd = copy.deepcopy(fd)
sd = np.gradient(sd_fd)
'''
x = copy.deepcopy(X)
sgf = scipy.signal.savgol_filter(X, 31, 12)
x_snv = copy.deepcopy(sgf)
snv = snv(x_snv)
x_msc = copy.deepcopy(sgf)
x_fd = copy.deepcopy(sgf)
msc = msc(x_msc)[0]
fd = np.gradient(x_fd)
x_sd = copy.deepcopy(fd)
sd = np.gradient(x_sd)

plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
xlabel_size = 22
ylabel_size = 22
title_size = 25

fig, axs = plt.subplots(figsize=(10, 4))
axs.plot(np.arange(741, 1072), x[0], label="Glass_raw", color='red')
#axs.plot(np.arange(741, 1072), sgf[0], label="Glass_SGF", color='yellow')
axs.plot(np.arange(741, 1072), snv[0], label="Glass_SNV", color='Green')
#axs.plot(np.arange(741, 1072), msc[0], label="Ceramic_MSC", color='pink')
#axs.plot(np.arange(741, 1072), fd[0][0], label="Ceramic_FD", color='blue')
#axs.plot(np.arange(741, 1072), sd[0][0][0], label="Ceramic_SD", color='brown')


'''
axs.plot(np.arange(741, 1072), X[0], label="Glass", color='blue')
axs.plot(np.arange(741, 1072), msc[0], label="Glass_MSC", color='yellow')
axs.plot(np.arange(741, 1072), snv[0], label="Glass_SNV", color='Green')
axs.plot(np.arange(741, 1072), sgf[0], label="Glass_SGF", color='red')
axs.plot(np.arange(741, 1072), fd[0][0], label="Glass_FD", color='pink')
axs.plot(np.arange(741, 1072), sd[0][0][0], label="Glass_SD", color='brown')'''
axs.legend(loc='upper right', prop={'size': 14})
axs.set_title('Glass', fontsize=title_size)
#axs.set_ylabel('Intensity', fontsize=ylabel_size)
axs.set_xlabel('Wavelength', fontsize=xlabel_size)
axs.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
axs.grid(True)

plt.show()
fig.savefig("/home/hui/Desktop/312312/Glass.pdf", bbox_inches='tight')
print("all plot saved!")




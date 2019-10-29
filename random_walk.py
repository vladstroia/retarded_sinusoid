from matplotlib import pyplot as plt
import random
from matplotlib.backends.backend_pdf import PdfPages
max = 100000 #number of random walk steps
pages = 1000 #number of random walks to be made
with PdfPages("rezultat.pdf") as pdf:
    for page in range(pages): 
        x = [i for i in range(max)] #time axis
        y = [0] #position axis
        for i in range(1, max): 
            y.append(y[i-1]  + random.randint(-1,1)) #go one step up, one step down or stay still  

        plt.plot(x, y)
        pdf.savefig()  # saves the current figure into a pdf page
        plt.close()

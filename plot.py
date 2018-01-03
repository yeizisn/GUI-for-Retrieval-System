from matplotlib import pyplot as plt

# font = {'family' : 'serif',  
#         'color'  : 'darkred',  
#         'weight' : 'normal',  
#         'size'   : 20,  
#         } 

def plotcurve(list1,list2):
    fig = plt.figure()
    ax=fig.add_subplot(1,1,1)
    #lgi_line, =ax.plot(q_list,lgi_list,color="lightcoral",linestyle='-',linewidth=3.0)
    ax.plot(list1,list2,color="lightcoral",linestyle='-',linewidth=3.0,label="q Intensity curve")
    #sigma_line, = ax.plot(q_list,sigma_line,"x",color="darkgreen",linestyle='-',linewidth=3.0)
    # lines = [lgi_line]
    # labels=["Intensity(log)"]
    #ax.figlegend(lines,labels, loc='upper right')
    ax.set_xlabel('q')
    ax.set_ylabel('Intensity')
    plt.show()


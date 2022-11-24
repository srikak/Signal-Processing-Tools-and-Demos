def MA(signal,t,window):
    length = len(signal)-(len(window)-1)

    # Initialise the lengths of the filtered and time arrays 
    filtered = [0]*length
    time = [0]*length

    for i in range(length):
      # Slice the signal such that the number of elements in the slice is same as that of the length of coefficients
        temp = signal[i:i+len(window)]

      # Multiply the slice and the window and find its average
        filtered[i] = np.mean(np.multiply(temp,window))
        time[i] = np.mean(t[i:i+len(window)])
    
    return filtered,time

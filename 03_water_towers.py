def get_peaks(towers):

    peaks = []  # list of peak positions

    # check for peak in first tower
    if towers[0] > towers[1]:  # first tower is peak
        peaks.append(0)

    # check for peaks in intermediate towers
    for i in range(0, len(towers)-1):
        if (towers[i-1] < towers[i]) and (towers[i] > towers[i+1]):  # it's a peak
            peaks.append(i)

    # check for peak in last tower
    if towers[len(towers)-2] < towers[len(towers)-1]:  # last tower is peak
        peaks.append(len(towers)-1)

    print('Initial peaks: {}'.format(peaks))
    return(peaks)


def remove_valleys(peaks, towers):

    if len(peaks) < 3:  # not enough peaks to form valley
        return peaks

    # create list of validates peak positions
    new_peaks = [peaks[0]]  # add first peak (cannot be in valley)

    # check if intermediate peaks are in a valley between adjoining peaks
    for i in range(1, len(peaks)-1):  # do not check first and last peak
        print('Checking peak at position {} and height {}'.format(
            peaks[i], towers[peaks[i]]))
        if (towers[peaks[i-1]] < towers[peaks[i]]) or (towers[peaks[i]] > towers[peaks[i+1]]):
            # This peak is not in a valley between adjoining peaks
            print('Previous peak hight: {}\n Current peak hight: {}\n Next peak hight: {}'.format(
                towers[peaks[i-1]], towers[peaks[i]], towers[peaks[i+1]]))
            print('The peak at position {} is not a valley'.format(peaks[i]))
            new_peaks.append(peaks[i])

    # add last peak (cannot be in valley)
    new_peaks.append(peaks[len(peaks)-1])

    print('Removed valleys: {}'.format(new_peaks))
    return(new_peaks)


def rain_volume(towers):

    print('towers: {}'.format(towers))
    if len(towers) < 3:  # not possible to have a valley with less than 3 towers
        return 0

    # find and count peaks

    peaks = get_peaks(towers)

    # remove intermediate peaks

    while len(remove_valleys(peaks, towers)) < len(peaks):
        peaks = remove_valleys(peaks, towers)

    # calculate amount of water in each valley (between pair of peaks)

    if len(peaks) < 2:  # only one peak, therefore no valleys
        return 0

    water = 0

    for i in range(0, len(peaks)-1):  # for each valley

        if towers[peaks[i]] > towers[peaks[i+1]]:  # second peak if lowest of the two
            shortest_peak_pos = peaks[i+1]
        else:
            shortest_peak_pos = peaks[i]

        #   print('the shortest of {} and {} is {}'.format(
        #       towers[peaks[i]], towers[peaks[i+1]], towers[shortest_peak_pos]))

        #   print('looking for peaks form {} to {}'.format(
        #       peaks[i]+1, peaks[i+1]))

        # add how much water there is for each position between the two peaks
        for x in range(peaks[i]+1, peaks[i+1]):
            water += towers[shortest_peak_pos] - towers[x]

    #  print(water)
    return water


print(rain_volume([7, 18, 22, 18, 4, 30, 35, 48, 42, 21, 14,
      1, 27, 19, 48, 26, 5, 3, 28, 47, 20, 10, 6, 1]))  # 312

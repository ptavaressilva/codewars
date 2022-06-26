def get_peaks(towers):

    peaks = []  # list of peak positions

    # check for peak in first tower
    if towers[0] > towers[1]:  # first tower is peak
        peaks.append(0)

    # check for peaks in intermediate towers
    for i in range(1, len(towers)-1):
        if (towers[i-1] < towers[i]) and (towers[i] > towers[i+1]):  # it's a peak
            peaks.append(i)

        # detect plateaus
        elif (towers[i-1] < towers[i]):
            if towers[i] == towers[i+1]:  # plateau
                # check next tower until we find one lower or higher
                for j in range(i+1, len(towers)):
                    if towers[i] != towers[j]:
                        if towers[i] > towers[j]:  # plateau drops. It's a peak!
                            peaks.append(i)
                            i = j  # skip forward to end of plateau

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
        if (towers[peaks[i-1]] < towers[peaks[i]]) or (towers[peaks[i]] > towers[peaks[i+1]]):
            # This peak is not in a valley between adjoining peaks
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
            if towers[x] < towers[shortest_peak_pos]:  # tower is lower than the peak
                water += towers[shortest_peak_pos] - towers[x]

    #  print(water)
    return water


print(rain_volume([39, 6, 23, 39, 2, 5, 13, 49,
      49, 29, 0, 2, 2, 25, 32, 2, 32, 6]))  # 278

def rain_volume(towers):

    if len(towers) < 3:  # not possible to have a valley with less than 3 towers
        return 0

    # find an count peaks

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
    print(peaks)

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

    print(water)
    return water


rain_volume([1, 0, 5, 2, 6, 3, 10])

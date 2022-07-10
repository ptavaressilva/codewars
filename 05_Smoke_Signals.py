# https://www.codewars.com/kata/62a3855fcaec090025ed2a9a

# days is a tuple containing the smoke signals and the events that occured
# on a single day. Ex.
# days = [
#   (["4","5.1"],["Ambush in the jungle","Orange army retreats"]),
#   (["4","5.1","3.2.1"],["Tanks deployed","Orange army retreats","Ambush in the jungle"]),
#   (["5.1"],["Orange army retreats"])
# ]

from pprint import pprint

OFF = 0
ON = 1
HIGH = 2
DEBUG = ON


def remove_decode(days, decoded_code, decoded_message):

    if DEBUG >= ON:
        print('\n------ Removing ({}, {}) from:\n'.format(decoded_code, decoded_message))
        pprint(days)
        print('\n')
    for row in range(0, len(days)):
        if decoded_code in days[row][0]:
            if DEBUG >= ON:
                print('\ndays[row][0] is {}'.format(days[row][0]))
            days[row][0].remove(decoded_code)
            days[row][1].remove(decoded_message)
    if DEBUG >= ON:
        print('\n------ Returning:')
        pprint(days)
        print('\n')
    return days


# days = [(['8.2.1', '4.3.4', '1'], ['Ambush in the jungle', 'General assassinated', 'Ambush in the jungle']),
#         (['1', '2.2', '9.3'], ['Ambush in the jungle',
#          'Orange army retreats', 'Push into the mountains']),
#         (['4.3.4', '6'], ['Ambush in the jungle', 'Orange general goes on vacation']),
#         (['8.2.1', '9.3', '1'], ['Ambush in the jungle', 'General assassinated', 'Push into the mountains'])]

# remove_decode(days, '8.2.1', 'Ambush in the jungle')


def decode_smoke_signals(days):

    print('\nTrying to decode {}'.format(days))

    not_done = True

    decoded_codes = {}  # decoded codes with corresponding messages
    decoded_messages = []  # list of decoded messages

    while not_done:

        dictionary = {}

        not_done = False  # do not repeat by default

        # Create dictionary with message counts for each code
        for day in days:

            if DEBUG == HIGH:
                print('\n Processing day {}'.format(day))

            # Process each day
            codes = day[0]
            messages = day[1]

            for code in codes:

                messages_seen_today = []

                if DEBUG == HIGH:
                    print('\n   processing code {}'.format(code))

                # Process eachcode seen in that day

                for message in messages:  # increase code count for each message

                    if DEBUG == HIGH:
                        print('\n      Processing message {}'.format(message))
                        print('\n      Messages seen today = {}'.format(
                            messages_seen_today))

                    if message in messages_seen_today:
                        if DEBUG == HIGH:
                            print('      Message "{}" already seen today. Skipping!'.format(
                                message))
                        continue
                    else:
                        if DEBUG == HIGH:
                            print('      Adding message "{}" to list of messages seen todays with this code.'.format(
                                message))
                        messages_seen_today.append(message)

                    # code seen previously (another day)
                    if code in dictionary:

                        # message associated before with this code

                        if DEBUG == HIGH:
                            print('      Code {} already in dictionary'.format(code))

                        if message in dictionary[code]:

                            if DEBUG == HIGH:
                                print('      This message is already associated with code {} in the dictionary. Increasing count to {}'.format(
                                    message, dictionary[code][message] + 1))

                            dictionary[code][message] += 1

                        else:  # first time message appeared with this code

                            if DEBUG == HIGH:
                                print('      Associating message "{}" with this code and count = 1.'.format(
                                    message, code))

                            dictionary[code][message] = 1

                    else:  # the code was not seen before

                        if DEBUG == HIGH:
                            print('      Adding code {} and message "{}" to dictionary with count = 1.'.format(
                                code, message))
                        dictionary[code] = {message: 1}

                if DEBUG == HIGH:
                    print(
                        '\n   Finished processing the code.\n\n   Dictionary =', end='')
                    pprint(dictionary)

        if DEBUG >= ON:
            print('\n\n--- Finished analysis ---\n')
            pprint(dictionary)
            print('\n--- Starting decode ---\n\n')

        # Try to decode each code present in days.
        # It is decoded whenever a message has a unique higher count for that code
        for code in dictionary:

            # if code in decoded_messages:
            #     if DEBUG == HIGH:
            #         print('{} already decoded. Skipping!'.format(code))
            #     next  # code already decoded

            maximum = 0
            unique = True

            # For each code, determine if there is a unique maximum message count.
            # if that is the case, the message was successfully decoded and
            #   - it will be removed from 'days' exactly once
            #   - the procecss starts over

            if DEBUG >= ON:
                print('\nStarting run for code {}\n'.format(code))

            for message in dictionary[code]:
                print('\n   code: {1}   message {0}   count: {2}'.format(
                    message, code, dictionary[code][message]))
                # if (message not in decoded_messages) and (code not in decoded_codes):  # not decoded

                if DEBUG >= ON:
                    print('      {} is not in {}'.format(
                        message, decoded_messages))

                # this message is the new decode candidate
                if dictionary[code][message] > maximum:
                    if DEBUG >= ON:
                        print(
                            '      {} has the current maximum count'.format(message))
                    maximum = dictionary[code][message]
                    unique = True
                    suspect = [code, message]

                # this message is as recurring as some other
                elif dictionary[code][message] == maximum:
                    if DEBUG >= ON:
                        print('      {} count is not unique'.format(message))
                    unique = False

                # ->> this message is less frequent than some other (not a candidate)
                else:
                    if DEBUG >= ON:
                        print('      {} has lower count'.format(message))

                # else:

                #     if DEBUG >= ON:
                #         print('      Skipped {} because it is in {}'.format(
                #             message, decoded_messages))

            if unique and (maximum == 0):
                if DEBUG >= ON:
                    print('      UNIQUE AND ZERO')

            if unique and (maximum != 0):  # add decoded message to list
                if DEBUG >= ON:
                    print('      DECODED: {} is "{}"'.format(
                        suspect[0], suspect[1]))
                decoded_messages.append(suspect[1])
                decoded_codes[suspect[0]] = suspect[1]
                days = remove_decode(days, suspect[0], suspect[1])
                not_done = True
                break  # exit from cycle to restart while loop and repeat analysis

    return(decoded_codes)


print('\nPROGRAM START ###########################################\n\n\n\n')

days = [(['8.2.1', '4.3.4', '1'], ['Ambush in the jungle', 'General assassinated', 'Ambush in the jungle']),
        (['1', '2.2', '9.3'], ['Ambush in the jungle',
         'Orange army retreats', 'Push into the mountains']),
        (['4.3.4', '6'], ['Ambush in the jungle', 'Orange general goes on vacation']),
        (['8.2.1', '9.3', '1'], ['Ambush in the jungle', 'General assassinated', 'Push into the mountains'])]

print('Solution is: {}'.format(decode_smoke_signals(days)))

print('\nPROGRAM END ###########################################\n\n\n\n')

# ----
# {
#     (['8.2.1', '4.3.4', '1'], ['Ambush in the jungle', 'General assassinated', 'Ambush in the jungle']),
#     (['1', '2.2', '9.3'], ['Ambush in the jungle', 'Orange army retreats', 'Push into the mountains']),
#     (['4.3.4', '6'], ['Ambush in the jungle', 'Orange general goes on vacation']),
#     (['8.2.1', '9.3', '1'], ['Ambush in the jungle', 'General assassinated', 'Push into the mountains'])
# }

# {'1': {'Ambush in the jungle': 4, <--
#        'General assassinated': 2,
#        'Orange army retreats': 1,
#        'Push into the mountains': 2},
#  '2.2': {'Ambush in the jungle': 1,
#          'Orange army retreats': 1,
#          'Push into the mountains': 1},
#  '4.3.4': {'Ambush in the jungle': 3,
#            'General assassinated': 1,
#            'Orange general goes on vacation': 1},
#  '6': {'Ambush in the jungle': 1, 'Orange general goes on vacation': 1},
#  '8.2.1': {'Ambush in the jungle': 3,
#            'General assassinated': 2,
#            'Push into the mountains': 1},
#  '9.3': {'Ambush in the jungle': 2,
#          'General assassinated': 1,
#          'Orange army retreats': 1,
#          'Push into the mountains': 2}}


# output = {
#     '8.2.1': 'Ambush in the jungle',
#     '9.3': 'Push into the mountains',
#     '6': 'Orange general goes on vacation',
#     '4.3.4': 'General assassinated',
#     '1': 'Orange army retreats'}

# # should equal

# {'4.3.4': 'Ambush in the jungle',
#  '6': 'Orange general goes on vacation',
#  '1': 'Ambush in the jungle',
#  '8.2.1': 'General assassinated',
#  '9.3': 'Push into the mountains',
#  '2.2': 'Orange army retreats'}

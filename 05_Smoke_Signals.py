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

    if DEBUG == HIGH:
        print('\n\n------ Removing ({}, {}) from:\n'.format(decoded_code, decoded_message))
        pprint(days)
        print('\n')
    for row in range(0, len(days)):
        if decoded_code in days[row][0]:
            print('days[row][0] is {}'.format(days[row][0]))
            days[row][0].remove(decoded_code)
            days[row][1].remove(decoded_message)
    if DEBUG == HIGH:
        print('\n\n------ Returning:')
        pprint(days)
        print('\n\n')
    return days


# days = [(['8.2.1', '4.3.4', '1'], ['Ambush in the jungle', 'General assassinated', 'Ambush in the jungle']),
#         (['1', '2.2', '9.3'], ['Ambush in the jungle',
#          'Orange army retreats', 'Push into the mountains']),
#         (['4.3.4', '6'], ['Ambush in the jungle', 'Orange general goes on vacation']),
#         (['8.2.1', '9.3', '1'], ['Ambush in the jungle', 'General assassinated', 'Push into the mountains'])]

# remove_decode(days, '8.2.1', 'Ambush in the jungle')


def decode_smoke_signals(days):

    print('Trying to decode {}'.format(days))
    dictionary = {}

    not_done = True

    decoded_codes = {}  # decoded codes with corresponding messages
    decoded_messages = []  # list of decoded messages

    while not_done:

        not_done = False  # do not repeat by default

        # Create dictionary with message counts for each code
        for day in days:
            codes = day[0]
            messages = day[1]
            for code in codes:
                for message in messages:  # increase code count for each message
                    if DEBUG == HIGH:
                        print('message {}\ncode: {}'.format(message, code))
                    if code in dictionary:  # code seen previously
                        # message associated before with this code
                        if DEBUG == HIGH:
                            print('code {} seen before'.format(code))
                        if message in dictionary[code]:
                            if DEBUG == HIGH:
                                print('message {} already seen for code {}. Increasing count to {}'.format(
                                    message, code, dictionary[code][message]+1))
                            dictionary[code][message] += 1
                        else:  # first time message appeared with this code
                            if DEBUG == HIGH:
                                print('message {} exists no seen before for code {}. Added message with count = 1.'.format(
                                    message, code))
                            dictionary[code][message] = 1
                    else:  # the code was not seen before
                        if DEBUG == HIGH:
                            print('code {} not seen before. Adding code with message {} = 1.'.format(
                                code, message))
                        dictionary[code] = {message: 1}

        if DEBUG == ON:
            print('\n\n--- Finished analysis ---\n\n')
            pprint(dictionary)
            print('\n\n--- Starting decode ---\n\n')

        improved = True

        # repeat while improving
        while(improved):

            improved = False

            # Try to decode each code present in days.
            # It is decoded whenever a message has a unique higher count for that code
            for code in dictionary:

                # if code in decoded_messages:
                #     print('{} already decoded. Skipping!'.format(code))
                #     next  # code already decoded

                maximum = 0
                unique = True

                # For each code, determine if there is a unique maximum message count.
                # if that is the case, the message was successfully decoded and
                #   - it will be removed from 'days' exactly once
                #   - the procecss starts over

                if DEBUG == ON:
                    print('----- Starting run for code {} ----'.format(code))
                for message in dictionary[code]:
                    print('code: {1}   message {0}   count: {2}'.format(
                        message, code, dictionary[code][message]))
                    if (message not in decoded_messages) and (code not in decoded_codes):  # not decoded
                        if DEBUG == ON:
                            print('> > {} is not in {}'.format(
                                message, decoded_messages))
                        # this message is the new decode candidate
                        if dictionary[code][message] > maximum:
                            if DEBUG == ON:
                                print(
                                    '{} has the current maximum count'.format(message))
                            maximum = dictionary[code][message]
                            unique = True
                            suspect = [code, message]
                        # this message is as recurring as∫ some other
                        elif dictionary[code][message] == maximum:
                            if DEBUG == ON:
                                print('{} count is not unique'.format(message))
                            unique = False
                        # ->> this message is less frequent than some other (not a candidate)
                        else:
                            if DEBUG == ON:
                                print('{} has lower count'.format(message))
                    else:
                        if DEBUG == ON:
                            print('Skipped {} because it is in {}'.format(
                                message, decoded_messages))

                if unique and (maximum == 0):
                    if DEBUG == ON:
                        print('UNIQUE AND ZERO')
                if unique and (maximum != 0):  # add decoded message to list
                    decoded_messages.append(suspect[1])
                    decoded_codes[suspect[0]] = suspect[1]
                    if DEBUG == ON:
                        print('DECODED: ', decoded_codes)
                    improved = True

    return(decoded_codes)


days = [(['8.2.1', '4.3.4', '1'], ['Ambush in the jungle', 'General assassinated', 'Ambush in the jungle']),
        (['1', '2.2', '9.3'], ['Ambush in the jungle',
         'Orange army retreats', 'Push into the mountains']),
        (['4.3.4', '6'], ['Ambush in the jungle', 'Orange general goes on vacation']),
        (['8.2.1', '9.3', '1'], ['Ambush in the jungle', 'General assassinated', 'Push into the mountains'])]

print('Solution is: {}'.format(decode_smoke_signals(days)))


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

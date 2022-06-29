# https://www.codewars.com/kata/62a3855fcaec090025ed2a9a

# days is a tuple containing the smoke signals and the events that occured
# on a single day. Ex.
# days = [
#   (["4","5.1"],["Ambush in the jungle","Orange army retreats"]),
#   (["4","5.1","3.2.1"],["Tanks deployed","Orange army retreats","Ambush in the jungle"]),
#   (["5.1"],["Orange army retreats"])
# ]

from pprint import pprint


def decode_smoke_signals(days):

    print('Trying to decode {}'.format(days))
    dictionary = {}

    # Create dictionary with message counts for each code
    for day in days:
        codes = day[0]
        messages = day[1]
        for code in codes:
            # print(code)
            for message in messages:  # increase code count for each message
                # print('message {}\ncode: {}'.format(message, code))
                if code in dictionary:  # code seen previously
                    # print('code {} seen before'.format(code))
                    # message associated before with this code
                    if message in dictionary[code]:
                        # print('message {} already seen for code {}. Increasing count to {}'.format(
                        #     message, code, dictionary[code][message]+1))
                        dictionary[code][message] += 1
                    else:  # first time message appeared with this code
                        # print('message {} exists no seen before for code {}. Added message with count = 1.'.format(
                        #     message, code))
                        dictionary[code][message] = 1
                else:  # the code was not seen before
                    # print('code {} not seen before. Adding code with message {} = 1.'.format(
                    #     code, message))
                    dictionary[code] = {message: 1}

    print('\n\n--- Finished analysis ---\n\n')
    pprint(dictionary)
    print('\n\n--- Starting decode ---\n\n')

    improved = True

    decoded_codes = {}  # decoded codes with corresponding messages
    decoded_messages = []  # list of decoded messages

    # repeat while improving
    while(improved):

        improved = False
        # try to decode each code
        for code in dictionary:

            # if code in decoded_messages:
            #     print('{} already decoded. Skipping!'.format(code))
            #     next  # code already decoded

            maximum = 0
            unique = True

            # For each code, determine if there is a unique maximum message count.
            # if that is the case, the message was successfully decoded

            print('----- Starting run for code {} ----'.format(code))
            for message in dictionary[code]:
                print('code: {1}   message {0}   count: {2}'.format(
                    message, code, dictionary[code][message]))
                if (message not in decoded_messages) and (code not in decoded_codes):  # not decoded
                    print('> > {} is not in {}'.format(
                        message, decoded_messages))
                    # this message is the new decode candidate
                    if dictionary[code][message] > maximum:
                        print('{} has the current maximum count'.format(message))
                        maximum = dictionary[code][message]
                        unique = True
                        suspect = [code, message]
                    # this message is as recurring as∫ some other
                    elif dictionary[code][message] == maximum:
                        print('{} count is not unique'.format(message))
                        unique = False
                    # ->> this message is less frequent than some other (not a candidate)
                    else:
                        print('{} has lower count'.format(message))
                else:
                    print('Skipped {} because it is in {}'.format(
                        message, decoded_messages))

            if unique and (maximum == 0):
                print('UNIQUE AND ZERO')
            if unique and (maximum != 0):  # add decoded message to list
                decoded_messages.append(suspect[1])
                decoded_codes[suspect[0]] = suspect[1]
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

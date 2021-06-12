SERVICE_CHARGE = 2
TICKET_PRICE = 10

ticket_remaining = 100


def calculate_price(number_of_tickets):
    return (ticket * TICKET_PRICE) + SERVICE_CHARGE

while ticket_remaining >= 1:
    print('There are {} tickets remaining.'.format(ticket_remaining))
    name = input('Please enter your name?  ')
    ticket = input('Hi {} how many tickets would you like?  '.format(name))
    try:
        ticket = int(ticket)
        if ticket > ticket_remaining:
            raise ValueError('There are only {} tickets remaining'.format(ticket_remaining)) 
    except ValueError as err:
        print("Oh no! we ran into an issue. {}. Try again...".format(err))
    else:
        order_total = calculate_price(ticket)
        print('Your total price is ${}'.format(order_total))
        proceed = input('{} do you what to proceed with the order Y/N?  '.format(name))
        if proceed.upper() == 'Y':
            # TODO: Gather credit card information and process it.
            print('SOLD!')
            ticket_remaining -= ticket
        else:
            print('Thank {}'.format(name))
print('We are Sold out')
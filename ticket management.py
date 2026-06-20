from chatbot import SimpleChatbot

data = [
    {'Movie ID': 301, 'Title': 'The Quantum Paradox', 'Genre': 'Science Fiction', 'Language': 'English', 'Duration': '145 min', 'Ticket Price (PKR)': 1200},
    {'Movie ID': 302, 'Title': 'Edge of Eternity', 'Genre': 'Action', 'Language': 'English', 'Duration': '140 min', 'Ticket Price (PKR)': 1500},
    {'Movie ID': 303, 'Title': 'Nebula Rising', 'Genre': 'Adventure', 'Language': 'English', 'Duration': '135 min', 'Ticket Price (PKR)': 1100},
    {'Movie ID': 304, 'Title': 'Shadow of the Blade', 'Genre': 'Action', 'Language': 'English', 'Duration': '120 min', 'Ticket Price (PKR)': 1400},
    {'Movie ID': 305, 'Title': 'Toofan', 'Genre': 'Action', 'Language': 'Urdu', 'Duration': '130 min', 'Ticket Price (PKR)': 850},
    {'Movie ID': 306, 'Title': 'Lal Haveli', 'Genre': 'Horror', 'Language': 'Urdu', 'Duration': '120 min', 'Ticket Price (PKR)': 700},
]

def refresh_movie(data):
    with open("movies.txt", "w") as file:
        file.truncate(0)  
        headers = f"{'Movie ID':<10} | {'Title':<30} | {'Genre':<17} | {'Language':<12} | {'Duration':<10} | {'Ticket Price (PKR)'}\n"
        file.write(headers)
  
       
        for movie in data:
            file.write(f"{movie['Movie ID']:<10} | {movie['Title']:<30} | {movie['Genre']:<17} | {movie['Language']:<12} | {movie['Duration']:<10} | {movie['Ticket Price (PKR)']}\n")

def show_movie():
    refresh_movie(data)
    with open("movies.txt", "r") as file:
         print(file.read())

def add_movie(data):
    try:
        if data!=[]:
            movieid=data[-1]['Movie ID'] + 1  
        else:
            movieid=301
        new_movie = {
            'Movie ID':movieid , 
            'Title': input('Enter Title of movie: ').title(),
            'Genre': input('Enter Genre of movie: ').title(),
            'Language': input('Enter Language of movie: ').title(),
            'Duration': input('Enter Duration of movie(Min): ').title() + ' min',
            'Ticket Price (PKR)': int(input('Enter Price of movie (PKR): '))  
        }
        data.append(new_movie)
        refresh_movie(data)
        print(f"Movie '{new_movie['Title']}' added successfully!")            
    except ValueError:
         print("Invalid input! Ensure the ticket price is an integer.")

def search_movie(data):
    from tabulate import tabulate
    import pandas as pd
    
    genre_list=['Any']
    language_list=['Any']
    for movie in data:
        if movie['Genre'] not in genre_list:
         genre_list.append(movie['Genre'])
    for movie in data:
        if movie['Language'] not in language_list:
         language_list.append(movie['Language'])
    con='y'
    while con=='y':
        data2 = []
        user_genre=input(f'Write genre from {genre_list} : ').title()
        user_language=input(f'Write language from {language_list} : ').title()
        if user_genre=='Any' and user_language=='Any':
                data2=data       
        elif user_genre=='Any' and user_language in language_list:
                for key in data:
                    if key['Language']==user_language:
                        data2.append(key) 
        elif user_language=='Any' and user_genre in genre_list:
                 for key in data:
                      if key['Genre'] == user_genre:
                          data2.append(key)
        elif user_genre in genre_list and user_language in language_list:
                 for key in data:
                     if key['Genre'] == user_genre and key['Language']==user_language:
                          data2.append(key)     
        else:
                print('Sorry, there are no available movies of this type.')

        df = pd.DataFrame(data2)
        print(tabulate(df, headers='keys', tablefmt='grid'))
        con=input('Do you want to continue (y/n):')
        if con!='y':
            break
        
def update_movie(data):
    show_movie()  
    movie_id = int(input('\nEnter the Movie ID you want to update: '))
    
    selected_movie =[]

    
    for key in data:
        if key['Movie ID'] == movie_id:
            selected_movie = key
            break
    else:
        print("Movie ID not found.")
        return  
    
    
    movie = selected_movie['Title']
    
    try:
        while True:
           
            field_to_change = input(f'Write what you want to change in movie "{movie}" from (Genre, Language, Ticket Price): ').lower()
            
        
            if field_to_change == 'genre':
                new_genre = input(f'Enter the new genre for "{movie}": ').title()
                selected_movie['Genre'] = new_genre
                print(f"Genre updated to: {new_genre}")
            elif field_to_change == 'language':
                new_language = input(f"Enter the new language for '{movie}': ").title()
                selected_movie['Language'] = new_language
                print(f"Language updated to: {new_language}")
            elif field_to_change == 'ticket price':
                new_price = int(input(f"Enter the new ticket price (PKR) for '{movie}': "))
                selected_movie['Ticket Price (PKR)'] = new_price
                print(f"Ticket price updated to: PKR {new_price}")
            else:
                print("Invalid choice. No updates were made.")
    
            
            con = input(f'Do you want to change any other thing from movie "{movie}"? (y/n): ').lower()
            if con == 'n':
                break
        
        refresh_movie(data)
    except ValueError:
        print("Invalid input! Ensure the Movie ID or ticket price is an integer.")

def delete_movie(data):
    try:
        movie_id = int(input('Enter Movie ID to delete: '))
        movie_found = False
    
        for movie in data:
            if movie['Movie ID'] == movie_id:
                data.remove(movie)
                movie_found = True
                print(f"Movie with ID {movie_id} has been deleted.")
                break
    
        if not movie_found:
            print(f"Movie with ID {movie_id} not found.")
    
        refresh_movie(data)
    except ValueError:
        print("Invalid input! Please enter Movie ID in integers.")
schedule = [
    {'Movie ID': 301, 'Show ID': 'S101', 'Date': '2024-12-01', 'Time': '12:00 PM', 'Screen Number': 1},
    {'Movie ID': 301, 'Show ID': 'S102', 'Date': '2024-12-01', 'Time': '06:00 PM', 'Screen Number': 2},
    {'Movie ID': 302, 'Show ID': 'S103', 'Date': '2024-12-01', 'Time': '03:00 PM', 'Screen Number': 1},
    {'Movie ID': 302, 'Show ID': 'S104', 'Date': '2024-12-01', 'Time': '09:00 PM', 'Screen Number': 3},
    {'Movie ID': 303, 'Show ID': 'S105', 'Date': '2024-12-01', 'Time': '01:00 PM', 'Screen Number': 2},
    {'Movie ID': 304, 'Show ID': 'S106', 'Date': '2024-12-01', 'Time': '04:30 PM', 'Screen Number': 4},
    {'Movie ID': 305, 'Show ID': 'S107', 'Date': '2024-12-01', 'Time': '02:00 PM', 'Screen Number': 5},
    {'Movie ID': 305, 'Show ID': 'S108', 'Date': '2024-12-01', 'Time': '08:00 PM', 'Screen Number': 1},
    {'Movie ID': 306, 'Show ID': 'S109', 'Date': '2024-12-01', 'Time': '10:00 PM', 'Screen Number': 3},
]

def refresh_show(schedule):
    with open("show.txt", "w") as file:
        file.truncate(0)  
        headers = f"{'Movie ID':<10} | {'Show ID':<30} | {'Date':<17} | {'Time':<10} | {'Screen Number'}\n"
        file.write(headers)
  
       
        for movie in schedule:
            file.write(f"{movie['Movie ID']:<10} | {movie['Show ID']:<30} | {movie['Date']:<17} | {movie['Time']:<10} | {movie['Screen Number']}\n")

def show_sch():
    refresh_show(schedule)
    with open("show.txt", "r") as file:
         print(file.read())

def add_show(schedule, data):
    last_show_id = schedule[-1]['Show ID']
    next_show_id = 'S' + str(int(last_show_id[1:]) + 1)
    while True:
        try:
            movie_id = int(input('Write MovieID you want to add: '))
            if any(movie['Movie ID'] == movie_id for movie in data):
                break  
            else:
                print("Invalid Movie ID! Please enter a valid ID from the movie list.")
        except ValueError:
            print("Invalid input! Please enter a numeric Movie ID.")

    new_sch = {
        'Movie ID': movie_id,
        'Show ID': next_show_id,
        'Date': input('Enter Date of movie (e.g., 2024-12-01): '),
        'Time': input('Enter Time of movie (e.g., 12:00 PM): '),
        'Screen Number': input('Enter Screen number of movie: ')
    }
    
    schedule.append(new_sch)
    refresh_show(schedule)
    print(f"Show with ID {next_show_id} added successfully!")


def search_show(data, schedule):
    from tabulate import tabulate
    import pandas as pd

    title_list = ['Any']
    date_list = ['Any']

    for movie in data:
        if movie['Title'] not in title_list:
            title_list.append(movie['Title'])

    for movie in schedule:
        if movie['Date'] not in date_list:
            date_list.append(movie['Date'])
    while True:
        data2 = []  

        
        user_title = input(f"Write Title from {title_list}: ").title()
        user_date = input(f"Write date from {date_list}: ").lower()

        
        movie_id = None
        for key in data:
            if key['Title'] == user_title:
                movie_id = key['Movie ID']

        
        if user_title == 'Any' and user_date == 'any':
            for key in schedule:
                data2.append(key)

        elif user_title == 'Any' and user_date in date_list:
            for key in schedule:
                if key['Date'] == user_date:
                    data2.append(key)

        elif user_date == 'any' and user_title in title_list:
            for key in schedule:
                if key['Movie ID'] == movie_id:
                    data2.append(key)

        elif user_title in title_list and user_date in date_list:
            for key in schedule:
                if key['Date'] == user_date and key['Movie ID'] == movie_id:
                    data2.append(key)

        else:
            print("Sorry, there are no available shows of this type")


        df = pd.DataFrame(data2)
        print(tabulate(df, headers='keys', tablefmt='grid'))
 
        y = input("Do you want to search again (y/n): ").lower()
        if y != 'y':
            break

def update_show(schedule, data):
    show_sch()  
    show_id = input('\nEnter the Show ID you want to update: ').title()
    
    selected_movie = None  
    for key in schedule:
        if key['Show ID'] == show_id:
            selected_movie = key
            break
    else:
        print("Show ID not found.")
        return 
    
    movie_id = selected_movie['Movie ID']
    movie = None

    for key in data:
        if key['Movie ID'] == movie_id:
            movie = key['Title']
            break
    else:
        print("Movie ID not found.")
        return  

    while True:
        field_to_change = input(f'Write what you want to change in movie "{movie}" from (Date, Screen number): ').lower()
        

        if field_to_change == 'date':
            new_date = input(f'Enter the new Date for "{movie}" in the form of (2024-12-01): ')
            selected_movie['Date'] = new_date
            print(f"Date updated to: {new_date}")
        
        elif field_to_change == 'screen number':
             new_number = int(input(f"Enter the new Screen number for '{movie}': "))
             selected_movie['Screen Number'] = new_number
             print(f"Screen Number updated to: {new_number}")         
        else:
            print("Invalid choice. No updates were made.")

        con = input(f'Do you want to change any other thing from movie "{movie}"? (y/n): ').lower()
        if con == 'n':
            break
    refresh_show(schedule)
def delete_show(schedule):
    show_sch()
    show_id = input('Enter Show ID to delete: ').title()
    show_found = False

    for movie in schedule:
        if movie['Show ID'] == show_id:
            schedule.remove(movie)
            show_found = True
            print(f"Show with ID {show_id} has been deleted.")
            break

    if not show_found:
        print(f"SHOW with ID {show_id} not found.")

    refresh_show(schedule)
bookings = []
def refresh_booking(bookings):
    with open("bookings.txt", "w") as file:
        headers = f"{'Booking ID':<10} | {'Show ID':<10} | {'Customer Name':<25} | {'Contact Number':<15} | {'Tickets':<7} | {'Assigned Seats'}\n"
        file.write(headers)

        for movie in bookings:
            seats_str = ", ".join(movie.get('Assigned Seats', ['N/A']))
            content = f"{movie['Booking ID']:<10} | {movie['Show ID']:<10} | {movie['Customer Name']:<25} | {movie['Contact Number']:<15} | {movie['Number of Tickets']:<7} | {seats_str}\n"
            file.write(content)

def assign_cinema_seats(show_id, num_tickets, bookings):
    """Generates unique seat numbers foe example F4, F5 etc for a specific show based on maximum 100 seats"""
    
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    all_seats = [f"{r}{c}" for r in rows for c in range(1, 11)]

    taken_seats = []
    for b in bookings:
        if b['Show ID'] == show_id:
            taken_seats.extend(b.get('Assigned Seats', []))
    available_seats = [seat for seat in all_seats if seat not in taken_seats]
    assigned = available_seats[:num_tickets]
    return assigned     
def book_ticket(schedule,data, bookings):
    import time
    from tabulate import tabulate
    import pandas as pd
    show_sch()
    show_id = input("Enter the Show ID for the show you want to book tickets for: ").title()
    selected_show = None
    for show in schedule:
        if show['Show ID'] == show_id:
            selected_show = show
            movieid=show['Movie ID']     
        
    if not selected_show:
        print("Invalid Show ID. Please try again.")
        return
    for key in data:
        if key['Movie ID']==movieid:
            price=key['Ticket Price (PKR)']
            break
                    
                
    try:              
        customer_name = input("Enter your name: ").title()
        contact_number = input("Enter your contact number: ")
        num_tickets = int(input("Enter the number of tickets to book: "))
    except ValueError:
        print("Invalid input! Number of tickets must be a  integer.")
        return
            
    max_seats = 100  
    booked_tickets = 0
    for booking in bookings:
        if booking['Show ID'] == show_id:
            booked_tickets += booking['Number of Tickets']
        
   
    available_seats = max_seats - booked_tickets
    if num_tickets > available_seats:
        print(f"Only {available_seats} seats are available. Please adjust your booking.")
        return

    demand_tension = (booked_tickets / max_seats) * 100
    dynamic_price = price
    
    if demand_tension >= 80:
        print("due to high demand we are applying surge pricing (+10%).")
        dynamic_price = int(price * 1.10)
    elif demand_tension <= 20:
        print("enjoy discount due to low demand (-5%).")
        dynamic_price = int(price * 0.95)
    else:
        print("Standard pricing applied.")

    total_cost = num_tickets * dynamic_price
    print(f"Original Price per ticket: PKR {price}")
    print(f"Dynamic Price per ticket: PKR {dynamic_price}")
    print(f"Total cost: PKR {total_cost}")

    if bookings!=[]:
        last_booking_id = bookings[-1]['Booking ID']
        next_booking_id = 'B' + str(int(last_booking_id[1:]) + 1)
    else:
        next_booking_id='B100'
        
    bookings.append({
        'Booking ID': next_booking_id,
        'Show ID': show_id,
        'Customer Name': customer_name,
        'Contact Number': contact_number,
        'Number of Tickets': num_tickets
    })
    refresh_booking(bookings)
    payment = input('Enter your payment option (1/2/3):\n 1. Debit Card\n 2. Credit Card\n 3. Easy Paisa\n')

    while True:
        if payment in ['1', '2', '3']:
            print('Processing...........') 
            time.sleep(2)
            print(f'Successful, {total_cost} deducted from {customer_name} Account.')
            break
        else:
            print("Invalid input. Please choose from (1/2/3).")
            payment = input('Enter your payment option (1/2/3): ')

    print("Booking Successful!")

    data2=[]
    data2.append({
        'Booking ID': next_booking_id,
        'Show ID': show_id,
        'Customer Name': customer_name,
        'Contact Number': contact_number,
        'Number of Tickets': num_tickets
    })
    df = pd.DataFrame(data2)
    print(tabulate(df, headers='keys', tablefmt='grid'))
    
def view_bookings():
    refresh_booking(bookings)
    with open("bookings.txt", "r") as file:
            print(file.read())
            
def cancel_ticket(bookings):
    booking_id = input("\nEnter the Booking ID to cancel: ").title()
    booking_to_cancel = None
    for key in bookings:
        if key['Booking ID'] == booking_id:
            booking_to_cancel = key
            break   
    
    if not booking_to_cancel:
        print("Invalid Booking ID. Please try again.")
        return
    bookings.remove(booking_to_cancel)
    refresh_booking(bookings)
    print(f'Booking with ID {booking_id} has been successfully canceled.')
def view_available_seats(schedule, bookings):
    print("\nAvailable Seats for Shows:")
    max_seats = 100  
    
    for show in schedule:
        booked_tickets = 0
        for booking in bookings:
            if booking['Show ID'] == show['Show ID']:
                booked_tickets += booking['Number of Tickets']
        available_seats = max_seats - booked_tickets
        print(f"Show ID: {show['Show ID']}, Date: {show['Date']}, Time: {show['Time']}, Available Seats: {available_seats}")

def total_sales_analysis(bookings,schedule,data):
    list=[]
    import numpy as np
    if not bookings:
        print("No bookings available for analysis.")
        return
    for booking in bookings:
        for show in schedule:
            if show['Show ID'] == booking['Show ID']:
                for movie in data:
                    if movie['Movie ID'] == show['Movie ID']:
                        ticket_price = movie['Ticket Price (PKR)']
                        list.append(ticket_price*booking['Number of Tickets'])
                        
    total = np.sum(list)                     
    print(f'Total Sales out of booking is {total}')
def most_popular_movie(bookings, schedule, data):
    import numpy as np

    if not bookings:
        print("No bookings available to determine the most popular movie.")
        return
    ticket_counts = {}

    for booking in bookings:
        for show in schedule:
            if show['Show ID'] == booking['Show ID']:
                movie_id = show['Movie ID']
                # Increment ticket count for the movie
                ticket_counts[movie_id] = ticket_counts.get(movie_id, 0) + booking['Number of Tickets']
                break

    movie_ids = np.array(list(ticket_counts.keys()))
    tickets = np.array(list(ticket_counts.values()))


    max_index = np.argmax(tickets)
    most_popular_id = movie_ids[max_index]

    # Step 4: Find the movie title using the Movie ID
    most_popular_title = next(movie['Title'] for movie in data if movie['Movie ID'] == most_popular_id)

    print(f"The most popular movie is '{most_popular_title}' with {tickets[max_index]} tickets sold.")

def generate_pricing_recommendations(schedule, data, bookings):
    from tabulate import tabulate
    import pandas as pd

    print("\n Prescriptive Pricing Strategy Dashboard ")
    print("Analyzing market demand and generating transparent recommendations...\n")

    recommendations = []
    max_seats = 100
    base_cost_per_seat = 400 

    for show in schedule:
        booked_tickets = sum(b['Number of Tickets'] for b in bookings if b['Show ID'] == show['Show ID'])
        capacity = (booked_tickets / max_seats) * 100

        movie = next((m for m in data if m['Movie ID'] == show['Movie ID']), None)
        if not movie:
            continue
        current_price = movie['Ticket Price (PKR)']
        price_floor = int(base_cost_per_seat * 1.20)
        if capacity >= 80:
            suggested_action = f"Increase by 10% (PKR {int(current_price * 1.10)})"
            reason = f"High demand tension ({capacity}% full). Maximize yield."
        elif capacity <= 20:
            discount_price = int(current_price * 0.90)
            if discount_price < price_floor:
                suggested_action = f"Hold Price (PKR {current_price})"
                reason = f"Low demand ({capacity}%), but a discount breaches minimum margin floor (PKR {price_floor})."
            else:
                suggested_action = f"Discount by 10% (PKR {discount_price})"
                reason = f"Low demand tension ({capacity}% full). Stimulate volume."
        else:
            suggested_action = f"Hold Price (PKR {current_price})"
            reason = f"Optimal demand tension ({capacity}% full). Stable market."

        recommendations.append({
            'Show ID': show['Show ID'],
            'Movie Title': movie['Title'],
            'Capacity': f"{capacity}%",
            'Current Price': current_price,
            'Suggested Action': suggested_action,
            'Analytical Reason': reason
        })

    if not recommendations:
        print("No active shows to analyze.")
        return
    df = pd.DataFrame(recommendations)
    print(tabulate(df, headers='keys', tablefmt='grid'))
def run_ai_assistant():
    """Opens a chat loop for the customer to talk to the AI"""
    print("\n" + "="*45)
    print("CINEMA AI ASSISTANT OPENED")
    print("Ask me about movie genres, ticket policies, or system help")
    print("(Type 'back' to return to the Customer Menu)")
    print("="*45)
    # Set up the bot with a cinema personality
    ticket_bot = SimpleChatbot(
        system_prompt="You are a helpful cinema ticketing assistant. Keep answers short, polite, and helpful."
    )
    
    while True:
        user_question = input("\nYou: ").strip()
        if user_question.lower() == 'back':
            print("Returning to menu...\n")
            break
            
        if not user_question:
            continue
            
        try:
            ai_answer = ticket_bot.chat(user_question)
            print(f"Assistant: {ai_answer}")
        except Exception as e:
            print(f"Error connecting to AI: {e}")
def detect_financial_anomalies(schedule, bookings, data):
    from tabulate import tabulate
    import pandas as pd

    print("\n Financial Risk & Anomaly Detection Engine ")
    print("Scanning transactions for scalping, revenue concentration, and ghost shows...\n")

    alerts = []
    
    # Scan for Ghost Shows which means shows with Zero bookings
    for show in schedule:
        booked_tickets = sum(b['Number of Tickets'] for b in bookings if b['Show ID'] == show['Show ID'])
        if booked_tickets == 0:
            movie = next((m for m in data if m['Movie ID'] == show['Movie ID']), None)
            movie_title = movie['Title'] if movie else "Unknown"
            alerts.append({
                'Show ID': show['Show ID'],
                'Risk Category': 'this is a ghost show because no one has booked any ticket for this show',
                'Details': f"Zero tickets sold for '{movie_title}'.",
                'Action Required': 'Consider canceling to save overhead costs.'
            })
    customer_purchases = {}
    for booking in bookings:
        # Group purchases by Show ID and their contact number to catch people booking multiple times
        key = (booking['Show ID'], booking['Contact Number'])
        if key not in customer_purchases:
            customer_purchases[key] = {'Name': booking['Customer Name'], 'Tickets': 0}
        customer_purchases[key]['Tickets'] += booking['Number of Tickets']

    for (show_id, contact), info in customer_purchases.items():
        tickets_bought = info['Tickets']
        if tickets_bought >= 20: 
            alerts.append({
                'Show ID': show_id,
                'Risk Category': 'SCALPING RISK',
                'Details': f"Customer '{info['Name']}' ({contact}) bought {tickets_bought} tickets.",
                'Action Required': 'Verify transaction. High refund/chargeback risk.'
            })
        elif tickets_bought >= 10:
            alerts.append({
                'Show ID': show_id,
                'Risk Category': 'CONCENTRATION RISK',
                'Details': f"Customer '{info['Name']}' bought {tickets_bought} tickets.",
                'Action Required': 'Monitor. Revenue heavily reliant on one party.'
            })

    if not alerts:
        print(" all systems clear so no financial anomalies detected.")
        return
    df = pd.DataFrame(alerts)
    print(tabulate(df, headers='keys', tablefmt='grid'))    
def what_if_simulator(data):
    print("\n 'What If' Decision Simulator")
    print("Model price elasticity and external factors on your profitability.")
    
    try:
        movie_id = int(input("Enter movie ID to simulate (for example enter: 301): "))
        selected_movie = None
        for movie in data:
            if movie['Movie ID'] == movie_id:
                selected_movie = movie
                break
                
        if not selected_movie:
            print("Movie not found.")
            return

        base_price = selected_movie['Ticket Price (PKR)']
        base_demand = 50 
        
        print(f"\nTargeting: {selected_movie['Title']}")
        print(f"Base Ticket Price: PKR {base_price}")
        print(f"Estimated Base Demand: {base_demand} tickets")

        while True:
            print("\n Configure Your Scenario ")
            new_price = int(input(f"1. Enter new hypothetical ticket price (Current: PKR {base_price}): "))
            overhead = int(input("2. Enter estimated fixed overhead costs (e.g., electricity, licensing) in PKR: "))
            
            print("3. Are there any external factors? (Choose 1-3)")
            print("   1. Normal Day")
            print("   2. Holiday / Weekend (Boosts demand)")
            print("   3. Heavy Rain / Bad Weather (Reduces demand)")
            factor_choice = input("Enter choice (1/2/3): ")

            price_change_pct = (new_price - base_price) / base_price
            demand_change_pct = -(price_change_pct * 0.5) 
            
            if factor_choice == '2':
                demand_change_pct += 0.30 
            elif factor_choice == '3':
                demand_change_pct -= 0.40 

            projected_demand = int(base_demand * (1 + demand_change_pct))
            
            # Cap demand at the physical limits of the cinema (Max 100 seats, Min 0 seats)
            projected_demand = max(0, min(100, projected_demand))

            gross_revenue = new_price * projected_demand
            net_profit = gross_revenue - overhead
            margin = (net_profit / gross_revenue * 100) if gross_revenue > 0 else 0

            print("\n" + "="*35)
            print("the results of your scenario:")
            print("="*35)
            print(f"Projected Tickets Sold: {projected_demand} / 100 seats")
            print(f"Gross Revenue:          PKR {gross_revenue}")
            print(f"Overhead Costs:         PKR {overhead}")
            print("-" * 35)
            if net_profit > 0:
                print(f"net profit:          PKR {net_profit} (Margin: {margin:.1f}%)")
            else:
                print(f"total loss:          PKR {net_profit}")
            print("="*35)
            again = input("\nDo you want to tweak this scenario again? (y/n): ").lower()
            if again != 'y':
                print("Exiting simulator...")
                break

    except ValueError:
        print("Invalid input! Please enter numeric values where required.")            
    
import hashlib
import json
import os

def secure_system_gateway():
    """this handles user registration and secure login before launching the main system so this is a very important security layer """
    
    # Load existing users or create a default admin if the file doesn't exis
    if not os.path.exists("users.json"):
        default_users = [{"username": "admin", "password_hash": hashlib.sha256("admin123".encode()).hexdigest()}]
        with open("users.json", "w") as f:
            json.dump(default_users, f)
    
    with open("users.json", "r") as f:
        users_list = json.load(f)
        
    while True:
        print("\n1. Log In")
        print("2. Register New Account")
        print("3. Exit Program")
        choice = input("Enter choice (1/2/3): ")
        
        if choice == "1":
            username = input("please enter your Username: ").strip()
            password = input("please enter your Password: ")
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            
            login_success = False
            for user in users_list:
                if user["username"] == username and user["password_hash"] == hashed_pw:
                    login_success = True
                    break
                    
            if login_success:
                print(f"\n Congratulations you have been granted access. Welcome, {username}!")
                return True 
            else:
                print("sorry you have been Denied access. Invalid username or password.")
                
        elif choice == "2":
            username = input("please enter a new username: ").strip()
            if any(u["username"] == username for u in users_list):
                print(" Username already exists. Try logging in or pick another.")
                continue
                
            password = input("please enter a secure password: ")
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            users_list.append({"username": username, "password_hash": hashed_pw})
            with open("users.json", "w") as f:
                json.dump(users_list, f)
                
            print(" You can now log in as you registration is sucessful")
            
        elif choice == "3":
            print("System shutting down. Goodbye")
            return False
            
        else:
            print("Invalid choice.")
def customer_loyalty_and_ltv_engine(bookings, schedule, data):
    from tabulate import tabulate
    import pandas as pd

    print("\n--- Customer Lifetime Value (CLTV) & Loyalty Engine ---")
    print("Segmenting customers for targeted marketing and retention...\n")

    customers = {}
    for booking in bookings:
        contact = booking['Contact Number']
        name = booking['Customer Name']
        tickets = booking['Number of Tickets']
        
        movie_price = 0
        for show in schedule:
            if show['Show ID'] == booking['Show ID']:
                for movie in data:
                    if movie['Movie ID'] == show['Movie ID']:
                        movie_price = movie['Ticket Price (PKR)']
                        break
                break
        
        spent = tickets * movie_price
        
        if contact not in customers:
            customers[contact] = {'Name': name, 'Total Tickets': 0, 'Total Spent (PKR)': 0}
        
        customers[contact]['Total Tickets'] += tickets
        customers[contact]['Total Spent (PKR)'] += spent

    if not customers:
        print("No customer data available for analysis.")
        return

    report = []
    for contact, stats in customers.items():
        spent = stats['Total Spent (PKR)']
        
        if spent >= 10000:
            tier = "Platinum (VIP)"
            action = "Send complimentary premiere tickets."
        elif spent >= 5000:
            tier = "Gold"
            action = "Offer 10 percent discount on next booking."
        elif spent >= 2000:
            tier = "Silver"
            action = "Enroll in loyalty points program."
        else:
            tier = "Bronze"
            action = "Standard marketing funnel."

        report.append({
            'Customer Name': stats['Name'],
            'Contact': contact,
            'Tickets Bought': stats['Total Tickets'],
            'Lifetime Value': f"PKR {spent}",
            'Loyalty Tier': tier,
            'Recommended Action': action
        })

    df = pd.DataFrame(report)
    df = df.sort_values(by='Tickets Bought', ascending=False)
    print(tabulate(df, headers='keys', tablefmt='grid'))           

def main():
    print("Welcome to the Movie Ticket Booking System!")
    while True:
        print("\nAre you an Admin or a Customer?")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            import hashlib
            correct_hash = hashlib.sha256("miss nida".encode()).hexdigest()
            password=input('Enter password (hint:miss nida):')
            if hashlib.sha256(password.encode()).hexdigest() == correct_hash:
                print("Successfully logined.....\nAdmin Panel")
                while True:
                    print("\nChoose an operation:")
                    print("1. Manage Movies")
                    print("2. Manage Shows")
                    print("3. View Bookings")
                    print("4. Analize Bookings")
                    print("5. simulator of what if")
                    print("6. Go Back")
                    admin_choice = input("Enter your choice: ")
    
                    if admin_choice == "1":
                        print("\nMovie Management:")
                        print("1. Add a Movie")
                        print("2. View All Movies")
                        print("3. Search for a Movie")
                        print("4. Update a Movie")
                        print("5. Delete a Movie")
                        movie_choice = input("Enter your choice: ")
    
                        if movie_choice == "1":
                            add_movie(data)
                        elif movie_choice == "2":
                            show_movie()
                        elif movie_choice == "3":
                            search_movie(data)
                        elif movie_choice == "4":
                            update_movie(data)
                        elif movie_choice == "5":
                            delete_movie(data)
                        else:
                            print("Invalid choice! Please try again.")
    
                    elif admin_choice == "2":
                        print("\nShow Management:")
                        print("1. Add a Show")
                        print("2. View All Shows")
                        print("3. Search for a Show")
                        print("4. Update a Show")
                        print("5. Delete a Show")
                        show_choice = input("Enter your choice: ").strip()
    
                        if show_choice == "1":
                            add_show(schedule,data)
                        elif show_choice == "2":
                            show_sch()
                        elif show_choice == "3":
                            search_show(data, schedule)
                        elif show_choice == "4":
                            update_show(schedule, data)
                        elif show_choice == "5":
                            delete_show(schedule)
                        else:
                            print("Invalid choice! Please try again.")
    
                    elif admin_choice == "3":
                        print("\nViewing All Bookings:")
                        view_bookings()
                    elif admin_choice == "4":
                        print("\n--- Analytics & Intelligence ---")
                        print("1. Analyze Total Sales (Gross Revenue)")
                        print("2. Analyze Most Popular Movie")
                        print("3. Run Prescriptive Pricing Dashboard") 
                        print("4. Run Financial Risk & Anomaly Scan") 
                        print("5. Run Customer Lifetime Value (CLTV) Engine")
                        
                        show_choice = input("Enter your choice: ").strip()
                        if show_choice == "1":
                            total_sales_analysis(bookings, schedule, data)
                        elif show_choice == "2":
                            most_popular_movie(bookings, schedule, data)
                        elif show_choice == "3":
                            generate_pricing_recommendations(schedule, data, bookings)
                        elif show_choice == "4":
                            detect_financial_anomalies(schedule, bookings, data)
                        elif show_choice == "5": 
                            customer_loyalty_and_ltv_engine(bookings, schedule, data)
                        else:
                            print("Invalid choice! Please try again.")
                    elif admin_choice == "5": 
                        what_if_simulator(data)    
                    elif admin_choice == "6":
                        print("Returning to main menu")
                        break
    
                    else:
                        print("Invalid choice! Please try again.")

        elif choice == "2":
            print("\nCustomer Panel")
            while True:
                print("\nChoose an operation:")
                print("1. View Movies")
                print("2. Search for a Movie")
                print("3. View Shows")
                print("4. Search for a Show")
                print("5. Book Tickets")
                print("6. View Available Seats")
                print("7. Cancel Tickets")
                print("8. Ask AI Assistant for Help")  # <-- NEW OPTION
                print("9. Go Back")
                customer_choice = input("Enter your choice: ").strip()

                if customer_choice == "1":
                    show_movie()
                elif customer_choice == "2":
                    search_movie(data)
                elif customer_choice == "3":
                    show_sch()
                elif customer_choice == "4":
                    search_show(data, schedule)
                elif customer_choice == "5":
                    book_ticket(schedule,data, bookings)
                elif customer_choice == "6":
                    view_available_seats(schedule, bookings)
                elif customer_choice == "7":
                    cancel_ticket(bookings)
                elif customer_choice == "8":
                    run_ai_assistant()
                elif customer_choice == "9":    
                    print("Returning to main menu")
                    break
                else:
                    print("Invalid choice! Please try again.")

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            
            print("Invalid choice. Please try again.")

if secure_system_gateway():
    main()
    

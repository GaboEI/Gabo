from datetime import datetime

def filter_events_by_date_range(event_list):
    if not event_list:
        print("⚠️ No events registered.")
        return

    try:
        start = input("📆 Enter start date (YYYY-MM-DD): ")
        end = input("📆 Enter end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        return

    print("\n🔎 Events found in that range:\n")
    found = []

    for i, event in enumerate(event_list, 1):
        try:
            event_date = datetime.strptime(event[3], "%Y-%m-%d")
            if start_date <= event_date <= end_date:
                found.append((i, event))
        except:
            continue  # Ignora errores si alguna fecha está mal

    if found:
        print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")
        print("-" * 90)
        for i, event in found:
            print(f"{i:<4} {event[1]:<20} {event[2]:<30} {event[3]:<20} {event[0]:<10}")
    else:
        print("🚫 No events found in the selected range.")
        
        
        7️⃣ ➤ Filter events by date range
        
        
        
        
        elif opcion == "7":
    eventos = read_event()
    filter_events_by_date_range(eventos)
    
    
    
    from datetime import datetime

def filter_events_by_date_range(event_list):
    if not event_list:
        print("⚠️ No events registered.")
        return

    try:
        start = input("🔷 Enter start date (YYYY-MM-DD): ")
        end = input("🔷 Enter end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError:
        print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
        return

    found = []
    for i, event in enumerate(event_list):
        try:
            # Convertimos solo la parte de la fecha del evento (ignoramos la hora)
            event_date = datetime.strptime(event[3], "%Y-%m-%d %H:%M").date()
            if start_date <= event_date <= end_date:
                found.append((i, event))
        except Exception as e:
            continue  # Si hay error al convertir, lo ignora

    if found:
        print("\n🗓️ Events found in that range:\n")
        print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")
        print("-" * 90)
        for i, event in found:
            print(f"{i:<4} {event[1]:<20} {event[2]:<30} {event[3]:<20} {event[0]:<10}")
    else:
        print("⚠️ No events found in the selected range.")
    
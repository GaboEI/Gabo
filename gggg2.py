def search_event(event_list):
    if not event_list:
        print("⚠️ No events registered.")
        return

    criterio = input("➤ Enter the keyword, date, name or status (e.g. 'pending', '2025-07-19'): ").lower()
    print("\n🔍 Search result:")
    found = []

    for i, event in enumerate(event_list, 1):
        status = event[0].lower()
        name = event[1].lower()
        desc = event[2].lower()
        date = event[3]

        if (
            criterio in status or
            criterio in name or
            criterio in desc or
            criterio in date
        ):
            found.append((i, event))

    if found:
        print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")
        print("-" * 90)
        for i, event in found:
            print(f"{i:<4} {event[1]:<20} {event[2]:<30} {event[3]:<20} {event[0]:<10}")
    else:
        print("❌ No events were found with this criterion")
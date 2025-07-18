def search_event(event_list):
    if not event_list:
        print("⚠️ No events registered.")
        return

    criterio = input("➤ Enter the Keyword or date (⏱️ %Y-%m-%d %H:%M) ").lower()
    print("\n🔍 Search result:")
    found = []

    for i, event in enumerate(event_list, 1):
        if criterio in event[1].lower() or criterio in event[2].lower() or criterio in event[3]:
            found.append((i, event))

    if found:
        for i, event in found:
            print(f"{i}. {event[3]} - {event[2]}")
    else:
        print("❌ No events were found with this criterion")
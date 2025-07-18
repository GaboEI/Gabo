import os
import datetime

event_file = "event.txt"

def read_event():
    events = []
    if os.path.exists(event_file):
        with open(event_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                while len(parts) < 4:       # 👉 CAMBIAR AQUÍ
                    parts.append("")        # 👉 CAMBIAR AQUÍ
                events.append(parts)
    return events

def save_events(events):
    with open(event_file, "w", encoding="utf-8") as f:
        for event in events:
            while len(event) < 4:           # 👉 CAMBIAR AQUÍ
                event.append("")            # 👉 CAMBIAR AQUÍ
            f.write(f"{event[0]}|{event[1]}|{event[2]}|{event[3]}\n")  # 👉 CAMBIAR AQUÍ

def add_event():
    name = input("📝 Enter the name of event: ")
    description = input("📝 Describe the new Event: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    events = read_event()
    events.append(["Pending", name, description, date])  # 👉 CAMBIAR AQUÍ
    save_events(events)
    print("✅ Event added correctly")

def view_events(status="all"):
    events = read_event()

    if status == "Pending":
        events = [e for e in events if e[0] == "Pending"]
    elif status == "Completed":
        events = [e for e in events if e[0] == "Completed"]

    if not events:
        print("📭 No events to display")
        return

    print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")  # 👉 CAMBIAR AQUÍ
    print("=" * 90)  # 👉 CAMBIAR AQUÍ

    for i, event in enumerate(events, 1):
        status = event[0]
        name = event[1]
        desc = event[2]
        date = event[3]
        print(f"{i:<4} {name:<20} {desc:<30} {date:<20} {status:<10}")  # 👉 CAMBIAR AQUÍ

def mark_completed():
    events = read_event()
    if not events:
        print("📭 No events available")
        return

    print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")  # 👉 CAMBIAR AQUÍ
    print("=" * 90)  # 👉 CAMBIAR AQUÍ
    for i, event in enumerate(events, 1):
        status = event[0]
        name = event[1]
        desc = event[2]
        date = event[3]
        print(f"{i:<4} {name:<20} {desc:<30} {date:<20} {status:<10}")  # 👉 CAMBIAR AQUÍ

    try:
        num = int(input("🔢 Indicate the number of the event to be marked as completed: "))
        if 1 <= num <= len(events):
            events[num - 1][0] = "Completed"  # 👉 CAMBIAR AQUÍ
            save_events(events)
            print("✅ Event status was updated correctly")
        else:
            print("⚠️  Number out of range")
    except ValueError:
        print("⚠️  Invalid entry, must enter a number")

def delete_event():
    events = read_event()
    if not events:
        print("📭 No events available to delete")
        return

    print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")  # 👉 CAMBIAR AQUÍ
    print("=" * 90)  # 👉 CAMBIAR AQUÍ
    for i, event in enumerate(events, 1):
        status = event[0]
        name = event[1]
        desc = event[2]
        date = event[3]
        print(f"{i:<4} {name:<20} {desc:<30} {date:<20} {status:<10}")  # 👉 CAMBIAR AQUÍ

    try:
        num = int(input("❌ Indicate the number of the event to delete: "))
        if 1 <= num <= len(events):
            deleted = events.pop(num - 1)
            save_events(events)
            print(f"🗑️  Event '{deleted[1]}' deleted correctly")
        else:
            print("⚠️  Number out of range")
    except ValueError:
        print("⚠️  Invalid entry, must enter a number")

def menu():
    while True:
        print("""
    == 📘 PERSONAL AGENDA MENU 📘 ==
    1️⃣  Add a new event
    2️⃣  See existing events
    3️⃣  Mark event as Completed
    4️⃣  View Completed Events
    5️⃣  Delete event
    0️⃣  Exit
        """)
        opcion = input("Choose One Option: ")
        if opcion == "1":
            add_event()
        elif opcion == "2":
            view_events("Pending")
        elif opcion == "3":
            mark_completed()
        elif opcion == "4":
            view_events("Completed")
        elif opcion == "5":
            delete_event()
        elif opcion == "0":
            print("👋 Leaving the 'Agenda'. See you soon!")
            break
        else:
            print("⚠️  Invalid option, please try again.")

if __name__ == "__main__":
    menu()
    print("📝 Thank you for using the agenda. You are doing a good job.")
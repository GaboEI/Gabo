# === Personal agenda to manage events from the terminal ===
#todo--------------------
import os
import datetime
event_file = "event.txt"
event_list = []
#todo--------------------

#!!----------------------------------
#? === First function: read_event ===
#!!----------------------------------
def read_event():
    events = []
    if os.path.exists(event_file):
        with open(event_file, encoding="utf-8") as f:
            lines = f.readlines()

            # Ignorar encabezado y línea de separación
            data_lines = lines[2:]

            for line in data_lines:
                line = line.strip()
                if not line:
                    continue

                # Extraer columnas por posición fija
                try:
                    name = line[7:27].strip()
                    desc = line[30:60].strip()
                    date = line[63:83].strip()
                    status = line[86:].strip()

                    events.append([status, name, desc, date])
                except IndexError:
                    continue  # en caso de línea mal formada
    return events

#!!--------------------------------------
#? === Second function: save_events. ===
#!!--------------------------------------
def save_events(events):
        with open(event_file, "w", encoding="utf-8") as f:
            h = f"{"No":<4} | {"Name":<20} | {"Description":<30} | {"Date":<20} | {"Status":<10}\n"
            f.write(h)
            f.write("-" * 100 + "\n")
            for i, event in enumerate(events, 1):
                while len(event) < 4:
                    event.append("")
                Status = event[0]
                name = event[1]
                des = event[2]
                date = event[3]
                line  = f"{i:<4} | {name:<20} | {des:<30} | {date:<20} | {Status:<10}\n"
                f.write(line)

#!!----------------------------------
#? === Third function: add_event. ===
#!!----------------------------------
def add_event():
    name = input("📝 Enter the name of event: ").title().strip()
    description = input("📝 Describe the new Event: ").strip().capitalize()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    events = read_event()
    events.append(["Pending", name, description, date])  
    save_events(events)
    print("✅ Event added correctly")

#!!-------------------------------------
#? === Fourth function: view_events. ===
#!!-------------------------------------
def view_events(status="all"):
    events = read_event()

    if status == "Pending":
        events = [e for e in events if e[0] == "Pending"]
    elif status == "Completed":
        events = [e for e in events if e[0] == "Completed"]

    if not events:
        print("📭 No events to display")
        return

    print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")  
    print("=" * 90)  

    for i, event in enumerate(events, 1):
        status = event[0]
        name = event[1]
        desc = event[2]
        date = event[3]
        print(f"{i:<4} {name:<20} {desc:<30} {date:<20} {status:<10}")

#!!----------------------------------------
#? === Fifth function: mark_completed. ===
#!!----------------------------------------
def mark_completed():
    events = read_event()
    if not events:
        print("📭 No events available")
        return
    print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")  
    print("=" * 90) 
    for i, event in enumerate(events, 1):
        status = event[0]
        name = event[1]
        desc = event[2]
        date = event[3]
        print(f"{i:<4} {name:<20} {desc:<30} {date:<20} {status:<10}")  
    try:
        num = int(input("🔢 Indicate the number of the event to be marked as completed: "))
        if 1 <= num <= len(events):
            events[num - 1][0] = "Completed"  
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
    print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")  
    print("=" * 90) 
    for i, event in enumerate(events, 1):
        status = event[0]
        name = event[1]
        desc = event[2]
        date = event[3]
        print(f"{i:<4} {name:<20} {desc:<30} {date:<20} {status:<10}")
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

#!!------------------------------------
#? === Sect function: Search event ===
#!!------------------------------------
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

#!!-------------------------------------------------
#? === 7th function: search events by date range ===
#!!-------------------------------------------------
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
            continue 

    if found:
        print("\n🗓️ Events found in that range:\n")
        print(f"{'No.':<4} {'Name':<20} {'Description':<30} {'Date':<20} {'Status':<10}")
        print("-" * 90)
        for i, event in found:
            print(f"{i:<4} {event[1]:<20} {event[2]:<30} {event[3]:<20} {event[0]:<10}")
    else:
        print("⚠️ No events found in the selected range.")

#!!--------------------------------------
#? === 8th function: export in agenda ===
#!!--------------------------------------
from datetime import datetime

def export_agenda(event_list):
    if not event_list:
        print("⚠️ No events to export.")
        return

    # Ordenamos por fecha
    try:
        event_list.sort(key=lambda x: datetime.strptime(x[3], "%Y-%m-%d %H:%M"))
    except:
        print("⚠️ Error sorting dates.")
        return

    try:
        with open("agenda_report.txt", "w", encoding="utf-8") as file:
            file.write(f"📅 Personal Agenda Report - {datetime.now().strftime('%Y-%m-%d')}\n")
            file.write("-" * 70 + "\n")
            file.write(f"{'No.':<4} {'Name':<20} {'Description':<25} {'Date':<20} {'Status':<10}\n")
            file.write("-" * 70 + "\n")
            for i, event in enumerate(event_list, 1):
                file.write(f"{i:<4} {event[1]:<20} {event[2]:<25} {event[3]:<20} {event[0]:<10}\n")
        
        print("✅ Agenda exported successfully to 'agenda_report.txt'.")
    except Exception as e:
        print(f"❌ Error writing report: {e}")
        

#*---------------------
#? === CENTRAL MENU ===
#*---------------------
def menu():
    while True:
        print(
            """
=== *** PERSONAL AGENDA *** ===
---------------------------------
1️⃣ → Add a new event            ▶️
2️⃣ → See existing events        ▶️
3️⃣ → Mark event as Completed    ▶️
4️⃣ → View Completed Events      ▶️
5️⃣ → Delete event               ▶️
6️⃣ → Search in Agenda           ▶️
7️⃣ → Filter events by date rang ▶️
8️⃣ → Export Agenda              ▶️
0️⃣ → Exit                       ▶️
---------------------------------
"""
        )
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
        elif opcion == "6":
            events = read_event()
            search_event(events)
        elif opcion == "7":
            event = read_event()
            filter_events_by_date_range(event)
        elif opcion == "8":
            events = read_event()
            export_agenda(events)
        elif opcion == "0":
            print("👋 Leaving the 'Agenda'. See you soon!")
            break
        else:
            print("⚠️  Invalid option, please try again.")
if __name__ == "__main__":
    menu()
    print("📝 Thank you for using the agenda. You are doing a good job.")
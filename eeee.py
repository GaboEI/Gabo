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
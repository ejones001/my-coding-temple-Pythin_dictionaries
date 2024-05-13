# Initial service ticket structure
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"New ticket {ticket_id} opened for {customer_name}.")
    else:
        print(f"Ticket ID {ticket_id} already exists.")

# Function to update the status of a ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Status of ticket {ticket_id} updated to {new_status}.")
    else:
        print(f"Ticket ID {ticket_id} does not exist.")

# Function to display all tickets or filter by status
def display_tickets(status_filter=None):
    print("Service Tickets:")
    for ticket_id, details in service_tickets.items():
        if status_filter is None or details["Status"] == status_filter:
            print(f"Ticket ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")


print("Initial Service Tickets:")
display_tickets()

print("\nOpening a new ticket:")
open_ticket("Ticket003", "Charlie", "Website not loading")

print("\nUpdating the status of a ticket:")
update_ticket_status("Ticket002", "open")

print("\nFiltered Service Tickets (Open):")
display_tickets("open")

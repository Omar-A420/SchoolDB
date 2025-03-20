# Booking System

## Overview
The Booking System is designed to allow teachers to book rooms and facilities in the school efficiently. The current manual process requires a teacher to email a staff member, who then manually inputs the booking into the database. This system automates the booking process, reducing workload and improving efficiency.

## Features
- User login system with authentication.
- Room and facility selection.
- Time slot selection for bookings.
- Real-time availability updates.
- Automatic data logging into a database.
- Prevention of double bookings.
- Booking cancellation feature.
- Display of fully booked rooms.
- Automatic email confirmation upon booking.

## Usage
1. **Login**: Users (teachers) log in using their school credentials.
2. **Select Room/Facility**: Choose the required room or facility for booking.
3. **Select Time Slot**: Pick an available time slot.
4. **Confirm Booking**: Confirm the selection.
5. **Receive Confirmation**: A confirmation email is sent.
6. **Cancel Booking (if needed)**: Users can cancel a booking if necessary.

## Benefits
- **Reduces workload**: Automates the booking process, allowing staff to focus on other responsibilities.
- **Improves security**: Uses a cloud-based system to protect school information.
- **Prevents double bookings**: Ensures no conflicts in room reservations.
- **Automates communication**: Sends confirmation emails instantly.

## System Design
- **User Authentication**: Only registered teachers can access the system.
- **Database Integration**: Stores and manages bookings efficiently.
- **Real-time Updates**: Ensures accurate availability tracking.
- **User-Friendly Interface**: Simplifies the booking process for teachers.

## Technical Details
- **Database**: Stores user details, room availability, and bookings.
- **Data Flow**:
  - User selects a room and time slot.
  - The system updates the database.
  - Confirmation is sent to the user.
- **Entity Relationship Diagram**: Defines relationships between users, bookings, and facilities.

## Future Enhancements
- Integration with school calendars (e.g., Outlook, Gmail).
- Mobile-friendly version for easier access.
- Advanced analytics for booking trends.

## Installation & Setup
1. Download the software.
2. Run the installation file.
3. Launch the application and log in with school credentials.
4. Begin booking rooms and facilities.

## Bookings
To view the bookings made:
1. Download a database file application - (e.g. DB Browser).
2. Open the file bookings.db in this application to view all bookings made.
3. To ensure user data is correct - open user_data.db in this application aswell. 

---

from abc import ABC, abstractmethod
from datetime import datetime

from EnumsConstants import *
from BookReservation import *

class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE) -> None:
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person
    
    def reset_password(self):
        pass


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE) -> None:
        super().__init__(id, password, person, status)
    
    def add_book_items(self, book_item):
        pass

    def block_memeber(self, member):
        pass

    def unblock_memeber(self, memeber):
        pass
    

class Memeber(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE) -> None:
        super().__init__(id, password, person, status)
        self.__date_of_memebership = datetime.today()
        self.__total_books_checkedout = 0
    
    def get_total_books_checkedout(self):
        return self.__total_books_checkedout
    
    def reserve_book_item(self, book_item):
        pass

    def increment_total_books_checkedout(self):
        pass

    def renew_book_item(self, book_item):
        pass

    def checkout_book_item(self, book_item):
        if self.get_total_books_checkedout() > Constants.MAX_BOOKS_ISSUED_TO_A_USER:
            print("User has already checked-out maximum number of books")
            return False
        
        book_reservation = BookReservation.fetch_reservation_details(
            book_item.get_barcode())
        
        if book_reservation and book_reservation.get_memeber_id() != self.get_id():
            # Book item has a pending reservation from another user
            print("This book is reserved by another memeber")
            return False
        elif book_reservation:
            # book has a pending reservation from the given memeber, update it
            book_reservation.update_status(ReservervationStatus.COMPLETED)
        

        if not book_item.checkout(self.get_id()):
            return False
        
        self.increment_total_books_checkedout()
        return True
    
    def check_for_fine(self, book_item_barcode):
        book_lending = BookLending.fetch_lending_details(book_item_barcode)
        due_date = book_lending.get_due_date()
        today = datetime.today()
        
        # check if the book has been returned within the due date
        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_memeber_id(), diff_days)
        
    def return_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(
            book_item.get_barcode())
        
        if book_reservation:
            # book has a pending reservation
            book_item.update_book_item_status(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
        book_item.update_book_item_status(BookStatus.AVAILABLE)
    
    def renew_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(
            book_item.get_barcode())
        
        # check if current book item has a pending reservation from another memeber
        if book_reservation and book_reservation.get_memeber_id() != self.get_member_id():
            print("Current book is reserved by another memeber")
            self.decrement_total_books_checkout()
            book_item.update_book_item_state(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            return False
        elif book_reservation:
            # Book item has a pending reservation from current user
            book_reservation.update_status(ReservervationStatus.COMPLETED)
        BookLending.lend_book(book_item.get_bar_code(), self.get_memeber_id())
        book_item.update_due_date(
            datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
        
        return True

    

class ContractNode:
    """
    A class representing a node in a linked list of Contract Line Items (CLINs).
    Each node contains a Clin object and a reference to the next node.
    """
    
    def __init__(self, name, clin):
        """
        Initialize a ContractNode with a Clin object.
        
        Parameters:
        -----------
        clin : Clin
            The Clin object to store in this node
            
        """
        
        self.clin = clin
        self.name = name
        self.next = None
    
    def get_clin(self):
        """
        Get the Clin object stored in this node.
        
        Returns:
        --------
        Clin
            The Clin object stored in this node
        """
        return self.clin
    
    def set_next(self, next_node):
        """
        Set the next node in the linked list.
        
        Parameters:
        -----------
        next_node : ContractNode
            The next node in the linked list
        """
        self.next = next_node
    
    def get_next(self):
        """
        Get the next node in the linked list.
        
        Returns:
        --------
        ContractNode or None
            The next node in the linked list, or None if this is the last node
        """
        return self.next
    
    def __str__(self):
        """Return a string representation of the ContractNode."""
        return f"ContractNode({self.clin})"
    
    def __repr__(self):
        """Return a representation of the ContractNode."""
        return self.__str__()


class ContractLinkedList:
    """
    A linked list implementation for managing Contract Line Items (CLINs).
    """
    
    def __init__(self):
        """Initialize an empty ContractLinkedList."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, clin):
        """
        Append a Clin to the end of the linked list.
        
        Parameters:
        -----------
        clin : Clin
            The Clin object to append
        """
        new_node = ContractNode(clin)
        
        if self.head is None:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # Add to the end
            self.tail.set_next(new_node)
            self.tail = new_node
            
        self.size += 1
    
    def prepend(self, clin):
        """
        Prepend a Clin to the beginning of the linked list.
        
        Parameters:
        -----------
        clin : Clin
            The Clin object to prepend
        """
        new_node = ContractNode(clin)
        
        if self.head is None:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # Add to the beginning
            new_node.set_next(self.head)
            self.head = new_node
            
        self.size += 1
    
    def find_by_name(self, clin_name):
        """
        Find a Clin by its name.
        
        Parameters:
        -----------
        clin_name : str
            The name of the Clin to find
            
        Returns:
        --------
        Clin or None
            The Clin object if found, None otherwise
        """
        current = self.head
        
        while current is not None:
            if current.get_clin().name == clin_name:
                return current.get_clin()
            current = current.get_next()
            
        return None
    
    def remove_by_name(self, clin_name):
        """
        Remove a Clin from the linked list by its name.
        
        Parameters:
        -----------
        clin_name : str
            The name of the Clin to remove
            
        Returns:
        --------
        bool
            True if the Clin was found and removed, False otherwise
        """
        if self.head is None:
            return False
            
        # Special case for head
        if self.head.get_clin().name == clin_name:
            self.head = self.head.get_next()
            if self.head is None:
                # List is now empty
                self.tail = None
            self.size -= 1
            return True
            
        # Search for the node to remove
        current = self.head
        while current.get_next() is not None:
            if current.get_next().get_clin().name == clin_name:
                # Found the node to remove
                if current.get_next() == self.tail:
                    # If removing the tail
                    self.tail = current
                current.set_next(current.get_next().get_next())
                self.size -= 1
                return True
            current = current.get_next()
            
        return False
    
    def get_all_clins(self):
        """
        Get all Clin objects in the linked list.
        
        Returns:
        --------
        list
            List of all Clin objects
        """
        clins = []
        current = self.head
        
        while current is not None:
            clins.append(current.get_clin())
            current = current.get_next()
            
        return clins
    
    def total_obligated(self):
        """
        Calculate the total obligated amount across all Clins.
        
        Returns:
        --------
        int
            The total obligated amount
        """
        total = 0
        current = self.head
        
        while current is not None:
            total += current.get_clin().total_obligated()
            current = current.get_next()
            
        return total
    
    def total_paid(self):
        """
        Calculate the total paid amount across all Clins.
        
        Returns:
        --------
        int
            The total paid amount
        """
        total = 0
        current = self.head
        
        while current is not None:
            total += current.get_clin().total_paid()
            current = current.get_next()
            
        return total
    
    def total_unpaid(self):
        """
        Calculate the total unpaid amount across all Clins.
        
        Returns:
        --------
        int
            The total unpaid amount
        """
        total = 0
        current = self.head
        
        while current is not None:
            total += current.get_clin().total_unpaid()
            current = current.get_next()
            
        return total
    
    def total_funding(self):
        """
        Calculate the total funding amount across all Clins.
        
        Returns:
        --------
        int
            The total funding amount
        """
        total = 0
        current = self.head
        
        while current is not None:
            total += current.get_clin().total_funding()
            current = current.get_next()
            
        return total
    
    def total_remaining_funding(self):
        """
        Calculate the total remaining funding across all Clins.
        
        Returns:
        --------
        int
            The total remaining funding
        """
        total = 0
        current = self.head
        
        while current is not None:
            total += current.get_clin().total_remaining_funding()
            current = current.get_next()
            
        return total
    
    def size(self):
        """
        Get the number of Clins in the linked list.
        
        Returns:
        --------
        int
            The number of Clins
        """
        return self.size
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
        --------
        bool
            True if the linked list is empty, False otherwise
        """
        return self.head is None
    
    def __str__(self):
        """Return a string representation of the ContractLinkedList."""
        if self.head is None:
            return "ContractLinkedList(empty)"
            
        result = "ContractLinkedList(\n"
        current = self.head
        while current is not None:
            result += f"  {current.get_clin()}\n"
            current = current.get_next()
        result += ")"
        return result
    
    def __repr__(self):
        """Return a representation of the ContractLinkedList."""
        return self.__str__()


# Example usage
if __name__ == "__main__":
    from Clin import Clin
    from subClin import subClin
    
    # Create subClins
    subclin1 = subClin("SubClin 1", 100, 50, 50, 2021, 100)
    subclin2 = subClin("SubClin 2", 200, 200, 0, 2021, 200)
    
    # Create Clins
    clin1 = Clin("Clin 1")
    clin1.add_subclin(subclin1)
    
    clin2 = Clin("Clin 2")
    clin2.add_subclin(subclin2)
    
    # Create ContractLinkedList
    contract = ContractLinkedList()
    contract.append(clin1)
    contract.append(clin2)
    
    print(contract)
    print(f"Total Obligated: ${contract.total_obligated()}")
    print(f"Total Paid: ${contract.total_paid()}")
    print(f"Total Unpaid: ${contract.total_unpaid()}")
    print(f"Total Funding: ${contract.total_funding()}")
    print(f"Total Remaining Funding: ${contract.total_remaining_funding()}")
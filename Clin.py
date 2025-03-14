from subClin import subClin  # Import the subClin class from the subClin module

class Clin:
    def __init__(self, name):
        """
        Initialize a Clin object that stores subClin objects.
        
        Parameters:
        -----------
        name : str
            The name of the Clin
        description : str, optional
            A description of the Clin (default is empty string)
        """
        self.name = name
        self.subclins = []  # Array to store subClin objects
    
    def add_subclin(self, subclin):
        """
        Add a subClin object to the Clin.
        
        Parameters:
        -----------
        subclin : subClin
            The subClin object to add
        """
        self.subclins.append(subclin)
    
    def remove_subclin(self, subclin_name):
        """
        Remove a subClin object from the Clin by name.
        
        Parameters:
        -----------
        subclin_name : str
            The name of the subClin to remove
            
        Returns:
        --------
        bool
            True if subclin was found and removed, False otherwise
        """
        for i, subclin in enumerate(self.subclins):
            if subclin.get_name() == subclin_name:
                self.subclins.pop(i)
                return True
        return False
    
    def get_subclin(self, subclin_name):
        """
        Get a subClin object by name.
        
        Parameters:
        -----------
        subclin_name : str
            The name of the subClin to get
            
        Returns:
        --------
        subClin or None
            The subClin object if found, None otherwise
        """
        for subclin in self.subclins:
            if subclin.get_name() == subclin_name:
                return subclin
        return None
    
    def get_all_subclins(self):
        """
        Get all subClin objects.
        
        Returns:
        --------
        list
            List of all subClin objects
        """
        return self.subclins
    
    def total_obligated(self):
        """
        Calculate the total obligated amount across all subClins.
        
        Returns:
        --------
        int
            The total obligated amount
        """
        return sum(subclin.get_obligated() for subclin in self.subclins)
    
    def total_paid(self):
        """
        Calculate the total paid amount across all subClins.
        
        Returns:
        --------
        int
            The total paid amount
        """
        return sum(subclin.get_paid() for subclin in self.subclins)
    
    def total_unpaid(self):
        """
        Calculate the total unpaid amount across all subClins.
        
        Returns:
        --------
        int
            The total unpaid amount
        """
        return sum(subclin.get_unpaid() for subclin in self.subclins)
    
    def total_funding(self):
        """
        Calculate the total funding amount across all subClins.
        
        Returns:
        --------
        int
            The total funding amount
        """
        return sum(subclin.get_funding() for subclin in self.subclins)
    
    def total_remaining_funding(self):
        """
        Calculate the total remaining funding across all subClins.
        
        Returns:
        --------
        int
            The total remaining funding
        """
        return sum(subclin.remaining_funding() for subclin in self.subclins)
    
    def __str__(self):
        """Return a string representation of the Clin object."""
        subclin_count = len(self.subclins)
        return f"Clin(name={self.name}, subclins={subclin_count})"
    
    def __repr__(self):
        """Return a representation of the Clin object."""
        return self.__str__()

if __name__ == "__main__":
    # Create example subClin objects
    subclin1 = subClin("SubClin 1", 100, 50, 50, 2021, 100)
    subclin2 = subClin("SubClin 2", 200, 200, 0, 2021, 200)
    subclin3 = subClin("SubClin 3", 300, 0, 300, 2021, 300)
    
    # Create a Clin and add subClins
    clin = Clin("Clin 1")
    clin.add_subclin(subclin1)
    clin.add_subclin(subclin2)
    clin.add_subclin(subclin3)
    
    print(clin)
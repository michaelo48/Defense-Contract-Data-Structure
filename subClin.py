class subClin:
    def __init__(self, name, obligated, paid, unpaid, fy, funding):
        """
        Initialize a subClin object with the specified parameters.
        
        Parameters:
        -----------
        name : str
            The name of the subClin
        obligated : int
            The obligated amount
        paid : int
            The paid amount
        unpaid : int
            The unpaid amount
        fy : int
            The fiscal year
        funding : int
            The funding amount
        """
        self.name = name
        self.obligated = obligated
        self.paid = paid
        self.unpaid = unpaid
        self.fy = fy
        self.funding = funding
    
    def __str__(self):
        """Return a string representation of the subClin object."""
        return f"subClin(name={self.name}, obligated={self.obligated}, paid={self.paid}, unpaid={self.unpaid}, fy={self.fy}, funding={self.funding})"
    
    def __repr__(self):
        """Return a representation of the subClin object."""
        return self.__str__()
    
    def remaining_funding(self):
        """Calculate and return the remaining funding."""
        return self.funding - self.obligated
    
    def payment_status(self):
        """Return the payment status based on obligated vs paid amounts."""
        if self.paid == self.obligated:
            return "Fully Paid"
        elif self.paid == 0:
            return "Not Paid"
        else:
            return "Partially Paid"
            
    def get_name(self):
        """Return the name parameter."""
        return self.name
        
    def get_obligated(self):
        """Return the obligated parameter."""
        return self.obligated
        
    def get_paid(self):
        """Return the paid parameter."""
        return self.paid
        
    def get_unpaid(self):
        """Return the unpaid parameter."""
        return self.unpaid
        
    def get_fy(self):
        """Return the fiscal year parameter."""
        return self.fy
        
    def get_funding(self):
        """Return the funding parameter."""
        return self.funding
sub = subClin("subClin1", 1000, 500, 500, 2021, 2000)

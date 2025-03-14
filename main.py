if __name__ == "__main__":
    from Clin import Clin
    from subClin import subClin
    from ContractLinkedList import ContractLinkedList
    
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
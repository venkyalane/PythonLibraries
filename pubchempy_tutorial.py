import pubchempy as pcp

## Enter chemical name to get information about that chemical anme or formula
chemical_name = input("Enter chemical name OR Formula: ")

try:
    compound = pcp.get_compounds(chemical_name, 'name')[0]
    # compound = pcp.Compound.from_cid(5793)
    print("IUPAC Name: ",compound.iupac_name)
    print("Comman Name: ",compound.synonyms[0])
    print("Molecular Weight: ",compound.molecular_weight)
    print("Formula: ",compound.molecular_formula)
    try:
        pcp.download('PNG', f'{compound.molecular_formula}.png', f'{chemical_name}', 'name')
        print("Image download completed...")
    except:
        print("There was problem in image download!!!")
except IndexError:
    print(f"No information found for {compound}")


# pcp.download('CSV', 's.csv', [1,2,3], operation='property/CanonicalSMILES,IsomericSMILES')
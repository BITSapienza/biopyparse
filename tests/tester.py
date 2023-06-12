from Bioparse import BioPyParse, findSpeciesFromFile

# Init the module
bio = BioPyParse(verbose=True)

# Set the connection wiht mongo database
bio.newDatabase("BiologyTest","192.168.1.197",27018)

# Auxiliary function for parsing organisms from a csv file
ist = findSpeciesFromFile("fileWithOrganisms.csv",splitColumns="\t",indexSearch=1,fromLine=1)

# Enter critical section
try:

    # Set up email for speed up
    # bio.setEmailAndToken("example@email.com","API_TOKEN")
    organismList = ["Chlorella", "Scenedesmus"]
    # Import Taxonomy data and generate the taxonomy tree
    taxIds = bio.importTaxonFromList(organismList,collectionName="taxonomy")
    bio.generateTaxonomyTree(collectionName="taxon_tree",taxonomyCollection="taxonomy")

    # Import data from Nucleotide & Protein
    bio.importData(collectionName="nucleotide",taxonomyCollection="taxonomy",typeimport="n")
    bio.importData(collectionName="protein",taxonomyCollection="taxonomy",typeimport="p")

    # Create a table with basic and advance info
    bio.createTable(collectionName="table",taxonomyCollection="taxonomy",nucleotideCollection="nucleotide",proteinCollection="protein")

    # Import genome datas from a list of taxonomy id
    bio.importSRA(taxIds,sraCollection="sequences")

    # Show collections in database
    collections = bio.showCollections()

    # Make custom database call
    list_data = bio.requestDatabase(bio.FINDONE,"taxonomy",{"TaxId":"3077"},{"ScientificName":1,"_id":0})


except Exception as e:
    print(f"Error executing {e}")
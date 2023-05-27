# BioPyParse

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MongoDb](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)


[Università La Sapienza Roma](https://www.uniroma1.it/en), [Dipartimento di Informatica](https://www.studiareinformatica.uniroma1.it/)

![Sapienza Università di Roma](https://www.uniroma1.it/sites/default/files/images/logo/sapienza-big.png)

### Credits

[`federico-rosatelli`](https://github.com/federico-rosatelli) [`Mat`](https://github.com/AxnNxs) [`Loriv3`](https://github.com/Loriv3) [`Samsey`](https://github.com/Samseys) [`Calli`](https://github.com/BboyCaligola)



# BioPyParse Module Description

Biopyparse is a simple module used to retrive data from [NCBI](https://www.ncbi.nlm.nih.gov/) and save it to a mongo-db database.

This program enable you to manage a large dataset of data accessible from other technologies and libraries. For faster data retrieval we recommend you to add you [NCBI login Email](https://account.ncbi.nlm.nih.gov/) with your [API Key](https://www.ncbi.nlm.nih.gov/account/settings/).

### Methods examples

The module consists of a class, called biopyparse, and a function. The class is initialized without access to the database which must be set with the method: 
```python
def newDatabase(self,databaseName:str,clientIp:str="localhost",clientPort:int=27017)
```

Assuming you have downloaded the desired taxonomic data, the method:
```python
def generateTaxonomyTree(self,collectionName:str|None = "taxonomy_tree",taxonomyCollection:str|None = "taxonomy_data")
```
will create a taxonomic tree structured like this
```json
[
    {
        "ScientificName": "ExampleScientificName",
        "TaxId": "ExampleTaxId",
        "Rank": "ExampleRank",
        "SubClasses": [
            {
                "ScientificName": "SubExampleScientificName",
                "TaxId"; "SubExampleTaxId"
            },
            ...
        ]
    },
    ...
]
```
and it'll import it into the database with the collection name as `collectionName`.

# Modules used

Pip3:                 "https://pip.pypa.io/en/stable/"

Biopython:            "https://biopython.org/wiki/Documentation"

Pymongo:              "https://pymongo.readthedocs.io/en/stable/"

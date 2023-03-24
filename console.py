# import pandas as pd
# table_string = 'id,institutionCode,collectionCode,ownerInstitutionCode,collectionID,basisOfRecord,occurrenceID,catalogNumber,otherCatalogNumbers,kingdom,phylum,class,order,family,scientificName,taxonID,scientificNameAuthorship,genus,specificEpithet,taxonRank,infraspecificEpithet,identifiedBy,dateIdentified,identificationReferences,identificationRemarks,taxonRemarks,identificationQualifier,typeStatus,recordedBy,recordNumber,eventDate,year,month,day,startDayOfYear,endDayOfYear,verbatimEventDate,occurrenceRemarks,habitat,fieldNumber,informationWithheld,dataGeneralizations,dynamicProperties,associatedTaxa,reproductiveCondition,establishmentMeans,lifeStage,sex,individualCount,samplingProtocol,samplingEffort,preparations,country,stateProvince,county,municipality,locality,locationRemarks,decimalLatitude,decimalLongitude,geodeticDatum,coordinateUncertaintyInMeters,verbatimCoordinates,georeferencedBy,georeferenceProtocol,georeferenceSources,georeferenceVerificationStatus,georeferenceRemarks,minimumElevationInMeters,maximumElevationInMeters,minimumDepthInMeters,maximumDepthInMeters,verbatimDepth,verbatimElevation,disposition,language,recordEnteredBy,modified,rights,rightsHolder,accessRights,recordId,references'

# df = pd.read_csv('data/animal_occurrences.csv')
# # print(df[:5])

# print(table_string, sep=',', end=' ')

from csv import reader
  
# Get CSV File Columns Name
with open('data/animal_occurrences.csv', 'r') as readObj:
    csvReader = reader(readObj)
    headers = next(csvReader)

# To SQL table format
# for header in headers:
#     print(header + ' VARCHAR,')

# Column names with space and comma
# for header in headers:
#     print(header, end=', ')

print(headers)
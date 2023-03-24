class Animal:
    __table__ = 'animals'
    columns = ['id', 'institutionCode', 'collectionCode', 'ownerInstitutionCode',
               'collectionID', 'basisOfRecord', 'occurrenceID', 'catalogNumber',
               'otherCatalogNumbers', 'kingdom', 'phylum', 'class_', 'order_',
               'family', 'scientificName', 'taxonID', 'scientificNameAuthorship',
               'genus', 'specificEpithet', 'taxonRank', 'infraspecificEpithet',
               'identifiedBy', 'dateIdentified', 'identificationReferences',
               'identificationRemarks', 'taxonRemarks', 'identificationQualifier',
               'typeStatus', 'recordedBy', 'recordNumber', 'eventDate', 'year',
               'month', 'day', 'startDayOfYear', 'endDayOfYear', 'verbatimEventDate',
               'occurrenceRemarks', 'habitat', 'fieldNumber', 'informationWithheld',
               'dataGeneralizations', 'dynamicProperties', 'associatedTaxa',
               'reproductiveCondition', 'establishmentMeans', 'lifeStage', 'sex',
               'individualCount', 'samplingProtocol', 'samplingEffort', 'preparations',
               'country', 'stateProvince', 'county', 'municipality', 'locality',
               'locationRemarks', 'decimalLatitude', 'decimalLongitude', 'geodeticDatum',
               'coordinateUncertaintyInMeters', 'verbatimCoordinates', 'georeferencedBy',
               'georeferenceProtocol', 'georeferenceSources',
               'georeferenceVerificationStatus', 'georeferenceRemarks',
               'minimumElevationInMeters', 'maximumElevationInMeters',
               'minimumDepthInMeters', 'maximumDepthInMeters', 'verbatimDepth',
               'verbatimElevation', 'disposition', 'language', 'recordEnteredBy',
               'modified', 'rights', 'rightsHolder', 'accessRights', 'recordId',
               'references_']
    
    def __init__(self, values, columns=columns):
        self.__dict__ = dict(zip(columns, values))
    

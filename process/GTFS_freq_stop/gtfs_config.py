################################################################################
# Script: gtfs_config.py

# Description: This script contain GTFS parameters defined for each study regions
# for importing to conduct stop frequency analysis

# Note: most cities' parameters are based upon the stardard GTFS format
# however, this may not be the case for every study regions
# therefore, further research may be needed to define correct agency and route types
################################################################################

# set up study region GTFS config
GTFS = {'adelaide':{'gtfs_filename':'gtfs_input_data/gtfs_au_sa_adelaidemetro_20191004',
                    'gtfs_provider' : 'AdelaideMetro',
                    'gtfs_year' : '2019',
                    # define month and day for "representative period" start and end date ie. not in school time
                    'start_date_mmdd' : '20191008',
                    'end_date_mmdd' : '20191205',
                    # get bounding box from study region boundary shapefile
                    # bounding box formatted as a 4 element tuple: (lng_max, lat_min, lng_min, lat_max)
                    # you can generate a bounding box by going to http://boundingbox.klokantech.com/ and selecting the CSV format.
                    'bbox' : (138.46098212857206, -35.15966609024628, 138.74830806651352, -34.71454282915053),
                    'crs': 'epsg:7845',
                    # define modes for GTFS feed(s) as per agency_id codes in agency.txt below
                    # this may varied across different cities
                    'modes' : {
                        'bus' : {'route_types': [3],
                                  'day_time' : ['07:00:00', '19:00:00'],
                                  'intervals': 30,
                                 'agency_id': None},
                        'tram':{'route_types': [0],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': None},
                        'train':{'route_types': [1,2],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': None},
                        'ferry':{'route_types': [4],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': None}
                    }
                   },
        'melbourne':{'gtfs_filename':'gtfs_input_data/gtfs_au_vic_ptv_20191004',
                    'gtfs_provider' : 'PublicTransportVictoria',
                    'gtfs_year' : '2019',
                    'start_date_mmdd' : '20191008',
                    'end_date_mmdd' : '20191205',
                     'bbox' : (144.59067957842007, -38.21131973169178, 145.39847326519424, -37.61837232908795),
                     'crs': 'epsg:7845',
                    'modes' : {
                        'bus' : {'route_types': [3],
                                  'day_time' : ['07:00:00', '19:00:00'],
                                  'intervals': 30,
                                 'agency_id': [4, 6]},
                        'tram':{'route_types': [0],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': [3]},
                        'train':{'route_types': [1,2],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': [1,2]}

                    }
                   },
        'sydney' : {'gtfs_filename':'gtfs_input_data/gtfs_au_nsw_tfnsw_complete_20190619',
                    'gtfs_provider' : 'NSW',
                    'gtfs_year' : '2019',
                    'start_date_mmdd' : '20191008',
                    'end_date_mmdd' : '20191205',
                    'bbox' : (150.6290606117829, -34.12321411958463, 151.3206735172292, -33.66275213092711),
                    'crs': 'epsg:7845',
                    'modes' : {
                        'bus' : {'route_types': [700,712,714],
                                  'day_time' : ['07:00:00', '19:00:00'],
                                  'intervals': 30,
                                 'agency_id': None},
                        'tram':{'route_types': [0],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': None},
                        'train':{'route_types': [2,401],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': None},
                        'ferry':{'route_types': [4],
                                'day_time' : ['07:00:00', '19:00:00'],
                                'intervals': 30,
                                'agency_id': None}
                    }
                   },
       'phoenix' : {'gtfs_filename':'gtfs_input_data/gtfs_us_phoenix_valleymetro_20190403',
                   'gtfs_provider' : 'Valleymetro',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (-112.32944760645097, 33.28617148327744, -111.9200170423412, 33.71516047286253),
                   'crs': 'epsg:32612',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                  },
       'mexico_city' : {'gtfs_filename':'gtfs_input_data/gtfs_mexico_mexico_city_fdg_20180101',
                   'gtfs_provider' : 'FederalDistrictGovernment',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (-99.33472129581168, 19.1632356281967, -98.93554618620378, 19.585767134392107),
                   'crs': 'epsg:32614',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                  },
       'baltimore' : {'gtfs_filename':'gtfs_input_data/gtfs_us_baltimore_MarylandMTA_20180101',
                   'gtfs_provider' : 'MarylandMTA',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (-76.71732081546881, 39.197419266639976, -76.5236521818912, 39.376708110613045),
                   'crs': 'epsg:32618',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                  },
       'sao_paulo' : {'gtfs_filename':'gtfs_input_data/gtfs_brazil_sao_paulo_SPTrans_20080101',
                   'gtfs_provider' : 'SPTrans',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20191008',
                   'end_date_mmdd' : '20191205',
                   'bbox' : (-46.830230353747325, -23.819961957892033, -46.36030177462541, -23.392833498544647),
                   'crs': 'epsg:32723',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                  }
                  },
       'auckland' : {'gtfs_filename':'gtfs_input_data/gtfs_newzealand_auckland_AucklandTransport_20190928',
                   'gtfs_provider' : 'AucklandTransport',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20191008',
                   'end_date_mmdd' : '20191205',
                   'bbox' :  (174.57726564925753, -37.089137447205424, 174.98796590474333, -36.68399669533544),
                   'crs': 'epsg:2193',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                               }
                               },
       'seattle' : {'gtfs_filename':'gtfs_input_data/gtfs_us_seattle_kingcountymetro_20190319',
                   'gtfs_provider' : 'KingCountyMetro',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (-122.44062497660697, 47.32215932339286, -122.14265080596407, 47.78244655092636),
                   'crs': 'epsg:32610',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                  },
       'odense' : {'gtfs_filename':'gtfs_input_data/gtfs_denmark_odense_Rejseplanen_20190314',
                   'gtfs_provider' : 'Rejseplanen',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (10.30381254797572, 55.33877682649117, 10.46065004137351, 55.44769823364561),
                   'crs': 'epsg:32632',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                  },
       'cologne' : {'gtfs_filename':'gtfs_input_data/gtfs_germany_cologne_VR_20171210',
                   'gtfs_provider' : 'VRS',
                   'gtfs_year' : '2018',
                   'start_date_mmdd' : '20180405',
                   'end_date_mmdd' : '20180605',
                   'bbox' : (6.8090292419421345, 50.82712108456513, 7.150063369469329, 51.074342237096744),
                   'crs': 'epsg:32631',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                   },
       'barcelona' : {'gtfs_filename':'gtfs_input_data/gtfs_spain_barcelona_TMB_20190402',
                   'gtfs_provider' : 'TMB',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (2.0822008749659653, 41.31251726667463, 2.2342770048946647, 41.47251143638445),
                   'crs': 'epsg:25831',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                   },
       'valencia' : {'gtfs_filename':'gtfs_input_data/gtfs_spain_valencia_metroValencia_20190123',
                   'gtfs_provider' : 'metroValencia',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (-0.4382381213256652, 39.36674924068613, -0.28735724339363344, 39.570614328215),
                   'crs': 'epsg:25830',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                   },
       'lisbon' : {'gtfs_filename':'gtfs_input_data/gtfs_portugal_lisbon_carris_20111015',
                   'gtfs_provider' : 'carris',
                   'gtfs_year' : '2019',
                   'start_date_mmdd' : '20190405',
                   'end_date_mmdd' : '20190605',
                   'bbox' : (-9.235578212348193, 38.686900346684894, -9.084818912088005, 38.80035575382599),
                   'crs': 'epsg:3763',
                   'modes' : {
                       'bus' : {'route_types': [3],
                                 'day_time' : ['07:00:00', '19:00:00'],
                                 'intervals': 30,
                                'agency_id': None},
                       'tram':{'route_types': [0],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'train':{'route_types': [1,2],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None},
                       'ferry':{'route_types': [4],
                               'day_time' : ['07:00:00', '19:00:00'],
                               'intervals': 30,
                               'agency_id': None}
                   }
                   }
                               }
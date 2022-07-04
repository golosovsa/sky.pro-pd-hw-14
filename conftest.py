"""
    conftest module
    fixtures for app testing
"""

# global imports
import sqlite3
import pathlib
import pytest
from flask import Flask

# local imports
from app import create_app
import config


@pytest.fixture(scope="module")
def test_app():
    """ Fixture for testing the app """

    app: Flask = create_app()
    app.config.from_object(config.Testing)

    with app.app_context(), app.test_request_context():
        yield app


@pytest.fixture(scope="module")
def test_db():
    dump_file = pathlib.Path(config.Testing.APP_DATA_FOLDER) \
        .joinpath("netflix.dump")

    with sqlite3.connect(":memory:") as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE netflix (
            show_id text, type text, title text, director text, cast text, 
            country text, date_added datetime, release_year int, rating text, 
            duration int, duration_type text, listed_in text, description text);
        """)

        data = [
            (
                's0', 'type1', 'title0', 'director5, director4', 'actor17, actor2, actor13, actor14',
                'country5', '2005-09-17', 2004, 'rating2', 336, 'durationtype1', 'genre4', 'description0'
            ),
            (
                's1', 'type1', 'title1', 'director7', 'actor9, actor11, actor20, actor3',
                'country3', '2018-06-07', 2012, 'rating4', 346, 'durationtype1', 'genre3', 'description1'
            ),
            (
                's2', 'type1', 'title2', 'director8', 'actor19, actor15, actor7, actor7', 'country2', '2014-11-19',
                2003, 'rating4', 500, 'durationtype1', 'genre3, genre2, genre3, genre4', 'description2'
            ),
            (
                's3', 'type2', 'title3', 'director2', 'actor6, actor5, actor20, actor19, actor18', 'country1',
                '2013-06-15',
                2019, 'rating1', 10, 'durationtype2', 'genre3, genre3, genre3, genre4', 'description3'
            ),
            (
                's4', 'type2', 'title4', 'director5', 'actor1, actor6, actor8', 'country4', '2011-09-21', 2015,
                'rating2',
                8, 'durationtype2', 'genre4, genre2, genre1, genre1, genre4', 'description4'
            ),
            (
                's5', 'type2', 'title5', 'director10', 'actor3, actor14, actor15', 'country5', '2017-09-25', 2014,
                'rating4', 7, 'durationtype2', 'genre4, genre1, genre1, genre4', 'description5'
            ),
            (
                's6', 'type1', 'title6', 'director2, director7, director10, director10',
                'actor10, actor19, actor5, actor7, actor18', 'country3', '2012-10-25', 2016, 'rating2', 278,
                'durationtype1', 'genre2', 'description6'
            ),
            (
                's7', 'type2', 'title7', 'director6', 'actor18, actor1, actor19, actor17', 'country3', '2008-08-19',
                2014, 'rating1', 11, 'durationtype2', 'genre3', 'description7'
            ),
            (
                's8', 'type2', 'title8', 'director5, director8', 'actor4, actor14, actor11, actor5, actor8, actor14',
                'country1', '2018-10-04', 2010, 'rating3', 'None', 'durationtype2', 'genre5', 'description8'
            ),
            (
                's9', 'type1', 'title9', 'director9', 'actor1, actor4, actor9, actor5, actor5', 'country5',
                '2000-04-25',
                2006, 'rating4', 263, 'durationtype1', 'genre2', 'description9'
            ),
            (
                's10', 'type2', 'title10', 'director2', 'actor2, actor14, actor15, actor19', 'country3', '2015-09-20',
                2001,
                'rating2', 5, 'durationtype2', 'genre4', 'description10'
            ),
            (
                's11', 'type1', 'title11', 'director3', 'actor10, actor18, actor5, actor10, actor16', 'country4',
                '2012-10-13', 2013, 'rating3', 319, 'durationtype1', 'genre5', 'description11'
            ),
            (
                's12', 'type1', 'title12', 'director9', 'actor9, actor13, actor3, actor12', 'country3', '2011-04-01',
                2019,
                'rating3', 458, 'None', 'genre2', 'description12'
            ),
            (
                's13', 'type1', 'None', 'director10', 'actor2, actor14, actor10', 'country3', '2002-07-23', 2003,
                'rating2',
                242, 'durationtype1', 'genre1', 'description13'
            ),
            (
                's14', 'type2', 'title14', 'director9', 'actor3, actor11, actor18, actor4', 'country1', '2010-09-28',
                2004,
                'rating3', 1, 'durationtype2', 'genre2', 'description14'
            ),
            (
                'None', 'type2', 'title15', 'director2', 'actor12, actor1, actor18, actor8, actor4', 'country3',
                '2013-03-13', 2000, 'rating3', 'None', 'durationtype2', 'genre4', 'description15'
            ),
            (
                's16', 'type1', 'title16', 'director8', 'actor5, actor12, actor17, actor4, actor7, actor11', 'country4',
                '2019-08-17', 2008, 'rating1', 483, 'durationtype1', 'genre3', 'description16'
            ),
            (
                's17', 'type2', 'title17', 'director4, director9, director10', 'actor10, actor16, actor10', 'country1',
                '2015-01-05', 2004, 'rating1', 11, 'durationtype2', 'genre3', 'description17'
            ),
            (
                's18', 'type2', 'title18', 'director10', 'actor4, actor16, actor16, actor11', 'country3', '2010-03-27',
                2002, 'rating2', 7, 'durationtype2', 'genre1', 'None'
            ),
            (
                's19', 'type1', 'title19', 'director3', 'actor14, actor13, actor17, actor12',
                'country4, country1, country4', '2018-09-07', 2016, 'rating4', 490, 'durationtype1', 'genre5',
                'description19'
            ),
            (
                's20', 'type1', 'title20', 'None', 'actor20, actor8, actor9, actor1', 'country3', '2007-09-22', 2003,
                'rating1', 346, 'durationtype1', 'genre5', 'description20'), (
                's21', 'type1', 'title21', 'director8, director3', 'actor15, actor8, actor17, actor18, actor8, actor1',
                'country5, country1, country5', '2012-09-11', 2001, 'rating1', 448, 'durationtype1', 'genre4',
                'description21'), (
                's22', 'type2', 'title22', 'director4', 'actor8, actor14, actor3, actor15, actor5', 'country2',
                '2011-08-27', 2019, 'rating3', 1, 'durationtype2', 'None', 'description22'), (
                's23', 'type2', 'title23', 'director10', 'actor16, actor20, actor1, actor5, actor5, actor3', 'country1',
                '2018-03-22', 2003, 'rating1', 6, 'durationtype2', 'genre3', 'description23'), (
                's24', 'type2', 'title24', 'director8', 'actor3, actor20, actor17, actor9, actor6, actor5', 'country1',
                '2019-09-08', 2008, 'rating1', 3, 'durationtype2', 'genre4', 'None'), (
                's25', 'type2', 'title25', 'director1', 'actor13, actor19, actor1', 'country3', '2007-11-28', 2014,
                'rating2', 12, 'durationtype2', 'genre1', 'description25'), (
                's26', 'type1', 'title26', 'director3', 'actor8, actor17, actor16', 'country3', '2014-01-15', 2012,
                'rating4', 261, 'durationtype1', 'genre5', 'description26'), (
                's27', 'type1', 'title27', 'director3', 'actor7, actor3, actor18, actor16, actor4', 'country4',
                '2001-04-14', 2013, 'rating3', 288, 'durationtype1', 'genre4', 'description27'), (
                's28', 'type1', 'title28', 'director10', 'actor19, actor8, actor10, actor8', 'country4', '2013-12-08',
                2014,
                'rating2', 481, 'durationtype1', 'genre1, genre3', 'description28'), (
                's29', 'type2', 'title29', 'director9', 'actor4, actor15, actor18, actor19, actor11', 'country4',
                '2016-06-15', 2014, 'rating3', 1, 'durationtype2', 'genre5', 'description29'), (
                's30', 'type2', 'title30', 'director2', 'actor7, actor14, actor13, actor1, actor8', 'country5',
                '2012-08-22', 2011, 'rating4', 8, 'durationtype2', 'genre2, genre3, genre1, genre4, genre4',
                'description30'), ('s31', 'type1', 'title31', 'director5, director1, director7, director5',
                                   'actor5, actor16, actor18, actor13, actor18', 'country1, country4, country4',
                                   '2001-06-03', 2005, 'rating2', 203, 'durationtype1', 'genre4', 'description31'), (
                's32', 'type2', 'title32', 'director6, director9, director8, director7', 'actor9, actor1, actor12',
                'country2', '2012-10-01', 2020, 'rating3', 5, 'durationtype2', 'genre1', 'description32'), (
                's33', 'type1', 'title33', 'director6', 'actor7, actor9, actor2', 'country4', '2014-01-23', 2016,
                'rating2',
                292, 'durationtype1', 'genre1, genre5', 'description33'), (
                's34', 'type1', 'title34', 'director6', 'actor14, actor12, actor19, actor9, actor19', 'country1',
                '2006-05-19', 2019, 'rating4', 338, 'durationtype1', 'genre4', 'description34'), (
                's35', 'type1', 'title35', 'director1', 'actor17, actor10, actor8', 'country3', '2020-12-23', 2016,
                'rating2', 225, 'durationtype1', 'genre3', 'description35'), (
                's36', 'type1', 'title36', 'director6', 'actor15, actor19, actor2, actor12, actor3', 'country4',
                '2018-10-13', 2017, 'rating3', 211, 'durationtype1', 'genre5', 'description36'), (
                's37', 'type2', 'title37', 'director1', 'actor18, actor12, actor15, actor7', 'country3', '2012-12-02',
                2017,
                'rating2', 11, 'durationtype2', 'genre4', 'description37'), (
                's38', 'None', 'title38', 'director6', 'actor10, actor5, actor19, actor18, actor9', 'country1',
                '2020-12-23', 2006, 'rating2', 5, 'durationtype2', 'genre2', 'None'), (
                's39', 'type1', 'title39', 'director7', 'actor13, actor5, actor13', 'country1', '2015-02-06', 2000,
                'rating2', 499, 'durationtype1', 'genre5', 'description39'), (
                's40', 'type2', 'title40', 'director5', 'actor14, actor7, actor13, actor11, actor1, actor20',
                'country5',
                '2011-08-06', 'None', 'rating3', 11, 'durationtype2', 'genre4', 'description40'), (
                's41', 'type2', 'title41', 'director4', 'None', 'country3', '2018-07-19', 2005, 'rating1', 2,
                'durationtype2', 'genre5, genre4, genre4, genre1, genre3', 'description41'), (
                's42', 'None', 'title42', 'director8', 'actor11, actor8, actor5, actor12, actor4, actor6', 'country5',
                '2014-05-05', 2000, 'rating4', 5, 'durationtype2', 'genre1', 'description42'), (
                's43', 'type1', 'title43', 'director9', 'actor18, actor5, actor8, actor19', 'country3, country3',
                '2016-06-12', 2014, 'rating1', 439, 'durationtype1', 'genre4', 'description43'), (
                's44', 'type1', 'title44', 'director7, director1', 'actor11, actor15, actor5, actor2', 'country2',
                '2013-06-15', 2004, 'rating2', 273, 'durationtype1', 'genre1', 'description44'), (
                's45', 'type2', 'title45', 'director8', 'actor3, actor12, actor5', 'country4', '2019-10-23', 2002,
                'rating2', 5, 'durationtype2', 'genre2', 'description45'), (
                's46', 'type2', 'title46', 'director1', 'actor13, actor9, actor5', 'country4', '2004-01-21', 2020,
                'rating3', 8, 'durationtype2', 'genre5', 'description46'), (
                's47', 'type1', 'title47', 'director3', 'actor12, actor15, actor17', 'country3', '2017-06-13', 2005,
                'rating2', 224, 'durationtype1', 'None', 'description47'), (
                's48', 'type2', 'title48', 'None', 'actor8, actor18, actor20, actor13', 'country1', '2016-11-01', 2005,
                'rating2', 1, 'durationtype2', 'genre4', 'description48'), (
                's49', 'type1', 'title49', 'director7', 'actor1, actor11, actor1, actor1', 'country2', '2004-11-21',
                2005,
                'rating2', 328, 'durationtype1', 'genre5', 'description49'), (
                's50', 'type1', 'title50', 'director5', 'actor8, actor11, actor3, actor2, actor4, actor10', 'country5',
                '2004-11-23', 2007, 'rating1', 313, 'durationtype1', 'genre3', 'description50'), (
                's51', 'type1', 'title51', 'director10', 'actor19, actor6, actor5', 'country3', '2007-04-23', 2016,
                'rating4', 393, 'durationtype1', 'genre2', 'description51'), (
                's52', 'type2', 'title52', 'director6', 'actor9, actor3, actor3, actor17', 'country2', '2005-05-21',
                2018,
                'rating4', 8, 'durationtype2', 'genre2', 'description52'), (
                's53', 'type1', 'title53', 'director9', 'actor8, actor5, actor10, actor17, actor15', 'country1',
                '2008-11-22', 2008, 'rating3', 270, 'durationtype1', 'genre5', 'description53'), (
                's54', 'type2', 'title54', 'director5', 'actor9, actor1, actor4, actor15', 'country1', '2014-11-18',
                2011,
                'rating2', 11, 'durationtype2', 'genre4', 'description54'), (
                's55', 'type1', 'title55', 'director7', 'actor6, actor14, actor9, actor19',
                'country2, country4, country5',
                '2018-09-27', 2013, 'rating4', 254, 'durationtype1', 'genre2', 'description55'), (
                's56', 'type2', 'title56', 'director4, director9, director7',
                'actor3, actor15, actor9, actor18, actor16',
                'country2', '2020-05-20', 2003, 'rating4', 8, 'durationtype2', 'genre2', 'description56'), (
                's57', 'type2', 'title57', 'director5', 'actor3, actor1, actor17', 'country5', '2013-09-26', 2018,
                'rating2', 6, 'durationtype2', 'genre4', 'description57'), (
                's58', 'type1', 'title58', 'director8', 'actor16, actor17, actor5, actor2, actor12', 'country5',
                '2003-12-18', 2009, 'rating2', 346, 'durationtype1', 'genre3', 'description58'), (
                's59', 'type2', 'title59', 'director6', 'actor14, actor15, actor1, actor11', 'country1, country2',
                '2003-03-10', 2007, 'rating1', 'None', 'durationtype2', 'genre3', 'description59'), (
                's60', 'type1', 'title60', 'director9, director4, director7', 'actor15, actor16, actor15', 'country5',
                '2015-05-08', 2014, 'rating1', 486, 'durationtype1', 'genre4', 'description60'), (
                's61', 'type2', 'title61', 'director6', 'actor2, actor17, actor6, actor10', 'country3', '2013-08-12',
                2020,
                'rating2', 5, 'durationtype2', 'genre4, genre3, genre2', 'description61'), (
                's62', 'type2', 'title62', 'director5', 'actor1, actor6, actor16, actor19', 'country2', '2015-06-27',
                2009,
                'rating1', 3, 'durationtype2', 'genre5', 'description62'), (
                's63', 'type2', 'title63', 'director5', 'actor18, actor19, actor19', 'country3', '2018-08-08', 2000,
                'rating4', 2, 'durationtype2', 'genre4, genre5, genre3', 'description63'), (
                's64', 'type2', 'title64', 'director7', 'actor2, actor9, actor7, actor10, actor18, actor5', 'country2',
                '2009-08-10', 2012, 'rating3', 8, 'durationtype2', 'genre4', 'description64'), (
                'None', 'type2', 'title65', 'director3', 'actor11, actor1, actor14, actor1, actor1, actor5', 'country4',
                '2000-08-19', 2009, 'rating4', 9, 'durationtype2', 'genre2, genre1, genre1', 'description65'), (
                's66', 'type2', 'title66', 'director7', 'actor18, actor5, actor1, actor14', 'country5', '2016-10-06',
                2005,
                'rating1', 7, 'durationtype2', 'genre4', 'description66'), (
                's67', 'None', 'title67', 'director10', 'actor9, actor8, actor10, actor1',
                'country1, country4, country3',
                '2016-11-07', 2001, 'rating3', 217, 'durationtype1', 'genre4', 'description67'), (
                's68', 'type2', 'None', 'director3', 'actor15, actor20, actor7, actor2, actor11, actor10', 'country5',
                '2011-01-04', 2001, 'rating4', 11, 'durationtype2', 'genre4', 'description68'), (
                's69', 'type2', 'title69', 'director2', 'actor2, actor3, actor11, actor9, actor5', 'country4',
                '2010-10-23',
                2012, 'rating4', 9, 'durationtype2', 'genre3', 'description69'), (
                's70', 'type1', 'title70', 'director4', 'None', 'country3', '2000-05-27', 2013, 'rating2', 'None',
                'durationtype1', 'genre4, genre5, genre5', 'description70'), (
                's71', 'type1', 'title71', 'director9', 'None', 'country5', '2000-10-03', 2000, 'rating1', 401,
                'durationtype1', 'genre4', 'description71'), (
                's72', 'type2', 'title72', 'director1', 'actor6, actor16, actor19', 'country1', '2015-05-17', 2008,
                'None',
                7, 'durationtype2', 'genre1', 'description72'), (
                's73', 'type1', 'title73', 'director9', 'actor11, actor17, actor12', 'country4, country3', '2003-05-20',
                2015, 'None', 334, 'durationtype1', 'genre2', 'description73'), (
                's74', 'type2', 'title74', 'director7', 'actor5, actor9, actor11, actor9', 'country1', '2016-11-16',
                2003,
                'rating4', 5, 'durationtype2', 'genre2', 'description74'), (
                's75', 'type1', 'title75', 'director1, director3', 'None', 'country3', '2005-12-22', 2000, 'rating3',
                440,
                'durationtype1', 'genre3, genre2, genre4', 'description75'), (
                's76', 'type2', 'title76', 'director9', 'actor15, actor9, actor8, actor7, actor11, actor20', 'country3',
                '2014-12-07', 2013, 'rating4', 12, 'durationtype2', 'genre4', 'description76'), (
                's77', 'type2', 'title77', 'director10', 'actor5, actor3, actor12, actor14, actor20', 'country4',
                '2008-10-02', 2013, 'rating1', 11, 'durationtype2', 'genre5', 'description77'), (
                's78', 'type2', 'title78', 'director2', 'actor12, actor6, actor10, actor20, actor11, actor6',
                'country2',
                '2001-04-17', 2013, 'rating2', 1, 'durationtype2', 'genre3', 'description78'), (
                's79', 'type1', 'title79', 'director2, director9, director5',
                'actor20, actor9, actor17, actor1, actor5, actor10', 'country4, country2', '2012-02-20', 2010,
                'rating2',
                426, 'durationtype1', 'genre5', 'description79'), (
                's80', 'type1', 'title80', 'director10, director2, director2',
                'actor9, actor10, actor13, actor4, actor18, actor15', 'country1', '2006-06-18', 2010, 'rating3', 425,
                'durationtype1', 'genre4', 'description80'), (
                's81', 'type2', 'title81', 'director9', 'actor18, actor12, actor11, actor9', 'country1', 'None', 2001,
                'rating1', 12, 'durationtype2', 'genre4', 'description81'), (
                's82', 'type2', 'title82', 'director2', 'actor8, actor10, actor15', 'country5', '2016-06-27', 2010,
                'rating1', 10, 'durationtype2', 'genre5', 'description82'), (
                's83', 'type2', 'title83', 'director6, director1, director9', 'actor13, actor4, actor20',
                'country5, country4, country1', '2018-04-08', 2008, 'rating4', 2, 'durationtype2', 'genre3',
                'description83'), (
                's84', 'type1', 'title84', 'director5', 'actor19, actor3, actor14, actor4, actor12, actor13',
                'country1',
                '2019-07-02', 2012, 'rating3', 301, 'None', 'genre3', 'description84'), (
                's85', 'type2', 'title85', 'director7', 'actor20, actor5, actor20', 'country2, country4, country4',
                '2003-08-01', 2015, 'rating1', 7, 'durationtype2', 'genre5', 'description85'), (
                's86', 'type1', 'title86', 'director8', 'actor3, actor5, actor13, actor15, actor20, actor11', 'None',
                '2017-02-03', 2015, 'rating1', 246, 'durationtype1', 'genre3, genre5, genre1, genre4', 'description86'),
            (
                's87', 'type1', 'title87', 'director7, director10', 'actor15, actor13, actor15', 'country1',
                '2006-04-07',
                2010, 'rating2', 450, 'durationtype1', 'genre4', 'description87'), (
                's88', 'type2', 'title88', 'director7', 'actor15, actor1, actor7, actor12', 'country3', '2006-08-27',
                2007,
                'rating3', 1, 'None', 'genre4, genre4, genre5, genre2, genre5', 'description88'), (
                's89', 'type2', 'title89', 'director6', 'actor19, actor2, actor8, actor19', 'country2', '2019-09-25',
                2009,
                'rating2', 12, 'durationtype2', 'genre1', 'description89'), (
                's90', 'type2', 'title90', 'director10', 'actor16, actor17, actor5', 'country5', '2008-11-19', 2003,
                'rating4', 3, 'durationtype2', 'genre5', 'description90'), (
                's91', 'type2', 'title91', 'director8, director1, director8',
                'actor13, actor20, actor6, actor20, actor10',
                'country2', '2020-11-23', 2000, 'rating1', 2, 'durationtype2', 'genre5', 'description91'), (
                's92', 'type1', 'title92', 'director4', 'actor5, actor13, actor13, actor10, actor9, actor4', 'country4',
                '2009-12-18', 2009, 'rating4', 321, 'durationtype1', 'genre3', 'None'), (
                's93', 'type2', 'title93', 'director3, director10, director1, director3',
                'actor16, actor18, actor3, actor19, actor19', 'country2', '2004-11-20', 2000, 'rating1', 4,
                'durationtype2',
                'genre1', 'description93'), (
                's94', 'type1', 'title94', 'director7', 'actor5, actor11, actor3, actor19, actor15', 'country2',
                '2017-08-11', 2007, 'rating2', 484, 'durationtype1', 'genre1', 'description94'), (
                's95', 'type1', 'title95', 'director3', 'actor9, actor9, actor5, actor5, actor13, actor9', 'country5',
                '2014-03-07', 2000, 'rating3', 222, 'durationtype1', 'genre2', 'description95'), (
                's96', 'type2', 'title96', 'director4', 'actor2, actor17, actor15, actor17, actor11, actor20',
                'country3',
                '2001-07-24', 2004, 'rating2', 7, 'durationtype2', 'genre1', 'None'), (
                's97', 'type2', 'title97', 'director4', 'actor3, actor7, actor9, actor15',
                'country2, country5, country3',
                '2013-06-15', 2013, 'rating2', 4, 'durationtype2', 'genre4', 'description97'), (
                's98', 'type2', 'title98', 'director1', 'actor18, actor14, actor2, actor17', 'country2', '2009-04-11',
                2006,
                'rating1', 9, 'durationtype2', 'genre2, genre1, genre4', 'description98'), (
                's99', 'type1', 'title99', 'director1', 'actor20, actor17, actor14', 'country2', '2003-12-10', 2010,
                'rating1', 387, 'durationtype1', 'genre4', 'description99')]

        yield conn.cursor()

Technical interview
===================

General considerations:
 - the code should be written for Python 3 interpreter
 - the JSON files are described in the next section
 - each answer should be written in its own folder (e.g. "./part_1/" for the first question)
 - at the end, zip the parent folder (.tar.xz, .tar.gz or .zip) and send it through Skype or by e-mail
 - about the Odoo add-on (question 4):
   + it won't be installed nor executed
   + source code should target Odoo version 11 or 12


Data set
========

This folder contains geographical and demographic data for countries and regions around the world.
These data come from two different sources from the United Nations.

The country/area identifier is the M49 code. It is a 3-digits code used by the United Nations Statistics Division (UNSD) to identify each country and area uniquely.

First 3 files come from the same data source, UNSD. They are consistent with each other.
Fourth file "data_stats.json" comes from the UNdata and is not exhaustive. Some areas don't have all statistics available.


File "data_areas.json" is a list of tuples:
 - 0: Area M49 code
 - 1: Parent area M49 code
 - 2: Area name


File "data_countries.json" is a list of tuples:
 - 0: Country M49 code
 - 1: Area M49 code
 - 2: Country ISO code (ISO 3166 - three-letter code)
 - 3: Country name


File "data_unsd.json" is a list of dictionaries
 - m49: Country M49 code
 - dc: Developing Country (as opposed to Developed Country)
 - ldc: Least Developed Country
 - lldc: Land Locked Developing Country
 - sids: Small Island Developing State


File "data_stats.json" is a list of dictionaries.
All keys are optional except "m49" and "name":
 - m49: Country or Area M49 code
 - name: Country or Area name
 - pop: Population estimates (millions)
 - pop_male: Population estimates for male (millions)
 - pop_female: Population estimates for female (millions)
 - pop_14: Population aged 0 to 14 years old (percentage)
 - pop_60: Population aged 60+ years old (percentage)
 - area: Surface area (thousand km2)



Question 1.
-----------
(Python only)

Write a program to load the data from "data_areas.json" and "data_countries.json".
This program should ask for a country name or ISO code (3 letters) or UN M49 code (3 digits) and print the breadcrumbs of this country or area.

Sample output:

Country? switzerland
 World < Europe < Western Europe < Switzerland
Country? GRL
 World < Americas < Northern America < Greenland


Question 2.
-----------
(Python only)

From the same data set, create a program to compute the number of countries for each area and print the results.
It should be printed in a hierarchical view, with indentation for each sub-region.
Only 3 levels should be printed (e.g. World < Africa < Northern Africa).


Question 3.
-----------
(Python only)

Load all 4 data files, including "data_stats.json" and "data_unsd.json".
Create a program which ask for a country name or code and return some information for this country or area.

Sample output:

Country? GRL
 Name: Greenland
 Continent: Americas
 M49 code: 304
 ISO code: GRL
 Population: 60'000
 Area: 2'166'000 km2
 Categories:
  - Developed Country


Question 4.
-----------
(Odoo 11/12 add-on)

Design and build an Odoo add-on to store and manage the geographical data in Odoo model(s).
This add-on should demonstrate some capabilities and features of the Odoo framework.

For example it could implement different field types, search methods, etc...

Other possible features, not exhaustive:
 - add an extended name with the country and its hierarchy (region, continent, ...)
 - compute the rank of the country compared to other countries of the same continent, by surface area.
 - compute a 'color' field depending on the size of the population (10'000 / 100'000 / 1 M / 10 M / 100 M)
 - helpers to extract interesting figures like population density or ratio men/women.





Data sources
============
http://data.un.org/
https://unstats.un.org/unsd/methodology/m49/

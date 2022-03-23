#=================================================================================================
#Project Name    : 仮設BIM効率化システム
#File Name       : 01BIM[Ver表記]仮設BIM効率化システム.dyn
#Encoding        : 該当なし
#Creation Date   : 2019.12.5～2020.08.04以降随時
# 
#Copyright c 2019.12.5 HIROYA MIZUMOTO and MANAMI MIWA and CHINATSU IZUMI rights reserved.
#
#This source code or any portion thereof must not be reproduced or used in any manner whatsoever.
#
#Each job is as follows.
#Total designed and writen by HIROYA MIZUMOTO. 
#Type:iQ scarfold system writen and implemented by CHINATSU IZUMI.
#Inch type scarfold system writen and implemented by MANAMI MIWA.
#These Revit family for temporary scarfold designed by HIROYA MIZUMOTO and MEGUMI TAKASHIMA and MANAMI MIWA and CHINATSU IZUMI.
#And a system provided separately, which counts scaffolding materials designed and writen by MEGUMI TAKASHIMA and MANAMI MIWA,advised the design by HIROYA MIZUMOTO.
#
#■If there is a discrepancy between the content shown in English below and the above Japanese text regarding this software, 
#  the interpretation in the Japanese text shall take precedence.
#
#■ Copyright / Terms of Use / Disclaimer, etc.
#・ Intellectual property rights such as copyrights related to this software belong to the author, S.M.I.Lab (s.m.i.lab.engineers@gmail.com https://github.com/S-M-I-Laboratory).
#・ The user acquires a non-exclusive right to use this software.
#・ The user can copy, modify, and use part or all of this software within the scope of personal use.
#・ Users are not allowed to create exclusive rights based on the knowledge gained by modifying, reverse engineering, or decompiling this software.
#・ This software can be used permanently free of charge as a shared property, and it is intended that it will be continuously modified and developed by volunteers.
#Unless otherwise stated, the terms of this license shall be duplicated. That is, if all or part of this software has been modified, or if any of the technologies 
#provided by this software are used, you may create paid software or change to another license agreement without permission Is not allowed.
#・ This software is provided as it is free of charge and no compensation, and the author does not guarantee normal operation.
#・ Any problems that occur with this software shall be resolved at the user's responsibility.
#・ The author shall not be liable for any damages caused by this software.
#
#Please use this software only if you agree with the above.
#
#■ About the concept of copyright for this system
#As a mechanism for sharing usage rights, instead of waiving copyright, in the form of a license (protected licence for free and no compensation)
#Take measures to protect sharing and collaborative creative activities. That is, "I have right of own the copyright and copy, modify, distribute (sell)"
#All thing is Has need my permission, but to anyone at any time, as long as it does not violate the intention of sharing and developing the software the purpose is to allow the use
#
#As a way to create such a mechanism
#
#"Transitioning a copied / modified shared property from a shared state to an exclusive state" is prohibited without the special permission of the author.
#
#It is based on a methodology, also known as copyleft (for copyright), with a strong willingness to share "does not allow the transition to a monopoly state".
#==================================================================================================

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit
from Revit.Elements import *
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
import System
import math

xplin = []
yplin = []
xendin = []
yendin = []
zzzzzin = []
dataEnteringNode = IN
xplin = IN[0]
yplin = IN[1]
vvvvvin = IN[2]
zpl = IN[6]
zsta = IN[7]
zstp = IN[8]
countz = IN[10]
waku1800 = IN[11]
waku1500 = IN[12]
waku1200 = IN[13]
waku900 = IN[14]
waku600 = IN[15]
waku001 = IN[16]
waku000 = IN[17]
bwaku = IN[18]
ssbk = IN[19]
swaku = IN[20]
esbk = IN[21]
ewaku = IN[22]
zenchouin = IN[23]
xendin = IN[24]
yendin = IN[25]
zzzzzin = IN[26]
tanbu1 = IN[27]
tanbu2 = IN[28]
sheetflg = IN[29]
sheetflg2 = IN[30]
tunagih = IN[31]
tunagil = IN[32]
rakkabou = IN[33]
habaki = IN[34]
tesuri = IN[35]
zsaijoudan = IN[36]
zsaikadan = IN[37]
ichiretu = IN[38]
irekae = IN[39]
ir18 = IN[40]
ir15 = IN[41]
ir12 = IN[42]
ir09 = IN[43]
ir06 = IN[44]
ir01 = IN[45]
ir00 = IN[46]
chouseinashi = IN[47]
jidou = IN[48]
jdesumi = IN[49]
jshiten = IN[50] 
jedesumi = IN[51]
jsyuuten = IN[52]
wakuhaba = IN[53]
j65 = IN[54]
setuzoku1 = IN[55]
setuzoku2 = IN[56]
kyouseitakasa = IN[57]
sheetselect = IN[58]
sheetselect2 = IN[59]
tankanb = IN[60]
asagao = IN[61]
asagaotan = IN[62]
kyouseishitaba = IN[63]
inchiashiba = IN[64]
iqashiba = IN[65]
uchinegaramisoto = IN[66]
sotoatamatsunagisoto = IN[67]
blaketnagasa = IN[68]
kabetunaginagasa = IN[69]
arubatorosu = IN[70]

i = 0
xsta = 0
xstp = 0
ysta = 0
ystp = 0

list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = [] 
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []
list19 = []
list20 = []
list21 = []
list22 = []
list23 = []
list24 = []
list25 = []
list26 = []
list27 = []
list28 = []
list29 = []
list30 = []
list31 = []
list32 = []
list33 = []
list34 = []
list35 = []
list36 = [] 
list37 = [] 
list38 = []
list39 = []
list40 = []

ffl1 = 0 
ffl2 = 0 
ffl3 = 1 
ffl4 = 0 
ffl5 = 1 
ffl6 = 0 
ffl7 = 0 
ffl8 = 0 
ffl9 = 0 
ffl10 = 0 
ffl11 = 0 
ffl12 = 0 
ffl13 = 0 
ffl14 = 0 
ffl15 = 0 
ffl16 = 'L'
ffl17 = 0
ffl18 = 'セットバック'
ffl19 = 0
ffl20 = 0
ffl21 = 0
ffl22 = 0
ffl23 = 1
ffl24 = 1
ffl25 = 1
ffl26 = 1
ffl27 = 1
ffl28 = 0
ffl29 = 0
ffl34 = 0
ffl35 = 0
ffl36 = 0
ffl37 = 0
ffl38 = blaketnagasa
ffl39 = kabetunaginagasa
ffl40 = 0
l18 = 1800
l15 = 1500
l12 = 1200
l09 = 900
l06 = 600
lc06 = 600
lc03 = 300
lcl = 300
lcc = 65
ltakasa = 1700
sheetname = 0

if inchiashiba == 1:
     l18 = 1829
     l15 = 1524
     l12 = 1219
     l09 = 914
     l06 = 610
     lc06 = 610
     lc03 = 304
     lcl = 305
     lcc = 65
     ltakasa = 1725
iqst = 0
if iqashiba == 1:
     l18 = 1829
     l15 = 1524
     l12 = 1219
     l09 = 914
     l06 = 610
     lc06 = 610
     lc03 = 304
     lcl = 305
     lcc = 0
     ltakasa = 1900 
     iqst = 106
if arubatorosu == 1:
     l18 = 1829
     l15 = 1524
     l12 = 1219
     l09 = 914
     l06 = 610
     lc06 = 610
     lc03 = 304
     lcl = 305
     lcc = 0
     ltakasa = 1800
     iqashiba = 1 
     iqst = 106
     sheetname = 1

familyName = "アルインコ_単管ブラケット足場"
typeName = "1829_H1725"
if tankanb == 1:
     irekae = 1
     familyName = "アルインコ_単管ブラケット足場"
     typeName = "1829_H1725"
     ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "1524_H1725"
     ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "1219_H1725"
     ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "914_H1725"
     ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "610_H1725"
     ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     familyName = "アルインコ_単管ブラケット足場 調整スパン"
     typeName = "600_H1725"
     ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "300_H1725"
     ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)

     if zstp == 1725:                                                         
          familyName = "アルインコ_単管ブラケット足場"
          typeName = "1829_H1725"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1524_H1725"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1219_H1725"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "914_H1725"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "610_H1725"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルインコ_単管ブラケット足場 調整スパン"
          typeName = "600_H1725"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1725"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 1244:
          familyName = "アルインコ_単管ブラケット足場"
          typeName = "1829_H1244"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1524_H1244"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1219_H1244"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "914_H1244"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "610_H1244"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルインコ_単管ブラケット足場 調整スパン"
          typeName = "600_H1244"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1244"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 939:
          familyName = "アルインコ_単管ブラケット足場"
          typeName = "1829_H939"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1524_H939"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1219_H939"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "914_H939"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "610_H939"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルインコ_単管ブラケット足場 調整スパン"
          typeName = "600_H939"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H939"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 515:
          familyName = "アルインコ_単管ブラケット足場"
          typeName = "1829_H515"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1524_H515"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "1219_H515"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "914_H515"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "610_H515"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルインコ_単管ブラケット足場 調整スパン"
          typeName = "600_H515"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H515"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 1900:
          familyName = "IQ単管ブラケット足場"
          typeName = "IQ18_H1900"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ15_H1900"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ12_H1900"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ09_H1900"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ06_H1900"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "IQ単管ブラケット足場 調整スパン"
          typeName = "600_H1900"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1900"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 1425:
          familyName = "IQ単管ブラケット足場"
          typeName = "IQ18_H1425"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ15_H1425"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ12_H1425"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ09_H1425"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "IQ06_H1425"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "IQ単管ブラケット足場 調整スパン"
          typeName = "600_H1425"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1425"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName) 
     if zstp == 2025:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H2025"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H2025"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H2025"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H2025"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H2025"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H2025"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H2025"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 1800:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H1800"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H1800"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H1800"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H1800"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H1800"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H1800"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1800"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 1575:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H1575"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H1575"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H1575"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H1575"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H1575"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H1575"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1575"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 1350:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H1350"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H1350"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H1350"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H1350"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H1350"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H1350"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1350"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 1125:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H1125"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H1125"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H1125"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H1125"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H1125"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H1125"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H1125"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 900:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H900"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H900"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H900"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H900"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H900"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H900"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H900"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 675:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H675"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H675"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H675"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H675"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H675"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H675"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H675"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     if zstp == 450:                                                      
          familyName = "アルバトロス単管ブラケット足場"
          typeName = "アルバトロス18_H450"
          ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス15_H450"
          ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス12_H450"
          ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス09_H450"
          ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "アルバトロス06_H450"
          ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          familyName = "アルバトロス単管ブラケット足場 調整スパン"
          typeName = "600_H450"
          ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
          typeName = "300_H450"
          ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)  

if asagao == 1:
     irekae = 1
     ichiretu = 1
     familyName = "アサガオ(アルインコ)"
     typeName = "朝顔18"
     ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔15"
     ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔12"
     ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔09"
     ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔06"
     ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     familyName = "アサガオ調整スパン(アルインコ)"
     typeName = "朝顔06"
     ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔06"
     ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)

if asagao == 1 and inchiashiba == 1:                                   
     irekae = 1
     ichiretu = 1
     familyName = "アサガオ(アルインコ)"
     typeName = "朝顔1829"
     ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔1524"
     ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔1219"
     ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔914"
     ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔610"
     ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     familyName = "アサガオ調整スパン(アルインコ)"
     typeName = "朝顔610"
     ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔610"
     ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)     
     
if asagao == 1 and iqashiba == 1:                                                           
     irekae = 1
     ichiretu = 1
     familyName = "アサガオ(IQ)"
     typeName = "朝顔1829"
     ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔1524"
     ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔1219"
     ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔914"
     ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔610"
     ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     familyName = "アサガオ調整スパン(IQ)"
     typeName = "朝顔610"
     ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔610"
     ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)     
     
if asagaotan == 1:
     irekae = 1
     ichiretu = 1
     familyName = "アサガオ(単管)"
     typeName = "朝顔18"
     ir18 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔15"
     ir15 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔12"
     ir12 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔09"
     ir09 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔06"
     ir06 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     familyName = "アサガオ調整スパン(単管)"
     typeName = "朝顔06"
     ir01 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)
     typeName = "朝顔06"
     ir00 = FamilyType.ByFamilyNameAndTypeName(familyName, typeName)

if zsaikadan == 0:
     sheetflg2 = 1

if irekae == 1:
     waku1800 = ir18
     waku1500 = ir15
     waku1200 = ir12
     waku900 = ir09
     waku600 = ir06
     waku001 = ir01
     waku000 = ir00

zsta = zsta + tesuri - zpl + 0.0
countz = math.ceil( zsta / zstp )
ztchousei = 0
if kyouseitakasa <> 0:
     countz = math.floor(kyouseitakasa)
if kyouseishitaba <> 0:
     countz = countz - math.floor(kyouseishitaba)
     ztchousei = math.floor(kyouseishitaba)
     zpl = zpl + zstp * ztchousei
          
if ichiretu ==1:
     zsta = zstp + zpl
     countz = 1
     tesuri = 0

if bwaku == 0:
     bwaku = l18
if swaku <= 0:
     swaku = bwaku

i = 0
ii = 1

xplai = []
yplai = []
zenchouai = []
xendai = []
yendai = []
zzzzzai = []
vvvvvai = []
ai = []

xpl = xplin
ypl = yplin
zenchou = zenchouin
xend = xendin
yend = yendin
zzzzz = zzzzzin
vvvvv = vvvvvin

xpl = float( xpl )
ypl = float( ypl )
zenchou = float( zenchou )
xend = float( xend )
yend = float( yend )
zzzzz = float( zzzzz )

xsta = xend - xpl
xstp = xsta / ( zenchou / bwaku )
ysta = yend - ypl
ystp = ysta / ( zenchou / bwaku )
countxy = ( zenchou / bwaku )

rx = 0
ry = 0
rp = 0
if xsta >= 0:
     rx = 1
else:
     rx = -1
if ysta >= 0:
     ry = 1
else:
     ry = -1
rp = -1 * rx * ry + ( 2 * ( ( rx + ry ) == -2 ) ) + ( -2 * (rx == -1) * (ry == 1) )
vvvvv = vvvvv * rp

xplai.append(xpl)
yplai.append(ypl)
zenchouai.append(zenchou)
xendai.append(xend)
yendai.append(yend)
zzzzzai.append(zzzzz)
vvvvvai.append(vvvvv)
if vvvvvai[i] < 45 and vvvvvai[i] >= -45:
     ai.append(6)
elif vvvvvai[i] < -45 and vvvvvai[i] >= -135:
     ai.append(8)
elif vvvvvai[i] < -135 and vvvvvai[i] >= -225:
     ai.append(4)
elif vvvvvai[i] < 135 and vvvvvai[i] >= 45:
     ai.append(2)
else:
     ai.append(2)

aista = []
aiend = []
aijdesumi = []
aijshiten = [] 
aijedesumi = []
aijsyuuten = []
aisetuzoku1 = []
aisetuzoku2 = []
mae = 0
koko = 0
ato = 0
tojiteiruka = 0
tojiteiruka1 = 0
tojiteiruka2 = 0

defsetuzoku1 = setuzoku1
defsetuzoku2 = setuzoku2
setuzoku1 = defsetuzoku1
setuzoku2 = defsetuzoku2
xpl = xplai[i]
ypl = yplai[i]
zenchou = zenchouai[i]
xend = xendai[i]
yend = yendai[i]
zzzzz = zzzzzai[i]
vvvvv = vvvvvai[i]

xsta = xend - xpl
xstp = xsta / ( zenchou / bwaku )
ysta = yend - ypl
ystp = ysta / ( zenchou / bwaku )
countxy = ( zenchou / bwaku )

zenchou = round(zenchou,1)

countxy = math.floor(countxy)

lchousei = 0
warikiri = 0
j65d = 0
j65ds = 0
tokuteijyouken2 = 0
if jidou == 1:
     if jdesumi == 1:
          if jshiten == 1:
               tanbu1 = 1
               ssbk = - wakuhaba
               swaku = wakuhaba
          if jshiten == 0:
               tanbu1 = 0
               ssbk = lcc
               swaku = bwaku
               lchousei = 1
               j65d = j65d + 1
     if jdesumi == 0:
          if jshiten == 1:
               tanbu1 = 3
               ssbk = 0
               swaku = wakuhaba
          if jshiten == 0:
               tanbu1 = 0
               ssbk = wakuhaba + lcc
               swaku = bwaku
               lchousei = 1
               j65d = j65d + 1
     if jedesumi == 1:
          if jsyuuten == 1:
               tanbu2 = 1
               esbk = - wakuhaba
               ewaku = wakuhaba
          if jsyuuten == 0:
               tanbu2 = 0
               esbk = 0 + (j65 == 1) * lcc
               ewaku = 0 + (j65 == 1) * bwaku
               j65d = j65d + 1
     if jedesumi == 0:
          if jsyuuten == 1:
               tanbu2 = 3
               esbk = 0
               ewaku = wakuhaba
          if jsyuuten == 0:
               tanbu2 = 0
               esbk = wakuhaba + (j65 == 1) * lcc
               ewaku = 0 + (j65 == 1) * bwaku
               j65d = j65d + 1
     if setuzoku1 == 1:
          tanbu1 = 0
          if jshiten == 1:
               ssbk = 0
               swaku = bwaku
          if jshiten == 0:
               ssbk = wakuhaba
               swaku = bwaku
     if setuzoku2 == 1:
          tanbu2 = 0


kyouseisc = 0
kyouseiec = 0
kyouseisn = 0
kyouseien = 0
if tanbu1 == 4 and lcc > 0:
     jidou = 0
     tanbu1 = 0
     kyouseisc = 1
if tanbu1 == 5:
     jidou = 0
     tanbu1 = 0
     kyouseisn = 1
if tanbu2 == 4 and lcc > 0:
     jidou = 0
     tanbu2 = 0
     kyouseiec = 1
if tanbu2 == 5:
     jidou = 0
     tanbu2 = 0
     kyouseien = 1
if ewaku > 0:
     ewakufl = 0
elif ewaku == 0:
     ewakufl = 1
else:
     ewaku = 0
     ewakufl = 2

strc = 0
strcxy = 0
strcz = 0
each = strc
peach = strcz
b1waku = waku1800
waku = b1waku
if bwaku <= 0:
     b1waku = waku000
     waku = b1waku
elif bwaku < lc03:
     b1waku = waku000
     waku = b1waku
elif bwaku < l06:
     b1waku = waku001
     waku = b1waku
elif bwaku < l09:
     b1waku = waku600
     waku = b1waku
elif bwaku < l12:
     b1waku = waku900
     waku = b1waku
elif bwaku < l15:
     b1waku = waku1200
     waku = b1waku
elif bwaku < l18:
     b1waku = waku1500
     waku = b1waku
else:
     pass
supan = zenchou - ssbk - swaku - esbk - ewaku

tokuteij3 = 0

if supan < lcc or swaku <l06:
     if jidou == 1:

          if jshiten == 1 and jsyuuten == 0:
               
               ssbk = -wakuhaba * (jdesumi == 1) + lcc * (jdesumi == 0)
               swaku = wakuhaba
               
               ewaku = 0
               esbk = (wakuhaba) * (jedesumi == 0) + lcc * (jedesumi == 1)
               supan = zenchou - ssbk - swaku - esbk - ewaku
               tokuteijyouken2 = 0


          if jshiten == 0 and jsyuuten == 0:
               ssbk = (wakuhaba + lcc) * (jdesumi == 0) + lcc * (jdesumi == 1)
               swaku = 0
               esbk = (wakuhaba) * (jedesumi == 0) + 0 * (jedesumi == 1)
               ewaku = 0
               supan = zenchou - ssbk - swaku - esbk - ewaku
               tokuteijyouken2 = 0
               if supan >= l06 + lcc:
                    if l18 <= bwaku and l18 <= supan:
                         swaku = l18
                    elif l15 <= bwaku and l15 <= supan:
                         swaku = l15                         
                    elif l12 <= bwaku and l12 <= supan:
                         swaku = l12
                    elif l09 <= bwaku and l09 <= supan:
                         swaku = l09
                    elif l06 <= bwaku and l06 <= supan:
                         swaku = l06
                    else:
                         swaku = supan
                    supan = zenchou - ssbk - swaku - esbk - ewaku
                    if supan + esbk < l06 + lcc:
                         esbk = (wakuhaba) * (jedesumi == 0) + 0 * (jedesumi == 1)
                         swaku = 0
                         supan = zenchou - ssbk - swaku - esbk - ewaku
                         if l18 <= bwaku and l18 <= supan:
                              swaku = l18
                         elif l15 <= bwaku and l15 <= supan:
                              swaku = l15                         
                         elif l12 <= bwaku and l12 <= supan:
                              swaku = l12
                         elif l09 <= bwaku and l09 <= supan:
                              swaku = l09
                         elif l06 <= bwaku and l06 <= supan:
                              swaku = l06
                         else:
                              swaku = supan
                         supan = zenchou - ssbk - swaku - esbk - ewaku
               else:
                    ssbk = (wakuhaba) * (jdesumi == 0) + 0 * (jdesumi == 1)
                    
                    esbk = wakuhaba * (jedesumi == 0)  + 0 * (jedesumi == 1)
                    ewaku = 0
                    swaku = zenchou - ssbk - esbk - ewaku
                    tokuteij3 = swaku
                    supan = zenchou - ssbk - swaku - esbk - ewaku
               if supan < lcc and swaku >= l06:
                    ssbk = (wakuhaba + lcc) * (jdesumi == 0) + lcc * (jdesumi == 1)
                    esbk = wakuhaba * (jedesumi == 0) + 0 * (jedesumi == 1)
                    if l18 <= swaku:
                         swaku = l15
                    elif l15 <= swaku:
                         swaku = l12                         
                    elif l12 <= swaku:
                         swaku = l09
                    elif l09 <= swaku:
                         swaku = l06
                    elif l06 <= swaku:
                         swaku = l06
                    else:
                         swaku = l06
                    ewaku = 0
                    supan = zenchou - ssbk - swaku - esbk - ewaku
                    tokuteij3 = 0
               if swaku < l06 or supan < 0:
                    ssbk = (wakuhaba) * (jdesumi == 0) + 0 * (jdesumi == 1)
                    esbk = wakuhaba * (jedesumi == 0) + 0 * (jedesumi == 1)
                    ewaku = 0
                    swaku = zenchou - ssbk - esbk - ewaku
                    tokuteij3 = swaku
                    supan = zenchou - ssbk - swaku - esbk - ewaku

          supan = zenchou - ssbk - swaku - esbk - ewaku
         
rzenchou = zenchou - ssbk - esbk
szenchou = zenchou - ssbk - swaku
ezenchou = zenchou - ssbk - swaku - esbk

zzzzzf = 0 
bwakus = 0
shoutotu = 0
loopfx = 0
if supan >= 0:
     chousei = supan / bwaku
     bwakus = math.floor(chousei)
     chousei = supan - ( bwaku * bwakus )
     
     if chousei <> 0 and chousei < (lcc + iqst) :
          if bwakus == 1:
               chousei = chousei + bwaku
               bwakus = 0
               shoutotu = 1
               loopfx = -1
          else:
               bwakus = bwakus - (bwakus > 0)
               chousei = chousei + bwaku * (bwakus > 0)
               shoutotu = 1

     else:
          supan = zenchou - ssbk - swaku - esbk - ewaku
          warikiri = ((math.floor( supan / lcl )) == ( supan / lcl ))
          j65ds = lcl - (lcl*(( supan / lcl ) - (math.floor( supan / lcl ))))
          if j65ds < (lcc + iqst) or j65ds > (lcl - (lcc + iqst)):
               if j65ds <> 0 and j65ds < lcl:
                    shoutotu = 1

     shoutotu = 0
     chousei = supan%bwaku
     bwakus = math.floor(supan / bwaku)
     
     if szenchou < 0:
          chousei = 0.0
          zzzzzf = 4
     elif ezenchou < 0:
          chousei = 0.0
          zzzzzf = 3
     elif supan < bwaku:
          zzzzzf = 2
     elif supan < ( bwaku + lc03 ):
          zzzzzf = 1
     else:
          zzzzzf = 0
else:
     chousei = 0.0
     zzzzzf = 4

if chouseinashi == 0:
     chousei = 0

loopcnt = 0
if zzzzzf == 1:
     loopcnt = 3 + ( chousei > 0 ) 
elif zzzzzf == 2:
     loopcnt = 2 + ( chousei > 0 ) 
elif zzzzzf == 3:
     loopcnt = 1 + ( chousei > 0 )
elif zzzzzf == 4:
     loopcnt = 0
else:
     loopcnt = 2 + bwakus + ( chousei > 0 )

cfl = 0
chousei0 = 0
chouseix = 0
rchousei = 0
warikiri = ((supan%bwaku) == 0)

c00 = 0

iqwarikiri = 0
zzchousei = (supan%bwaku)

if iqst > 0:
     if zzchousei-l18 == 0:
          iqwarikiri = 1
     if zzchousei-l15 == 0:
          iqwarikiri = 1
     if zzchousei-l12 == 0:
          iqwarikiri = 1
     if zzchousei-l09 == 0:
          iqwarikiri = 1
     if zzchousei-l06 == 0:
          iqwarikiri = 1
     if zzchousei-l12-l09 == 0:
          iqwarikiri = 1
     if zzchousei-lc03 == 0:
          iqwarikiri = 1
     if zzchousei == 0:
          iqwarikiri = 1
 
if iqwarikiri == 0 and iqst > 0:
     if zzchousei-l18 < iqst and zzchousei-l18 > 0:
          shoutotu = 1
     if zzchousei-l15 < iqst and zzchousei-l15 > 0:
          shoutotu = 1
     if zzchousei-l12 < iqst and zzchousei-l12 > 0:
          shoutotu = 1
     if zzchousei-l09 < iqst and zzchousei-l09 > 0:
          shoutotu = 1
     if zzchousei-l06 < iqst and zzchousei-l06 > 0:
          shoutotu = 1
     if zzchousei-l12-l09 < iqst and zzchousei-l12-l09 > 0:
          shoutotu = 1
     if zzchousei-lc03 < iqst and zzchousei-lc03 > 0:
          shoutotu = 1
     if zzchousei < iqst and zzchousei > 0:
          shoutotu = 1
          chousei = chousei + bwaku*(bwakus>0)
          bwakus = bwakus - 1*(bwakus>0)
          loopcnt = loopcnt - 1*(bwakus>1)

if tanbu2 > 0 and tanbu2 < 4:
     if zzchousei-l18 == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l15 == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l12 == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l09 == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l06 == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l12-l09 == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-lc03 == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei == 0 and lcc > 0:
          iqwarikiri = 1

if tanbu2 < 1 or tanbu2 > 3:
     if zzchousei-l18-lcc == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l15-lcc == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l12-lcc == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l09-lcc == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l06-lcc == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-l12-l09-lcc == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-lc03-lcc == 0 and lcc > 0:
          iqwarikiri = 1
     if zzchousei-lcc == 0 and lcc > 0:
          iqwarikiri = 1

if iqwarikiri == 0 and lcc > 0:
     if tanbu2 < 1 or tanbu2 > 3:
          if zzchousei-l18 < lcc and zzchousei-l18 >= 0:
               shoutotu = 1
          if zzchousei-l15 < lcc and zzchousei-l15 >= 0:
               shoutotu = 1
          if zzchousei-l12 < lcc and zzchousei-l12 >= 0:
               shoutotu = 1
          if zzchousei-l09 < lcc and zzchousei-l09 >= 0:
               shoutotu = 1
          if zzchousei-l06 < lcc and zzchousei-l06 >= 0:
               shoutotu = 1
          if zzchousei-l12-l09 < lcc and zzchousei-l12-l09 >= 0:
               shoutotu = 1
          if zzchousei-lc03 < lcc and zzchousei-lc03 >= 0:
               shoutotu = 1
          if zzchousei < lcc and zzchousei >= 0:
               shoutotu = 1
               chousei = chousei + bwaku*(bwakus>0)
               bwakus = bwakus - 1*(bwakus>0)
               loopcnt = loopcnt - 1*(bwakus>1)
     if tanbu2 > 0 and tanbu2 < 4:
          if zzchousei-l18 < lcc and zzchousei-l18 > 0:
               shoutotu = 1
          if zzchousei-l15 < lcc and zzchousei-l15 > 0:
               shoutotu = 1
          if zzchousei-l12 < lcc and zzchousei-l12 > 0:
               shoutotu = 1
          if zzchousei-l09 < lcc and zzchousei-l09 > 0:
               shoutotu = 1
          if zzchousei-l06 < lcc and zzchousei-l06 > 0:
               shoutotu = 1
          if zzchousei-l12-l09 < lcc and zzchousei-l12-l09 > 0:
               shoutotu = 1
          if zzchousei-lc03 < lcc and zzchousei-lc03 > 0:
               shoutotu = 1
          if zzchousei < lcc and zzchousei > 0:
               shoutotu = 1
               chousei = chousei + bwaku*(bwakus>0)
               bwakus = bwakus - 1*(bwakus>0)
               loopcnt = loopcnt - 1*(bwakus>1)

jjjzzz = ((iqst + lcc) *(iqwarikiri==0) )

iqtokusyu = 0
if chousei < iqst and chousei > 0 and iqst > 0 and swaku > lcl and iqwarikiri == 0:
     if (swaku + chousei) < (l06 + lcc + iqst) and (swaku + chousei) > l06:
          chousei = swaku + chousei
          swaku = 0
          supan = 0
          cfl = 1
          iqtokusyu = 1
          
          c0waku = waku000
          c1waku = waku000
          chousei1 = 0
          chousei2 = 0
          chouseix = chousei
          chousei = 0
          rchousei = 1
          c00 = 1

     else:
          swaku = swaku - lcl
          chousei = chousei + lcl

if iqtokusyu == 1:
     pass

elif chousei == 0 and supan%bwaku == 0 and supan >= bwaku and iqwarikiri == 1 and jsyuuten == 0 and lcc > 0: 
     chousei = bwaku 
     bwakus = bwakus - 1

     if bwaku == l18:
          if bwakus > 0:
               c0waku = waku1800
               c1waku = waku1500
               chousei0 = l18
               chousei1 = l15
               chousei2 = chousei - chousei1
               chouseix = chousei - chousei1
               cfl = 1
          else:
               c1waku = waku1500
               chousei1 = l15
               chousei2 = chousei - chousei1
                           
     elif bwaku == l15:
          if bwakus > 0:
               c0waku = waku1500
               c1waku = waku1200
               chousei0 = l15
               chousei1 = l12
               chousei2 = chousei - chousei1
               chouseix = chousei - chousei1
               cfl = 1
          else:
               c1waku = waku1200
               chousei1 = l12
               chousei2 = chousei - chousei1
     elif bwaku == l12:
          if bwakus > 0:
               c0waku = waku1200
               c1waku = waku900
               chousei0 = l12
               chousei1 = l09
               chousei2 = chousei - chousei1
               chouseix = chousei - chousei1
               cfl = 1
          else:
               c1waku = waku900
               chousei1 = l09
               chousei2 = chousei - chousei1
     elif bwaku == l09:
          if bwakus > 0:
               c0waku = waku900
               c1waku = waku600
               chousei0 = l09
               chousei1 = l06
               chousei2 = chousei - chousei1
               chouseix = chousei - chousei1
               cfl = 1
          else:
               c1waku = waku600
               chousei1 = l06
               chousei2 = chousei - chousei1
     elif bwaku == l06:
          if bwakus > 0:
               c0waku = waku600
               c1waku = waku001
               chousei0 = l06
               chousei1 = lc06
               chousei2 = chousei - chousei1
               chouseix = chousei - chousei1
               cfl = 1
          else:
               c1waku = waku001
               chousei1 = lc06
               chousei2 = chousei - chousei1
     else:
          if bwakus > 0:
               c0waku = waku1800
               c1waku = waku1500
               chousei0 = l18
               chousei1 = l15
               chousei2 = chousei - chousei1
               chouseix = chousei - chousei1
               cfl = 1
          else:
               c1waku = waku1500
               chousei1 = l15
               chousei2 = chousei - chousei1

elif chousei <= 0:
     c1waku = waku000
     chousei1 = 0
     chousei2 = 0
     chouseix = chousei
     rchousei = 1
elif chousei <= 0 + jjjzzz:
     c1waku = waku000
     chousei1 = 0
     chousei2 = 0
     chouseix = chousei
     rchousei = 1
     c00 = 1
elif chousei < lc03 + jjjzzz:
     c1waku = waku000
     chousei1 = chousei
     chousei2 = 0
     chouseix = chousei
elif chousei == lc03 + jjjzzz and zzzzzf == 0:
     if bwaku >= l18:
          c0waku = waku1200
          c1waku = waku900
          chousei0 = l12
          chousei1 = l09
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     elif bwaku >= l15:
          c0waku = waku900
          c1waku = waku900
          chousei0 = l09
          chousei1 = l09
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     elif bwaku >= l12:
          c0waku = waku900
          c1waku = waku600
          chousei0 = l09
          chousei1 = l06
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     elif bwaku >= l09:
          c0waku = waku600
          c1waku = waku600
          chousei0 = l06
          chousei1 = l06
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     else:
          c0waku = waku600
          c1waku = waku600
          chousei0 = l06
          chousei1 = l06
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 

elif chousei < lc06 + jjjzzz and zzzzzf > 0: 
     c1waku = waku001
     chousei1 = chousei
     chousei2 = 0
     chouseix = chousei
elif chousei < l06 + jjjzzz and bwaku <= l06:
     c1waku = waku001
     chousei1 = chousei
     chousei2 = 0
     chouseix = chousei
     
elif chousei < l06 + jjjzzz:

     if bwaku >= l18:
          c0waku = waku1200
          c1waku = waku900
          chousei0 = l12
          chousei1 = l09
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     elif bwaku >= l15:
          c0waku = waku900
          c1waku = waku900
          chousei0 = l09
          chousei1 = l09
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     elif bwaku >= l12:
          c0waku = waku900
          c1waku = waku600
          chousei0 = l09
          chousei1 = l06
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     elif bwaku >= l09:
          c0waku = waku600
          c1waku = waku600
          chousei0 = l06
          chousei1 = l06
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
     else:
          c0waku = waku600
          c1waku = waku600
          chousei0 = l06
          chousei1 = l06
          chousei2 = chousei - lcl
          chouseix = chousei - lcl
          cfl = 1 
elif chousei < l09 + jjjzzz:
     c1waku = waku600
     chousei1 = l06
     chousei2 = chousei - chousei1
elif chousei < l12 + jjjzzz:
     c1waku = waku900
     chousei1 = l09
     chousei2 = chousei - chousei1
elif chousei < l15 + jjjzzz:
     c1waku = waku1200
     chousei1 = l12
     chousei2 = chousei - chousei1
elif chousei < l18 + jjjzzz:
     c1waku = waku1500
     chousei1 = l15
     chousei2 = chousei - chousei1
else:
     c1waku = waku1800
     chousei1 = l18
     chousei2 = chousei - chousei1

chousei3 = 0
chouseixx = 0
if chousei2 == 65:
     c2waku = waku000
     chouseixx = chousei2
     chousei2 = 0
     chousei3 = 0
     rchousei = 1
     c00 = 2
elif chousei2 <= 0:
     c2waku = waku000
     chouseixx = chousei2
     chousei2 = 0
     chousei3 = 0
     rchousei = 1
elif chousei2 <= 0 + jjjzzz:
     c2waku = waku000
     chouseixx = chousei2
     chousei2 = 0
     chousei3 = 0
     rchousei = 1
     c00 = 2
elif chousei2 < lc03 + jjjzzz:
     c2waku = waku000
     chouseixx = chousei2
     chousei3 = chousei2
elif chousei2 < lc06 + jjjzzz:
     c2waku = waku001
     chouseixx = chousei2
     chousei3 = chousei2
elif chousei2 < l09 + jjjzzz:
     c2waku = waku600
     chousei2 = l06
     chousei3 = chousei - chousei1 - chousei2
elif chousei2 < l12 + jjjzzz:
     c2waku = waku900
     chousei2 = l09
     chousei3 = chousei - chousei1 - chousei2
elif chousei2 < l15 + jjjzzz:
     c2waku = waku1200
     chousei2 = l12
     chousei3 = chousei - chousei1 - chousei2
elif chousei2 < l18 + jjjzzz:
     c2waku = waku1500
     chousei2 = l15
     chousei3 = chousei - chousei1 - chousei2
else:
     c2waku = waku1800
     chousei2 = l18
     chousei3 = chousei - chousei1 - chousei2

loopcnt = loopcnt + ( chousei0 > 0 ) + ( chousei3 > 0 ) + loopfx

cx = 0
cy = 0
ccount = supan / bwaku
ccount = math.floor(ccount)
clen = ssbk + swaku + ( ccount * bwaku ) 
if zenchou <> 0 and clen <> 0:
     cx = xsta / ( zenchou / clen ) 
     cy = ysta / ( zenchou / clen )  
c1wakux = 0
c1wakuy = 0
if chousei1 <> 0 and zenchou <> 0:
     c1wakux = xsta / ( zenchou / chousei1 ) 
     c1wakuy = ysta / ( zenchou / chousei1 ) 

if zenchou <> 0 and ( clen + chousei1 ) <> 0:
     cx2 = xsta / ( zenchou / ( clen + chousei1 ) ) 
     cy2 = ysta / ( zenchou / ( clen + chousei1 ) ) 
c2wakux = 0
c2wakuy = 0
if chousei2 <> 0 and zenchou <> 0:
     c2wakux = xsta / ( zenchou / chousei2 ) 
     c2wakuy = ysta / ( zenchou / chousei2 ) 

cx0 = 0
cy0 = 0
if chousei0 <> 0 and zenchou <> 0 and ( clen - bwaku + chousei0 ) <> 0:
     cx0 = xsta / ( zenchou / ( clen - bwaku + chousei0 ) ) 
     cy0 = ysta / ( zenchou / ( clen - bwaku + chousei0 ) ) 
c0wakux = 0
c0wakuy = 0
if chousei0 <> 0 and zenchou <> 0:
     c0wakux = xsta / ( zenchou / chousei0 ) 
     c0wakuy = ysta / ( zenchou / chousei0 ) 

bwakux = 0
bwakuy = 0
if chousei2 <> 0 and zenchou <> 0 and bwaku <> 0:
     bwakux = xsta / ( zenchou / bwaku ) 
     bwakuy = ysta / ( zenchou / bwaku ) 

ex = 0
ey = 0 
if zenchou <> 0 and ( (zenchou) - ( ssbk + swaku + esbk + ewaku ) ) <> 0:
     ex = xsta / ( (zenchou)  / ( (zenchou) - ( ssbk + swaku + esbk + ewaku ) ) )
     ey = ysta / ( (zenchou) / ( (zenchou) - ( ssbk + swaku + esbk + ewaku ) ) ) 
if zenchou <> 0 and ( (zenchou) - ( ssbk + swaku + esbk + ewaku ) ) == 0:
     ex = 0
     ey = 0
ewakux = 0
ewakuy = 0
if ewaku <> 0:
     ewakux = xsta / ( (zenchou) / ewaku ) 
     ewakuy = ysta / ( (zenchou) / ewaku ) 

e1waku = waku1800
cfl2 = 0
chouseixxx = 0
supanchouseifl = 0
if ewaku <= 0:
     e1waku = waku000
     cfl2 = 1
     chouseixxx = ewaku
     rchousei = 1
elif ewaku < lc03:
     e1waku = waku000
     chouseixxx = ewaku
     supanchouseifl = 1
elif ewaku < lc06:
     e1waku = waku001
     chouseixxx = ewaku
     supanchouseifl = 1
elif ewaku < l09:
     e1waku = waku600
elif ewaku < l12:
     e1waku = waku900
elif ewaku < l15:
     e1waku = waku1200
elif ewaku < l18:
     e1waku = waku1500
else:
     pass

if zstp < ltakasa:
     cfl2 = 1

sx = 0
sy = 0
if zenchou <> 0 and ssbk <> 0: 
     sx = xsta / ( zenchou / ssbk )
     sy = ysta / ( zenchou / ssbk )
swakux = 0
swakuy = 0
if swaku <> 0:
     swakux = xsta / ( zenchou / swaku )
     swakuy = ysta / ( zenchou / swaku )

s1waku = waku1800
if swaku <= 0:
     pass
elif swaku < lc03:
     s1waku = waku000
elif swaku < l06:
     s1waku = waku001
elif swaku < l09 and tokuteij3 > 0:
     s1waku = waku001
elif swaku < l09:
     s1waku = waku600
     swaku = l06
elif swaku < l12:
     s1waku = waku900
     swaku = l09
elif swaku < l15:
     s1waku = waku1200
     swaku = l12
elif swaku < l18:
     swaku = l15
     s1waku = waku1500
elif swaku == l18:
     swaku = l18
     s1waku = waku1800
else:
     pass

countxy = ( ( zenchou - ssbk - swaku - esbk - ewaku ) / bwaku ) + 1
countxyi = math.floor(countxy)
xzz = 0
yzz = 0
cfl3 = 0

loopcnt = loopcnt - (cfl)
while peach < (countz - 0):

     enfl = 0
     ffl27 = 1
     ffl8z = 0
     fflsd12 = 0
     each = 0
     while each < ( loopcnt ):

          saisyonogyou = 0
          x = xpl + sx - (xstp - swakux) + ( xstp * (each - strcxy) )
          y = ypl + sy - (ystp - swakuy) + ( ystp * (each - strcxy) )
          z = zpl + ( zstp * (peach - strcz) )
          if each == 0:
               waku = s1waku
               saisyonogyou = 1
               x = xpl + sx
               y = ypl + sy

          if cfl == 1 and ( each ) == ( bwakus - 0 + 0 ):
               waku = c0waku

          if ( each ) == ( bwakus - 0 + 1 ):
               waku = c1waku
               if cfl == 1:
                    x = xpl + sx - (xstp - swakux) + ( xstp * (each - 1 ) - strcxy) + c0wakux
                    y = ypl + sy - (ystp - swakuy) + ( ystp * (each - 1 ) - strcxy) + c0wakuy
                    xzz = x
                    yzz = y

          if ( each ) == ( bwakus - 0 + 2 ):
               waku = c2waku
               x = xpl + sx + swakux + ex
               y = ypl + sy + swakuy + ey
               if cfl == 1:
                    x = xzz + c1wakux +c2wakux 
                    y = yzz + c1wakuy +c2wakuy 

          if ( each ) == ( loopcnt - 1 ) and each <> 0:
               waku = e1waku
               x = xpl + sx + swakux + ex 
               y = ypl + sy + swakuy + ey 
               enfl = 1

          z= z + zzzzz
          if ( each ) == ( loopcnt - 1 ) and each <> 0 and ewakufl <> 0:
               pass
          elif ( each ) == ( loopcnt - 2 ) and chousei2 <> 0 and each <> 0 and ewakufl == 2:
               pass
          elif cfl == 1 and ( each ) == ( bwakus - 0 + 2 ) and chousei3 <> 0 and ewakufl == 2:
               pass

          else:
               ffl1 = 0
               ffls1 = 0
               fflss1 = 0
               if ( peach + 1 ) >= (countz - 0):
                    ffl1 = 1
                    ffls1 = 1
               if ( peach + 2 ) >= (countz - 0) and ffls1 == 0:
                    fflss1 = 1
               ffl2 = 0
               ffls2 = 0
               if peach == 0:
                    ffl2 = 1
                    ffls2 = 1
               ffl3 = 0
               ffls3 = 0
               ffl8 = 0

               if each == 0:
                    ffl8 = 1
                    if tanbu1 > 0:
                         ffls3 = 1
                         ffl3 = 1

               ffl4 = 0
               ffls4 = 0
               if ( each + 1 ) >= ( loopcnt - 0 ) and tanbu2 > 0:
                    ffl4 = 1
                    ffls4 = 1
               ffl5 = 0
               if sheetflg == 1:
                    ffl5 = 1
               ffl6 = 0
               ffls6 = 0
               ffl15 = 0
               if sheetflg == 1 and ffls4 == 1 and tanbu2 > 0:
                    ffl6 = 1
                    ffls6 = 1
                    ffl15 = 1
               ffl7 = 0
               ffls7 = 0
               ffl14 = 0
               
               if sheetflg == 1 and ffls3 == 1 and tanbu1 > 0:
                    ffl7 = 1
                    ffls7 = 1
                    ffl14 = 1
               if sheetflg2 == 0 and ffls2 == 1:
                    ffl5 = 0
                    ffl6 = 0
                    ffl7 = 0

               ffl28 = 0
               if ffl8 == 1 and lchousei == 1:
                    ffl28 = 1
                    
               if ffl8 == 1 and lchousei == 1 and arubatorosu == 1:
                    ffl28 = 0

               ffl29 = 0
               if jidou == 1 and chouseix == 0 and chouseixx == 0 and cfl == 0 and ( each ) == ( bwakus - 0 + 0 ) and chousei2 == 0 and rchousei == 1 and jsyuuten == 0:
                    ffl29 = 1
                    if arubatorosu == 1:
                         ffl29 = 0
               if jidou == 1 and chouseix == 0 and chouseixx == 0 and cfl == 1 and ( each ) == ( bwakus - 0 + 1 ) and chousei3 == 0 and rchousei == 1 and jsyuuten == 0:
                    ffl29 = 1
                    if arubatorosu == 1:
                         ffl29 = 0
               zzz1 = ( each ) == ( bwakus - 0 + 0 )
               zzz2 = ( each ) == ( bwakus - 0 + 0 )
               zzz3 = rchousei

               ffl9 = 0
               ffls9 = 0
               fflss9 = 0.0
               fflsss9 = peach + 1.0
               fflssss9 = peach + 0.0
               if zsaikadan == 0:
                    fflsss9 = peach  + 2.0
                    fflssss9 = peach + 1.0
               ffl10 = 0
               ffl11 = 0
               if rakkabou > 0:
                    fflss9 = (fflsss9 + ztchousei) / rakkabou
                    fflsss9 = int(fflss9)
                    fflssss9 = (fflssss9 + ztchousei) / rakkabou
                    fflssss9 = int(fflssss9)

               if ( fflssss9 + 1 ) == fflsss9 and rakkabou > 0 and fflss9 > 0 and fflsss9 > 0:
                    ffls9 = 1
               if ffls2 == 1 and zsaikadan == 1 and ztchousei == 0:
                    ffls9 = 0
               if ffls1 == 1:
                    ffls9 = 0
               if fflss1 == 1:
                    ffls9 = 1                    
               if rakkabou > 0 and ffls9 == 1:
                    ffl9 = 1
                    ffl11 = 1
               if ffls7 == 1 and rakkabou > 0 and ffls9 == 1:                    
                    ffl10 = 1

               ffl12 = 0
               ffls12 = 0
               fflss12 = 0.0
               fflsss12 = peach + 0.0
               fflssss12 = peach - 1.0
               if zsaikadan == 0:
                    fflsss12 = peach  + 1.0
                    fflssss12 = peach + 0.0
               if tunagih > 0:
                    fflss12 = (fflsss12 + ztchousei) / tunagih
                    fflsss12 = int(fflss12)
                    fflssss12 = (fflssss12 + ztchousei) / tunagih
                    fflssss12 = int(fflssss12)

               if ( fflssss12 + 1 ) == fflsss12 and tunagih > 0 and fflss12 > 0 and fflsss12 > 0:
                    ffls12 = 1
                    fflsd12 = 1
               if ffls2 == 1 and zsaikadan == 1:
                    ffls12 = 1
                    fflsd12 = 1
               if ffls1 == 1 and fflsd12 == 0:
                    ffls12 = 1
                    fflsd12 = 1
               if fflss1 == 1:
                    pass
                    
               fflx12 = each + 1.0
               if tunagil > 0:
                    fflx12 = fflx12 / tunagil
               fflx12 = int(fflx12)
               fflxx12 = each + 0.0
               if tunagil > 0:
                    fflxx12 = fflxx12 / tunagil
               fflxx12 = int(fflxx12)
               fflxxx12 = 0
               fflxxxx12 = 0               
               if tunagih > 0 and ffls12 == 1 and tunagil > 0:
                    if ( fflxx12 + 1 ) == fflx12:
                         ffl12 = 1
                    if ( each ) == 0:
                         ffl12 = 0
                    if ( each + 1 ) >= (loopcnt - 0):
                         fflxxx12 = 1
                         ffl12 = 0
                    if ( each + 2 ) >= (loopcnt - 0) and fflxxx12 == 0:
                         fflxxxx12 = 1  
                         ffl12 = 1                   

               ffl13 = 1
               ffl21 = 0
               ffl22 = 0
               if ffls4 == 1 and tanbu2 == 1:         
                    if ffls2 == 0:
                         ffl13 = 0
                    ffl10 = 0
                    ffl11 = 0 
                    ffl13 = 0
                    if ffl9 == 1:
                         ffl22 = 0
                         if enfl == 1:
                              ffl9 = 0

               if ffls3 == 1 and tanbu1 == 1:         
                    if ffls2 == 0:
                         ffl13 = 0
                    ffl10 = 0
                    ffl11 = 0 
                    ffl13 = 0
                    if ffl10 == 1:
                         ffl21 = 0

               ffl20 = 1
               ffl27 = 1
               if ffls4 == 1 and tanbu2 == 3:           
                    if ffls2 == 0:
                         ffl20 = 0
                    ffl5 = 0
                    ffl6 = 0
                    ffl20 = 0
                    if ffl9 == 1:
                         ffl22 = 1
                    if enfl == 1:
                         ffl6 = 0
                         ffl27 = 0			

               if ffls3 == 1 and tanbu1 == 3:           
                    if ffls2 == 0:
                         ffl20 = 0
                    ffl5 = 0
                    ffl20 = 0
                    if ffl10 == 1:
                         ffl21 = 1
                    if each == 0:
                         ffl7 = 0
                         ffl27 = 0
             
               ffl16 = '右端部'
               ffl17 = 1
               ffl18 = '右端部'
               ffl19 = 1

               if ffl8z == 2:
                    ffl8 = 1
                    ffl8z = 0

               if waku == waku000 or waku == waku001:
                    if ewaku < l06:
                         if cfl == 1:
                              ffl16 = 'L'
                              ffl17 = chouseix + (chouseixx * (chouseix == 0)) + (chouseixxx * (chouseix * chouseixx == 0)) + tokuteijyouken2
                              ffl18 = 'セットバック長さ'
                              ffl19 = chouseix * (chouseix <> chouseixx) + tokuteijyouken2
                              ffl8z = 1
                         else:
                              ffl16 = 'L'
                              ffl17 = chouseix + (chouseixx * (chouseix == 0)) + (chouseixxx * (chouseix * chouseixx == 0)) + tokuteijyouken2
                              ffl18 = 'セットバック長さ'
                              ffl19 = chouseix * (chouseix <> chouseixx) + tokuteijyouken2
                              ffl8z = 1
                    else:
                         if cfl == 1:
                              ffl16 = 'L'
                              ffl17 = chouseix + (chouseixx * (chouseix == 0)) + (chouseixxx * (chouseix * chouseixx == 0)) + tokuteijyouken2
                              ffl18 = 'セットバック長さ'
                              ffl19 = chouseix * (chouseix <> chouseixx) + tokuteijyouken2
                              ffl8z = 1
                         else:
                              ffl16 = 'L'
                              ffl17 = chouseix + (chouseixx * (chouseix == 0)) + (chouseixxx * (chouseix * chouseixx == 0)) + tokuteijyouken2
                              ffl18 = 'セットバック長さ'
                              ffl19 = chouseix * (chouseix <> chouseixx) + tokuteijyouken2
                              ffl8z = 1
                              
                    if ffl17 <= lcc:
                         ffl5 = 0
                    if tokuteij3 > 0:
                         ffl16 = 'L'
                         ffl17 = tokuteij3
                         ffl18 = 'セットバック長さ'
                         ffl19 = tokuteij3
                         ffl8z = 1
                         ffl5 = 1
                         if sheetflg2 == 0 and ffls2 == 1:
                              ffl5 = 0
               if ffl8z == 1:
                    ffl8z = ffl8z + 1

               ffl23 = 1
               ffl24 = 1
               ffl25 = 1
               ffl26 = 1
               if habaki <= 0:
                    ffl23 = 0
                    ffl24 = 0
                    ffl25 = 0
                    ffl26 = 0
               if habaki == 1:
                    pass
               if habaki == 2:
                    ffl23 = 0
                    ffl24 = 1
                    ffl25 = ( ffl7 == 0 )
                    ffl26 = ( ffl6 == 0 )
                    if ffls2 == 1 and sheetselect2 > 0:
                         ffl25 = ffl25 * ( ffls7 == 0 )
                         ffl26 = ffl26 * ( ffls6 == 0 )
                         ffl26 = (ffls6 == 1) * (tanbu2 == 3)
               if habaki >= 3:
                    ffl23 = 1
                    ffl24 = 0
                    ffl25 = ( ffls7 == 1 )
                    ffl26 = ( ffls6 == 1 )

               if zsaijoudan == 0 and ffl1 ==1:
                    ffl1 = 0
               if zsaikadan == 0:
                    ffl2 = 0
               if setuzoku1 == 1 and saisyonogyou == 1:
                    ffl8 = 0
                    ffl7 = 0
                    ffl3 = 0
                    ffl25 = 0
               if ( each + 1 ) >= (loopcnt - 0) and warikiri ==2:
                    ffl29 = 1
                    if arubatorosu == 1:
                         ffl29 = 0
               if ( each + 2 ) >= (loopcnt - 0) and c00 > 0 and jidou == 1 and jsyuuten == 0:
                    ffl29 = 1
                    if arubatorosu == 1: 
                         ffl29 = 0
               if ( each + 2 ) == (loopcnt - 0) and c00 > 0 and jidou == 1 and jsyuuten == 1:
                    ffl29 = 1
                    if arubatorosu == 1: 
                         ffl29 = 0
               if ( each + 1 ) == (loopcnt - 0) and c00 > 0 and jidou == 1 and jsyuuten == 1:
                    ffl8 = 1

               ffl5 = (ffl5 == 1) * sheetselect
               ffl6 = (ffl6 == 1) * sheetselect2
               ffl7 = (ffl7 == 1) * sheetselect2

               ffl34 = 0
               if (iqashiba == 1 or arubatorosu == 1) * (saisyonogyou == 1) * (ffl20 == 1) * (ffl13 == 1) > 0:
                    ffl8 = 0
                    ffl34 = 1
                    if ffl1 == 1:
                         ffl34 = 0
               ffl35 = 0
               if (iqashiba == 1) * (saisyonogyou == 1) * (ffl20 == 0) * (ffl2 == 1) * (ffl13 == 1) > 0:
                    ffl35 = 1

               lastl = 0
               if ( each + 1 ) == ( loopcnt - 1 ) and each <> 0 and ewakufl <> 0:
                    lastl = 1
               if ( each + 1 ) == ( loopcnt - 2 ) and chousei2 <> 0 and each <> 0 and ewakufl == 2:
                    lastl = 1
               if cfl == 1 and ( each + 1 ) == ( bwakus - 0 + 2 ) and chousei3 <> 0 and ewakufl == 2:
                    lastl = 1
               if ( each + 1 ) == ( loopcnt - 0 ) and each <> 0 and ewakufl == 0:
                    lastl = 1
               ffl40 = 0

               if ( (iqashiba == 1) * (lastl == 1) * (supanchouseifl == 0) * ( ((esbk == wakuhaba)*(tanbu2 == 0)) or ((esbk == 0)*(tanbu2 == 0)) ) ) > 0:
                    ffl40 = 1

               if ffl8 == 1 and kyouseisc == 1:
                    ffl28 = 1
               if ffl8 == 1 and kyouseisn == 1 and each == 0:
                    ffl8 = 0

               if ( each + 2 ) >= (loopcnt - 0) and kyouseiec == 1:
                    ffl29 = 1
                    ffl17 = ffl17 + lcc
                    ffl19 = ffl19 + lcc
                    if arubatorosu == 1: 
                         ffl29 = 0
               if (lastl == 1) * (kyouseien == 1) > 0:
                    ffl40 = 2

               ffl5 = ffl5 + (3*(ffl5 == 3)*(sheetname == 1))
               ffl6 = ffl6 + (3*(ffl6 == 3)*(sheetname == 1))
               ffl7 = ffl7 + (3*(ffl7 == 3)*(sheetname == 1))
     
               list0.append(x)
               list1.append(y)
               list2.append(z)
               list3.append(waku)
               list4.append(vvvvv)
               list5.append(ffl1)
               list6.append(ffl2)
               list7.append(ffl3)
               list8.append(ffl4)
               list9.append(ffl5)
               list10.append(ffl6)
               list11.append(ffl7)
               list12.append(ffl8)
               list13.append(ffl9)
               list14.append(ffl10)
               list15.append(ffl11)
               list16.append(ffl12)
               list17.append(ffl13)
               list18.append(ffl14)
               list19.append(ffl15)
               list20.append(ffl16)
               list21.append(ffl17)
               list22.append(ffl18)
               list23.append(ffl19)
               list24.append(ffl20)
               list25.append(ffl21)
               list26.append(ffl22)
               list27.append(ffl23)
               list28.append(ffl24)
               list29.append(ffl25)
               list30.append(ffl26)
               list31.append(ffl27)
               list32.append(ffl28)
               list33.append(ffl29)
               list34.append(ffl34)
               list35.append(ffl35)
               list36.append(ffl36)
               list37.append(ffl37)
               list38.append(ffl38)
               list39.append(ffl39)
               list40.append(ffl40)

          waku = b1waku
          each += 1
     each = strc
     peach += 1

OUT =[list0,list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16,list17,list18,list19,list20,list21,list22,list23,list24,list25,list26,list27,list28,list29,list30,list31,list32,list33,list34,list35,list36,list37,list38,list39,list40]

###end

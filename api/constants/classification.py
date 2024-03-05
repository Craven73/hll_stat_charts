AXIS_INF = ['STG44', 'GEWEHR 43', 'KARABINER 98K', 'MP40', 'PANZERSCHRECK', 'MG42', 'M43 STIELHANDGRANATE', 'FG42 x4',
           'KARABINER 98K x8', 'S-MINE', 'LUGER P08', 'MG34', 'TELLERMINE 43']
ALLIES_INF = ['BAZOOKA', 'M1 GARAND', 'M1 CARBINE', 'M1903 SPRINGFIELD', 'M3 GREASE GUN', 'BROWNING M1919',
             'MK2 GRENADE', 'M1918A2 BAR', 'M1A1 THOMPSON', 'M97 TRENCH GUN', 'COLT M1911', 'M2 AP MINE',
             "GMC CCKW 353", 'SCOPED SVT40', 'SCOPED MOSIN NAGANT 91/30', 'PPSH 41', 'SVT40', 'DP-27',
             'RG-42 GRENADE', 'MOSIN NAGANT M38', 'PPSH 41 W/DRUM', 'MOSIN NAGANT 91/30', 'FG42', 'POMZ AP MINE']

AXIS_TANK = ['75MM CANNON [Sd.Kfz.171 Panther]', 'COAXIAL MG34 [Sd.Kfz.171 Panther]',
            '75MM CANNON [Sd.Kfz.161 Panzer IV]', 'COAXIAL MG34 [Sd.Kfz.161 Panzer IV]',
            'HULL MG34 [Sd.Kfz.171 Panther]', 'COAXIAL MG34 [Sd.Kfz.234 Puma]', '50mm KwK 39/1 [Sd.Kfz.234 Puma]',
            'HULL MG34 [Sd.Kfz.161 Panzer IV]', '20MM KWK 30 [Sd.Kfz.121 Luchs]', 'COAXIAL MG34 [Sd.Kfz.121 Luchs]',
            'Sd.Kfz.161 Panzer IV', 'Sd.Kfz.171 Panther', 'COAXIAL MG34 [Sd.Kfz.181 Tiger 1]', '88 KWK 36 L/56 [Sd.Kfz.181 Tiger 1]',
            'Sd.Kfz.181 Tiger 1','HULL MG34 [Sd.Kfz.181 Tiger 1]', 'Sd.Kfz.234 Puma']
ALLIES_TANK = ['75MM CANNON [Sherman M4A3(75)W]', 'COAXIAL M1919 [Sherman M4A3(75)W]', '37MM CANNON [Stuart M5A1]',
              '76MM M1 GUN [Sherman M4A3E2(76)]', 'COAXIAL M1919 [Sherman M4A3E2(76)]', 'COAXIAL M1919 [M8 Greyhound]',
              'M6 37mm [M8 Greyhound]', 'HULL M1919 [Stuart M5A1]', 'COAXIAL M1919 [Stuart M5A1]', 'Sherman M4A3(75)W',
              'HULL M1919 [Sherman M4A3(75)W]', 'HULL M1919 [Sherman M4A3E2(76)]', 'M8 Greyhound','D-5T 85MM [IS-1]',
              'COAXIAL DT [T70]','COAXIAL DT [IS-1]','IS-1','19-K 45MM [BA-10]','76MM ZiS-5 [T34/76]',
              'COAXIAL DT [T34/76]','HULL DT [T34/76]','HULL DT [IS-1]','45MM M1937 [T70]', 'Sherman M4A3E2(76)', "OQF 6 - POUNDER Mk.V [Churchill Mk.III]",
              'QF 75MM [Cromwell]', 'COAXIAL BESA [Cromwell]', 'COAXIAL BESA 7.92mm [Churchill Mk.III]', 'HULL BESA 7.92mm [Churchill Mk.III]', 'QF 2-POUNDER [Tetrarch]',
              'QF 2-POUNDER [Daimler]', 'COAXIAL BESA [Tetrarch]', 'COAXIAL BESA [Daimler]']

AXIS_ARTY = ['150MM HOWITZER [sFH 18]']
ALLIES_ARTY = ['155MM HOWITZER [M114]', '122MM HOWITZER [M1938 (M-30)]', 'QF 25-POUNDER [QF 25-Pounder]']

ALLIES_TANK_SHORT = ["Sherman M4A3(75)W", "Stuart M5A1", "Sherman M4A3E2(76)", "M8 Greyhound", 'T70','IS-1','BA-10','T34/76', 'Churchill Mk.III', 'Cromwell', 'Tetrarch', 'Daimler']
AXIS_TANK_SHORT = ["Panther", "Panzer IV", "Puma", "Luchs", "Tiger"]

ALLIES_WEAPONS = ALLIES_ARTY + ALLIES_TANK + ALLIES_INF
AXIS_WEAPONS = AXIS_ARTY + AXIS_TANK + AXIS_INF
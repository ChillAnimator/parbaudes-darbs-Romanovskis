# ----------------------------------------------------------------------
# B2. PowerShell — diska vieta failā
# ----------------------------------------------------------------------

# Saglabā informāciju par brīvo vietu diskos CSV failā diski.csv, ko var atvērt Excel. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                         

$diski = Get-PSDrive -PSProvider FileSystem |
    Select-Object Name, Used, Free

$diski | Export-Csv -path "diski.csv" -NoTypeInformation

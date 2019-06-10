'''This function designed to get the filename under the certain path,
but the filename must be number-letters/characters or just consisted
by letters/characters like 1-江苏国源电力工程有限公司 or 江苏国源电力工程有限公司'''
def getFilenames(path, txtname, exlname):
    '''path is the distance you want to extract the filenames from
       txtname is the txt file that will store your extracted filenames
       exlname is the excel file that will store your extracted filenames'''
    import os, re, openpyxl
    os.chdir(path)
    Filelist = os.listdir()
    Fileobject = open(txtname, 'w')
    wb = openpyxl.Workbook()
    sheet = wb.get_active_sheet()
    for item in Filelist:
        nameregex = re.compile(r'(\w+)-(\w+)')
        num = Filelist.index(item) + 1
        if nameregex.search(item) != None:
            sheet.cell(row = num, column = 1).value = str(nameregex.search(item).group(2))
            Fileobject.write(str(nameregex.search(item).group(2)))
            Fileobject.write('\n')
        else:
            nameregex = re.compile(r'(\w+)')
            sheet.cell(row = num, column = 1).value = str(nameregex.search(item).group())
            Fileobject.write(str(nameregex.search(item).group()))
            Fileobject.write('\n')
    wb.save(exlname)
    Fileobject.close()


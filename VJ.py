# -*- coding: utf-8 '-*-
import os,sys
import glob
import PyPDF2 as pyPdf

class Paper:
    def __init__(self,Params):
        self.Name = Params['Name']
        self.Contributor = Params['Contributor']
        self.Journal = Params['Journal']
        self.Num_of_pages = Params['Num_of_pages']
        self.Full_name = Params['Full_name']
Volume=int(sys.argv[1])
Papers = []
params = {'Name':'',
          'Journal':'',
          'Contributor':'',
          'Full_name':''}    
def GetContributor(item):
    return item.Contributor
for filename in glob.glob('*.pdf'):
    
    with open(os.path.join(os.getcwd(), filename), 'r'):
        if (len(filename.split('_'))>2):
            reader = pyPdf.PdfFileReader(filename)
            params['Num_of_pages'] = reader.getNumPages()
            print(filename.split('_'))
            params['Name'] = ' '.join((filename.split('_'))[1].split('+'))
            params['Journal'] = filename.split('_')[0]
            #params['Num_of_pages'] = filename.split('_')[-2]
            params['Contributor'] = (filename.split('_')[-1]).split('.')[0]
            params['Full_name'] = filename
            item = Paper(params)
            Papers += [item]
        else:
            pass
Papers.sort(key=GetContributor)      
#%% 
print(Papers)
with open('VJ_'+str(Volume)+'.tex','w+') as file:
    file.write('\\documentclass[10pt,a4paper]{scrreprt}\n')
    file.write('\\usepackage[applemac]{inputenc}        \n')
    file.write('\\usepackage[T1]{fontenc}   \n')
#    file.write('\\usepackage[ngerman]{babel}\n')
    file.write('\\usepackage{graphicx}\n')
    file.write('\\usepackage{float}\n')
    file.write('\\usepackage{typearea}\n')
    file.write('\\usepackage{hyperref}\n')
    file.write('\\usepackage{wasysym}\n')
#    file.write('\\usepackage{pst-all}\n')
    file.write('\\usepackage{array}\n')
    file.write('\\usepackage{caption}\n')
    file.write('\\usepackage{wrapfig}\n')
    file.write('\\usepackage{pdfpages}\n')
    
    file.write('\\setlength{\\topmargin}{5pt} \n')
    file.write('\\setlength{\\oddsidemargin}{5pt} \n')
    file.write('\\setlength{\\marginparwidth}{5pt} \n')
    file.write('\\setlength{\\headheight}{5pt} \n')
    file.write('\\setlength{\\headsep}{2pt} \n')
    file.write('\\setlength{\\textwidth}{600pt} \n')
    file.write('\\setlength{\\textheight}{700pt} \n')
    file.write('\\setlength{\\columnsep}{10pt} \n')
    
#    file.write('\\newcommand{\\webpage}{https://www.simonsfoundation.org/quanta/20131107-physicists-eye-quantum-gravity-interface/}\n')
#    file.write('\\addto\\captionsngerman{\\renewcommand{\\figurename}{}}\n')
    file.write('\\pagestyle{myheadings}\n')
    file.write('\\markright{\\today}\n')
    file.write('\\begin{document}\n')
    
    file.write('\\typearea{20} \n')
    
    file.write('\\parskip 6pt \n')
    file.write('\\parindent 0pt\n')
    
    file.write('\\begin{center}\n')
    file.write('\\Huge\n')
    file.write('\\textbf{The Virtual Journal}\\\ \n')
    file.write('\\huge\n')
    file.write('\\textbf{Vol. '+str(Volume)+'}\n')
    file.write('\\end{center}\n')
    
    file.write('\\vspace{0.2cm} \n')
    file.write('\\begin{table}[H] \n')
    file.write('\\centering \n')
    file.write('\\fbox{ \n')
    file.write('\\begin{tabular}{m{6.5cm}|c|c|c} \n')
    file.write('Title	&	Journal	&	Cont. by	&	Page	\\\ \n')
    file.write('\\hline \n')
    file.write('\\vspace{0.3cm} \n')
    
    pageCount = 3
    for ii in range(len(Papers)):
         file.write('\hyperlink{page.'+str(pageCount)+'}{'+Papers[ii].Name+'} & ' + Papers[ii].Journal + ' & ' + Papers[ii].Contributor + ' & ' + str(pageCount) + ' \\\ \n')
         file.write('& & & \\\ \n')
         pageCount+=int(Papers[ii].Num_of_pages)
    file.write('\end{tabular}}\n')
    file.write('\end{table}\n')
    file.write('\\includepdf[pages={-}]{JournalScouting.pdf}\n')
    for ii in range(len(Papers)):
        file.write('\\includepdf[pages={-}]{'+Papers[ii].Full_name+'}\n')
    file.write('\end{document}\n')
